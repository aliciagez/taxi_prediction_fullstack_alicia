EDA / Cleaning data:
I did some basic eda on the dataset, checking datatypes and such. 

For the cleaning i deciden to do 2 version of the origal dataset. One with removed nan values and one with filled nan values. I decided to remove the colums for weather and traffic conditions since they did not seem that relevant. I made the passenge coun to ints since it doesn't make sense for them to be floats. I did some dummy encdoing for time of day and made them into ints and same for day of week. The i export them to their own csv files. 


ML models: 

Linjer regression: 
I will be using the dataset with removed nan values for this and using price as the target varibel (trip price). I also removed all outliers to protect the goal of the model but not in the featurs beacuse it can contain real data that can help the (Daniela ask teacher).
I evaluated it by locking at the meritics and compatred it to a base line (LLM). The model wasnt terrible but it mosty only predeiced on the mean so it was not the best. 

Logistic regression: (mostly for fun)
For this i will first test with y as time of day and then if its a weekday or not, using the same removed nan values dataset. I also removed all outliers and classifyed the traget varible. it did farly well but usings labes for price is not realistic so will not use this model. 

Random forest: 
I did random forest regression since doing classifications for the price does not really make sense(like i started above). I did no scaling since it does not requeire it but i did remove all nan values and did remove all outliers since random forest is sensetive for outliers. I did use LLM to get the garf for visulasation. 

---------------------------------------------------------------------------------------------------------------------------------------------------

EVALUATION OF MODELS: 

Linjer regression with filled nan values: 
- Mean absolut error 9.510847547245534 
- Mean squarerd error 215.57370217114592
- Root Mean squared error 14.682428347216476
- Baseline = np.float64(59.6996599055302), 25.07280855350934

Linjer regression with removed nan values:
- Mean absolut error 9.501317345842137 
- Mean squarerd error 271.639742629564
- Root Mean squared error 16.481496977810117
- Baseline = np.float64(57.1563652603273), 25.763832419671406

Logistic reregssion with removed nan: 
 - accuray: 0.7186147186147186

Logistic reregssion with filled nan: 
 - accuray: 0.6847133757961783

Randomforest regression: 
- Mean squared error 24.61984726742346
- R-squared 0.9334463147156996
- Out of bounds score 0.9341150032752581


To summarise: 
For startes is logistic regression not really applicalbel on this task since it is not logical to catogorice price but i though it was fun to try atlest. 

For the linjer regerssion it did ok in genreal but not very good with mulitble features 

The randomfroest regerssen was the winner, will be expored to joblib

-------------------------------------------------------------------------------------------------------------------------------------

Backend: 
I did the basemodel classes and some data validation in the data_procssesing. I decied to have all the featurs in so a user can fill in them all but i maked the time of day and time of week optional. As for the catagorical values i added validation/user ui so instead of puting in 1 and 0 they can just check a box with selectbox funktion for esay use. LLM was used on how to make the catogorical vales optinal so the program would not crash if time of day/time of week was not specifyed. Since they did not have that much inpact on the prediction i figuerd i could make them optional. 

Frontend: 
For the frontend with streamlit i wanted to have some diffrent pages so its just not one page and so the predicons could have their own page and one home and one for the raw data and one home page with some introduction. I focused more on the pratical aspects then the estetics. 