# Exploring OkCupid Profiles
Dating Web Site EDA

<img src="./img/logo.png" alt="logo" width="400"/>

### Table of Contents
1. [Overview](#overview)
2. [The Data Set](#the-data-set)
3. [Cleaning the data](#cleaning-the-data)
4. [End Goal Questions](#end-goal-questions)
5. [Data Analysis and Visualization](#data-analysis-and-visualization)
6. [Further Data Analysis](#further-data-analysis)
7. [What else?](#what-else)
8. [Conclusion](#conclusion)
9. [Credits and References](#credits-and-references)

## **Overview**
OkCupid is a U.S.-based, international operating online dating, friendship, and formerly also a social networking website and application. It was launched in January 19th, 2004 by a group a developers from Harvard University. It is currently owned by Match Group which also owns Tinder, Hinge, Plenty of Fish and many other popular dating apps and sites. 

OkCupid is a dating platform that is similiar to other dating app such as Tinder, but rather provided a game feel, it also feels like a social networking sites. OkCupid is considered to be a dating platform designed to be less centered on physical appearance. Despite that facts, the dating world however proving a completely rather otherwise picture. We are in this data exploring quest, mainly focus on the data and graph (that is the most picture thing I could provided). 
## **The Data Set**
This dataset was created with the use of a python script that pulled the data from public profiles on www.okcupid.com. It compromises of 59946 user profiles, which includes people within a 25 mile radius of San Francisco. 

The dataset categorize user profiles with 31 different columns: 
- 21 of which columns are user's natural consistent attribute (things that biographically distingushed between person) such as a person's `age`, `sex`, `height`, `education`, `ethnicity`, `speaks`, ... etc.



- 10 of which columns in the name of `essay0`, `essay1`, `essay2`, ... `essay9` etc. are pre-made questions that a user could answer in which to make their profiles stand out and/or find their potential match. OkCupid engine also use this data to find and/or recommend matchs, such finding might be outside the scope of this analysis. However, I hope to  The categories meaning is listed as follow:

| Column_name | Meaning                                        |
|-------------|------------------------------------------------|
| essay0      | My self summary                                |
| essay1      | What I’m doing with my life                    |
| essay2      | I’m really good at                             |
| essay3      | The first thing people usually notice about me |
| essay4      | Favorite books, movies, show, music, and food  |
| essay5      | The six things I could never do without        |
| essay6      | I spend a lot of time thinking about           |
| essay7      | On a typical Friday night I am                 |
| essay8      | The most private thing I am willing to admit   |
| essay9      | You should message me if...                    |

***NOTE: Due to Github upload file size restriction, the dataset is not included in this repository but it can be downloaded at [`okcupid_profiles.csv`](https://www.kaggle.com/code/captainqq/dating-profiles-analysis-and-visualization/data). After downloading, be sure to save it in the `data` folder.


## **Cleaning the data**
1. Process null value
    - 
2. Check for dupliated row
    - found none 
3. Combined possible similar data without compromised the data integrity, to reduce number of labeling
    - crunching/generalize the `education` column
    - ~~crunching/generalize the `ethnicity` column~~ 
        - (it is challenging to generalize people with mixed races, so I've withdrawed from this task)



## **End Goal Questions**
1. 
2. 
3. 
## **Data Analysis and Visualization**
## **Further Data Analysis**
## **What else?**
## **Conclusion**
## **Credits and References**
https://github.com/rudeboybert/JSE_OkCupid

https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles

https://sparkbyexamples.com/pandas/pandas-remap-values-in-column-with-a-dictionary-dict/