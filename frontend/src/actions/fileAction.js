import {
  FILE_UPLOAD_REQUEST,
  FILE_UPLOAD_SUCCESS,
  FILE_UPLOAD_FAIL,
  FILE_UPLOAD_RESET,
} from "../constants/fileConstant";
import axios from "axios";

const API = process.env.REACT_APP_API;

export const fileUpload = (formData) => async (dispatch) => {
  try {
    //console.log(formData);
    dispatch({ type: FILE_UPLOAD_REQUEST });
    //const url = JSON.stringify(`${API}/file_upload`);
    const response = await fetch("/file_upload", {
      method: "POST",
      body: formData,
      // mode: "no-cors",
      // headers: {
      //   Accept: "application/json",
      // },
    })
      .then((result) => result.json())
      .then((data) => console.log(data))
      .catch((error) => error.message);

    dispatch({
      type: FILE_UPLOAD_SUCCESS,
      payload: response.msg,
    });
  } catch (error) {
    dispatch({
      type: FILE_UPLOAD_FAIL,
      payload:
        error.response && error.response.data.msg
          ? error.respone.data.msg
          : error,
    });
  }
};

export const sayHi = () => async (dispatch) => {
  try {
    console.log("calling data");

    // const { data } = axios
    //   .get({ url: `${API}/say_hi` })
    //   .then((res) => res.data);
    const data = await fetch(`${API}/say_hi`)
      .then((response) => response.json())
      .then((data) => console.log(data));

    if (data) {
      console.log(data);
    }
  } catch (e) {
    console.log(e.message);
  }
};
