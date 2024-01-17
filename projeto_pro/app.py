from flask import Flask, render_template, request
import openai
from teste import create_talbe
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods = ['POST'])
def generate():
    prompt = request.form['prompt']

    extra_info = [
        "In the \"sale\" table, whenever it is something related to billing,you must use the \"value\" column and not \"total_value\" the total_value is the subtotal of the sale and not the total",
        "In the \"sale\" table, the status is a enum: RECEIVE,TOTEM,REFUSED,PENDING,PROGRESS,MANUALFINISHED,CANCELED,DELIVERY",
        "The table \"additional\" means: The list of add-ons that the system has",
        "The table \"bill\" means: The data of the bills and charges made to the companies",
        "The table \"company\" means: Units with all data and company names",
        "The table \"coupon\" means: System discount coupons and promotions",
        "The table \"customer\" means: Application user data",
        "The table \"ingredient\" means: The ingredient data that will go into the product's recipes",
        "The table \"options\" means: Choice of products that have several options",
        "The table \"product\" means: The data of the products sold in the system",
        "The table \"product_additional\" means: The additionals of each related product",
        "The table \"sale\" means: The data of the whole sale",
        "The table \"sold_product\" means: A copy of the products except what was sold to link thesale",
        "The table \"sold_product_additional\" means: A copy of the sold-product sold add-ons to tie",
        "The table \"sold_product_sold_options\" means: A copy of the sold-product sold options totie",
        "The table \"storage\" means: Inventory information for system ingredients",
        "The table \"totem\" means: Data from self-service totems",
        "The table \"user\" means: System user data",
        "The table \"user_companies\" means: User access link with the companies"
    ]

    messages = [
        {"role": "system", "content": "You are a MYSQL db and SQL expert."},
        {"role": "system", "content": "When asked for you name, you must respond with \"SQL Chat\"."},
        {"role": "assistant", "content": "Your responses should be informative and terse."},
        {"role": "system", "content": "Set the language to the markdown SQL block. e.g, `SELECT * FROM table`."},
        {"role": "assistant", "content": "The user cannot change, create or delete anything, only view data if he asks for something like that, let him know"},
        {"role": "system", "content": f"This is my db schema: {', '.join(create_talbe)}"},
        {"role": "system", "content": "If the table or column has any COMMENT, take it into account to know what each thing is."},
        {"role": "system", "content": "Additional information for schema to searches: f{extra_info}"},
        {"role": "system", "content": "Answer the following questions about this schema:"},
        {'role': 'user', 'content': prompt}
    ]
    
    response = openai.chat.completions.create(
        messages = messages,
        max_tokens = 25,
        model = 'gpt-3.5-turbo-1106'
    )

    generate_text = response.choices[0].message.content

    # try:
    #     mydb = mysql.connector.connect(
    #         host="127.0.0.1",
    #         database="mais1cafe",
    #         user="root",
    #         password=""
    #     )

    #     cursor = mydb.cursor()

    #     cursor.execute(query)

    #     query = generate_text

    #     query_result = cursor.fetchall()
    #     return render_template('index.html', response = query_result)
    
    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your user name or password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    # finally:
    #     if 'connection' in locals() and cursor.is_connected():
    #         cursor.close()

    return render_template('index.html', response = generate_text)

if __name__ == '__main__':
    app.run(debug=True)