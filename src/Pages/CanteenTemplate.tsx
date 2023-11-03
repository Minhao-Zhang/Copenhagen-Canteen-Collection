import React from "react";
import NavigationBar from "../Components/NavigationBar";
import { Table } from "react-bootstrap";

interface CanteenProps {
  canteenInfo: any;
  menuInfo: any;
}

interface CanteenStates {}

class CanteenTemplate extends React.Component<CanteenProps, CanteenStates> {
  constructor(props: CanteenProps) {
    super(props);
    this.state = {};
  }

  render() {
    const displayName = this.props.canteenInfo.DisplayName;
    const address = this.props.canteenInfo.Address;
    const googleMapLink = this.props.canteenInfo.GoogleMapLink;
    const openHours = this.props.canteenInfo.Hours;
    const price = this.props.canteenInfo.Price;

    // check if menu is empty
    let menuUnavailable = false;
    for (let key in this.props.menuInfo) {
      if (this.props.menuInfo.hasOwnProperty(key)) {
        menuUnavailable = false;
        break;
      }
    }

    // check
    let currentDate = new Date();
    const startDate = new Date(currentDate.getFullYear(), 0, 1);
    const days = Math.floor(
      (currentDate.getTime() - startDate.getTime()) / (24 * 60 * 60 * 1000)
    );
    const weekNumber = Math.ceil(days / 7);
    if (this.props.menuInfo.WeekNumber != weekNumber) {
      menuUnavailable = true;
    }

    // if menu is empty, display "Menu is not available"
    let thisWeekMenu = <p>Menu is not available</p>;
    // if menu is available, display the menu
    if (!menuUnavailable) {
      const monfri = this.getMondayAndFridayThisWeek();
      thisWeekMenu = (
        <div>
          <div className="tw-text-center tw-text-xl tw-font-bold">
            Week {weekNumber}, from{" "}
            {monfri.monday.toLocaleDateString("en-US", {
              month: "short",
              day: "numeric",
            })}{" "}
            to{" "}
            {monfri.friday.toLocaleDateString("en-US", {
              month: "short",
              day: "numeric",
            })}
          </div>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Date</th>
                <th>Menu</th>
              </tr>
              <tr>
                <td>Monday</td>
                <td>{this.getLinedMenu(this.props.menuInfo.Monday)}</td>
              </tr>
              <tr>
                <td>Tuesday</td>
                <td>{this.getLinedMenu(this.props.menuInfo.Tuesday)}</td>
              </tr>
              <tr>
                <td>Wednesday</td>
                <td>{this.getLinedMenu(this.props.menuInfo.Wednesday)}</td>
              </tr>
              <tr>
                <td>Thursday</td>
                <td>{this.getLinedMenu(this.props.menuInfo.Thursday)}</td>
              </tr>
              <tr>
                <td>Friday</td>
                <td>{this.getLinedMenu(this.props.menuInfo.Friday)}</td>
              </tr>
            </thead>
            <tbody></tbody>
          </Table>
        </div>
      );
    }

    return (
      <div>
        <NavigationBar />
        <div className="tw-m-5 sm:tw-my-10 sm:tw-mx-20 lg:tw-mx-72 tw-font-serif">
          <h1 className="tw-my-4">{displayName}</h1>
          <h2 className="tw-my-2">Location</h2>
          <a className="tw-text-lg" href={googleMapLink}>
            {address}
          </a>
          <h2 className="tw-my-2">Open Hours</h2>
          <p>{openHours}</p>
          <h2 className="tw-my-2">Price</h2>
          <p>{price}</p>
          <h2>Menu</h2>

          {thisWeekMenu}
        </div>
      </div>
    );
  }

  getMondayAndFridayThisWeek() {
    const currentDate = new Date();
    const dayOfWeek = currentDate.getDay(); // 0 (Sunday) to 6 (Saturday)

    // Calculate the date of this week's Monday and Friday
    const daysUntilMonday = 1 - dayOfWeek; // 1 for Monday
    const daysUntilFriday = 5 - dayOfWeek; // 5 for Friday

    const thisMonday = new Date(currentDate);
    thisMonday.setDate(currentDate.getDate() + daysUntilMonday);

    const thisFriday = new Date(currentDate);
    thisFriday.setDate(currentDate.getDate() + daysUntilFriday);

    return { monday: thisMonday, friday: thisFriday };
  }

  getLinedMenu(menu: string) {
    let displayedMenu = [];
    const menuLines = menu.split("\n");
    for (let i = 0; i < menuLines.length; i++) {
      displayedMenu.push(<div key={i}>{menuLines[i]}</div>);
    }
    return displayedMenu;
  }
}

export default CanteenTemplate;
