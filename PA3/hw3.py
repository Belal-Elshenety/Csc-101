import data
import build_data
import hw3


# Part 1
# Description:population_total with one parameter (of
#     type list[CountyDemographics]), a list of county demographics objects (note that this is a
#     parameter of the function and is not necessarily the full data set). This function must
#     return the total 2014 Population across the set of counties in the provided list.
def population_total(list:list[data.CountyDemographics])->int:
    population = 0
    for county in list:
        population += county.population['2014 Population']
    return population
# Part 2
# Description: filter_by_state with two parameters, a list of county
#     demographics objects and a two-letter state abbreviation. This function must return a list
#     of county demographics objects from the input list that are within the specified state. If
#     the provided key does not exist in the list, then the result should be the empty list.
def filter_by_state(list:[data.CountyDemographics],state:str)->list[data.CountyDemographics]:
    state_demographics = []
    for object in list:
        if object.state == state:
          state_demographics.append(object)
    return state_demographics
# Part 3
# test population_by_education
#     Description:population_by_education with two parameters: a list of
#     county demographics objects and the education key of interest (e.g., "Bachelor's Degree or
#     Higher"). This function must return the total 2014 sub-population across the set of
#     counties in the provided list for the specified key of interest.If the provided key does not exist, the
#     result should be 0.
def population_by_education(list:[data.CountyDemographics],key:str) -> float:
    for k in list:
        if not key in k.education:
            return 0
    sum = 0
    for county in list:
        key_value = county.population['2014 Population'] * county.education[key]/100
        sum += key_value
    return sum
# Description: population_by_ethnicity with two parameters: a list of county
#     demographics objects and the ethnicity key of interest (e.g., 'Two or More Races'). This
#     function must return the total 2014 sub-population across the set of counties in the
#     provided list for the specified key of interest. If the provided key does not exist, the
#     result should be 0.
def population_by_ethnicity(list:[data.CountyDemographics],key:str) -> float:
    for k in list:
        if not key in k.ethnicities:
            return 0
    sum = 0
    for county in list:
        key_value = county.population['2014 Population'] * county.ethnicities[key]/100
        sum += key_value
    return sum
# test population_below_poverty_level
#     Description:population_below_poverty_level with one parameter: a list
#     of county demographics objects. This function must return the total 2014 sub-population
#     indicated by income key 'Persons Below Poverty Level' across the set of counties in the
#     provided list for the specified key of interest.
def population_below_poverty_level(list:[data.CountyDemographics]) -> float:
    sum = 0
    for county in list:
        key_value = county.population['2014 Population'] * county.income['Persons Below Poverty Level']/100
        sum += key_value
    return sum
#     Description:percent_by_education with two parameters: a list of county
#     demographics objects and the education key of interest (e.g., "Bachelor's Degree or
#     Higher"). This function must return the specified 2014 sub-population as a percentage of
#     the total 2014 population across the set of counties in the provided list for the specified
#     key of interest. This function can be defined using the corresponding functions from
#     Parts 1 and 2. If the provided key does not exist, the result should be 0.
# Part 4
def percent_by_education(list:[data.CountyDemographics],key:str) -> float:
    key_value = hw3.population_by_education(list,key)
    total_pop = hw3.population_total(list)
    return key_value*100 /total_pop

#     Description: percent_by_ethnicity with two parameters: a list of county
#     demographics objects and the ethnicity key of interest (e.g., 'Two or More Races'). This
#     function must return the specified 2014 sub-population as a percentage of the total 2014
#     population across the set of counties in the provided list for the specified key of interest.
#     This function can be defined using the corresponding functions from Parts 1 and 2. If
#     the provided key does not exist, the result should be 0.
def percent_by_ethnicity(list:[data.CountyDemographics],key:str) -> float:
    key_value = hw3.population_by_ethnicity(list, key)
    total_pop = hw3.population_total(list)
    return key_value * 100 / total_pop
# Description: percent_by_education with one parameter: a list of county
#     demographics objects. This function must return the 2014 sub-population indicated by
#     income key 'Persons Below Poverty Level' as a percentage of the total 2014 population
#     across the set of counties in the provided list for the specified key of interest.
def percent_below_poverty_level(list:[data.CountyDemographics]) -> float:
    key_value = hw3.population_below_poverty_level(list)
    total_pop = hw3.population_total(list)
    return key_value * 100 / total_pop
# Description:education_greater_than and education_less_than, each taking
#     three parameters: a list of county demographics objects, the education key of interest,
#     and a numeric threshold value. This function must return a list of all county
#     demographics objects for which the value for the specified key is greater than or less
#     than (as appropriate by function name) the specified threshold value. For instance, we
#     might want to find all counties in which the "Bachelor's Degree or Higher" population is
#     greater than 60 percent.
def education_greater_than(list:list[data.CountyDemographics],key:str, value:float)->list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.education[key] > value:
            new_list.append(county)
    return new_list

def education_less_than(list:list[data.CountyDemographics],key:str, value:float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.education[key] < value:
            new_list.append(county)
    return new_list
# Description:ethnicity_greater_than and ethnicity_less_than, each taking
#         three parameters: a list of county demographics objects, the ethnicity key of interest,
#         and a numeric threshold value. This function must return a list of all county
#         demographics objects for which the value for the specified key is greater than or less
#         than (as appropriate by function name) the specified threshold value. For instance, we
#         might want to find all counties in which the 'Hispanic or Latino' population is greater than
#         30 percent.
def ethnicity_greater_than(list:list[data.CountyDemographics],key:str, value:float)->list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.ethnicities[key] > value:
            new_list.append(county)
    return new_list

def ethnicity_less_than(list:list[data.CountyDemographics],key:str, value:float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.ethnicities[key] < value:
            new_list.append(county)
    return new_list
# Description:below_poverty_level_greater_than and below_poverty_level_less_than,
#     each taking two parameters: a list of county demographics objects and a numeric
#     threshold value. This function must return a list of all county demographics objects for
#     which the value for key 'Persons Below Poverty Level' is greater than or less than (as
#     appropriate by function name) the specified threshold value. For instance, we might
#     want to find all counties in which the population below the poverty level is greater than
#     30 percent.
def below_poverty_level_greater_than(list:list[data.CountyDemographics], value:float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.income['Persons Below Poverty Level'] > value:
            new_list.append(county)
    return new_list

def below_poverty_level_less_than(list:list[data.CountyDemographics], value:float) -> list[data.CountyDemographics]:
    new_list = []
    for county in list:
        if county.income['Persons Below Poverty Level'] < value:
            new_list.append(county)
    return new_list







