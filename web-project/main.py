import web

urls = (
    '/', 'index'
)

app = web.apllication(urls, )


class index:
    def GET(self, name):
        print("Hello", name, "How are you today")


if __name__ == "_main_":
    app.run()
