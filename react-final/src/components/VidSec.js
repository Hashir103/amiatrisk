import React from 'react';
import '../App';
import { Button } from './Button';
import './VidSec.css';
import videoBg from '../videos/mainvid.mp4';

function VidSec() {
  return (
    <div className='hero-container'>
      <video src={videoBg} autoPlay loop muted />
      <h1>AM I AT RISK</h1>
      <p>Stay Informed, Stay Alive</p>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          destination='/screening'
        >
          GET STARTED WITH YOUR TEST TODAY
        </Button>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          destination='/applynow'
        >
          Sign Your Company Up for a Free Health Screening
        </Button>
      </div>
    </div>
  );
}

export default VidSec;
