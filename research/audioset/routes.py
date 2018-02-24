from flask import Flask, render_template_string

app = Flask(__name__)


# First example
# @app.route('/')
# def hello_world():
#     return 'Welcome to our Library!'

# Second example
# @app.route('/')
# def hello_world():
#     html = """
#         <html>
#             <h1>Welcome to our Library!</h1>
#             {authors_ul}
#         </html>
#     """
#     authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
#
#     authors_list = "<ul>"
#     authors_list += "\n".join(["<li>{author}</li>".format(author=author) for author in authors])
#     authors_list += "</ul>"
#     # build an <ul> with authors
#     return html.format(authors_ul=authors_list)

# Third example
@app.route('/')
def hello_world():
    library_name = "Poe"
    html = """
        <html>
            <h1>Welcome to {{library}} library!</h1>
            <ul>
                {% for author in authors %}
                    <li>{{author}}</li>
                {% endfor %}
            </ul>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    rendered_html = render_template_string(html, library=library_name, authors=authors)

    # Using an <ul> tag add the authors using the template engine
    return rendered_html
