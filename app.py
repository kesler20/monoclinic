from flask import redirect, url_for, render_template
from flask import Flask

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>/', methods=['POST','GET'])
def show(page):
    if page == 'login':
        redirect(url_for('logins'))

    elif page == 'account':
        redirect(url_for('accounts'))

    elif page == 'transactions':
        redirect(url_for('transactions'))
    
    elif page == 'mine':
        redirect(url_for('miners'))

    elif page == 'blockchain':
        redirect(url_for('blockchains'))
    else:
        pass
    return render_template(f'{page}.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
