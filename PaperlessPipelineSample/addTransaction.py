from clicknium import clicknium as cc, ui, locator
from clicknium.core.models.web.browsertab import BrowserTab
import pandas

# Read records from Excel file data.xlsx
def read_excel(excel_file:str, sheet_name: str = 'Sheet1'):
    excel_date_df = pandas.read_excel(excel_file, sheet_name)
    excel_date_df = excel_date_df.where(excel_date_df.notnull(), None)
    dicts = excel_date_df.to_dict(orient='records')
    return dicts

# fill each row data to Transaction form
def fill_tran(rec, browser: BrowserTab):

    # Get fileds from excel row data
    name = rec['name']
    mls = str(rec['mls'])
    status = rec['status']
    label = rec['label']
    listingDate  = rec['listingDate']
    acceptDate  = rec['acceptDate']
    closeDate = rec['closeDate']
    seller = rec['sellerName']
    buyer = rec['buyerName']
    listPrice = str(rec['listPrice'])
    salePrice = str(rec['salePrice'])
    commission = str(rec['commission'])
    listingAgent = rec['listing agent']
    buyingAgent = rec['buying agent']

    print("Add transaction for: ", name)

    # Fill in name and mls
    browser.find_element(locator.plp.trans.name).set_text(name)
    browser.find_element(locator.plp.trans.mls).set_text(mls)
    
    # Select status and lable by mouse clicking
    browser.find_element(locator.plp.trans.select_status).click()
    browser.find_element(locator.plp.trans.li_status, {'status': status} ).click()
    browser.find_element(locator.plp.trans.select_label).click()    
    browser.find_element(locator.plp.trans.li_label, {'label': label} ).click()    
    
    # Set several date
    browser.find_element(locator.plp.trans.listed_date).set_text(listingDate)
    browser.find_element(locator.plp.trans.accepted_date).set_text(acceptDate)
    if(closeDate != ''): 
        browser.find_element(locator.plp.trans.closed_date).set_text(closeDate)

    # Set the seller, buyer, and price info
    browser.find_element(locator.plp.trans.seller).set_text(seller)
    browser.find_element(locator.plp.trans.buyer).set_text(buyer)
    browser.find_element(locator.plp.trans.list_price).set_text(listPrice)
    browser.find_element(locator.plp.trans.sale_price).set_text(salePrice)
    browser.find_element(locator.plp.trans.commission).set_text(commission)

    # Set the agents by searching the name
    # listing agent
    browser.find_element(locator.plp.trans.searchagents).set_text(listingAgent)
    cc.wait_appear(locator.plp.trans.qcManagement,{'agent':listingAgent});    
    browser.find_element(locator.plp.trans.checkbox_listing_agents).set_checkbox('check')    

    # buying agent
    browser.find_element(locator.plp.trans.searchagents).set_text(buyingAgent)
    cc.wait_appear(locator.plp.trans.qcManagement,{'agent':buyingAgent});
    browser.find_element(locator.plp.trans.checkbox_selling_agents).set_checkbox('check')
    
    # submit the transaction
    browser.find_element(locator.plp.trans.addTransaction).click()


# Entry point of the script
if __name__ == "__main__":
    # Attach to an opened edge browser
    # to open a new browser, use cc.edge.open(url) and login to the platform
    # you may refer to login.py for the login automation process
    tab = cc.edge.attach_by_title_url(url="https://app.paperlesspipeline.com/tx/add/")

    # read data from excel
    data = read_excel('data.xlsx')
    for d in data: 
        fill_tran(d, tab)
        # add a  new transaction by clicking "Add Transaction" button
        tab.find_element(locator.plp.trans.span_addtransaction).click()
