from flask import Flask, render_template, request
from openpyxl import load_workbook

app = Flask(__name__)

@app.route("/")
def homepage():
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]
    object_list = [[tale.value, tale.offset(column=1).value] for tale in page["A"][1:]]
    return render_template("homepage.html", object_list=object_list)


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


@app.route("/book/<num>/")
def book(num):
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]
    object_list = [[tale.value, tale.offset(column=1).value, tale.offset(column=2).value] for tale in page["A"][1:]]
    obj = object_list[int(num)]
    obj.append(num)
    return render_template(
        "book.html", obj=obj
        )


@app.route("/book/<num>/edit/")
def book_edit(num):
    num = int(num) + 2
    excel = load_workbook("tales.xlsx")
    page = excel["Sheet"]
    tale = page[f"A{num}"]
    author = page[f"B{num}"]
    image = page[f"C{num}"]
    obj = [tale.value, author.value, image.value, num]
    return render_template("book_edit.html", obj=obj)


@app.route("/book/<num>/save/", methods=["POST", "GET"])
def book_save(num):
    if request.method == "POST":
        num = int(num)
        excel = load_workbook("tales.xlsx")
        page = excel["Sheet"]
        form = request.form
        page[f"A{num}"] = form["tale"]
        page[f"B{num}"] = form["author"]
        page[f"C{num}"] = form["image"]
        excel.save("tales.xlsx")
        return render_template("saved.html")
    else:
        print("this method is get")

@app.route("/add/")
def book_add():
    return render_template("book_add.html")

@app.route("/save", methods=["POST", "GET"])
def book_new_save():
    if request.method == "POST":
        f = request.form
        print(f["author"], f["book"])
        excel = load_workbook("tales.xlsx")
        page = excel["Sheet"]
        last = len(page["A"]) + 1
        page[f"A{last}"] = f["book"]
        page[f"B{last}"] = f["author"]
        excel.save("tales.xlsx")
        return "saved successfully"
    else:
        print("error")