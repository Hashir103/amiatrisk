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
        >
          GET STARTED
        </Button>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          onClick={console.log('hey')}
        >
          Click Here to Learn More
        </Button>
      </div>
    </div>
  );
}

export default VidSec;
