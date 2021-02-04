from flask import Flask, render_template, request
from openpyxl import load_workbook

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("authors.html")

@app.route("/books/")
def books():
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]

    object_list = [[tale.value, tale.offset(column=1).value] for tale in page["A"][1:]]
    print(object_list)
    return render_template(
        "books.html", object_list=object_list
        )

#     tales = [tale.value for tale in page["A"]][1:]

#     authors = [author.value for author in page["B"]][1:]

#     html = """
#         <a href="/authors">Авторы</a>
#         <a href="/books">Книги</a>
#         <h1>Тут будет список книг</h1>
#     """

#     for i in range(len(tales)):
#         html += f"<h2>{tales[i]} - {authors[i]}</h2>"

#     return html 

@app.route("/authors/")
def authors():
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]
    authors = {author.value for author in page["B"][1:]}
    return render_template("authors.html", authors=list(authors))
   

@app.route("/add/", methods=["POST"])
def add():
    f = request.form
    # print(f["author"], f["book"])
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]
    last = len(page["A"]) + 1
    page[f"A{last}"] = f["author"]
    page[f"B{last}"] = f["book"]
    excel.save("tales.xlsx")
    return "форма получена"