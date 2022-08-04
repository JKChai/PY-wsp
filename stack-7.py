import pandas as pd

df = pd.DataFrame([{
    'itemID': '4',
    'systemSku': '210000000004',
    'defaultCost': '0.1',
    'avgCost': '0',
    'discountable': 'true',
    'tax': 'true',
    'archived': 'false',
    'itemType': 'non_inventory',
    'serialized': 'false',
    'description': 'description',
    'modelYear': '0',
    'upc': '',
    'ean': '',
    'customSku': '',
    'manufacturerSku': '',
    'createTime': '2019-10-16T16:11:20+00:00',
    'timeStamp': '2022-07-09T19:41:08+00:00',
    'publishToEcom': 'false',
    'categoryID': '3',
    'taxClassID': '1',
    'departmentID': '0',
    'itemMatrixID': '2',
    'manufacturerID': '0',
    'seasonID': '0',
    'defaultVendorID': '185',
    'Prices': {
        'ItemPrice': [{
            'amount': '0.2',
            'useTypeID': '1',
            'useType': 'Default'
        }, {
            'amount': '0.2',
            'useTypeID': '2',
            'useType': 'MSRP'
        }, {
            'amount': '0.2',
            'useTypeID': '3',
            'useType': 'Online'
        }]
    }
},{
    'itemID': '4',
    'systemSku': '210000000004',
    'defaultCost': '0.1',
    'avgCost': '0',
    'discountable': 'true',
    'tax': 'true',
    'archived': 'false',
    'itemType': 'non_inventory',
    'serialized': 'false',
    'description': 'description',
    'modelYear': '0',
    'upc': '',
    'ean': '',
    'customSku': '',
    'manufacturerSku': '',
    'createTime': '2019-10-16T16:11:20+00:00',
    'timeStamp': '2022-07-09T19:41:08+00:00',
    'publishToEcom': 'false',
    'categoryID': '3',
    'taxClassID': '1',
    'departmentID': '0',
    'itemMatrixID': '2',
    'manufacturerID': '0',
    'seasonID': '0',
    'defaultVendorID': '185',
    'Prices': {
        'ItemPrice': [{
            'amount': '0.2',
            'useTypeID': '1',
            'useType': 'Default'
        }, {
            'amount': '0.2',
            'useTypeID': '2',
            'useType': 'MSRP'
        }, {
            'amount': '0.2',
            'useTypeID': '3',
            'useType': 'Online'
        }]
    }
}])

print(df['Prices'])