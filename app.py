import itertools

import json
import pandas as np
from flask import Flask, render_template, request
import pickle

import matplotlib.pyplot as plt 



app = Flask(__name__)

steel_model = pickle.load(open('steel_model.pkl', 'rb'))

plastics_model = pickle.load(open('plastics_model.pkl', 'rb'))

iron_model = pickle.load(open('iron_model.pkl', 'rb'))

aluminium_model = pickle.load(open('aluminium_model.pkl', 'rb'))

rubber_model = pickle.load(open('rubber_model.pkl', 'rb'))

glass_model = pickle.load(open('glass_model.pkl', 'rb'))

copper_model = pickle.load(open('copper_model.pkl', 'rb'))


@app.route('/')
def home():
       return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        startYear = request.form['startyear']
        endYear = request.form['endyear']
        difference = int(endYear) - int(startYear)
        
        result = []
        s = "value"
        for i in range(0,difference):
            res = (str(s)+str(i))
            result.append(int(request.form[res]))
        
        print(result)
        
        steel_output = []
        plastics_output = []
        iron_output = []
        rubber_output = []
        aluminium_output = []
        glass_output = []
        copper_output = []
        
        years = []
        start = int(startYear)
        end = int(endYear)

        next = (start % 100) + 1
        snext = ""
        while start < end:
            snext = str(start) +'-'+ str(format(next, '02d'))
            years.append(snext)
            start += 1
            next += 1


        for i in result:
            steel = steel_model.predict([[i]])
            steel_output.append(steel[0][0].round(2))
            
            plastics = plastics_model.predict([[i]])
            plastics_output.append(plastics[0][0].round(2))

            iron = iron_model.predict([[i]])
            iron_output.append(iron[0][0].round(2))
            
            rubber = rubber_model.predict([[i]])
            rubber_output.append(rubber[0][0].round(2))

            aluminium = aluminium_model.predict([[i]])
            aluminium_output.append(aluminium[0][0].round(2))

            glass =  glass_model.predict([[i]])
            glass_output.append(glass[0][0].round(2))

            copper = copper_model.predict([[i]])
            copper_output.append(copper[0][0].round(2))

        # years_predict = []
        steel_predict = []
        plastic_predict = []
        iron_predict = []
        rubber_predict = []
        aluminium_predict = []
        glass_predict = []
        copper_predict = [] 

        # years_predict = result
        steel_predict = steel_output
        plastic_predict = plastics_output
        iron_predict = iron_output
        rubber_predict = rubber_output
        aluminium_predict = aluminium_output
        glass_predict = glass_output
        copper_predict = copper_output
        
        print(steel_predict)
        print(plastic_predict)
        print(iron_predict)
        print(rubber_predict)
        print(aluminium_predict)
        print(glass_predict)
        print(copper_predict)
        # print(years_predict)



        steel_to_tabarle = []
        years_to_table = []
        diff = 0
        d = 0

        years_table = []
        steel_table = []


        return render_template("index.html", 
                            startYear=" Your Starting Year for Prediction is {} ".format(startYear),
                            endYear="Your Ending Year for Prediction is {} ".format(endYear),
                                years_to_render = str(years)[1:-1].replace(',',' ').replace("'",' '),
                                years = years,
                                steel_to_render = str(steel_predict)[1:-1].replace(',',' '),       
                                steel_table = steel_predict,
                                start = startYear ,
                                end  = endYear ,
                                plastic_to_render = str(plastic_predict)[1:-1].replace(',',' '),
                                plastic_table = plastic_predict, 
                                iron_to_render = str(iron_predict)[1:-1].replace(',',' '),
                                iron_table = iron_predict,
                                rubber_to_render = str(rubber_predict)[1:-1].replace(',',' ' ),
                                rubber_table = rubber_predict,
                                diff = int(endYear)-int(startYear),
                                d = diff,
                                aluminium_to_render = str(aluminium_predict)[1:-1].replace(',',' '),
                                aluminium_table = aluminium_predict,
                                glass_to_render = str(glass_predict)[1:-1].replace(',',' '),
                                glass_table=glass_predict,
                                copper_to_render = str(copper_predict)[1:-1].replace(',',' '),
                                copper_table=copper_predict,
                                Years = "Years",
                                Materials = "Materials",
                                Steel = "Steel",
                                Plastic = "Plastic",
                                Iron = "Iron",
                                Rubber = "Rubber",
                                Aluminium = "Aluminium",
                                Glass = "Glass",
                                Copper = "Copper"
                            )











#         steel_output = []
#         plastics_output = []
#         iron_output = []
#         rubber_output = []
#         aluminium_output = []
#         glass_output = []
#         copper_output = []
        
#         years = []
#         start = int(startYear)
#         end = int(endYear)

#         next = (start % 100) + 1
#         snext = ""
#         while start <= end:
#             snext = str(start) +'-'+ str(format(next, '02d'))
#             years.append(snext)
#             start += 1
#             next += 1


#         for i in result:
#             steel = steel_model.predict([[i]])
#             steel_output.append(steel[0][0].round(2))
            
#             plastics = plastics_model.predict([[i]])
#             plastics_output.append(plastics[0][0].round(2))

#             iron = iron_model.predict([[i]])
#             iron_output.append(iron[0][0].round(2))
            
#             rubber = rubber_model.predict([[i]])
#             rubber_output.append(rubber[0][0].round(2))

#             aluminium = aluminium_model.predict([[i]])
#             aluminium_output.append(aluminium[0][0].round(2))

#             glass =  glass_model.predict([[i]])
#             glass_output.append(glass[0][0].round(2))

#             copper = copper_model.predict([[i]])
#             copper_output.append(copper[0][0].round(2))

#         years_predict = []
#         steel_predict = []
#         plastic_predict = []
#         iron_predict = []
#         rubber_predict = []
#         aluminium_predict = []
#         glass_predict = []
#         copper_predict = [] 

#         years_predict =result 
#         steel_predict = steel_output
#         plastic_predict = plastics_output
#         iron_predict = iron_output
#         rubber_predict = rubber_output
#         aluminium_predict = aluminium_output
#         glass_predict = glass_output
#         copper_predict = copper_output
 
#         data = { 
#             "steel_chart":steel_predict,
#             "plastic_chart":steel_predict,
#             "iron_chart":steel_predict,
#             "rubber_chart":steel_predict,
#             "aluminium_chart":steel_predict,
#             "glass_chart":steel_predict,
#             "copper_chart":steel_predict
#             }
#         return data








if __name__ == '__main__':
   app.run(use_reloader = True,debug=True)















































