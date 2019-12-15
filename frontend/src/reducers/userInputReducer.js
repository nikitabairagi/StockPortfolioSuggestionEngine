import {ERROR, SAVE_USER_INPUT, USER_LOGGED_IN} from '../constants/actionTypes';
import objectAssign from 'object-assign';
import initialState from './initialState';

export default function userInputReducer(state = initialState.userInput, action) {

  switch (action.type) {
    case SAVE_USER_INPUT:
      return  objectAssign({}, state, {allocation: action.allocation, error: ""});

    case ERROR:
      return  objectAssign({}, state, {error: action.error});

    default:
      return state;
  }
}
