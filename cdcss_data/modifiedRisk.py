def modRisk(risk, race, fam, disease):

# risk is an number/float
# race is a string (ex. "Black")
# fam is a string ("Yes" or "No")
# disease is the disease in string (ex. "Heart failure")

    if disease == "Acute myocardial infarction":
        if race == "African Canadian":
            modR = risk*1.5

        elif race == "Hispanic/Latino":
            modR = risk*0.8

        elif race == "Asian Canadian":
            modR = risk*0.6

        elif race == "Native Canadian":
            modR = risk*1.4     
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*2.5
  
        return modR

    if disease == "Heart failure":
        if race == "African Canadian":
            modR = risk*1.75

        elif race == "Hispanic/Latino":
            modR = risk*1.35


        elif race == "Asian Canadian":
            modR = risk*1.0

        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*2.5
            
        return modR

    if disease == "Hypertension":
        if race == "African Canadian":
            modR = risk*1.5


        elif race == "Hispanic/Latino":
            modR = risk*1.0


        elif race == "Asian Canadian":
            modR = risk*0.7
        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*1.75
            
        return modR

    

    if disease == "Ischemic heart disease":
        if race == "African Canadian":
            modR = risk*1.5


        elif race == "Hispanic/Latino":
            modR = risk*1.0


        elif race == "Asian Canadian":
            modR = risk*0.7

        elif race == "Native Canadian":
            modR = risk*1.3
        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*2.5
            
        return modR

    

    if disease == "Stroke":
        if race == "African Canadian":
            modR = risk*2.1


        elif race == "Hispanic/Latino":
            modR = risk*1.0


        elif race == "Asian Canadian":
            modR = risk*0.65

        elif race == "Native Canadian":
            modR = risk*3
        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*2.5
            
        return modR

    

    if disease == "Asthma":
        if race == "African Canadian":
            modR = risk*1.7


        elif race == "Hispanic/Latino":
            modR = risk*1.5


        elif race == "Asian Canadian":
            modR = risk*0.7
        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*3.5
            
        return modR

    if disease == "Chronic obstructive pulmonary disease (COPD)":

        if fam == "Yes":
            modR = modR*4
            
        return modR


    if disease == "Dementia, including Alzheimer's disease":
        if race == "African Canadian":
            modR = risk*1.4


        elif race == "Hispanic/Latino":
            modR = risk*1


        elif race == "Asian Canadian":
            modR = risk*0.7

        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*2.2
            
        return modR

    if disease == "Epilepsy":
        if race == "African Canadian":
            modR = risk*1.3

        
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*3
            
        return modR
    

    if disease == "Diabetes mellitus (types combined), excluding gestational diabetes":
        if race == "African Canadian":
            modR = risk*1.7
        elif race == "Hispanic/Latino":
            modR = risk*2.0
        elif race == "Asian Canadian":
            modR = risk*2.1
        elif race == "Native Canadian":
            modR = risk*3.4
        else:
            modR = risk
        if fam == "Yes":
            modR = modR*2.5
    if disease == "Osteoporosis-related fracture - hip (annual)":
        if fam == "Yes":
            modR = risk*1.75
        else:
            modR = risk
    if disease == "Osteoporosis":
        if fam == "Yes":
            modR = risk*3
        else:
            modR = risk
    if disease == "Osteoarthritis":
        if race == "African Canadian":
            modR = risk*0.7
        elif race == "Hispanic/Latino":
            modR = risk*1.0
        else:
            modR = risk
        if fam == "Yes":
            modR = modR*4.5
    if disease == "Gout and other crystal arthropathies":
        if race == "African Canadian":
            modR = risk*2.5
        else:
            modR = risk
        if fam == "Yes":
            modR = modR*4.5
    if disease == "Rheumatoid arthritis":
        if race == "African Canadian":
            modR = risk*.65
        else:
            modR = risk
        if fam == "Yes":
            modR = modR*2.5
            
    if disease == "Gout and other crystal arthropathies (active)":
        if fam == "Yes":
            modR = risk*4.5
        else:
            modR = risk
    if disease == "Use of health services for arthritis":
        if fam == "Yes":
            modR = risk*2.5
        else:
            modR = risk
    if disease == "Oseteoporosis-related fracture":
        if fam == "Yes":
            modR = risk*1.75
        else:
            modR = risk
    
    if disease == "Multiple sclerosis":


        if fam == "Yes":
            modR = risk*3
        
        else:
            modR = risk
        
        return modR
  

    if disease == "Parkinsonism, including Parkinson's disease":


        if fam == "Yes":
            modR = risk*2.5
        else: 
            modR = risk
        
        return modR


    if disease == "Schizophrenia":
        if race == "African Canadian":
            modR = risk*1.75

       
        else:
            modR = risk

        if fam == "Yes":
            modR = modR*9.0
        

    return modR


risk = float(input("Enter the General Relative Risk: "))
# Hashir input this directly so that it does need to be asked

# Make a list of the 22 diseases
disease = input("Enter the disease of interest (e.g., Stroke): ")

# The options of races

print('The options are:')
print('-> African Canadian')
print('-> Asian Canadian')
print('-> Native Canadian')
print('-> Hispanic/Latino')
print('-> Causasian')

race = input('Which of the following best describes your Race/Ethnicity: ')
print()

fam = input('Do you have any family history with the disease of interest? Please enter "Yes" or "No": ')
print()


modified = modRisk(risk, race, fam, disease)

print()
print('Your personalized Relative Risk (RR) for', disease, ' is ', modified)