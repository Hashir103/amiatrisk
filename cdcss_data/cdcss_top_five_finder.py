'''cdcss_top_five_finder.py - This file is used for testing the top 5 per demographic'''
import csv
import re

def getTopDiseases(province, sex, age):
    if sex == '1':
        sex = 'Males'
    else:
        sex = 'Females'

    if province == '1':
        province = 'British Columbia'
    elif province == '2':  
        province = 'Alberta'
    elif province == '3':
        province = 'Saskatchewan'
    elif province == '4':
        province = 'Manitoba'
    elif province == '5':
        province = 'Ontario'
    elif province == '6':
        province = 'Quebec'
    elif province == '7':
        province = 'New Brunswick'
    elif province == '8':
        province = 'Nova Scotia'
    elif province == '9':
        province = 'Prince Edward Island'
    elif province == '10':
        province = 'Newfoundland and Labrador'
    elif province == '11':
        province = 'Yukon'
    elif province == '12':
        province = 'Northwest Territories'
    else:
        province = 'Nunavut'

    age = int(age)

    ages = [
        [0, 19],
        [20, 34],
        [35, 49],
        [50, 64],
        [65, 79]
    ]

    for x in ages:
        if x[1] >= int(age):
            age = x
            break

    files = [
    "cdcss_data/diseases_regression/cardiovascular_diseases/hypertension.csv",
    "cdcss_data/diseases_regression/cardiovascular_diseases/ischemic_heart_disease.csv",
    "cdcss_data/diseases_regression/cardiovascular_diseases/heart_failure.csv",
    "cdcss_data/diseases_regression/cardiovascular_diseases/acute_myocardial_infarction.csv",
    "cdcss_data/diseases_regression/cardiovascular_diseases/schizophrenia.csv",
    "cdcss_data/diseases_regression/cardiovascular_diseases/stroke.csv",
    "cdcss_data/diseases_regression/chronic_respiratory_diseases/chronic_obstructive_pulmonary.csv",
    "cdcss_data/diseases_regression/chronic_respiratory_diseases/asthma.csv",
    "cdcss_data/diseases_regression/diabetes/diabetes.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/osteoporosis.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/gout.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/health_services_arthritis.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/osteoporosis_fracture_all.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/osteoarthritis.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/rheumatoid_arthritis.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/osteoporosis_hip.csv",
    "cdcss_data/diseases_regression/musculoskeletal_disease/gout_active.csv",
    "cdcss_data/diseases_regression/neurological_diseases/epilepsy.csv",
    "cdcss_data/diseases_regression/neurological_diseases/epilepsy_active.csv",
    "cdcss_data/diseases_regression/neurological_diseases/parkinsons.csv",
    "cdcss_data/diseases_regression/neurological_diseases/dementia.csv",
    "cdcss_data/diseases_regression/neurological_diseases/sclerosis.csv"
    ]

    #province, sex, age = 'Ontario', 'Males', [20,34]
    diseases = {}
    diseaseNumbers = []

    for file in files:
        with open(file) as csvfile:
            reader = csv.reader(csvfile)
            counter = 0
            rows = []
            validAge = False

            for row in reader:
                if counter == 1:
                    minAge = int(re.sub("[^0-9]", "", row[-1])[:2])
                    if (int(age[0]) >= minAge):
                        validAge = True
                        rows.append(row)
                    
                if validAge:
                    if province == row[3] and sex == row[4] and (row[5][:2] == str(age[0]) or row[5][-2:] == str(age[1])):
                        rows.append(row)

                counter += 1
            
            if len(rows) > 0:
                disease_name = re.sub("^.*?/","",file[31:-4])
                canadaRatio = float(rows[0][2])/100_000
                demoRatio = float(rows[1][2])/100_000
                realRatio = demoRatio/canadaRatio

                if realRatio >1:
                    diseases[disease_name] = realRatio
                    diseaseNumbers.append(realRatio)

    diseaseNumbers.sort()

    diseasesItems = diseases.items()
    for item in diseasesItems:
        diseaseNumbers[diseaseNumbers.index(item[1])] = item[0]

    diseaseNumbers.reverse()

    s = f'Predicted 2023 Highest Relative Risk Factor for {province} {sex} Aged {age[0]}-{age[1]}'
    s += '<br><br>'
    counter = 1
    for x in diseaseNumbers:
        s += f'{counter}. {x.replace("_", " ").capitalize()}: {diseases[x]:.3g}' + '<br>'
        counter += 1
    
    return s