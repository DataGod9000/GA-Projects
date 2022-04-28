# Project 1: Evaluate if U.S. colleges should continue exemption of SAT for the long run

## Problem Statement:
- Evaluate if U.S. colleges should continue exemption of SAT for the long run
---

## Background:
The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). 

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from sudents' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry. Lately, more and more schools are opting to drop the SAT/ACT requirement for their Fall 2021 applications ([*read more about this here*](https://www.cnn.com/2020/04/14/us/coronavirus-colleges-sat-act-test-trnd/index.html)).

### Datasets selected:
- sat_act_by_college.csv
- datafrom web scraping/ college databases

- The datasets provides data on the participation rate of high school students in each state who took the SAT in 2017, 2018 and 2019, and their average scores aggregated at state-level. It will be used to identify states where participation rates have declined significantly over the years.
---

## Additional Information:

- SAT Score Components: The SAT is scored out of 1600 and is a combination of the section scores (800 for reading/writing and math respectively). The essay is optional and will not be factored into the overall SAT score. The essay scores will be shown separately on the report [(source)](https://www.khanacademy.org/test-prep/sat/new-sat-tips-planning/new-sat-about-sat/a/scoring-on-the-redesigned-sat).
- SAT is not compulsory for all States and requires a registration fee, hence some States may have lower participation rates [(source)](https://collegereadiness.collegeboard.org/sat/register/fees).
- Students can take the SAT multiple times, and most colleges consider a student's highest SAT score when making admission decisions. And if they get a total SAT score by at least 100 points higher than their previous SAT score, they could be eligible to earn an Improve Your Score scholarship worth 2,000 dollars [(source)](https://parents.collegeboard.org/faq/how-many-times-can-student-take-sat-when-should-take). 
- Many schools use a process called "superscoring", which combines a student's highest Math section score with their highest Evidence-Based Reading and Writing section score, even if those scores are from different test dates, to come up with the student's total SAT score [(source)](https://parents.collegeboard.org/faq/how-many-times-can-student-take-sat-when-should-take). 

- One way to increase SAT participation rate is to cover all or part of exam fees: fee waivers are available for low‐income students, particularly those to whom exam fees would present an undue burden. The College Board also provides a free tool for school counselors to track students’ progress in registering for the SAT and using fee waivers. The College Board reports that fee waivers are more common than ever and supported 23 percent of SAT takers in 2013. However, obtaining a fee waiver does not guarantee test participation. The College Board found that the two most common reasons for test day absenteeism among fee‐waiver recipients were 1) feeling unprepared and 2) not having transportation. Fee‐waiver recipients indicated that the school counselor was the most important influence in deciding whether to register, and they would have been more likely to be present on test day with more encouragement, increased accessibility to test centers, and more preparation." - [(source)](https://www.hanoverresearch.com/media/Best-Practices-to-Increase-SAT-Participation-1.pdf)


**States that require the SAT [(source)](https://blog.collegevine.com/states-that-require-sat/)**:
 - Colorado high school juniors have been required to take the SAT since the 2016-2017 school year and sophomores are administered the PSAT. 
 - In the 2015-2016 academic year, taking the SAT became a graduation requirement for Connecticut high schoolers, replacing the Smarter Balanced Assessment Consortium (SBAC) exam. 
 - Delaware has provided the SAT free of charge to students since 2011, but in 2016, it replaced its Smarter Balanced Assessment exam with the SAT. 
 - Idaho students must take either the SAT or ACT before the completion of 11th grade—the state offers the SAT for free to high school juniors and the PSAT for free to sophomores.
 - As of 2017, all Illinois juniors are required to take the SAT. 
 - The SAT is a requirement in the state of Maine—the state still provides the exam for free to third-year high school students. 
 - Michagan moved away from the ACT and began administering the SAT in 2016. 
 - In 2016, New Hampshire transitioned from using Smarter Balanced exams to the SAT. 
 - All Ohio juniors are required to take either a state-funded ACT or SAT exam. 
 - In 2018, the SAT and PSAT became graduation requirements in Rhode Island. 
 - The SAT is mandatory for all West Virginia 11th graders with the exception of students with cognitive disabilities who are given the West Virginia Alternate Assessment.
 - Florida offers free SAT for Florida Public High School Students, and has compulsory SAT requirement [(source)](https://www.orlandosentinel.com/news/education/os-fsa-algebra-passing-scores-alternative-20180330-story.html).

**States that provide SAT for free**:
 - Washington, D.C., does not require high schoolers to take the SAT, but it has provided the exam—as well as the PSAT—for free since 2013. 
 - Oklahoma provides funding for every public school junior to take either the ACT or SAT for free on a specific testing date.
 - South Carolina does not require either the SAT or the ACT; however, it provides both exams to 11th graders at no cost.  
 - All Tennessee high school students in 11th grade are required to take either the SAT or ACT—school districts are given the choice of which test to provide or may offer both exams. 
---

## Data Dictionary:

|Feature|Type|Dataset|Description|
|---|---|---|---| 
|state|*object*|modified_sat_merged.csv|States where the high school graduates who took the SAT reside in.| 
|participation_rate_2017|*float*|modified_sat_merged.csv|Percentage (in 2 decimal places) of the state's high school graduates who took the SAT in 2017, e.g. 0.25 means 25%.| 
|ebrw_score_2017|*integer*|modified_sat_merged.csv|Average Evidence-Based Reading and Writing (EBRW) score (200-800) of high school graduates by state in 2017.| 
|math_score_2017|*integer*|modified_sat_merged.csv|Average Math score (200-800) of high school graduates by state in 2017.|
|total_score_2017|*integer*|modified_sat_merged.csv|Average Total (EBRW + Math) score (400-1,600) of high school graduates by state in 2017.| 
|participation_rate_2018|*float*|modified_sat_merged.csv|Percentage (in 2 decimal places) of the state's high school graduates who took the SAT in 2018, e.g. 0.25 means 25%.| 
|ebrw_score_2018|*integer*|modified_sat_merged.csv|Average Evidence-Based Reading and Writing (EBRW) score (200-800) of high school graduates by state in 2018.| 
|math_score_2018|*integer*|modified_sat_merged.csv|Average Math score (200-800) of high school graduates by state in 2018.|
|total_score_2018|*integer*|modified_sat_merged.csv|Average Total (EBRW + Math) score (400-1,600) of high school graduates by state in 2018.| 
|participation_rate_2019|*float*|modified_sat_merged.csv|Percentage (in 2 decimal places) of the state's high school graduates who took the SAT in 2019, e.g. 0.25 means 25%.| 
|ebrw_score_2019|*integer*|modified_sat_merged.csv|Average Evidence-Based Reading and Writing (EBRW) score (200-800) of high school graduates by state in 2019.| 
|math_score_2019|*integer*|modified_sat_merged.csv|Average Math score (200-800) of high school graduates by state in 2019.|
|total_score_2019|*integer*|modified_sat_merged.csv|Average Total (EBRW + Math) score (400-1,600) of high school graduates by state in 2019.|
|delta_1718|*float*|modified_sat_merged.csv|Percentage change (in 2 decimal places) in state's participation rate from 2017 to 2018.| 
|delta_1819|*float*|modified_sat_merged.csv|Percentage change (in 2 decimal places) in state's participation rate from 2018 to 2019.| 

---

## Findings:
#More then 75% of us college dont require sat and act as of 2021
#SAT scores are moderately correlated with first year retention rate and graduation rate(4 years), with respective coefficient value of 0.51 and 0.5
#37% less people submmited sat/act scores upon the exemption in 2019
#9.7% increase in admission of minority in US colleges
#A sharp drop in grdaution rate and a sharp increase in freshman retention rate upon exemption of sat/act test


---

## Conclusions/Recommendations:
#benefit of exempting sat and act scores outweights its setbacks, therefore US colleges are encourge to continute exemption of test results post covid

#Analysis Areas for Improvement:
#Confidence of recommendation may improve, alter, or amend upon increase avaliability of post-exemption data
#Pre-2013 college data are not included for the analysis; accuracy of analysis may improve with pre-2013 data
#Correlations of HSGPA/SAT vs College GPA are based on a sample size of 30 universities; accuracy may improve with the inclusion of a bigger sample size
