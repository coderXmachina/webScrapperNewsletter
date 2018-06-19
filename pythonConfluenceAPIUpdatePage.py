from PythonConfluenceAPI import ConfluenceAPI #using api
import confluenceConfigTest
import json
import requests

def get_page_json(page_id, expand = False):
    if expand: #if expand is true
        suffix = "?expand=" + expand 
                              #body.storage
    else:      #if expand is false
        suffix = ""

    url="http://confluence.tmrnd.com.my:8080/rest/api/content/" + page_id + suffix
    response = requests.get(url, auth=(confluenceConfigTest.tmrndConfluenceUsername, confluenceConfigTest.tmrndConfluencePassword))
    response.encoding = "utf8"  #up until here its just a string

    json_data = json.loads(response.text) #I have the json in json_data

    #file_object  = open('currentVersion', w)

    #print("This is file_object: ", file_object)

    json_data['version'] = {"number": confluenceConfigTest.spaceCurrentVersion} #artificially put, 'hard coded'

    ### can we read/write to python file?
    #confluenceConfig.spaceCurrentVersion = confluenceConfig.spaceCurrentVersion + 1
    
    #json_data['version']['number']= 1 #artificially put
    
    print(json_data['version']) #number: 12
    #print(json_data['space']['key'])
    #print(json_data['value'])
    #print(json_data['key'])

    return(json_data)

def set_page_json(page_id,json_content):
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.put("http://confluence.tmrnd.com.my:8080/rest/api/content/" + page_id, headers=headers, data=json.dumps(json_content),
                 auth=(confluenceConfigTest.tmrndConfluenceUsername, confluenceConfigTest.tmrndConfluencePassword))
    
    return(response.text) 

def confirm_Success(page_id):
    print("\nSuccessfully fetch page with id:")
    print(page_id)
    
def confirm_Update_Success(page_id):
    print("\nPage Updated")
    print(page_id)
    
###############################################################################
   
get_page_json("8094285", "body.storage") #Call function to get my test space

confirm_Success("8094285")

json_dat = get_page_json("8094285", "body.storage")

new_json_data = json_dat                                                                                                              #make it equivalent
new_json_data['id'] = json_dat['id']                                                                                                  #same id
new_json_data['type'] = json_dat['type']                                                                                              #same type
new_json_data['title'] = json_dat['title']                                                                                            #same title
new_json_data['type'] = json_dat['type']                                                                                              #same type
new_json_data['version'] = {"number": json_dat['version']['number']}                                                                  #plus 1 to version
#if not 'key' in json_dat:                                                                                                            #set key, not sure how to do it
    #new_json_data['key'] = json_dat['space']['key']
#else:
    #new_json_data['key'] = json_dat['key']
bodyDict = '<h1>Latest on Vulnerability Assessment</h1><p>Latest News on Vulnerability Assessment. Page changed on 5/6/2018</p><p>Welcome to Confluence</p><p><table><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr><tr><td>Jill</td><td>Smith</td><td>50</td></tr><tr><td>Eve</td><td>Jackson</td><td>94</td></tr></table><h1>Latest on Malware</h1><p>Interesting things from the realm of Malware</p></p>'

new_json_data['body'] = {'storage':{'value':bodyDict,'representation':'storage'}}   #set body...

#I'm not updating it...
print(set_page_json('8094285',new_json_data)) #now just send it all in

print("Page has been changed");
