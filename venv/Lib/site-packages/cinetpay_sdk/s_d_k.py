import requests
try:
    from exceptions import Exceptions
except ImportError:
    from .exceptions import Exceptions

exc = Exceptions()

class Cinetpay :
    """This class allows to create Cinetpay Client"""
 
    def __init__(self,apikey,site_id):
  
        self.url_base_1 = 'https://api-checkout.cinetpay.com/v2/payment'  
        self.url_base_2 =  'https://api-checkout.cinetpay.com/v2/payment/check'
        self.apikey = apikey  
        self.site_id = site_id
                                                                                                                                     
    def PaymentInitialization(self,data_from):
        if exc.exceptions(data_from) == None :

            """Here is the Client's method which permits to Initialize a payment"""    
            r = requests.post(self.url_base_1,                                   
                    data = {                                                                                  
                        "amount": data_from['amount'],                                                                       
                        "apikey": self.apikey,                                                                       
                        "site_id": self.site_id,
                        "transaction_id":data_from['transaction_id'],                                                                    
                        "currency": data_from['currency'],                                                                                                                        
                        "description": data_from['description'],                                                             
                        "return_url:": data_from['return_url'],                                                              
                        "notify_url:": data_from['notify_url'],                                                              
                        "customer_name:": data_from['customer_name'],                                                        
                        "customer_surname:": data_from['customer_surname']                                                   
                    },                                                                                          
                )                                                                                               
                                                                                                                
            return r.json() 
        else :
            return exc.exceptions(data_from)                                                                                                                                                                                  
                                                                                                            
    def TransactionVerfication_trx(self,transaction_id) : 

        """This method permits to check or verify any transaction by transaction Id"""                                                  
                                                                  
        r = requests.post(self.url_base_2,                         
        data = {                                                                                        
        "apikey": self.apikey,                                                                               
        "site_id": self.site_id,                                                                             
        "transaction_id": transaction_id                                                                
        },                                                                                              
        )                                                                                               
                                                                                                            
        return r.json()  

    def TransactionVerfication_token(self,token) :

        """This method permits to check or verify any transaction by token""" 
                                                                                                                                                                                                     
        r = requests.post(self.url_base_2,                         
            data = {                                                                                    
            "apikey": self.apikey,                                                                           
            "site_id": self.site_id,                                                                         
            "token": token                                                                              
        },                                                                                              
        )         
        return r.json()                                                                                      
                                                                                                            

