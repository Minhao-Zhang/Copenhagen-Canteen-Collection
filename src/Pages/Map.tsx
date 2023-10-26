import React from "react";
import NavigationBar from "../Components/NavigationBar";
import "./Map.css";
import "leaflet/dist/leaflet.css";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.webpack.css";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import MENUS from "../Components/load_menu";
import LOCATIONS from "../Components/load_canteen";

const NAMES = [
  "KU_BIO_CENTERET",
  "KU_FOLKEKOKKEN",
  "KU_GAMLE_TAASTRUP",
  "KU_GEOCENTER_CITY",
  "KU_GIMLE_KANTINE",
  "KU_GUMLE_KANTINE",
  "KU_HCØ_KANTINEN",
  "KU_HUM_KANTINEN",
  "KU_JUR_KANTINEN",
  "KU_NBI_KANTINEN",
  "KU_TEO",
];

interface EmptyProps {}

interface EmptyStats {}

class Map extends React.Component<EmptyProps, EmptyStats> {
  constructor(props: EmptyProps) {
    super(props);
    this.state = {};
  }

  render() {
    let markers = [];
    // get the week number
    let currentDate = new Date();
    const startDate = new Date(currentDate.getFullYear(), 0, 1);
    const days = Math.floor(
      (currentDate.getTime() - startDate.getTime()) / (24 * 60 * 60 * 1000)
    );

    const weekDays: { [index: number]: string } = {
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
    };

    const weekNumber = Math.ceil(days / 7);
    const weekDay = weekDays[currentDate.getDay()];

    // write a for loop to add markers
    for (let i = 0; i < NAMES.length; i++) {
      const key = NAMES[i];
      const lat = LOCATIONS[key].Lat;
      const lon = LOCATIONS[key].Lon;
      const displayName = LOCATIONS[key].DisplayName;

      let todayMenu = MENUS[key][weekDay];
      // check whether the menu is up-to-date
      if (parseInt(MENUS[key].WeekNumber) !== weekNumber) {
        todayMenu = "No updated menu available";
      }
      // check whether the menu exists
      if (todayMenu === undefined) {
        todayMenu = "No menu available";
      }
      // properly display multi-line menu
      const menuLines = todayMenu.split("\n");
      let displayedMenu = [];
      for (let j = 0; j < menuLines.length; j++) {
        displayedMenu.push(<div key={j}>{menuLines[j]}</div>);
      }

      // push them into the markers array
      markers.push(
        <Marker key={i} position={[lat, lon]}>
          <Popup>
            <h5>{displayName}</h5>
            {displayedMenu}
          </Popup>
        </Marker>
      );
    }

    return (
      <div>
        <NavigationBar />
        <MapContainer
          center={[55.68228, 12.56679]}
          zoom={13}
          scrollWheelZoom={true}
        >
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {markers}
        </MapContainer>
      </div>
    );
  }
}

export default Map;
