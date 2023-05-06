import { useCallback } from 'react';

// Default V2 theme
import 'survey-core/defaultV2.min.css';
// Modern theme
// import 'survey-core/modern.min.css';
import { Model } from 'survey-core';
import { Survey } from 'survey-react-ui';

// const SURVEY_ID = 1;

const surveyJson = {
    "title": "Health Assessment Screening Application",
    "description": "All fields with an asterisk (*) are required fields and must be filled out in order to process the information in strict confidentiality.",
    "focusFirstQuestionAutomatic": false,
    "completedHtml": "<h3>Thank you for completing the application!</h3>",
    "pages": [
     {
      "name": "company-info",
      "elements": [
       {
        "type": "panel",
        "name": "full-name",
        "elements": [
         {
          "type": "text",
          "name": "first-name",
          "title": "First name",
          "isRequired": true,
          "maxLength": 25
         },
         {
          "type": "text",
          "name": "last-name",
          "startWithNewLine": false,
          "title": "Last name",
          "isRequired": true,
          "maxLength": 25
         },
         {
          "type": "text",
          "name": "question1",
          "title": "Name of Workplace/Senior Home",
          "isRequired": true
         }
        ],
        "title": "Full name"
       },
       {
        "type": "panel",
        "name": "personal-info",
        "elements": [
         {
          "type": "text",
          "name": "question2",
          "title": "Number Of Employees/Seniors being Assessed ",
          "isRequired": true,
          "inputType": "number"
         },
         {
          "type": "text",
          "name": "birthdate",
          "title": "Available Date for Assessment ",
          "isRequired": true,
          "inputType": "date"
         }
        ]
       }
      ],
      "title": "Company Information"
     },
     {
      "name": "finalization",
      "elements": [
       {
        "type": "comment",
        "name": "additional-info",
        "title": "Additional information"
       },
       {
        "type": "text",
        "name": "date",
        "title": "Date",
        "inputType": "date"
       },
       {
        "type": "signaturepad",
        "name": "signature",
        "startWithNewLine": false,
        "title": "Signature"
       }
      ],
      "title": "Additional Inquires and Confirmation"
     }
    ],
    "showQuestionNumbers": "off",
    "questionErrorLocation": "bottom",
    "completeText": "Submit",
    "widthMode": "static",
    "width": "1000px"
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