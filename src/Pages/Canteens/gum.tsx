import React from "react";
import CanteenTemplate from "../CanteenTemplate";
import canteenData from "../../Components/load_canteens";
import menuData from "../../Components/load_menus";

interface EmptyProps {}

interface EmptyStats {}

class GUM extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <CanteenTemplate
        canteenInfo={canteenData.KU_GUMLE_KANTINE}
        menuInfo={menuData.KU_GUMLE_KANTINE}
      />
    );
  }
}

export default GUM;
