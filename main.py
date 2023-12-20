from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import xlrd

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.
# JSON_KEY_FILE = "service_account_fileSteven.json"
# JSON_KEY_FILE = "service_account_fileAnisha.json"
# JSON_KEY_FILE = "service_account_fileSRobin.json"
# JSON_KEY_FILE = "service_account_fileDivya.json"
# JSON_KEY_FILE = "service_account_fileJoney.json"
# JSON_KEY_FILE = "service_account_fileRadhe.json"
# JSON_KEY_FILE = "service_account_fileIshaan.json"
# JSON_KEY_FILE = "service_account_fileManish.json"
# JSON_KEY_FILE = "service_account_fileMohan.json"
# JSON_KEY_FILE = "service_account_fileAyush.json"
# JSON_KEY_FILE = "service_account_fileDigitAff.json"
# JSON_KEY_FILE = "service_account_fileKaivin.json"
# JSON_KEY_FILE = "service_account_fileJammy.json"
JSON_KEY_FILE = "service_account_file62.json"
# JSON_KEY_FILE = "service_account_fileSaurakshi.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
service = build('indexing', 'v3', credentials=credentials)

def insert_event(request_id, response, exception):
    if exception is not None:
        print(request_id + ' ' + str(exception))
    else:
        print(request_id + ' ' + str(response))


batch = service.new_batch_http_request(callback=insert_event)
# workbook = xlrd.open_workbook('C:\\Users\\DELL\\PycharmProjects\\BloggerExplore\\Url.xls')
workbook = xlrd.open_workbook('C:\\Users\\DELL\\PycharmProjects\\BloggerExplore2\\Url.xls')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows
curr_row = 0
while curr_row < num_rows:
    url = worksheet.cell(curr_row, 0)
    link = url.value
    if JSON_KEY_FILE == "service_account_fileSaurakshi.json":
        link = link.replace("http", "https")

    batch.add(service.urlNotifications().publish(
        body={"url": "" + link + "", "type": "URL_UPDATED"}))
    curr_row = curr_row + 1
batch.execute()
