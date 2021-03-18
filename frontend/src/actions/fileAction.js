import {
  FILE_UPLOAD_REQUEST,
  FILE_UPLOAD_SUCCESS,
  FILE_UPLOAD_FAIL,
  FILE_UPLOAD_RESET,
} from "../constants/fileConstant";

export const fileUpload = (formData) => async (dispatch) => {
  dispatch({ type: FILE_UPLOAD_REQUEST });
  await fetch("/file_upload", {
    method: "POST",
    body: formData,
  })
    .then((result) => result.json(0))
    .then((data) => {
      data.response_code & (data.response_code !== 200)
        ? dispatch({ type: FILE_UPLOAD_FAIL, payload: data.message })
        : dispatch({ type: FILE_UPLOAD_SUCCESS, payload: data.data });
    })
    .catch((error) => {
      console.log(error);
      dispatch({ type: FILE_UPLOAD_FAIL, payload: error });
    });
};

export const sayHi = () => async (dispatch) => {
  try {
    console.log("calling data");
    const data = await fetch(`/say_hi`)
      .then((response) => response.json())
      .then((data) => console.log(data));

    if (data) {
      console.log(data);
    }
  } catch (e) {
    console.log(e.message);
  }
};
