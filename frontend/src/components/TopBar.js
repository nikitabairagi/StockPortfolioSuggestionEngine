import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
// import IconButton from '@material-ui/core/IconButton';
// import AccountCircle from '@material-ui/icons/AccountCircle';
import MultilineChart from '@material-ui/icons/MultilineChart';
import "../styles/styles.scss";

export class TopBar extends React.Component{

  useStyles = ()=>{
    return makeStyles(theme => ({
      root: {
        flexGrow: 1,
      },
      menuButton: {
        marginRight: theme.spacing(2),
      },
      title: {
        flexGrow: 1,
      },
    }))
  };

  render(){
    const classes = this.useStyles();

    return (
      <div className={classes.root}>
        <AppBar className="top-app-bar" position="static">
          <Toolbar>
            <MultilineChart/>
            <Typography variant="h6" className={"title"}>
              Stock Portfolio
            </Typography>

            <div className="auth-toolbar">
              {/*<IconButton*/}
              {/*  aria-label="account of current user"*/}
              {/*  aria-controls="menu-appbar"*/}
              {/*  aria-haspopup="true"*/}
              {/*  color="inherit"*/}
              {/*>*/}
              {/*  <AccountCircle />*/}
              {/*</IconButton>*/}
              {/*<Typography variant="h9" className={classes.title}>*/}
              {/*  Hi, Akshay!*/}
              {/*</Typography>*/}
              <Button className={"logout-button"} color="inherit">Logout</Button>
            </div>
          </Toolbar>
        </AppBar>
      </div>
    );
  }

}
