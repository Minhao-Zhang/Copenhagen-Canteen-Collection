import React from "react";
import NavigationBar from "../Components/NavigationBar";
import "./App.css";

interface EmptyProps {}

interface EmptyStats {}

class App extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <NavigationBar />
        <div className="tw-m-5 sm:tw-my-10 sm:tw-mx-20 lg:tw-mx-72 tw-font-serif">
          <h1 className="tw-my-6">Copenhagen Canteen Collection</h1>
          <h2 className="tw-my-4">How to use this</h2>
          <p className="tw-text-lg">
            This is a collection of canteens in Copenhagen. You can look up
            daily menu for each canteen. Do note that there might be some errors
            as the data is scraped from the canteen websites.
          </p>
          <p className="tw-text-lg">
            We provide a <a href="#/Map"> map </a> where you can see all the
            canteens. If you are interested, you can also go into each canteen
            and see the details like price and location about that canteen. Just
            click on the canteens that are grouped by campus.
          </p>
          <h2 className="tw-my-4">Feedback & collaboration</h2>
          <p className="tw-text-lg">
            If you want to make a suggestion, please send an email to{" "}
            <a href="mailto:z.minhao.01+coding@gmail.com">Minhao Zhang</a>. If
            you are looking for collaboration, please visit{" "}
            <a href="https://github.com/Minhao-Zhang/Copenhagen-Canteen-Collection">
              the GitHub repository
            </a>{" "}
            . I am actively looking for collaborators to help me improve this
            project and any help is appreciated.
          </p>
        </div>
      </div>
    );
  }
}

export default App;
