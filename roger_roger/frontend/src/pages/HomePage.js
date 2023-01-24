import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
} from "react-router-dom";

import Finance from "./finance/Finance";

export default class HomePage extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (
            <Router>
                <Routes>
                    <Route exact path="/" element={<Finance/>}></Route>
                    <Route path="/finance/" element={<Finance/>}>
                        <Route path="update/">
                            <Route path="qrcode/"></Route>
                        </Route>
                    </Route>
                </Routes>
            </Router>
        );
    }
}