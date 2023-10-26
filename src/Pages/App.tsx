import React from "react";
import NavigationBar from "../Components/NavigationBar";

interface EmptyProps {}

interface EmptyStats {}

class App extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
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

export default App;
