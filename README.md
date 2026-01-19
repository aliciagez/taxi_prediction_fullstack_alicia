EDA / Cleaning data:
I did some basic eda on the dataset, checking datatypes and such. 

For the cleaning i deciden to do 2 version of the origal dataset. One with removed nan values and one with filled nan values. I decided to remove the colums for weather and traffic conditions since they did not seem that relevant. I made the passenge coun to ints since it doesn't make sense for them to be floats. I did some dummy encdoing for time of day and made them into ints and same for day of week. The i export them to their own csv files. 


ML models: 

Linjer regression: 
I will be using the dataset with removed nan values for this and using price as the target varibel (trip price). I also removed outliers in the traget varible only becase to protect the goal of the model but not in the featurs beacuse it can contain real data that can help the (Daniela/ LLM).
I evaluated it by locking at the meritics and compatred it to a base line (LLM). The model wasnt terrible but it mosty only predeiced on the mean so it was not the best. 

Logistic regression: (mostly for fun)
For this i will first test with y as time of day and then if its a weekday or not, using the same removved nan values dataset. 

Random forest: 







