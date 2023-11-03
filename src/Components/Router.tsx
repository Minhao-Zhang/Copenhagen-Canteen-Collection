import React from "react";
import { createHashRouter, RouterProvider } from "react-router-dom";
import App from "../Pages/App";
import Map from "../Pages/Map";
import BIO from "../Pages/Canteens/bio";
import FOL from "../Pages/Canteens/fol";
import GAM from "../Pages/Canteens/gam";
import GIM from "../Pages/Canteens/gim";
import GUM from "../Pages/Canteens/gum";
import HCO from "../Pages/Canteens/hco";
import HUM from "../Pages/Canteens/hum";
import JUR from "../Pages/Canteens/jur";
import NBI from "../Pages/Canteens/nbi";
import TEO from "../Pages/Canteens/teo";

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
      {
        path: "/canteens/bio",
        element: <BIO />,
      },
      {
        path: "/canteens/fol",
        element: <FOL />,
      },
      {
        path: "/canteens/gam",
        element: <GAM />,
      },
      {
        path: "/canteens/gim",
        element: <GIM />,
      },
      {
        path: "/canteens/gum",
        element: <GUM />,
      },
      {
        path: "/canteens/hco",
        element: <HCO />,
      },
      {
        path: "/canteens/hum",
        element: <HUM />,
      },
      {
        path: "/canteens/jur",
        element: <JUR />,
      },
      {
        path: "/canteens/nbi",
        element: <NBI />,
      },
      {
        path: "/canteens/teo",
        element: <TEO />,
      },
    ]);
    return <RouterProvider router={router} />;
  }
}

export default Router;
