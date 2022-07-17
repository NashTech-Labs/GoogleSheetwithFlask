# Flask Setup
import os
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# configure the service account
path_to_creds = "credentials.json"
credential = ServiceAccountCredentials.from_json_keyfile_name(path_to_creds,
                        ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)

# connecting sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/12g-lce2EdDbJXGEUjcRW1saQYxHbTcCiscLp5pYImjE/edit?usp=sharing'
gsheet = client.open_by_url(sheet_url)

#get all sheets available
@app.route('/', methods=["GET"])
def total_sheets():
    sheets = []
    for sheet in gsheet.worksheets():
        sheet_title = list(sheet.__dict__['_properties'].items())[1]
        sheets.append(sheet_title)
    return jsonify(sheets)

#get data of paticular sheet
@app.route('/data/<sheet_title>/', methods=["GET"])
def data(sheet_title):
    return jsonify(gsheet.worksheet(sheet_title).get_all_records())

#create a new sheet
@app.route('/create/<string:sheet_title>/', methods=["POST"])
def create(sheet_title):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        req = request.get_json()
        print(req)
        print(type(req),"\n\n")
        row,column = req["rows"],req["columns"]
        gsheet.add_worksheet(title=sheet_title, rows=row, cols=column)
        sheet = gsheet.worksheet(sheet_title)
        return total_sheets()
    else:
        return 'Use Header as "Content-Type: application/json"'
    

# add data to a sheet
@app.route('/add_data/<string:sheet_title>/', methods=["POST"])
def add(sheet_title):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        req = request.get_json()
        sheet = gsheet.worksheet(sheet_title)
        row = [req["id"], req["name"], req["email"]]
        row_number = 2 # since first row is heading
        sheet.insert_row(row, row_number)  
        return jsonify(sheet.get_all_records())
    else:
        return 'Use Header as "Content-Type: application/json"'

#delete data
@app.route('/delete/<string:sheet_title>/<string:data>/', methods=["DELETE"])
def del_review(sheet_title,data):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sheet = gsheet.worksheet(sheet_title)
        cells = sheet.findall(str(data))
        for c in cells:
            sheet.delete_row(c.row)
        return jsonify(sheet.get_all_records())
    else:
        return 'Use Header as "Content-Type: application/json"'    

# modify or PATCH Route to update a review
@app.route('/update/<string:sheet_title>/', methods=["PATCH"])
def update(sheet_title):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sheet = gsheet.worksheet(sheet_title)
        req = request.get_json()
        cells = gsheet.findall(req["id"])
        for c in cells:
            gsheet.update_cell(c.row, 3, req["email"])
        return jsonify(gsheet.get_all_records())
    else:
        return 'Use Header as "Content-Type: application/json"'  
    


if __name__ == "__main__":
    app.run(host='0.0.0.0',use_reloader=True, debug=True, port=os.environ.get('PORT', 9191))