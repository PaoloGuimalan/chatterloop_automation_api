class Persistent:
    count = []
    
    # def __init__(self):
    #     self = self
        
    def rewrite_stream(self, userID, newcount):
        # print(newcount)
        self.count.append({
            "userID": userID,
            "message": newcount
        })
    
    def get_stream(self, userID):
        # print(len(self.count))
        filteredarray = [flt for flt in self.count if flt["userID"] == userID]
        
        if len(filteredarray) == 0:
            return ""
        else:
            return filteredarray[len(filteredarray) - 1]["message"]