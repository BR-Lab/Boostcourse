from bs4 import BeautifulSoup

with open("books.xml", "r", encoding="utf8") as books_file:
    books_xml = books_file.read()

soup = BeautifulSoup(books_xml, "lxml") #lxml parser를 사용해서 데이터 분석

#author가 들어간 모든 element 추출
for book_info in soup.find_all("author"):
    print(book_info)
    print(book_info.get_text())