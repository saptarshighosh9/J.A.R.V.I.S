import os
import datetime
from random import randint
import platform
import speech
import pygame, sys
from pygame import *
import urllib
import urllib2
import webbrowser
import datetime
import sys
import subprocess

pygame.init()


print "\n \n \n ******************************************* J . A . R . V . I . S *********************************************************\n\n"
speech.say("System set up initiated")
speech.say("All modules included")
print "                                      S y s t e m       C a p a b i l i t i e s          \n" 
print "------------------------------------------------------------------------------------------------------------------------------- \n \n"
print "                                             Status : Online \n \n"
print "                                           1.  Voice activation -Browser.\n"
print "                                                                     - www.google.com \n"
print "                                                                     - www.youtube.com \n"
print "                                                                     - www.facebook.com \n"
print "                                                                -Picture Directory \n"
print "                                                                -Video Directory \n"
print "                                                                -Music \n"
print "                                                                -Games Directory\n"
print "                                                                -Movie Directory\n"
print "                                           2.  Date and Time  \n"


speech.say("Nice to see you sir")
speech.say("Jurvis is up and online in your service.")

#picture
p1="Pictures"
p2="Can u open my pictures"
p3="Open my pictures" 
p4="Can you open picture library for me"
p5="Open picture library for me"


#video
v1="Videos"
v2="Can u open my videos"
v3="Open my videos" 
v4="Can you open video library for me"
v5="Open video library for me"




while True:
    
    phrase = speech.input()
    now=datetime.datetime.now()
    y=now.year
    m=now.month
    d=now.day
    h=now.hour
    mi=now.minute   
    if h>11:
       h=h-12
       pat="The current system time is %s %s P M"%(str(h),str(mi))   
    else:
       if h==0:
       	  h=12     
       pat="The current system time is %s %s A M"%(str(h),str(mi))  	
    if m==1:
      month="January"
    elif m==9:
      month= "September"
    elif m==10:
      month= "November"
    elif m==11:
      month= "December"	
    dat="This is %s"%(str(d))
    dat+="%s"%(month)
    dat+="%s"%(str(y))

  
 ##################### TALK ###############################################
    
    if phrase== "Hello jurvis":
       speech.say("Hello sir.")   
    
    elif phrase== "Jurvis"  :
       speech.say("what is it sir")    
    elif phrase== "Your name"  :
       speech.say("Hello, I am JARVIS , build with intel core i3")    

 ################### INTERNET /NETWORKING #################################
    elif phrase== "Browser"  :
       speech.say("Starting google chrome")
       webbrowser.open("www.google.com")
    elif phrase== "Google":
       speech.say("Looking for google.com ")
       webbrowser.open("www.google.com")
    elif phrase== "Youtube":
       speech.say("Opening youtube.com ")  
       webbrowser.open("www.youtube.com")
    elif phrase== "Facebook":
       speech.say("opening facebook.com ")  
       webbrowser.open("www.facebook.com")   
############################################################################

############################# PICTURE ####################################
    elif phrase== p1 or  phrase== p2 or phrase== p3 or phrase== p4 or phrase== p5  :
       speech.say("Opening picture library for u sir")  
       os.startfile("C:\Users\Gooblu\Pictures")
    elif phrase == "Movies":
       speech.say("Opening movies directory ")
       os.startfile("A:\movies")
    elif phrase == "My  games":
       speech.say("Opening game directory ")
       os.startfile("A:\Games")
    elif phrase == "My programs":
       speech.say("Opening your program directory")
       os.startfile("B:\My Program")   
############################# video ###################################       
    elif phrase== v1 or  phrase== v2 or phrase== v3 or phrase== v4 or phrase== v5  :
       speech.say("Opening video library for u sir")  
       os.startfile("C:\Users\Gooblu\Videos")
    elif phrase=="Music":
       pp=randint(1,7)	    
       sttt="C:\Users\Gooblu\Music\\%s.mp3"%(pp)
 
       speech.say("Starting music for you sir ")
       speech.say("I will also be enjoying the music .")
       speech.say(" Switching system to manual")
       
       
       speech.say("Close the music file to switch to control mode. ")
       os.startfile(sttt)
############################################################################ 
    elif phrase== "Open c drive"  :
       speech.say("Opening c drive") 
       os.startfile("C:\\")
    elif phrase== "What is the correct date" :
       speech.say(dat) 
    elif phrase== "Tell me the time" :
    	   
       speech.say(pat)  	    
#############################################################################
    
############################## Appreciation ##############################       
    elif phrase=="Grate"  :
       speech.say("Thank you sir ")    
    elif phrase=="Nothing"  :
       speech.say("Ok sir ")    
    elif phrase == "Offline":
       speech.say("Jurvis is offline.Closing system")
       break
    else:
       speech.say("")	
       
       
    
    
    
