import React, { Component } from 'react';
import Joystick from './Joystick';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to Proboty</h2>
        </div>
        <Joystick/>
      </div>
    );
  }
}

export default App;
