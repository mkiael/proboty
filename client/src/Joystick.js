import React, { Component } from 'react';
import './Joystick.css'

class Joystick extends Component {
  handleTouchStart(e) {
    console.log('Touch start!', e);
  }

  handleTouchMove(e) {
    console.log('Touch move!', e);
  }

  handleTouchEnd(e) {
    console.log('Touch end!', e);
  }
  
  render() {
    return(
        <div className="Joystick" onTouchStart={(e) => this.handleTouchStart(e)} onTouchMove={(e) => this.handleTouchMove(e)} onTouchEnd={(e) => this.handleTouchEnd(e)}>
        This is a joystick
      </div>
    )
  }
}

export default Joystick;
