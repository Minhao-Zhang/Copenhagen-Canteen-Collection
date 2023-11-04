import React from "react";
import CanteenTemplate from "../CanteenTemplate";
import canteenData from "../../Components/load_canteens";
import menuData from "../../Components/load_menus";

interface EmptyProps {}

interface EmptyStats {}

class TEO extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <CanteenTemplate
        canteenInfo={canteenData.KU_TEO}
        menuInfo={menuData.KU_TEO}
      />
    );
  }
}

export default TEO;
