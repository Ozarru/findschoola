class Exceptions :
    def __init__(self) :
        pass
    def exceptions(self,data) :
        KEYS = ["amount", "currency", "return_url", "notify_url", "customer_name", "customer_surname", "transaction_id"]
        to_add = []
        for key in KEYS :
            if key not in list(data.keys()) :
                to_add.append("{} is required".format(key))
        if  to_add != [] : 
            return to_add
        