from flask import Flask, request

app = Flask("bank_web_app")

# bank REST api
# get /customers
# get /customers/id


@app.route("/customers/<int:customer_id>")
def get_customer(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    print(request)
    return 'test'

@app.route("/customers")
def get_customers():
    print(f"called /customers")
    print(request)
    return 'test'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# running from commandline or code
# debugging
if __name__ == '__main__':
    app.run(debug=True)