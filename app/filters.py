
def register_filters(app):

    @app.template_filter()
    def pretty_date(value):
        return value.strftime('%b %d %Y')
