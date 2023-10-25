import React from "react";
import { createHashRouter, RouterProvider } from "react-router-dom";
import App from "../Pages/App";
import Map from "../Pages/Map";

interface RouterProps {}

interface RouterStates {}

class Router extends React.Component<RouterProps, RouterStates> {
  constructor(props: RouterProps) {
    super(props);
    this.state = {};
  }

  render() {
    const router = createHashRouter([
      {
        path: "/",
        element: <App />,
      },
      {
        path: "/Map",
        element: <Map />,
      },
    ]);
    return <RouterProvider router={router} />;
  }
}

export default Router;
