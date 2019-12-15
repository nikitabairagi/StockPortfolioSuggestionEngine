import {SAVE_USER_INPUT, ERROR} from '../constants/actionTypes';
import {allocate} from "../api/api"


export function saveUserInput(userInput) {
  return function (dispatch){
    return allocate(userInput)
      .then(res => res.json())
      .then(response => {

        if(response.error) {
          // dispatch success
          dispatch( {
            type: ERROR,
            error: response.error
          });
        } else {
          // dispatch error
          dispatch( {
            type: SAVE_USER_INPUT,
            allocation: response
          });
        }
    })
  }
}
