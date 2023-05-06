import { useCallback } from 'react';

// Default V2 theme
import 'survey-core/defaultV2.min.css';
// Modern theme
// import 'survey-core/modern.min.css';
import { Model } from 'survey-core';
import { Survey } from 'survey-react-ui';

// const SURVEY_ID = 1;

const surveyJson = {
    "title": "Health Screening Questionnaire",
    "logoPosition": "right",
    "focusFirstQuestionAutomatic": false,
    "completedHtml": "<h3>Thank you for doing the Questionaire!</h3>",
    "pages": [
     {
      "name": "page1",
      "elements": [
       {
        "type": "dropdown",
        "name": "question5",
        "title": "Age Group",
        "isRequired": true,
        "choices": [
         {
          "value": "Item 1",
          "text": "0-19"
         },
         {
          "value": "Item 2",
          "text": "20-34"
         },
         {
          "value": "Item 3",
          "text": "35-49"
         },
         {
          "value": "Item 4",
          "text": "50-64"
         },
         {
          "value": "Item 5",
          "text": "65-79"
         }
        ]
       },
       {
        "type": "dropdown",
        "name": "question3",
        "title": "Sex",
        "isRequired": true,
        "choices": [
         {
          "value": "Item 1",
          "text": "Male"
         },
         {
          "value": "Item 2",
          "text": "Female"
         }
        ]
       },
       {
        "type": "dropdown",
        "name": "question4",
        "title": "Province",
        "isRequired": true,
        "choices": [
         "Alberta",
         "British Columbia",
         "Manitoba",
         "New Brunswick",
         "Newfoundland and Labrador",
         "Northwest Territories",
         "Nova Scotia",
         "Nunavut",
         "Ontario",
         "Prince Edward Island",
         "Quebec",
         "Saskatchewan",
         "Yukon"
        ]
       },
       {
        "type": "boolean",
        "name": "question6",
        "title": "Family History with Highest Risk Disease"
       },
       {
        "type": "dropdown",
        "name": "question1",
        "title": "Race",
        "choices": [
         {
          "value": "- African American",
          "text": "African American"
         },
         {
          "value": "- Hispanics/Latino",
          "text": "Hispanics/Latino"
         },
         {
          "value": "- Asian American",
          "text": "Asian American"
         },
         {
          "value": "- Native Americans",
          "text": "Native Americans"
         },
         {
          "value": "- Caucasian",
          "text": "Caucasian"
         },
         {
          "value": "-Mixed Race",
          "text": "Mixed Race"
         },
         {
          "value": "-Other",
          "text": "Other"
         }
        ]
       }
      ]
     }
    ],
    "showQuestionNumbers": "off",
    "questionErrorLocation": "bottom",
    "checkErrorsMode": "onComplete",
    "completeText": "Submit",
    "widthMode": "responsive"
   };

function Surve() {
  const survey = new Model(surveyJson);
  const alertResults = useCallback((sender) => {
    const results = JSON.stringify(sender.data);
    // saveSurveyResults(
    //   "https://your-web-service.com/" + SURVEY_ID,
    //   sender.data
    // )
  }, []);

  survey.onComplete.add(alertResults);

  return <Survey model={survey} />;
}

// function saveSurveyResults(url, json) {
//   const request = new XMLHttpRequest();
//   request.open('POST', url);
//   request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
//   request.addEventListener('load', () => {
//     // Handle "load"
//   });
//   request.addEventListener('error', () => {
//     // Handle "error"
//   });
//   request.send(JSON.stringify(json));
// }

export default Surve;