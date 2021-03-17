import React, { Fragment } from "react";
import { Route, Switch } from "react-router-dom";
import Navbar from "../components/Navbar";
import Professors from "../components/Professors";
import HomeScreen from "../components/Screens/Home";
function App() {
  return (
    <Fragment>
      <Navbar />
      <Switch>
        <Route path="/users" component={Professors} />
        {/* <Route path="/about" component={FileUpload} /> */}
        <Route path="/" component={HomeScreen} exact />
      </Switch>
    </Fragment>
  );
}

export default App;
