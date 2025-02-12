# Using the open-webui REST APIs, downloads pdfs from url,
# creates knowledge collection, upload files and adds file
# to the knowledge collection

import json
import requests
from pathlib import Path

token = Path('.token.txt').read_text().strip()
print(f'{token = }')

def extract_pdf_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    pdf_links = [
        a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')
    ]

    ### To download all the files, comment out this block
    for url in pdf_links:
        if url == 'https://www.fia.com/sites/default/files/2025_international_sporting_code_fr-en_clean_version_27.01.2025.pdf':
            pdf_links = [ url ]
            break
    ###
    for url in pdf_links:
        print(url)

    return pdf_links


def download_pdfs_from_page(page_url, dir):
    try:
        resp = requests.get(page_url)
        resp.raise_for_status()  # Check for HTTP errors
        pdf_urls = extract_pdf_links(resp.content)
        Path(dir).mkdir(
            parents=True, exist_ok=True
        )  # Create dir if it doesn't exist
        for url in pdf_urls:
            try:
                pdf_resp = requests.get(url)
                pdf_resp.raise_for_status()
                fname = Path(url).name
                fpath = Path(f'{dir}/{fname}')
                with fpath.open('wb') as f:
                    f.write(pdf_resp.content)
                print(f"Downloaded: {fpath}")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_url}: {e}")

def upload_file(token, f):
    url = f'http://localhost:8080/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    data = {
        'file': (f, open(f, 'rb'), 'application/pdf')
    }

    response = requests.post(url, headers=headers, files=data)
    return response.json()

def create_knowledge(token):
    url = f'http://localhost:8080/api/v1/knowledge/create'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    data = {
        'name': 'RB',
        'description': 'RB desc'
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

def add_file(token, k_id, f_id):
    url = f'http://localhost:8080/api/v1/knowledge/{k_id}/file/add'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    data = {
        'file_id': f_id
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


# Example usage
#page_url = "https://www.example.com/page-with-pdfs"
page_url = 'https://www.fia.com/regulation/category/123'
download_pdfs_from_page(page_url, "pdf_downloads")

ret = create_knowledge(token)
k_id = ret.get('id')
print(f'Created knowledge, {k_id = }')

f = 'pdf_downloads/2025_international_sporting_code_fr-en_clean_version_27.01.2025.pdf'
ret = upload_file(token, f)
f_id = ret.get('id')
print(f'Uploaded file, {f = } {f_id = }')

ret = add_file(token, k_id, f_id)
print(f'Added {f} to knowledge')
