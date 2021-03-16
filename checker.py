from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_checker():
    return render_template("checker.html", rows=8, columns=8)

@app.route('/<int:columns>')
def rows_check(columns):
    return render_template("checker.html", rows=8, columns=columns)

@app.route('/<int:rows>/<int:columns>')
def rows_columns_check(rows, columns):
    return render_template("checker.html", rows=rows, columns=columns)

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def rows_columns_colors_check(rows, columns, color1, color2):
    return render_template("checker.html", rows=rows, columns=columns, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
