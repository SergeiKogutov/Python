import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import json

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

async def fetch_with_retries(session, url, headers):
    while True:  # Бесконечный цикл для повторных попыток
        try:
            async with session.get(url, headers=headers, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
                elif response.status == 404:
                    print(f"404 Not Found: {url}")
                    return None  # Возвращаем None для обработки 404
                else:
                    print(f"Failed to retrieve {url}. Status code: {response.status}")
                    await asyncio.sleep(2)  # Задержка перед повторной попыткой
        except asyncio.TimeoutError:
            print(f"Timeout while trying to access {url}. Retrying...")
            await asyncio.sleep(2)  # Задержка перед повторной попыткой
        except Exception as e:
            print(f"An error occurred while accessing {url}: {e}")
            await asyncio.sleep(2)  # Задержка перед повторной попыткой

async def scrape_website(session, url, output_dir, index, error_log_file, ignored_urls, user_agent):
    headers = {
        'User-Agent': user_agent
    }
    
    html_content = await fetch_with_retries(session, url, headers)

    if html_content is None:
        # Если контент не получен (например, 404), записываем в лог
        try:
            with open(error_log_file, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{index}: {url}\n")
        except Exception as e:
            print(f"Error writing to error log file: {e}")
            # Если не удалось открыть файл, создаем новый с увеличенным номером
            base_name, ext = os.path.splitext(error_log_file)
            counter = 2
            new_log_file = f"{base_name}_{counter}{ext}"
            while os.path.exists(new_log_file):
                counter += 1
                new_log_file = f"{base_name}_{counter}{ext}"
            with open(new_log_file, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{index}: {url}\n")
            print(f"Logged to new file: {new_log_file}")
        return  # Прерываем выполнение, если 404

    soup = BeautifulSoup(html_content, 'html.parser')
    
    file_name = f"parse_{index}"
    file_name = clean_filename(file_name)
    file_path = os.path.join(output_dir, file_name + ".json")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    report_data = {
        "url": url,
        "headers": [],
        "spans": [],
        "good_info": [],
        "params": {},
        "product_items": {}
    }

    h1 = soup.find('h1')
    if h1:
        report_data["headers"].append(h1.text.strip())
    
    spans = soup.find_all('span')
    for span in spans:
        text = span.text.strip()
        if text:
            report_data["spans"].append(text)

    good_info = soup.find_all('div', class_='good_info_text')
    for info in good_info:
        text = info.text.strip()
        if text:
            report_data["good_info"].append(text)

    product_items = soup.find_all('div', class_='product_item')
    for item in product_items:
        product_name = item.find('div', class_='product_name vz')
        if product_name:
            link = product_name.find('a')
            if link:
                key = link.text.strip()
                params = item.find_all('div', class_='param vz')
                values = {}
                for param in params:
                    span_value = param.find('span', class_='param_value')
                    if span_value:
                        values[key] = span_value.text.strip()
                report_data["product_items"][key] = values

    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(report_data, json_file, ensure_ascii=False, indent=4)
        print(f"Parsing {index}: Data from {url} saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

async def scrape_from_file(file_path, user_agents):
    output_dir = 'resultdata'
    os.makedirs(output_dir, exist_ok=True)
    error_log_file = 'error_log.txt'  # Файл для записи ошибок 404
    ignored_urls_file = 'ignored_urls.txt'  # Файл для игнорируемых URL

    # Загружаем игнорируемые URL из файла, если он существует
    ignored_urls = set()
    if os.path.exists(ignored_urls_file):
        with open(ignored_urls_file, 'r') as f:
            ignored_urls = set(line.strip() for line in f)

    async with aiohttp.ClientSession() as session:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        
        tasks = []
        for index, url in enumerate(urls, start=1):
            url = url.strip()
            if url in ignored_urls:
                print(f"Skipping ignored URL: {url}")
                continue  # Пропускаем игнорируемый URL

            if url:
                file_name = f"parse_{index}"
                file_path = os.path.join(output_dir, clean_filename(file_name) + ".json")
                
                # Проверяем, существует ли файл с данными
                if os.path.exists(file_path):
                    print(f"Report for index {index} already exists. Skipping URL: {url}")
                    continue  # Пропускаем этот URL, если файл уже существует
                
                # Меняем user-agent каждые 5 запросов
                user_agent = user_agents[(index // 5) % len(user_agents)]
                print(f"Scraping URL: {url} with user-agent: {user_agent}")
                tasks.append(scrape_website(session, url, output_dir, index, error_log_file, ignored_urls, user_agent))
                
                # Добавляем задержку между запросами
                # await asyncio.sleep(1)  # Задержка в 1 секунду между запросами
        
        await asyncio.gather(*tasks)

    # Сохраняем игнорируемые URL в файл
    with open(ignored_urls_file, 'w') as f:
        for url in ignored_urls:
            f.write(f"{url}\n")

# Укажите путь к вашему файлу с URL и список user-agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/85.0",
    # Добавьте больше user-agents здесь
]

asyncio.run(scrape_from_file('urls.txt', user_agents))