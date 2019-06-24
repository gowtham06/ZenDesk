from MongoConnect import *
import pprint,sys
from os import listdir
from os.path import isfile, join

def print_rows(json_documents):
    #print the rows in required format
    try:
        nos_documents=len(json_documents)
        for i in range(nos_documents):
            print("---------------------------------------------")
            print("Row number:%s"%(str(i+1)))
            for key in json_documents[i]:
                # line_string+=key.strip()+"\t\t\t\t"+str(json_documents[i][key]).strip()+"\n"
                sys.stdout.write("%-50s %-200s\n" % (key,json_documents[i][key]))
    except Exception :
        return False
        
def print_searchable_fields(mongoConnect):
    #function to print the searchable field
    try:
        field_map=mongoConnect.get_collection_field_map()
        for key,value in field_map.items():
            print("--------------------------------------------")
            print("Search %s with "%key.upper())
            for field in value:
                print(field)
        print("--------------------------------------------")
    except Exception:
        return False
            
        
def search_menu(mongoConnect):
    #function to implement the search menu
    try:
        print("""Select 1) Users or 2) Tickets" or 3) Organizations """)
        input_2=input()
        collection_list=mongoConnect.get_collecton_list()
        collection_dict=mongoConnect.get_collection_field_map()
        if input_2 in ["1","2","3"]:
            if input_2=="1":
                collection_name=[item for item in collection_list if item.lower()=="Users".lower()][0]
            elif input_2=="2":
                collection_name=[item for item in collection_list if item.lower()=="Tickets".lower()][0]
            else:
                collection_name=[item for item in collection_list if item.lower()=="Organizations".lower()][0]
            print("""Enter search term""")
            search_term=input()
            if search_term not in collection_dict[collection_name]:
                print("""Invalid, option, Press 'Enter' to continue""")
                input()
            else:
                print("""Enter search value""")
                search_value=input()
                documents=mongoConnect.execute_query(collection_name,search_term,search_value)
                if not documents:
                    print("Searching %s for %s with a value of %s"%(collection_name,search_term,search_value))
                    print("No results found")
                else:
                    print_rows(documents)
                
        else:
            print("""Invalid, option, Press 'Enter' to continue""")
            input()
    except Exception:
        return False
        
def command_line():
    # wrapper function for command line app
    try:
        db_name="zendesk"
        port=27017
        host_name="localhost"
        mongoConnect=MongoConnection(host_name,port,db_name)
        execute_flag=True
    
        print("Welcome to Zendesk Search")
        print("""Type 'quit' to exit at any time, Press 'Enter' to continue""")
        input_temp=input()
        if input_temp=="quit":
            execute_flag=False
        while execute_flag:
            print("""Select search options:\n\t\t* Press 1 to search Zendesk\n\t\t* Press 2 to view list of searchable fields\n\t\t* Type 'quit' to exit""")
            input_1=input()
            if input_1=='quit':
                execute_flag=False
                break
            elif input_1=="1":
                search_menu(mongoConnect)
            elif input_1=="2":
                print_searchable_fields(mongoConnect)
        return True
    except Exception :
        return False


if __name__ == "__main__":
    command_line()
    