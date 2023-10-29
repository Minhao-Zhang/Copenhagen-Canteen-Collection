import React from "react";
import NavigationBar from "../Components/NavigationBar";

interface CanteenProps {}

interface CanteenStates {}

class CanteenTemplate extends React.Component<CanteenProps, CanteenStates> {
  constructor(props: CanteenStates) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="min-h-screen bg-gray-300">
        <NavigationBar />
      </div>
    );
  }
}

export default CanteenTemplate;
