from flask import render_template, redirect, url_for, request, flash
from . import main
from .. import db
from ..models import User, Share, Question
import random
from app.main.forms import ShareForm, QuestionForm


@main.route('/index/<uid>', methods=['GET', 'POST'])
def index(uid):
    user = User.query.get(uid)
    share_form = ShareForm()
    question_form = QuestionForm()
    return render_template('index.html', user=user,share_form=share_form,question_form=question_form,
                           rand=random.randint(1000,9999))


@main.route('/index/delete_share/<uid>/<sid>', methods=['GET', 'POST'])
def delete_share(uid, sid):
    share = Share.query.get(sid)
    if share:
        try:
            db.session.delete(share)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除分享出错')
            db.session.rollback()
    else:
        flash('没有这条分享')
    return redirect(url_for('index', uid=uid))


@main.route('/index/delete_question/<uid>/<qid>', methods=['GET', 'POST'])
def delete_question(uid, qid):
    question = Question.query.get(qid)
    if question:
        try:
            db.session.delete(question)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除问题出错')
            db.session.rollback()
    else:
        flash('没有这条问题')
    return redirect(url_for('index', uid=uid))

