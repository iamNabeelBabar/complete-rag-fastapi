
def clean_data(pages):
    cleaned_data = []
    for page in pages:
        text = page.page_content
        cleaned_text = " ".join(text.split())
        page.page_content = cleaned_text
        cleaned_data.append(page)
    return cleaned_data

