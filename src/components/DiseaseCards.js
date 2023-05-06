import React from 'react';
import './DiseaseCards.css';
import DiseaseCardItem from './DiseaseCardItem';
import cardio from '../images/car.jpg';
import diabetes from '../images/diabe.jpg';
import neurologic from '../images/neuro.jpg';
import respir from '../images/res.jpg';
import musskel from '../images/mus.jpg';
import videoBbg from '../videos/bubb.mp4';

function DiseaseCards() {
  return (
    <div className='cards'>
      <video src={videoBbg} autoPlay loop muted />
      <h1>Gain More Insight Into the Top Medical Issues Facing Canadians</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <DiseaseCardItem
              src={cardio}
              text='Cardiovascular diseases are conditions that affect the heart or blood vessels and are often caused by genetic and lifestyle factors. They are the leading cause of death globally, but many cases can be prevented or managed through lifestyle changes and medical treatments.'
              label='Cardiovascular Diseases'
              path='/screening'
            />
            <DiseaseCardItem
              src={diabetes}
              text='Diabetes is a chronic condition that affects how the body processes glucose and can lead to a range of complications such as heart disease, kidney disease, nerve damage, and blindness. It can be managed through medication, diet, exercise, and lifestyle changes.'
              label='Diabetes'
              path='/screening'
            />
          </ul>
          <ul className='cards__items'>
            <DiseaseCardItem
              src={neurologic}
              text='Neurological diseases are conditions that affect the brain and nervous system, causing symptoms such as memory loss, tremors, and difficulty with movement. Treatments such as medication, therapy, and lifestyle changes can help manage symptoms and improve quality of life.'
              label='Neurological Conditions'
              path='/screening'
            />
            <DiseaseCardItem
              src={musskel}
              text='Musculoskeletal diseases are conditions that affect the muscles, bones, and joints, causing pain, stiffness, and decreased mobility. Treatment options include medication, exercise, physical therapy, and surgery.'
              label='Musculoskeletal Disorders'
              path='/applynow'
            />
            <DiseaseCardItem
              src={respir}
              text='Chronic respiratory diseases are conditions that affect the lungs and breathing and can be caused by a variety of factors, such as smoking and air pollution. They can often be managed through medication and lifestyle changes but can also be life-threatening if left untreated.'
              label='Chronic Respiratory Diseases'
              path='/diseases'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default DiseaseCards;