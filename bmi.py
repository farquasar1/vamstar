import pandas as pd
import numpy as np
import json
import argparse

def read_data(file):
    with open('data.json','r') as f:
        data = json.load(f)
    return data

def status(x):
    if x < 18.4:
        y = 'underweight'
    elif x >= 18.5 and x < 24.9:
        y = 'Normal weight'
    elif x >= 25 and x < 29.9:
        y = 'Overweight'
    elif x >= 30 and x < 39.9:
        y = 'Moderately obese'
    elif x >= 30 and x < 39.9:
        y = 'Severely obese'
    else:
        y = 'Very severely obese'

    return y

def function_BMI(mass, height):
    ''' This function calculates the Body Mass Index. 
    NB: Height cannot be negative'''
    assert height != 0, "height cannot be zero"
    assert mass > 0, "mass must be positive"

    try:
        x = 10000*float(mass) / float(height * height)

    except ZeroDivisionError:
        print("height cannot be zero")

    else:
        return x
    
def print_table(data):
    ''' This function receives the data as a list and prints a table with the body mass index 
    BMI = weight / height**2'''

    df = pd.DataFrame(data)
    bmi = []
    category = []

    for v in data:
        x_bmi = np.round(function_BMI(v['WeightKg'], v['HeightCm']),1)
        category.append(status(x_bmi))
        bmi.append(x_bmi)

    df['BMI (Kg/m2)'] = bmi
    df['BMI_category'] = category
    overweighted = df.groupby(['BMI_category']).size()['Overweight']

    print("Table of Body Mass Index \n")
    print(df)
    print('\n number of overweighted individuals = ', overweighted)
    print('\n fraction of overweighted individuals = ', str(np.round(100*overweighted / df.shape[0],2)) + ' %')

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("path", help="path of the data")
    args = parser.parse_args()
    config = vars(args)
    filepath = config['path']

    data = read_data(filepath)
    print_table(data)
    
