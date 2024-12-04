import data
import county_demographics
from build_data import get_data
from data import CountyDemographics
import hw3_tests
import math


import build_data
full_data = get_data()
#print(full_data)

# Part 1

#This function's purpose is to return the total population of 2014 for the counties in the list. The input
#is the list of county demographics, with the output being an integer which represents the total 2014 population.
#The parameter is of type list and an integer is returned
def population_total(value: list[data.CountyDemographics]) -> int:
    pop = 0
    for county in value:
        pop = pop + county.population['2014 Population']
    return pop


# Part 2

#This function's purpose is to return a county list that is from a specific state. The input is a list
#of county demographics as well as a two letter state abbreviation, with the output being a list of counties
#that are within the state being specified. The parameters are of type list and string, and a list is returned
def filter_by_state(countyList: list[CountyDemographics], abbr: str)->list[CountyDemographics]:
    filter = []
    for county in countyList:
        if county.state == abbr:
            filter.append(county)
    return filter


#Part 3

#This function's purpose is to find the subpopulation from 2014 in the set of counties for a specified education
#key. The input of this function is an education key of interest and a list of county demographics. The output is
#the 2014 subpopulation. The parameters are of type list and string and a float is returned
def population_by_education(countyList: list[CountyDemographics], educationKey: str)->float:
    totalPopulation = 0
    for county in countyList:
        if educationKey in county.education:
            totalPopulation += county.population["2014 Population"] * (county.education[educationKey])
    return totalPopulation

#This function's purpose is to return the subpopulation of 2014 across a set of counties with the key specifying ethnicity.
#The input is an ethnicity key of interest as well as a list of county demographics. The output is the subpopulation of
#2014. The parameters are of type list and string and a float is returned
def population_by_ethnicity(countyList: list[CountyDemographics], ethKey: str)->float:
    totalPopulation = 0
    for county in countyList:
        if ethKey in county.ethnicities:
            totalPopulation += county.population["2014 Population"] * (county.ethnicities[ethKey])
    return totalPopulation

#This function's purpose is to return the subpopulation of 2014 across a set of counties for the income key "Persons Below Poverty Level"
#The inputs are the income key, as previously stated "Persons Below Poverty Level" as well as a list of county demographics
#The output is the 2014 subpopulation. The parameter is of type list and a float is returned
def population_below_poverty_level(countyList: list[CountyDemographics])-> float:
    totalPopulation = 0
    for county in countyList:
        if "Persons Below Poverty Level" in county.income:
            totalPopulation += county.population["2014 Population"] * (county.income["Persons Below Poverty Level"])
    return totalPopulation


#Part 4

#This function's purpose is to find the subpopulation of 2014 for the specified education key as a percentage of the total
#2014 population of the counties. The inputs are a list of county demographics and an education key of interest. The output
#is the 2014 subpopulation as a percentage of the total 2014 population. The parameters are of type list and string, and a
#float is returned
def percent_by_education(countyList: list[CountyDemographics],educationKey: str) -> float:
    totalPopulation = population_total(countyList)
    educationPopulation = population_by_education(countyList, educationKey)
    if totalPopulation > 0:
        percentage = (educationPopulation/totalPopulation)
    else:
        percentage = 0.0
    return percentage

#This function's purpose is to find the subpopulation of 2014 for the specified ethnicity key as a percentage of the total
#2014 population of the counties. THe inputs are a list of county demogrpahics as well as an ethnicity key of interest. The
#output is the subpopulation of 2014 as a percentage of the total population of 2014. The parameters are of type list and
#type string, and a float is returned
def percent_by_ethnicity(countyList: list[CountyDemographics], ethnicity: str) -> float:
    totalPopulation = population_total(countyList)
    ethnicityPopulation = population_by_ethnicity(countyList, ethnicity)
    if totalPopulation>0:
        percentage = (ethnicityPopulation/totalPopulation)
    else:
        percentage = 0.0
    return percentage

#This function's purpose is to find the subpopulation of 2014 for the income key "Persons Below Poverty Level" as a percentage
#of the total 2014 population of the counties. The input is a list of county demographics as well as an income key as previously
#stated. The output is the 2014 subpopulaiton as a percentage of the total population of 2014. The parameter is of type list
#and a float is returned
def percent_below_poverty_level(countyList: list[CountyDemographics])-> float:
    totalPopulation = population_total(countyList)
    povertyPopulation = population_below_poverty_level(countyList)
    if totalPopulation > 0:
        percentage = (povertyPopulation/totalPopulation)
    else:
        percentage = 0.0
    return percentage


# Part 5

#This funciton's purpose is to return a list of county demogrpahic objects where the value for the education key is greater
#than a specified threshold. The inputs are a list of county demographics as well as the education key of interest and also
#a threshold value. The output is  a lit of county demographic objects. The paramters are of type list, string, and float. A
#list is returned in this function
def education_greater_than(countyList: list[CountyDemographics], edu: str, limit: float)-> list[CountyDemographics]:
    result = []
    for county in countyList:
        if edu in county.education:
            if county.education[edu] > limit:
                result.append(county)
    return result

#This function's prupose is to return a list of county demographic objects where the value for the education key is less than a
#specified threshold. The inputs are a list of county demographics and the education key of interest and a threshold value. The
#output is a list of country demographic objects. The parameters are of type list, string, and float, and a list is returned
def education_less_than(countyList: list[CountyDemographics], educ: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in countyList:
        if educ in county.education:
            if county.education[educ] < limit:
                result.append(county)
    return result

#This function's purpose is to return a list of county demographic objects where the value for the ethncity key is greater than
#a specified threshold. The inputs are a list of county demographics and the ethnicity key of interest and also a threshold
#value. The output is a list of county demographic objects. THe parameters are type list, string, and float, and a list is returned
def ethnicity_greater_than(countyList: list[CountyDemographics], ethn: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in countyList:
        if ethn in county.ethnicities:
            if county.ethnicities[ethn]>limit:
                result.append(county)
    return result

#This function's purpose is to return a list of county demographic objects where the value of the ethnicity key is less than
#that of a specified threshold. The inputs are a list of county demographics and the ethnicity key of interest and a threshold
#value. theh output is a list of country demogrpahic objects. The parameters are of type list, string, and float, and a list is
#returned
def ethnicity_less_than(countyList: list[CountyDemographics], ethn: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in countyList:
        if ethn in county.ethnicities:
            if county.ethnicities[ethn]<limit:
                result.append(county)
    return result

#This function's purpose is to return a list of county demographic objects where the value for the key is greater than the specified
#threshold. The key is "Persons Below Poverty Level". The inputs are the list of county demographics and a threshold value as well
#as the key (previously stated). The output is a list of county demographic objects and the parameters are of type list and float. A
#list is returned
def below_poverty_level_greater_than(countyList: list[CountyDemographics], limit: float) -> list[CountyDemographics]:
    result = []
    for county in countyList:
        if "Persons Below Poverty Level" in county.income:
            if county.income["Persons Below Poverty Level"] > limit:
                result.append(county)
    return result

#This function's purpose is to return a list of county demographic objects where the value for the key is less than that of the
#specified threshold. Also, the key is "Persons Below Poverty Level". The inputs are the list of county demographics and a
#threshold value as well as the key, which has previously been stated. The output is a list of county demographic objects. The
#parameters are of type list and float, and a list is returned
def below_poverty_level_less_than(countyList: list[CountyDemographics], limit: float) -> list[CountyDemographics]:
    result = []
    for county in countyList:
        if "Persons Below Poverty Level" in county.income:
            if county.income["Persons Below Poverty Level"] < limit:
                result.append(county)
    return result