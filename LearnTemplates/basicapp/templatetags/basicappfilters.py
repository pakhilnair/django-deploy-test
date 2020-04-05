from django import Template

register = Template.Library()

def cut_func(value, arg):
    return value.replace(arg,"")

register.filter("cut",cut_func)
