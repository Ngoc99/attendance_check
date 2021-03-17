import {
  FILE_UPLOAD_REQUEST,
  FILE_UPLOAD_SUCCESS,
  FILE_UPLOAD_FAIL,
  FILE_UPLOAD_RESET,
  FILE_DOWNLOAD_REQUEST,
  FILE_DOWNLOAD_SUCCESS,
  FILE_DOWNLOAD_FAIL,
} from "../constants/fileConstant";

export const fileUploadReducer = (state = {}, action) => {
  switch (action.type) {
    case FILE_UPLOAD_REQUEST:
      return { loading: true };
    case FILE_UPLOAD_SUCCESS:
      return { loading: false, success: true, file: action.payload };
    case FILE_UPLOAD_FAIL:
      return { loading: false, error: action.payload };
    case FILE_UPLOAD_RESET:
      return {};
    default:
      return state;
  }
};
