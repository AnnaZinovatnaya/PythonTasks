# routes.py


from flask import request, redirect, render_template
from flask import current_app as app
from models import db, Keywords
from libs.rabbit_manager import global_rqueue

from sug_config import ALPHABETS, NUM_SUGGESTIONS_ON_PAGE


def add_suffixes(keyword):
    for char in ALPHABETS:
        yield '{} {}'.format(keyword, char)


@app.route('/', methods=["POST", "GET"])
def suggestions():
    if request.method == "POST":
        # search_for = search_for or 'apple'
        search_for = request.form['keyword']
        if search_for:
            return redirect('/?q={}&page=1'.format(search_for))
        else:
            return redirect('/')

    next_page = 0
    prev_page = 0
    start_index = 0

    search_for = request.args.get('q')
    app.logger.info("got request with q = '{}'".format(search_for))
    if search_for:
        suggestions = db.session.query(Keywords).filter(
           Keywords.keyword.like('%' + search_for + '%')).all()

        app.logger.info("for '{}' in base {} rows".format(
            search_for, len(suggestions)))

        if len(suggestions) < 50:
            for part in add_suffixes(search_for):
                task = {"keyword": part,
                        "country": "US",
                        "search_engine": "duckduckgo"}
                global_rqueue.publish(task)

        app.logger.debug("for '{}' found {}".format(
            search_for, suggestions
        ))

        current_page = int(request.args.get('page'))
        next_page = current_page + 1
        prev_page = current_page - 1

        if current_page == 1:
            if len(suggestions) <= NUM_SUGGESTIONS_ON_PAGE:
                next_page = None

            suggestions = suggestions[:NUM_SUGGESTIONS_ON_PAGE]
            start_index = 1
            prev_page = None

        else:
            if len(suggestions) <= NUM_SUGGESTIONS_ON_PAGE * current_page:
                next_page = None

            suggestions = suggestions[NUM_SUGGESTIONS_ON_PAGE * (current_page - 1) : NUM_SUGGESTIONS_ON_PAGE * (current_page - 1) + NUM_SUGGESTIONS_ON_PAGE]

            start_index = NUM_SUGGESTIONS_ON_PAGE * (current_page - 1) + 1
    else:
        suggestions = []

    if next_page is None:
        next_url = None
    else:
        next_url = '/?q={}&page={}'.format(search_for, next_page)

    if prev_page is None:
        prev_url = None
    else:
        prev_url = '/?q={}&page={}'.format(search_for, prev_page)
    return render_template('suggestions.html',
                           keyword=search_for,
                           suggestions=suggestions,
                           pagination=True,
                           next_url=next_url,
                           prev_url=prev_url,
                           start_index=start_index)
