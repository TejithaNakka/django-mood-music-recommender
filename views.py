
from django.shortcuts import render, redirect
from django.http import HttpResponse
from detect import webcam
import random as re


# Create your views here.
happy=["Arere Yekkada","Baguntundhi Nuvvu Navvithe","Choosa Choosa","Crazy Feeling","Hoyna Hoyna","Hrudayamaa","Inthandham","Kalavathi","Kumkumala","Neetho Vunte","Nuvvunte Naa Jathagaa","Padi Padi Leche","Ramuloo Ramulaa","Samajavaragamana"]
angry=["Bhayapadi Adivantha","Bhu Bhu Bhujangam Ditthai Tarangam","Kammukonna Cheekatlona","Karraata Kurraat","Katthula Toh","Thudilenidhi","Usure Poyene","Vilaya Pralaya Moorthy"]
disgust=["Choododde Nannu","Ee Manase Se Se","Em Cheppanu","Hrudayam Jaripe","Inthena Inthena","Manakadha","Okariki Okaru","Raletti","Sakhiyae","Sandram Lona Neerantha","Tharagathi Pathos","Vellipomakey","Vellipove Vellipove","Yemaiundacho"]
neutral=["Cheliya","Eeru Vaka","Manasuna Manasi","Na Kanne Hamsa","Poovullo Daagunna","Preminche Premavaa","Rave Naa Cheliya","Tholisaari","Vachinda Megham","Ye Mantramo"]
sad=["Adiga Adiga","Emai Poyave","Mate Rani Maina","Nammaka Thappani","Nanu Preminchananu","Nee Selavadigi","O Priya O priya","Prapanchamantha"]
fear=["Bhayapadi Adivantha","Bhu Bhu Bhujangam Ditthai Tarangam","Kammukonna Cheekatlona","Karraata Kurraat","Katthula Toh","Thudilenidhi","Usure Poyene","Vilaya Pralaya Moorthy"]
surprised=["Sivangivey","Ramuloo Ramulaa","Inthena Inthena","Maanini","I Go Crazy","Hai Rama Orike","New York Nagarama"]
global data
son=[1,2,3,4]

def home(request):
    
    global happy,angry,disgust,neutral,sad,fear,son
    data=webcam.modelno()
    print(data)
    
	
    if(data=='Happy'):
        son=happy
        
        
    elif(data=='Angry'):
       
        son=angry
    elif(data=='Disgust'):
        
        son=disgust
    elif(data=='Fear'):
        
        son=fear
    elif(data=='Sad'):
        
        son=sad
    elif(data=='Neutral'):
       
        son=neutral
    
    print(son)
    game=re.choice(son) 
    return render(request,'detect/home.html',{'song':game,'emotion':data})
    
