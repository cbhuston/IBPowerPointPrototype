import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './navbar/Navbar'
import Home from './home/Home'

class App extends Component {
  render() {
    return (
    <div>
      <Navbar/>
      <Home/>
    </div>
    );
  }
}

export default App;
