from tkinter import *
import urllib.request as requests
from bs4 import BeautifulSoup
import pandas as pd
import global_setting as gs
import openpyxl

class Receipt:
    # Class attribute
    receipt_data = {
                "found": 404,
                "place name": "null",
                "place cnpj": "null",
                "place address": "null",
                "total items": "null",
                "total value": "null",
                "discount": "null",
                "final value": "null",
                "date": "null",
                "buyer": "null",
                "payment": "null",
                "receipt key": "null"
    }
    item_data = [{
        "category": "null",
        "description": "null",
        "type": "null",
        "qtd": 0,
        "unit": "null",
        "unit cost": 0.0,
        "total cost": 0.0
    }]
    receipt_header = {
        "Date": "Date",
        "Place Name": "Place Name",
        "Category": "Category",
        "Description": "Description",
        "Type": "Type",
        "Qtd": "Qtd",
        "Unit": "Unit",
        "Unit Cost": "Unit Cost",
        "Total Cost": "Total Cost",
        "Receipt Key": "Receipt Key"
    }        

    # Class methods

    #region MANIPULATE RECEIPT DATA
    def printReceiptData(self, root: Tk):
        key_receipt_list = list(self.receipt_data.keys())
        val_receipt_list = list(self.receipt_data.values())
        
        for i in range(1, len(self.receipt_data)):
            if (key_receipt_list[i] == "total items"):
                for j in range(len(self.item_data)):
                    val_item_list = list(self.item_data[j].values())
                    reportLabel = Label(root, text=str(val_item_list))
                    reportLabel.pack()

            reportLabel = Label(root, text=str(val_receipt_list[i]))
            reportLabel.pack()

        return
    
    def getReceiptData(self, readAddress):
        # Autor: View || Data: 2022/12/15
        def fixSpaces(address: str):
            address = address.strip()
            flag = FALSE
            newAddress = ''
            for char in address:
                if char == '\t' or char == '\n':
                    continue
                elif char == ' ':
                    if flag == TRUE:
                        newAddress += char
                        flag = FALSE
                elif char == ',':
                    newAddress += ', '
                else:
                    newAddress += char
                    flag = TRUE

            return newAddress.replace(', , ', ', ')

        if(readAddress):
            with requests.urlopen(readAddress) as res:
                body = res.read()
                soup = BeautifulSoup(body, 'html.parser')

                # Get Place informations
                receipt_title = soup.find(id="conteudo").select('div')[1]
                place_name = receipt_title.select('div')[0].text.strip()
                place_cnpj = receipt_title.select('div')[1].text
                place_cnpj = place_cnpj.replace('CNPJ:', '').strip()

                place_address = receipt_title.select('div')[2].text.strip()
                place_address = fixSpaces(place_address)

                # Get bougth items informations
                all_tr_data = []
                for item_row in soup.find(id="tabResult").select('tr'):
                    item_name = item_row.select('td')[0].select('span')[0].text.strip()

                    item_qtd = item_row.select('td')[0].select('span')[2].text.strip()
                    item_qtd = item_qtd.replace('Qtde.:', '')
                    item_qtd = float(item_qtd.replace(',','.'))


                    item_unit = item_row.select('td')[0].select('span')[3].text.strip()
                    item_unit = item_unit.replace('UN: ', '')

                    item_unit_price = item_row.select('td')[0].select('span')[4].text.strip()
                    item_unit_price = item_unit_price.replace('Vl. Unit.:', '')
                    item_unit_price = float(item_unit_price.replace(',','.'))
                    
                    item_total = item_row.select('td')[1].select('span')[0].text.strip()
                    item_total = float(item_total.replace(',','.'))

                    all_tr_data.append({
                        "category": "null",
                        "description": item_name,
                        "type": "null",
                        "qtd": item_qtd,
                        "unit": item_unit,
                        "unit cost": item_unit_price, 
                        "total cost": item_total
                    })

                # receipt total
                receipt_total = soup.find(id="totalNota").select('div')

                if(len(receipt_total) > 5):
                    total_value = receipt_total[1].select('div > span')[0].text.strip()
                    total_value = float(total_value.replace(',','.'))

                    discount = receipt_total[2].select('div > span')[0].text.strip()
                    discount = float(discount.replace(',','.'))
                    
                    final_value = receipt_total[3].select('div > span')[0].text.strip()
                    final_value = float(final_value.replace(',','.'))
                
                else:
                    discount = 0

                    final_value = receipt_total[1].select('div > span')[0].text.strip()
                    final_value = float(final_value.replace(',','.'))
                    total_value = final_value

                total_items = receipt_total[0].select('div > span')[0].text.strip()
                total_items = float(total_items.replace(',','.'))


                # Receipt Date
                receipt_date_info = soup.find(id="infos").select('div')[0].select('div > ul > li')[0].text.strip()
                date_end_index = receipt_date_info.find("  - Via Consumidor")
                receipt_date = ''
                for i in range((date_end_index - 19), date_end_index):
                    receipt_date += receipt_date_info[i]



                # Payment form
                if len(receipt_total) > 5:
                    payment_form = soup.find(id="totalNota").select('div')[5].select('div > label')[0].text.strip()

                else:
                    payment_form = soup.find(id="totalNota").select('div')[3].select('div > label')[0].text.strip()

                # Buyer Information
                if(len(soup.find(id="infos").select('div')[2].select('div > ul > li')) > 2):
                    receipt_buyer = soup.find(id="infos").select('div')[2].select('div > ul > li')[1].text.strip()
                    receipt_buyer = receipt_buyer.replace('Nome: ', '')

                else:
                    receipt_buyer = ""

                # Receipt Key
                receipt_key = soup.find(id="infos").select('div')[1].select('div > ul > li > span')[0].text.strip()

            self.receipt_data = {
                "found": 200,
                "place name": place_name,
                "place cnpj": place_cnpj,
                "place address": place_address,
                "total items": total_items,
                "total value": total_value,
                "discount": discount,
                "final value": final_value,
                "date": receipt_date,
                "buyer": receipt_buyer,
                "payment": payment_form,
                "receipt key": receipt_key
            }
            self.item_data = all_tr_data

        else:
            print("QR Code address cannot exist")
            return FALSE

        return TRUE
    
    #endregion

   
    #region MANIPULATE SHEETS
    def updateSheets(self):
        def writerBackUp(header, data, file_name: str):
            pd.DataFrame(data).to_csv(file_name, columns=header, index=False)

        def getRowValues(data: dict):
            val = list(data.values())
            return val

        def updateSheet(data: list):
            book = openpyxl.load_workbook(gs.__expenses__)
            sheet = book[gs.__expenses_page__]

            for i in range(len(data)):
                val = getRowValues(data[i])
                sheet.append(val)

            book.save(gs.__expenses__)


        receipt_date =  self.receipt_data["date"].replace('/', '_').replace(' ', '_').replace(':', '_')
        filename = gs.__data_base__ + "/expenses/" + receipt_date + ".csv"
        header = self.receipt_header
    
        data = []
        receipt = self.receipt_data

        for i in range(len(self.item_data)):
            item = self.item_data[i]

            item_row = {
                'Date': receipt['date'],
                'Place Name': receipt['place name'],
                'Category': item['category'],
                'Description': item['description'],
                'Type': item['type'],
                'Qtd': item['qtd'],
                'Unit': item['unit'],
                'Unit Cost': item['unit cost'],
                'Total Cost': item['total cost'],
                "Receipt Key": receipt['receipt key']
            }

            data.append(item_row)

        writerBackUp(header, data, filename)
        updateSheet(data)

    


    #endregion