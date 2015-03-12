# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app


frontend = Blueprint('frontend', __name__)


@frontend.route('/experiment1')
def experiment1():
    # current_app.logger.debug('debug')

    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client.encode
    experiments = list(db.experiment.find())
    
    return render_template('experiment1.jade', ct=len(experiments), experiments=experiments)

@frontend.route('/experiment')
def experiment():
    # current_app.logger.debug('debug')

    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client.biomics
    experiments = list(db.roadmap.find())
    
    return render_template('experiment.jade', ct=len(experiments), experiments=experiments)



@frontend.route('/')
def index():
    current_app.logger.debug('debug')

    return render_template('index.jade')