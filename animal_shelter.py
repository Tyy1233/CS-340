from pymongo import MongoClient
from bson.objectid import ObjectId


#creates variables to be stored for later
userCreate = {}
userSearch = {}
userUpdateFromTarget = {}
userUpdateToTarget = {}
userDelete = {}

class AnimalShelter(object):
    """ """
    def __init__(self, username, password):
        #init to connect to mongodb without auth
        #self.client = MongoClient('mongodb://localhost:39475')
        #init connect to mongodv with auth
        self.client = MongoClient('mongodb://%s:%s@localhost:39475/?authMechanism=DEFAULT&authSource=AAC'(username, password))
        self.database = self.client['AAC']
        
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, becuase data parameter is empty")
            
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor
    
    def read(self, data):
        cursor = self.database.animals.find_one(data)
        return cursor
    
    #Crud R Method
    def obtainReadData(self):
        for i in range(1):
            key = input("Enter Search key: ") #creates key for search
            value = input("Enter Desired Value: ") #creates value for search
            user.SearchTarget.update({key: value}) #does the search
    
    #Crud R method
    def read(self, target):
        try:
            if target is not None:
                read_result= list(self.database.animals.find(data, {"_id": False}))
                cursor = read_results 
                return cursor #prints the results
            else:
                raise Exception("Parameter is empty please try again.") #tells user that the inputs are incorrect
                return False
        except Exception as e:
            print("An exception has happened: ", e)

    #Crud Method U
    def obtainUpdateData(self):
        if fromTarget is not None:
            for i in range(1):
                key = input("Enter update Key: ")#creates key for search
                value = input("Enter Update Value: ")#creates value to search
            userUpdateFromTarget.update({key: value})#gives key and value to updater from for later
            for i in range(1):
                key = input("Enter Update Key: ")#gets the key to update
                value = input("Enter new Value: ")#gets new value to update with
            userUpdateToTarget.update({'$set': {key: value}})#completes the update
            print(userUpdateToTarget)#shows the user
            
            
    #crud method U
    def update(self, fromTarget, toTarget, count):
        if fromTarget is not None:
            if count == 1:#first attempt
                update_result = self.database.animals.update_one(fromTarget, toTarget) #updating that information
                print("Match Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))#shows count
                      
                if update_result.modified_count == 1:#makes sure that is actually counted
                    print("Update Completed")#show the user that it worked
                    print(update_result)
                    return True
                      
                else:
                    print("Something is incorrect, please enter information again")#shows user that is failed
                    return False
                      
            elif count == 2:#attempt 2
                update_result = self.database.animals.update_many(fromTarget, toTarget)
                print("Match Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == update_result.match_count:
                    print("Update Completed!")
                    print(update_result)
                    return True
                else:
                    print("Something is incorrect, please enter information again")
                    print(update_results)
                    return True
            else:
                print("Count not correct please try again")#shows that is may have worked but needs to be checked
                return False
        else:
            raise Exception("There is nothing in those search paramiters, please try again")#shows that what is being asked might not be right
        return False
    #crud method D
    def obtainDeleteData(self):
        for i in range(1):
            key = input("Enter key you wish to delete: ")#key to be searched
            value = input("Enter value you wish to delete: ")#value to be removed
            userDelete.update({key: value})#gives the information for later
    #crud method d
    def deleteData(self, target, count):
        if target is not None:
            if count == 1:#attempt 1
                try:
                    delete_result = self.database.animals.delete_one(target)#action to delete
                    #print("Delete count: " + str(delete_result.deleted_count)#telling user the count
                    if delete_result.deleted_count == 0:
                          #checking if it worked
                        print("Nothing to delete in those paramiters.")#tells user is failed
                        print(delete_result)#shows results
                        return True
                    else:
                        print("Deletion complete.")#shows that is workd
                        print(delete_result)#shows what was deleted
                        return True
                except Exception as e:#shows errors
                    print("A Error has Occured: ", e)
            elif count == 2:#attempt 2
                try:
                    delete_result = self.database.animals.delete_one(target)#action to delete
                    #print("Delete count: " + str(delete_result.deleted_count)#telling user the count
                    if delete_result.deleted_count == 0:
                          #checking if it worked
                        print("Nothing to delete in those paramiters.")#tells user is failed
                        print(delete_result)#shows results
                        return True
                    else:
                        print("Deletion complete.")#shows that is workd
                        print(delete_result)#shows what was deleted
                        return True
                except Exception as e:#shows errors
                    print("A Error has Occured: ", e)
                    return False
        else:#tells user that something was not correct in the search
            raise Exception("Nothing to delete, please try again.")
            return False
                          