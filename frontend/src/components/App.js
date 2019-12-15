/* eslint-disable import/no-named-as-default */
import { NavLink, Route, Switch } from "react-router-dom";

import HomePage from "./HomePage";
import NotFoundPage from "./NotFoundPage";
import PropTypes from "prop-types";
import React from "react";
import { hot } from "react-hot-loader";
import Reports from "./Reports";
import {TopBar} from "./TopBar";

class App extends React.Component {
  render() {
    const activeStyle = { color: 'blue' };
    return (
      <div className="container">
        <TopBar/>
        {/*<div>*/}
        {/*  <NavLink exact to="/" activeStyle={activeStyle}>Home</NavLink>*/}
        {/*  {' | '}*/}
        {/*  <NavLink to="/reports" activeStyle={activeStyle}>Reports</NavLink>*/}
        {/*  {' | '}*/}
        {/*  <NavLink to="/logout" activeStyle={activeStyle}>Logout</NavLink>*/}
        {/*</div>*/}
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/reports" component={Reports} />

          <Route component={NotFoundPage} />
        </Switch>
      </div>
    );
  }
}

App.propTypes = {
  children: PropTypes.element
};

export default hot(module)(App);
