import React from "react";
// import * as menu from "../Components/load_menu";
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

  parseJSONWithNewlines(jsonData: string) {
    const parsedText = jsonData
      .split("\n")
      .map((line, index) => <p key={index}>{line}</p>);
    return parsedText;
  }
}

export default App;
