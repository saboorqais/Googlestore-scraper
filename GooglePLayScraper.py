### Scrapper script to scrape reviews from Google Play Store ###   
### and Apple Play Store                                     ### 



###  IMPORTS ###           
from play_scraper import search
from google_play_scraper import app ,reviews, Sort,reviews_all 
import datetime
import csv
from pprint import pprint
from app_store_scraper import AppStore
from os import path
import time

##LIST TO STORE REspective DATA
app_id_list=[]
reviews_results=[]
app_title=[]

        


##looP TO CONTROL OVER ALL ITERATION
while(True):

        ##Asking User for decsion between different store
        options=int(input("Press 1 for Google Store:\nPress 2 to exit:"))
       
        
        ##FOr google playstore
        if options==1:

                    while(True):
                            ##search key to be entered in google play search box
                            search_key=input("Enter the search query:")
                            ##using google Play library attribute search to enter keywords
                            results=search(search_key,page=10)

                            ##data to be stored over iteration    
                            data={}
                            reviews_list=list()
                            final_data={}
                            x=1
                            ##Searching in the TOP 10 Results
                            for each in results[:10]:

                                ##app id is used to determine unique app
                                pprint(str(x)+") "+each['title'])
                                app_id_list.append(each["app_id"])
                                app_title.append(each["title"])
                                x=x+1

                        
                        
                            decesion=int(input("Are these  searches related to you!!!? \nIf Yes press 1\nIf no press 2 to Enter related keywords:"))    
                            if decesion==1:
                                break

                    print("**********************************************")
                    print("**********************************************")
                    print("**********************************************")       
                    
                    decesion2=int(input("Enter the Number of the App you want to see their review:s"))
                    
                    decesion3=int(input("IF you want 100 reviews press 1:\nIF you want all reviews press 2:"))
                      ##again library used REVIEWS to get reveiws against app id

                    decesion5=input("Enter the code of the country:")

                    if decesion3==1:
                        try:
                             review,continuation_token=reviews(app_id_list[decesion-1]
                        , lang='en', # defaults to 'en'
                        country=decesion5, # defaults to 'us'
                        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                   
                    
                        )
                        except :

                            print("**********************************************")
                            print("**********************************************")
                            print("You have entered wrong country code\nDefault Country result is showing")
                            print("********************ALERT**********************")
                            print("**********************************************")
                            time.sleep(2)
                            review,continuation_token=reviews(app_id_list[decesion-1]
                        , lang='en', # defaults to 'en'
                        country="us", # defaults to 'us'
                        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                   
                    
                        )
                    if decesion3==2:

                        try:
                            review=reviews_all(app_id_list[decesion-1]
                        , lang='en', # defaults to 'en'
                        country=decesion5, # defaults to 'us'
                        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                   
                    
                        )
                        except :
                            print("**********************************************")
                            print("**********************************************")
                            print("You have entered wrong country code\nDefault Country result is showing")
                            print("********************ALERT**********************")
                            print("**********************************************")
                            time.sleep(2)
                            review=reviews_all(app_id_list[decesion-1]
                        , lang='en', # defaults to 'en'
                        country='us', # defaults to 'us'
                        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                   
                    
                        )
                    pprint(review)

             
                    print("**********************************************")
                    print("**********************************************")
                    print("**********************************************")    
                    
                    print("**********************************************")
                    print("********************ALERT**********************")
                    print("**********************************************")
                    ##If result is not accoring to the choice
                    decesion=int(input("Are You satisfied with  reviews!!!? \nIf Yes press 1\nIf no press 2 to Enter related keywords:"))    
                    if decesion==1:
                        ##OPing csv again to store data
                        ##checking if file exist not wrtitng titles to avoid redundancy 
                        if not path.exists(search_key+"Google"+".csv"):
                            with open(search_key+"Google"+".csv","a+",newline="") as f:
                                writer=csv.writer(f)
                                #gIVING TITLES
                                writer.writerow(["APP_ID", "REVIEWER NAME","COMMENT","TIME","REPLY COMMENT","LIKES","REPLY TIME","RATING"]) 
                        with open(search_key+"Google"+".csv","a+",newline="",encoding='utf-8') as f:
                                    writer=csv.writer(f)
                                    ##retreiving data to be stored in csv file
                                    for key in review:
                                            try:
                                                date=key['at'].strftime("%m/%d/%Y, %H:%M:%S")
                                            except:
                                                date="Not commented"
                                            try:
                                                reply_date=key['repliedAt'].strftime("%m/%d/%Y, %H:%M:%S")
                                            except:
                                                reply_date="Not replied" 
                                                  
                                            writer.writerow([app_title[decesion2-1], key['userName'], key['content'], date, key['replyContent'] , key['thumbsUpCount'], reply_date, key['score']])   
                    decesion=int(input("Do You want to add more ?\nIf Yes press 1\nIf no press 2 to Exit:"))
                    if decesion==2:         
                            break
                    final_data={}
                    app_id_list=[]
                    app_title=[]    
       


        if options==2:
            break            