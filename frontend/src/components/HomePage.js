import React from 'react';
import {StockInputForm} from "./StockInputForm";
import {bindActionCreators} from "redux";
import * as actions from "../actions/stockInputActions";
import {connect} from "react-redux";
import PropTypes from "prop-types";
import Reports from "./Reports";
import Widget from "./Widget";

export class HomePage extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="home-page">

        <div className="input-form">
          <StockInputForm {...this.props}/>
        </div>

        <div className="reports">
          <Widget/>
          <Reports/>
        </div>


        {this.props.userInput.error && <div>{this.props.userInput.error}</div>}
      </div>
    );
  }
}

HomePage.propTypes = {
  actions: PropTypes.any,
  userInput: PropTypes.any,
  history: PropTypes.any
};

function mapStateToProps(state) {
  return {
    userInput: state.userInputReducer
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(actions, dispatch)
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(HomePage);

