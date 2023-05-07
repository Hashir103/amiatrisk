## Am I At Risk
Am I at Risk empirically identifies the user's most prevalent diseases using machine learning and historical government data.

## How To Run
Open the project directory and run app.py

## Inspiration
Though there are many problems with the Canadian healthcare system, one of the more prevalent issues is the lack of available family physicians, which was made worse during COVID-19. Around 6.5 million Canadians fail to obtain a family doctor. The role of a family doctor is essential in regularly evaluating patient health risks. Considering millions do not have a family physician, a plethora of our population is unaware of their own health. Our country is in need of an accurate health risk predictor that is personalized to every individual.

## What it does
Am I at Risk provides a way for Canadians who want to assess their health when they otherwise could not. An individual's risk for possible diseases is first assessed through a general questionnaire based on their answers. This information is then compared with detailed incidence and prevalence trends from 20 years of historical data, and an updated prediction of the users risk is provided. The exact statistical technique used for this risk assessment was a linear regression.


## How we built Am I At Risk
The website was building using React JS and was connected to a Flask backend. The chatbot was created using HTML/CSS/Javascript and was connected to a Cohere generating API to generate answers based of the user’s question. We scraped data from the Government of Canada and developed a Linear Regression model for the user's demographic risk for the current year using Python and SciKit Learn.

## Challenges we ran into
The challenges that we faced when creating this project was implementing the React JS frontend with the Flask backend. In the end we had to get a static snapshot of the website and convert minified code back to HTML/CSS & JS, which then interacted with our backend. In addition, parsing data efficiently and accounting for all the variance within the data posed a challenge. Finally, creating a coherent and continuous chatbot integration was difficult as there were issues parsing the data from the frontend with the Flask backend.


## Accomplishments that we're proud of
Overall, we are extremely proud of our mission to assist the Canadian healthcare system with our knowledge of statistical analyses. For years now, Canada has been in a healthcare crisis and our creation provides a novel method to potentially mitigate our Countries drawbacks. Furthermore, we are proud to claim that this type of statistical solution has not been approached prior to Am I At Risk. Last but not least, we are thrilled to overcome the multiple challenges we faced throughout the process of creation.


## What we learned
In addition to our research on the Canadian healthcare system and its drawbacks, we have all greatly developed our technical skills. We improved understanding and skill on website design, linking our frontend to backend, applying a statistical analysis (i.e., linear regression) to an extensive dataset. Altogether, we have gained great appreciation for healthcare workers in Canada to deal with the high stress environment.


## What's next for Am I At Risk
Our future plans for the healthcare web application include putting the parsed data into a cloud database like MongoDB to retrieve data as more years are added. Microsoft Azure will eventually be used to host the application, which is important for handling traffic and storing screening requests. This is also necessary for handling multiple screenings. By utilizing these technologies, we can ensure that our application is scalable, reliable, and can handle large amounts of data and traffic. Additionally, this will enable us to provide a better user experience for patients and healthcare providers, while also improving the accuracy and efficiency of the screening process.

