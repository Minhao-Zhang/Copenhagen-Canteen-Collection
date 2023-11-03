import React from "react";
import CanteenTemplate from "../CanteenTemplate";
import canteenData from "../../Components/load_canteens";
import menuData from "../../Components/load_menus";

interface EmptyProps {}

interface EmptyStats {}

class JUR extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <CanteenTemplate
        canteenInfo={canteenData.KU_HUM_KANTINEN}
        menuInfo={menuData.KU_HUM_KANTINEN}
      />
    );
  }
}

export default JUR;
