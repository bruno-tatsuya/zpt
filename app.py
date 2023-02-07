from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return '<p>Integration service for Zendesk</p>'


@app.get('/admin_ui')
def admin_ui():
    return_url = request.args.get('return_url')
    return render_template('admin_ui.html', return_url=return_url)

@app.post('/pull')
def pull():

    test_data = {
        "external_resources": {
          "external_id": "123456789_test",
          "message": "Please help. My printer is on fire.",
          "html_message": "Please help. <b>My printer is on fire.</b>",
          "created_at": "2023-02-06T22:48:09Z",
          "author": {
            "external_id": "FakeUserID",
            "name": "James Bon",
            "locale": "en-US"
          },
          "allow_channelback": True
        }
      }

    return jsonify(test_data), 200

@app.post('/channelback')
def channelback():
    return 'OK'

@app.get('/manifest')
def manifest():
    glitch_url = 'https://zendeskpython.glitch.me'
    data = {
        "name": "Zendesk Python",
        "id": "my-zendesk-python",
        "version": "1.0.0",
        "urls": {
            "admin_ui": f"{glitch_url}/admin_ui",
            "pull_url": f"{glitch_url}/pull",
            "channelback_url": f"{glitch_url}/channelback"
        }
    }
    return data

if __name__ == '__main__':
    app.run()