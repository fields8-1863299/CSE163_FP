# Analysis of Poverty Patterns Based on Multiple Factors
## By Ishita Singh, Vinay Patel, and Sam Fields


To run this project and reproduce our results, you will need to download the following libraries: plotly `conda install -c plotly plotly=4.8.1` and seaborn `conda install seaborn`.

After installing the necessary packages, find the `plots.py` file in the folder and run `python plots.py` in the terminal. All output files and images will be in the `plots` folder.

<!-- Copy and paste the converted output. -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 2.157 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sun Jan 10 2021 14:45:52 GMT-0800 (PST)
* Source doc: Part 2
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 2.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


Analysis of Poverty Patterns Based on Multiple Factors

By Ishita Singh, Vinay Patel, and Sam Fields

**<span style="text-decoration:underline;">Summary of Research Questions and Results:</span>**

**How does poverty vary with factors such as race, age, and sex? **

In terms of race, poverty seems to be more prevalent in African American and Latino communities rather than White and Asian communities. Over 2017 to 2018, it can be seen that poverty decreased in every racial group except for the Asian community. In terms of sex, females are slightly higher likely to be in poverty. Over 2017 to 2018, both groups decreased in poverty. 

**How do levels of education and work experience correspond with poverty? Does there exist a correlation in representation of ethnicity in poverty and education achievement? **

	Education and work experience seemed to be negatively correlated with poverty (as levels of education increased, poverty decreased) throughout 2017 to 2018. Different races also appeared to have different levels of education achievement.

**Does annual income differ with different types of household family structures? Does ethnicity have an impact on the annual income? **

	Annual income was highest in family households, with married couples getting 80,000 dollars. Different ethnicities corresponded to different incomes, with Asians ranking the highest.

**What are the levels of poverty across states in the US? What are some of the most dense states? **

All states have at least 7% poverty ranging up to 20% but according to the map (shown in the results section), poverty is most prevalent (around 15-19%) in the southern belt of states including New Mexico, Louisiana, Alabama, Arkansas, and Missourri.

**Is there a correlation between poverty and regions of residence? If so, do poverty levels here depict consistent relations with race?**

There is a small correlation between percentage of population below poverty and residence types inside principal cities inside a metropolitan and outside metropolitan areas with each having ~15% of population the population living below the poverty line compared to the ~12% average for inside metropolitan areas and ~9% for outside principal cities and inside metropolitan areas.



---


**<span style="text-decoration:underline;">Motivation and background:</span>**

Poverty is a persistent issue across the United States and is a leading cause for a number of socio-economic problems in the country, such chronic illness, lack of education, ability to work, and much more[^1]. Understanding correlations and potential causes relating to poverty would allow people to address these issues and possibly help alleviate the financial problems for certain groups of people. 

With data analysis techniques and data visualizations, we can recognize how factors such as state residence, race, city residence, or educational achievement are related to the percentage of population below the US poverty level. Analyzing data through means of bar charts or other methods of visualization to recognize patterns across these areas can be effective in deciphering patterns. We want to discern whether people with certain factors are more likely to be in poverty than others.Through our analysis, we hope to understand variables correlated to poverty in the hopes of providing people with these parameters to address and improve upon.



---


**<span style="text-decoration:underline;">Dataset(s):</span>**



1. [https://drive.google.com/open?id=1xGuJ1XXidTlCmDjccU_OUL7w12cMSqFE](https://drive.google.com/open?id=1xGuJ1XXidTlCmDjccU_OUL7w12cMSqFE)
    1. US 2017, 2018 Percentage and number below and above poverty by race, sex, age, nativity, region, residence, work experience, disability status, and educational attainment.
2. [https://drive.google.com/open?id=1NFBn6fdAjvJjOkKGFOtaSWn_YBdAFOox](https://drive.google.com/open?id=1NFBn6fdAjvJjOkKGFOtaSWn_YBdAFOox)
    2. 2017, 2018 US percentage below poverty and above poverty percentage and number by household type, family descriptors, and non-families.
3. [https://drive.google.com/open?id=16mnd_PvP-E7uyk5iXRIwXDHA9z1qS_vo](https://drive.google.com/open?id=16mnd_PvP-E7uyk5iXRIwXDHA9z1qS_vo)
    3. US percentage of state population in poverty by using 2 year average, one for 2015-2016 and another for 2017-2018, and using 3 year average 2015-2018 (State)
4. [https://drive.google.com/open?id=1iWyu_euBIO9PM8562_14qUqoGHQhcW8d](https://drive.google.com/open?id=1iWyu_euBIO9PM8562_14qUqoGHQhcW8d)
    4. 2017 Below poverty number and percentage by race, gender, age, nativity, region, residence, work experience, disability status, and educational attainment
5. [https://drive.google.com/open?id=1f83qPbRCgNvY-1ahHerKVZMLhPpmK5X9](https://drive.google.com/open?id=1f83qPbRCgNvY-1ahHerKVZMLhPpmK5X9)
    5. 2017-2018 median income of households by household type, ethnicity of household, age, US region, and residence.
6. [https://drive.google.com/file/d/1DeudcpqMiGEtCq-5oDcPPEvso0qTYH85/view?usp=sharing](https://drive.google.com/file/d/1DeudcpqMiGEtCq-5oDcPPEvso0qTYH85/view?usp=sharing,)
    6. Number and percentage of master's degrees conferred to US citizens, residents, and non-resident aliens by ethnicity per year (white, black, hispanic, asian/pacific islander, and two or more races)
7. [https://drive.google.com/file/d/1RsrRanOY64gJdnDxOT8ur37LVXZcdtJ_/view?usp=sharing](https://drive.google.com/file/d/1RsrRanOY64gJdnDxOT8ur37LVXZcdtJ_/view?usp=sharing)
    7. Number and percentage of associate’s degrees conferred to US citizens, residents, and non-resident aliens by ethnicity per year (white, black, hispanic, asian/pacific islander, and two or more races)
8. [https://drive.google.com/file/d/1ZpSck4Kgx7F4ZGjDnXS61uaM3LEC80YY/view?usp=sharing](https://drive.google.com/file/d/1ZpSck4Kgx7F4ZGjDnXS61uaM3LEC80YY/view?usp=sharing)
    8. Number and percentage of below-associate’s degrees conferred to US citizens, residents, and non-resident aliens by ethnicity per year (white, black, hispanic, asian/pacific islander, and two or more races)
9. [https://drive.google.com/file/d/1aSG-PDh38BtJ8pS1P8pdeIqZDyUNHu0s/view?usp=sharing](https://drive.google.com/file/d/1aSG-PDh38BtJ8pS1P8pdeIqZDyUNHu0s/view?usp=sharing)
    9. Number and percentage of doctor’s degrees conferred to US citizens, residents, and non-resident aliens by ethnicity per year (white, black, hispanic, asian/pacific islander, and two or more races)
10. [https://drive.google.com/file/d/1bHW3Siqa9IXY0EvuHDw3Oq_I5rBmy6q0/view?usp=sharing](https://drive.google.com/file/d/1bHW3Siqa9IXY0EvuHDw3Oq_I5rBmy6q0/view?usp=sharing)
    10. Number and percentage of bachelor’s degrees conferred to US citizens, residents, and non-resident aliens by ethnicity per year (white, black, hispanic, asian/pacific islander, and two or more races)

Same information as Part 0.



11. [https://worldpopulationreview.com/states/state-abbreviations/](https://worldpopulationreview.com/states/state-abbreviations/)
    11. States and their respective state codes.



---


**<span style="text-decoration:underline;">Challenge Goals:</span>**

**<span style="text-decoration:underline;">	</span>**For this project, we decided to challenge ourselves by attempting to work with multiple messy datasets as well as use a new library called plotly to make interactive plots.

**Multiple DataSets: **One of the challenge goals we met during our project was the use of multiple messy data sets. This challenge worked well for our project given that poverty is a fairly complex topic with multiple factors that contribute to it. Given that there are multitudinous relationships (i.e. with race, gender, education, etc), using multiple datasets that emphasize these relationships gave us a far better scope of understanding than just one would. Taking the time to clean, merge, and utilize these datasets in a meaningful way helped us identify many answers to our research questions.

	**New Libraries: **We also met another challenge goal through the use of a newly learned Python Library. This challenge was beneficial to meet as there are multiple ways of data analyzation and depiction in python. A new library was useful in finding different ways to represent/plot our data, as well as contribute to the project as a whole. We learned and utilized the **Plotly **library in our project. Our project aimed to investigate the relation between poverty and other factors, such as education, and a strong approach to achieve and depict this is through robust data visualizations. We believe implementing interactive data visualizations through plotly is the best way to do this. These interactive plots allow the viewers greater accessibility into the data we wanted to portray



---


**<span style="text-decoration:underline;">Methodology (algorithm or analysis):</span>**

Before making plots and calculations to answer our research questions, we started by organizing/ cleaning and merging data from the different datasets we have collected. The goal of this is to create a few common, generic databases which are referred to by other functions in our program. This process is planned carefully in order to ensure we have enough data and that the data from the multiple datasets correspond with each other in a meaningful manner. Since we are highlighting multiple key factors in our research questions, we specifically generated datasets which pertain to key information we are looking for which can help answer our research questions. 

We grouped the original datasets based on common factors such as race, income, region of residence, education, family structure, and age. In order to do so we proceeded by combining datasets 1, 2, and 5 (dataset A), datasets 6-10 (dataset B), and independent dataset 3 (dataset C). Since the datasets  1,2, and 5 have rows in common but different columns, they were merged using an outer join. We used these 3 total datasets to do our analysis of our research questions below. 

**_<span style="text-decoration:underline;">Following includes Methodology for each research question:</span>_**

**How does poverty vary with factors such as race, age, and sex?**

For this question, using dataset A we individually compared poverty with each factor by creating two separate corresponding datatables. Each datatable contains aggregated data by some factor (race or sex) for those who are in poverty. Using this information, we plotted two separate bar plots focusing on how poverty varies based on each factor over the course of the years 2017 to 2018. The y-axis will show percent in poverty and the x-axis will show different categories within each factor. The results of the expected graphs are intended to highlight the data showing some groups having higher chances of poverty than others. We want to be able to determine what those factors are and do further analysis about the results to understand the bigger picture of poverty trends in America.

**How do levels of education and work experience correspond with poverty? Does there exist a correlation in representation of ethnicity in poverty and education achievement?**

 To analyze education and work experience in relation to poverty, dataset A was used. Using the work experience rows (“Worked full-time”,year-round”; “Less than full time”, year round”; “Did not work at least 1 week”), a double bar graph (for years 2017 and 2018), was plotted with work experience (independent variable) on the x axis with the corresponding numbers of people in poverty (dependent variable) on the y axis. Results would likely indicate that lower work experience corresponds to higher levels of poverty.

Additionally, a second bar graph was plotted to compare the rows of educational attainment (“No high school diploma”; “high school, no college”; “some college”; “Bachelor’s degree or higher”) as the independent variable compared with the number of people in poverty (dependent variable). This was done using DataSet A. This will help to understand the relationship between the amount of schooling and work experience someone has and poverty. We predict that lower schooling experience (such as only possessing an associate’s or bachelor’s degree) would correspond to higher poverty. However, we are uncertain whether some colleges compared to higher degrees (such as a bachelor’s or higher) depict a significant difference in poverty levels, and are interested in finding this out during our analysis.

The years 2016-2017 from Dataset B was used to determine correlation with race and educational attainment. A bar graph was made for each degree type, representing number of people with the degree on the y-axis, with each race (“white”, “black”, “hispanic”, “Asian/Pacific Islander”, “American Indian/ Alaskan Native”) on the x-axis.. This information can help us determine if races’ overall annual income pattern matches with levels/severity of poverty. It is possible that historically oppressed groups would depict higher levels of poverty.

**Does annual income differ with different types of household family structures? Does ethnicity have an impact on the annual income? **

From dataset A, 2 double bar graphs for the years 2017 and 2018 were plotted comparing the types of households to average annual income. The household types in question are family households for the first graph(with sub categories of “Married couple”; “Female householder, no spouse present”; “Male Householder, no spouse present”) and non-family household for the second graph (with subcategories of “Female Householder”; “Male Householder”). Using the graphs, our results will allow us to be able to identify a correlation between income and the family structure of a person. We will anticipate families with a larger number of providers, i.e. married couples, would be correlated to a higher annual income. 

Another double bar graph (for the years 2017 and 2018) was plotted describing the relationship between race and annual income. The row categories for race are “White”; “white, not Hispanic”; “Black”; “Asian”; “Hispanic (any race)”. This information can help us determine if races’ overall annual income pattern matches with levels/severity of poverty. It is possible that traditionally oppressed groups would be correlated to lower annual income levels, and this is something we wish to investigate further in our analysis.

**What are the levels of poverty across states in the US? What are some of the most dense states?**

Using dataset C, we determined the relationship between poverty across the US by state during the years 2017 to 2018. Using plotly in conjunction with our dataset, we used built-in mapping functions to plot a map of the US states colored by the percentage of their population below the poverty level. We started by cleaning our dataset for desired rows and columns and joined it with a third party plotly csv file with states and their state codes. Using these codes combined with the data, we created an interactive output highlighting the poverty differences in the US.

 We included a hover feature that, when hovering over a state, will give the state’s name as well as the percentage of the population below the poverty level. This plot contrasts states with a higher level of percentage population in poverty starkly against states with a lower percentage making them easier to distinguish.

We initially anticipate that states with a higher GDP, such as California, Washington, New York, etc, would have a lower percentage population below the poverty level relative to their counterparts. According to our graph, those states still had higher poverty rates than some other states despite having a higher GDP. 

**Is there a correlation between poverty and regions of residence?**

Dataset A contains information on the percentage above and below poverty during the years 2017 and 2018. This information is related to metadata, such residence defined as either “inside metropolitan areas” (broken into subcategories of “inside or outside principal cities”) or “outside of metropolitan areas”. We plotted three different types of plots using both 2017 and 2018 data: the total population by each residence type, the total population below the poverty line by residence type, and the percentage of population below the poverty line by residence type. 

Using plotly, for each plot we made a series of two groups (2017 and 2018) of four column bar charts to investigate this question. The four different residence types(“inside metropolitan areas”, “inside principal cities”, “outside principal cities”, “outside of metropolitan areas”) are plotted for each group on the x axis, while the total population / population under poverty line / percentage population below poverty line for these areas are plotted on the y-axis.

With these visualizations, we are able to determine that there is a correlation between poverty and regions of residence by identifying major discrepancies in ration of percentage difference in the number of people below the poverty level by the different residences types. Initially, we assumed that those “outside of metropolitan areas” would have a distinctly higher percentage of population impoverished. By analysing the “Percentage of population below poverty line by residence”, we identified that areas with higher percentages of population impoverished included both “outside metropolitan areas” and also “outside principal cities inside metropolitan areas”.



---


**<span style="text-decoration:underline;">Results:</span>**

**<span style="text-decoration:underline;">How does poverty vary with factors such as race and sex?</span>**

All groups face poverty, but some face it more often than others. The bar chart showing poverty based on race groups (Figure 1) shows that minorities such as Hispanics and African Americans are more likely to be in poverty compared to other communities. This can be due to a multitude of factors stemming from discrimination, unequal opportunities, all the way to systematic/ perpetual poverty within certain groups. The bar chart showing poverty based on gender (Figure 2) shows that females are more likely to be in poverty compared to males. After some research, this is due to males having a strong lead in the workforce causing many women to struggle for low-paying jobs. Over the year 2017 to 2018, all but one group of people decreased in poverty percentage showing that overall, the total poverty decreased over these years.  

**<span style="text-decoration:underline;">How do levels of education and work experience correspond with poverty?</span>**

   

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")
                            

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")
    

Figure 3 depicts poverty varying by the level of schooling someone has. The relationships observed here are somewhat predictable; however, the plot does not show a steadily decreasing relationship with increasing levels of education as we had initially predicted. While it depicts that having a college education and subsequently higher degrees(such as Bachelors), tend to correspond with lower levels of poverty, the same cannot be said for having a high school diploma compared to not having one. We were under the impression that the highest number of people in poverty would be those who had minimal schooling and lacked a diploma. The graph revealed that the highest number of people (around 8000 people for 2017 and 2018) in poverty were those who possessed only a highschool diploma. While initially these results were shocking, upon further reflection we concluded that it is simply likely that people who do not complete atleast highschool make up a smaller percentage of the population, and therefore would have lower numbers of people in poverty. Other than that, the pattern of higher degrees corresponding to fewer individuals in poverty remains consistent. This pattern coincides with what we would expect, as people with higher degrees will be more likely to get high-paying jobs. There was no significant relationship observed with a time difference of 1 year, as poverty was lower or higher in 2018 depending on the degree. 

Figure 5 illustrates that there tend to be more people in poverty as work experience decreases. For example, working full time had only about 2000 people in poverty. However, this number increases to 6000 people if they worked less than full time, and skyrockets to roughly 14,000 who did not work at least a week. This pattern also corresponds with our initial prediction of higher work experience tending to have fewer people in poverty. This result also makes logical sense, as those working would obviously have a source of income compared to those who aren’t. 

**<span style="text-decoration:underline;">Does there exist a correlation in representation of ethnicity in poverty and education achievement?</span>**    

                        

                                                                                

                                     

Figures 5 through 7 show the relationship between race and people with a certain degree. There are quite a few observations here. We noticed that starting with Bachelor's degrees, the total number of people with each degree tended to decline, regardless of race. It was observed consistently throughout the figures that the highest number of degrees were awarded to those who were white. It is important to consider that this racial disparity is influenced by the fact that the statistics come from the United States, a country that is predominantly white to begin with. Hispanics tended to have a higher number of degrees awarded to them compared to those who are black, as can be observed by Figures 5, 6, and 7. The severity of this difference declines in figures 8 and 9, with the numbers being roughly equal. 

Comparing these patterns with Figure 1, we can see that poverty according to race tends to correspond to lower levels of degrees to the same race. Those who were black and hispanic had the highest levels of poverty in Figure 1, and black and hispanic people figures 5 through 9 also have lower levels of degrees awarded. Those who are asian exhibited a lower number of poverty in figure 1, and also show a higher number of doctor’s degrees in figure 9 as compared to those who are black or hispanic.

**<span style="text-decoration:underline;">Does annual income differ with different types of household family structures?</span>**

**<span style="text-decoration:underline;">	</span>**Figures 10 and 11 describe income according to family and non-family households. We predicted that family households, especially married couples would have the highest median income. This was reflected in our graph (figure 10), with married couples having the highest income at approximately 90,000. This is not unexpected, as marriage between two people results in twice the income. Therefore, married couples would be at a reduced risk for poverty.

**<span style="text-decoration:underline;">Does ethnicity have an impact on the annual income?</span>**

	Figure 12 depicts the races in terms of annual income. As can be observed by  the graph, Asians show the highest income, followed by White, Hispanic, and Black. These results are directly consistent with what is observed in Figure 1, with Asians having the lowest number of people In Poverty, followed by White, Hispanic, and Black. This also confirms our initial thoughts in a sense, that traditionally oppressed groups tend to have a lower annual income and higher rates of poverty. Asians having the highest income is also consistent with Figure 8 and 9, as people who are Asian have higher rates of obtaining a master’s or doctor’s degree. This leads us to believe that there is significant association/correlation with race and income.

**<span style="text-decoration:underline;">What are the levels of poverty across states in the US? What are some of the most dense states? </span>**

Across the country, each state is affected by poverty (at least 7%). Some states are more affected than others. Looking at the static image to the right, it can be noted that the southern belt of states including New Mexico, Louisiana, Alabama, Arkansas, and Missouri have the highest poverty percentages in the country. Our initial expectation was that states with high GDP would have lower poverty, but it was found that most poverty is contributed to by socioeconomic factors such as race, income, and education. Utah was the state with the lowest poverty rate, while Louisiana was the state with the highest poverty rate. In order to view the interactive image of this map, access it by opening the states.html file after running the code which will allow you to hover over states to see the exact poverty percentage. Plotly requires an account to otherwise view interactive plots created by others. 

**<span style="text-decoration:underline;">Is there a correlation between poverty and regions of residence? </span>**

Observing the total population across all residence types, it is apparent that there is a significantly larger proportion of people who live “Inside metropolitan statistical areas” which is defined by the census bureau as being an “area [that] must have at least one urbanized area of 50,000 or more inhabitants.” The population who live inside these areas are then divided into “Inside principal cities” and “Outside principal cities”. A principal city is defined by the census bureau as the largest city in the metropolitan area.

	


            When observing the total population count below the poverty line by residence type, it is obvious that the majority of the impoverished population resides inside metropolitan areas with an equal distribution between inside and outside principal cities. However, from observing the distribution of the total population by residence type and knowing that metropolitan areas have the largest population count, it is difficult to infer if there is correlation between residence type and poverty since it is possible that metropolitan areas may have more people below the poverty line simply do to metropolitan areas having a larger total population.

In order to observe if there exists a correlation between residence type and poverty we should observe the percentage of the population below the poverty line by residence. Looking at the graph that shows this relation, we can see that the two most indicative residence types for poverty are “inside principal cities” inside metropolitan areas and “outside metropolitan areas” with each having roughly 15% of the population being below the poverty line. 



---


**<span style="text-decoration:underline;">Work Plan Evaluation:</span>**



1. **Loading, Cleaning, and Merging/ Joining the data (5 hours) **~ Done By Sam
    1. Load each of the 10 databases we use
    2. Filter each of the 10 databases to only contain information we want to know more about for this project
    3. Merge/ Join different databases for the sake of readability based on matching information

    **Evaluation:**


    Took roughly 6~7 hours. However, the cleaning and filtering wasn’t quite equally distributed. Datasets C and D were the fastest and easiest since they only required formatting the pandas dataframe in the way we wanted it. However, Datasets A and B took about 2~3 hours each** **since they not only required formatting the pandas dataframe correctly but they also required labeling the columns and rows in a way where they would be easy to combine through concatenation or joining.

2. **How does poverty vary with factors such as race, age, and sex? (1.5 hours) **~ Done by Vinay
    4. Create three new databases by filtering for needed information
    5. Create three plots highlighting the correlation between poverty and each factor.
    6. Analyze and identify trends in each plot and what they mean

    **Evaluation:**


    It took roughly about 3 hours. Smaller datasets were easily extracted from the larger dataset to host data for individual topics. Took a bit longer than expected to find how to make a dual bar chart other than that this part was pretty straightforward. Wasted about an hour using datasets that were not from aggregated data so I had to redo the work.

3. **How do levels of education and work experience correspond with poverty? Does there exist a correlation in representation of ethnicity in poverty and education achievement? (2 hours) **~ Done by Ishita
1. Aggregate data as needed by education, poverty, and experience.
2. Plot bar graph: education vs poverty
3. Plot bar graph: work experience vs poverty
4. Plot line graph: ethnicities vs poverty

    **Evaluation:**


    This part took around 4 hours. Much of this time included figuring out which rows needed to be extracted and how so. Even when extracted, the data had to be reshaped in a way that the different columns could both be plotted as values on the y axis, which was not something that was considered in the initial estimate. 

4. **Does annual income differ with different types of household family structures? Does education have an impact on the annual income? Does ethnicity have an impact on the annual income? (2 hours) **~ Done by Ishita
1. Aggregate data as needed by household, education, ethnicity.
2. Plot bar graph: household vs annual income
3. Plot bar graph: ethnicity vs annual income

    **Evaluation:**


    This part took about 2.5 hours. Reshaping the data was similar to what I had done before, with only a few new strategies. So the time estimate ended up being fairly accurate. There were some issues with being able to extract the rows and the values not showing up, so that ended up taking an extra half hour.

5. **What are the levels of poverty across states in the US? What are some of the most dense states? (1 hour) **~ Done by Sam
    7. Format dataset C[ ](https://www2.census.gov/programs-surveys/demo/tables/p60/266/state.xls)
    8. Aggregate data with geospatial data by State
    9. Plot data to US map defined by state colored by 3 year average of percentage below poverty level by state.

    **Evaluation:**


    This part took about 2 hours. The data needed to be processed and cleaned a bit, a secondary csv file was needed to be added, and new material was needed to be learned in order to use plotly to make an interactive map.

6. **Is there a correlation between poverty and regions of residence? If so, do poverty levels here depict consistent relations with race? (1.5 hr) **~ Done by Vinay
    10. Format dataset A
    11. Plot percentage below poverty level by residence (2017 and 2018)
    12. Plot number below poverty level next to total population by residence (2017 and 2018)

    **Evaluation:**


    Took about ~3 hrs. Had to reformat the ways the plots were depicted because the scaling of certain plots made it too difficult to make any meaningful interpretations. Also, I spent about an hour trying to figure out how to make subplots in plotly using multiple figures before realizing it was not a feature they had implemented. Decided to save to multiple different plots instead.

7. **Report Writing/ Group Work (6 hours)**
    13. Perform analysis as necessary for each component, trying to find a trend/ pattern of poverty rates among certain types of people (work split up on Google Docs)
    14. Sharing Code: Each person does their section individually and tests it before pushing it to Git where we will collaboratively merge pieces together.

    **Evaluation:**


    Took about ~4 hours. We divided the bigger writing components amongst each other and each individually wrote up our own results sections based on the work we did. We ran into problems using Github for source control. So, we decided to send our python files aggregate to one individual who then created the Github repository and added all the relevant files that way.`




---


**<span style="text-decoration:underline;">Testing:</span>**

**<span style="text-decoration:underline;">	</span>**Testing the code was definitely one of the more difficult aspects of our project. Since almost everything was done by plotting graphs, it made using any assert equals methods seem impractical. We also didn’t see the value in testing smaller datasets, as our dataset was already small enough to fit into one excel page. Therefore, much of our testing was done by debugging to make sure the code ran properly, extracting values the code produced and matching with the dataset, and visually looking at the graphs and using common sense.

In order to test that our code was graphing the correct values, we extracted a few values from the datasets and compared it visually to the different plots. For example, from dataset A, we extracted the “2017 Total Below Poverty” number for the “High school, no college” category and received a value of  8054. We then looked at our original excel dataset and confirmed this as the same value.  Looking at Figure 3, the bar for these values was just over 8000, thereby confirming that our plot was also graphing the correct values. This process of extracting values was repeated for dataset B and compared to other graphs visually. Since there was no way to test graphs, we used this method as it was common sense. 

These results were also conducted multiple times throughout the whole coding process, and the relationships we observed between the different graphs and variables were consistent with our predictions. Since one of our challenge goals consisted of merging datasets, we made sure this was accomplished by extracting the column for “Category”. We observed that all the columns from both datasets that were merged were present in Category, and this confirmed that the merging process was done correctly. For figure 13, we had to analyze it visually and deduce that it was correct. Looking at Dataset C and visually analyzing the values, the highest poverty level states were the darkest on the state map, leading us to believe that our code produced the correct values.



---


**<span style="text-decoration:underline;">Collaboration:</span>**

For this project, our group of three did all of the work by ourselves with the help of some online resources. Some of the online resources we used include the plotly website, the census bureau, stack overflow, as well as online course materials (Ed and lecture videos). Overall our team worked well together using a text group chat to stay in contact with each other about project details. We held calls multiple times during the week to check in and ensure our project would be completed on time with our goals accomplished. 


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     [https://moveforhunger.org/the-effects-of-poverty](https://moveforhunger.org/the-effects-of-poverty)
# Poverty-Analysis
