from newspaper import Article
from pypdf import PdfReader

def load_article(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def load_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
