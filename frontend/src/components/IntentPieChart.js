import {

Chart as ChartJS,

ArcElement,

Tooltip,

Legend

} from "chart.js";

import { Pie } from "react-chartjs-2";

ChartJS.register(

ArcElement,

Tooltip,

Legend

);

function IntentPieChart({ intents }) {

const data = {

labels:

intents.map(

i=>i._id

),

datasets:[

{

label:"Intent Distribution",

data:

intents.map(

i=>i.count

)

}

]

};

return <Pie data={data}/>;

}

export default IntentPieChart;