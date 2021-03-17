import React, { Fragment, useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Navbar from "../Navbar";
import { fileUpload, sayHi } from "../../actions/fileAction";

const data_csv =
  "/Users/ngocho/Downloads/TKBQLMH HK2 2020-2021 xuat 21.02.CheckAttendance.xls";

const HomeScreen = (props) => {
  const dispatch = useDispatch();
  const [selectedFile, setSelectedFile] = useState({});
  const [isFilePicked, setIsFilePicked] = useState(false);
  const { loading, error, success, file } = useSelector(
    (state) => state.fileUpload
  );
  // useEffect(() => {
  //   console.log(selectedFile);
  // });

  const changeHandler = (event) => {
    console.log(event);
    setSelectedFile(event.target.files[0]);
    //console.log(event.target.files[0]);
    setIsFilePicked(true);
  };
  const uploadHandler = (e) => {
    e.preventDefault();
    console.log(selectedFile);
    var formData = new FormData();
    formData.append("name", selectedFile);

    // formData.append("uploadFile", selectedFile);
    console.log(formData.get("name"));
    dispatch(fileUpload(formData));
  };
  // useEffect(() => {
  //   try {
  //     const result = dispatch(sayHi());
  //     if (result) {
  //       console.log("Success");
  //       console.log("Hi");
  //     }
  //   } catch (e) {
  //     console.log(e.message);
  //   }
  // });
  return (
    <Fragment>
      <form id="formData" onSubmit={uploadHandler}>
        <div className="form-group">
          <label for="fileUpload">Choose a file for uploading</label>
          <input
            type="file"
            name="fileUpload"
            id="fileUpload"
            onChange={changeHandler}
          />
        </div>

        <div>
          <button type="submit">Upload</button>
        </div>
      </form>
    </Fragment>
  );
};

export default HomeScreen;
