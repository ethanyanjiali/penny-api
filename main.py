import penny

app = penny.create_app()

if __name__ == '__main__':
    config = penny.get_config()
    app.run(host='127.0.0.1', port=config.PORT, debug=config.DEBUG)
