import React from 'react';
import {bindActionCreators} from "redux";
import * as actions from "../actions/stockInputActions";
import {connect} from "react-redux";
import PropTypes from "prop-types";
import {LineBarAreaComposedChart} from "./LineBarChart";
import {StockPieChart} from "./StockPieChart";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

class Reports extends React.Component {

  constructor(props) {
    super(props);
  }

  getRows = () => {
   let rows = [];
    let allocation = this.props.userInput.allocation ? this.props.userInput.allocation["allocation"] : {};
    let totalAllocation = this.props.userInput.allocation && Array.isArray(this.props.userInput.allocation.weekly_trend) &&
      this.props.userInput.allocation.weekly_trend.find(x=> x.name === "Latest Value")["Total Portfolio"];
    let counter = 0;
    for (let key of Object.keys(allocation)) {
      let holdingValue = allocation[key]["price"] * allocation[key]["stocks"];
      let holdingRatio = holdingValue/totalAllocation *100;
      rows.push(<TableRow key={counter}>
        <TableCell align="right">{key}</TableCell>
        <TableCell align="right">{allocation[key]["stocks"]}</TableCell>
        <TableCell align="right">${allocation[key]["price"].toFixed(2)}</TableCell>
        <TableCell align="right">${holdingValue.toFixed(3)}</TableCell>
        <TableCell align="right">{holdingRatio.toFixed(2)}%</TableCell>
        <TableCell align="right">{allocation[key]["strategy"]}</TableCell>
      </TableRow>);
      counter++;
    }

    return rows;
  };

  render() {
    return (
      <div className="report-container">

        {this.props.userInput && this.props.userInput.allocation &&
        this.props.userInput.allocation.weekly_trend && this.props.userInput.allocation.allocation &&
        <Paper className="table-container">
          <Typography className="title" variant="h6">
            Stock Allocations Based On Strategies
          </Typography>
          <Divider/>
          <div className="table-parent">
            <Table className={"allocation-table"} aria-label="allocation table">
              <TableHead>
                <TableRow>
                  <TableCell align="right">Symbol</TableCell>
                  <TableCell align="right">Number of Stocks</TableCell>
                  <TableCell align="right">Latest Price</TableCell>
                  <TableCell align="right">Holding Value</TableCell>
                  <TableCell align="right">Holding Ratio</TableCell>
                  <TableCell align="right">Strategy</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.getRows()}
              </TableBody>
            </Table>
          </div>
        </Paper>
        }


        {this.props.userInput && this.props.userInput.allocation &&
        this.props.userInput.allocation.pie_chart_data &&
        <Paper className="pie-paper">
          <Typography className="title" variant="h6">
            Holding Ratio
          </Typography>
          <Divider/>
          <StockPieChart data={this.props.userInput.allocation.pie_chart_data}/>
        </Paper>}

        {this.props.userInput && this.props.userInput.allocation &&
        this.props.userInput.allocation.weekly_trend &&
        <Paper className="chart-paper">
          <Typography className="title" variant="h6">
            Portfolio Weekly Trend
          </Typography>
          <Divider/>
          <LineBarAreaComposedChart data={this.props.userInput.allocation.weekly_trend}/>
        </Paper>}


        {this.props.userInput.error && <div>{this.props.userInput.error}</div>}
      </div>
    );
  }
}

Reports.propTypes = {
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
)(Reports);

