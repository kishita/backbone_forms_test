# -*- coding: utf-8 -*-
from backbone_form import add_lib

def index():
    add_lib()
    template ="""\
    <div style="border: 1px solid blue">\
    	<label for="{{id}}">{{title}}</label>\
    	<div>{{editor}}</div>\
    	<div>{{help}}</div>\
    </div>\
    """
    return dict(template=template)

