from flask import render_template, request, Blueprint
from your_blogs.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_created.desc()).paginate(per_page=5, page = page)
    return render_template('home_page.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')