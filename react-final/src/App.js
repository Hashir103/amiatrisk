import React from 'react';
import './App.css';
import NavBar from './components/NavBar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/webpages/Home';
import Screening from './components/webpages/Screening';
import Diseases from './components/webpages/Diseases';
import ApplyNow from './components/webpages/ApplyNow';

function App() {
  return (
    <>
    <Router>
      <NavBar />
      <Switch>
        <Route path='/' exact component= {Home}/>
        <Route path='/Screening' exact component= {Screening}/>
        <Route path='/Diseases' exact component= {Diseases}/>
        <Route path='/ApplyNow' exact component= {ApplyNow}/>
      </Switch>
    </Router>  
    </>

  );
}

export default App;
