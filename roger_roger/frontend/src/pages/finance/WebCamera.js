import React, { Component } from "react";
import ReactDOM from "react-dom/client";

export default class WebCamera extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <p>Hi</p>
        );
    }
}

const cameraDiv = ReactDOM.createRoot(document.getElementById("camera"));
cameraDiv.render(<WebCamera />);