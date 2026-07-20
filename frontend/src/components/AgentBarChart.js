import {

Chart as ChartJS,

CategoryScale,

LinearScale,

BarElement,

Title,

Tooltip,

Legend

} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(

CategoryScale,

LinearScale,

BarElement,

Title,

Tooltip,

Legend

);

function AgentBarChart({ agents }) {

const data={

labels:

agents.map(

a=>a._id

),

datasets:[

{

label:"Agent Usage",

data:

agents.map(

a=>a.count

)

}

]

};

return <Bar data={data}/>;

}

export default AgentBarChart;
