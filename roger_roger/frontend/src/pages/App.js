import React, { Component } from "react";
import ReactDOM from "react-dom/client";
import { render } from "react-dom";
import HomePage from "./HomePage";

export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return <HomePage />;
    }
}

const appDiv = ReactDOM.createRoot(document.getElementById("app"));
appDiv.render(<App />);