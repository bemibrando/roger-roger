import React, { Component } from "react";
import { Link, Outlet } from "react-router-dom";

export default class Finance extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return <>
            <a href="/finance/update">Finance Update</a>
        </>;
    }
}