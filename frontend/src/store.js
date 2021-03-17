import { createStore, compose, applyMiddleware, combineReducers } from "redux";
import thunk from "redux-thunk";
import { fileUploadReducer } from "./reducer/fileReducer";

const reducer = combineReducers({
  fileUpload: fileUploadReducer,
});
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  reducer,
  //   initialState,
  composeEnhancer(applyMiddleware(thunk))
);

export default store;
