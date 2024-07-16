import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# 定義 Google Sheets 相關資訊
json_keyfile = "calendar-429607-63075a14d6df.json"
scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = SAC.from_json_keyfile_name(json_keyfile, scope)
client = gspread.authorize(credentials)

# 開啟指定的 Google Sheets 表單
spreadsheet_key = "1Oe6R5yB_NvD7ebgdDGvHi0fsWtAxpIEZ237EwSvtcFs"
sheet = client.open_by_key(spreadsheet_key).sheet1

app = FastAPI()

@app.get("/")
def getAllData():
    return sheet.get_all_records()
class Info(BaseModel):
    id: int
    data: list
@app.post("/addNewEvents")
def getInformation(info: Info):
    sheet.append_row(info.data)
    return {"status": "SUCCESS", "data": info}

#dataTitle = ["date","time","events","place"]
# 新增一筆假資料
#data_values = ["03/11", "15:00", "dinner", "taipei"]
#sheet.append_row(dataTitle)
#sheet.append_row(data_values)

# 輸出結果
##print("寫入成功")
#print(sheet.get_all_values())
