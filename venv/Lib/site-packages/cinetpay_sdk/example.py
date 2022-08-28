from s_d_k import Cinetpay

apikey = "39955468c7a8c0cef1.68322505" #your apikey                                                              |   #
site_id = "124598" #your site_id  

example = Cinetpay(apikey,site_id)


# """"""""""""""""""""""""""""""""""""""""""PAYMENT INITIATION""""""""""""""""""""""""""""""""""""""""""""""
#                                                                                                           #
#                                                                                                           #
# --------------------------------------------Request Example---------------------------------------------  #
#                                                                                                        |  #
data = {               #                                                                                 |  #
    'amount' : 00000,  #   transaction’s amount-------                                                   |  #                                                                                                                             |
    'currency' : "XOF",  # transaction’s currency (XOF, XAF, CDF, GNF)                                   |  #                
    'transaction_id' : "GRD123456789",  # unique transaction ID                                          |  #                
    'description' : "TRANSACTION DESCRIPTION", # description of the transaction’s purpose                |  #         
    'notify_url' : "https://www.example.com/notify", # the payment notification link                     |  #
    'customer_name' : "example",  #the customer’s name                                                   |  #                                                  
    'customer_surname' : "example", #the customer’s surname                                              |  #
    'return_url' : "https://www.example.com/return",#the link of the page to which the customer will     |  #
                                                    # be redirected after the payment|  #                |  #                                                    
}                                   #                                                                    |  #
#---------------------------------------------------------------------------------------------------------  #
print("Initialization: ",example.PaymentInitialization(data))                                                                  #
#                                                                                                           #
#                   *****************************************************************                       #
#                   *                 Success Reply Example :                       *                       #
#                   *                                                               *                       #
#                   *  {                                                            *                       #
#                   *     "code": "201",                                            *                       #
#                   *     "message": "CREATED",                                     *                       #
#                   *     "description": "Transaction created with success",        *                       #
#                   *     "data": {                                                 *                       #
#                   *     "payment_token": "YOUR_TOKEN_HERE",                       *                       #
#                   *     "payment_url": "PAYMENT_URL_HERE"                         *                       #
#                   *     },                                                        *                       #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                       #
#                   *  }                                                            *                       #
#                   *****************************************************************                       #
#                                                                                                           #
#                                                                                                           #
#                   *****************************************************************                       #
#                   *                 Failure Reply Example                         *                       #
#                   *                                                               *                       #
#                   * {                                                             *                       #
#                   *    "code": "ERROR_CODE",                                      *                       #
#                   *    "message": "ERROR_MESSAGE ",                               *                       #
#                   *    "description": "ERROR_DESCRIPTION",                        *                       #
#                   *    "api_response_id": "RESPONSE_ID_HERE"                      *                       #
#                   * }                                                             *                       #
#                   *****************************************************************                       #
#                                                                                                           #
############################################################################################################



#"""""""""""""""""""""""""""""""""""""""""""CHECK TRANSACTION WITH TOKEN""""""""""""""""""""""""""""""""""""#
#                                                                                                           #
# --------------------------------------------Request Example----------------------------------------       #
#                                                                                                   |       #
token ="hglkdkf458555s"  # the payment_token obtained in the transaction initiation                 |       #                                               |       #
# ---------------------------------------------------------------------------------------------------       #                                                                                                  
print("Check transaction using token :",example.TransactionVerfication_token(token))                                                          #
#                                                                                                           #
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Success Reply Example :                       *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "00",                                          *                        #
#                  *        "message": "SUCCES",                                   *                        #
#                  *        "api_response_id": "1617808789.7749",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "operator_id": "8210407187720",                        *                        #
#                  *        "payment_method": "FLOOZ",                             *                        #
#                  *        "payment_date": "2021-04-07 14:07:24",                 *                        #
#                  *        "phone_number": "0102324373",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#                                                                                                           #                                                                                                         
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Failure Reply Example:                        *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "600",                                         *                        #
#                  *        "message": "PAYMENT_FAILED",                           *                        #
#                  *        "api_response_id": "1617808521.2503",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "payment_method": "OM",                                *                        #
#                  *        "payment_date": " ",                                   *                        #
#                  *        "phone_number": "0749012966",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #   
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#############################################################################################################




#""""""""""""""""""""""""""""""""""CHECK TRANSACTION WITH TRANSACTION ID""""""""""""""""""""""""""""""""""""#
#                                                                                                           #
# --------------------------------------------Request Example----------------------------------------       #
#                                                                                                   |       #
transaction_id = "Dt1111"  # Your transaction_id                                                    |       #
# ---------------------------------------------------------------------------------------------------       #                                                                                                  
print("Check transaction using transaction :",example.TransactionVerfication_trx(transaction_id))                                                   #      #
#                                                                                                           #
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Success Reply Example :                       *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "00",                                          *                        #
#                  *        "message": "SUCCES",                                   *                        #
#                  *        "api_response_id": "1617808789.7749",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "operator_id": "8210407187720",                        *                        #
#                  *        "payment_method": "FLOOZ",                             *                        #
#                  *        "payment_date": "2021-04-07 14:07:24",                 *                        #
#                  *        "phone_number": "0102324373",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#                                                                                                           #                                                                                                         
#                                                                                                           #
#                  *****************************************************************                        #
#                  *                 Failure Reply Example:                        *                        #
#                  *                                                               *                        #
#                  *    {                                                          *                        #
#                  *        "code": "600",                                         *                        #
#                  *        "message": "PAYMENT_FAILED",                           *                        #
#                  *        "api_response_id": "1617808521.2503",                  *                        #
#                  *        "data": {                                              *                        #
#                  *        "payment_method": "OM",                                *                        #
#                  *        "payment_date": " ",                                   *                        #
#                  *        "phone_number": "0749012966",                          *                        #
#                  *        "phone_prefix": "225"                                  *                        #
#                  *        }                                                      *                        #   
#                  *    }                                                          *                        #
#                  *****************************************************************                        #
#                                                                                                           #
#############################################################################################################