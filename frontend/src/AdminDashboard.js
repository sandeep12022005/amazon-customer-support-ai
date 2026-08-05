import { useEffect, useState } from "react";
import axios from "axios";

import DashboardCards from "./components/DashboardCards";
import IntentPieChart from "./components/IntentPieChart";
import AgentBarChart from "./components/AgentBarChart";

function AdminDashboard(){

const [data,setData]=useState(null);

useEffect(()=>{

axios.get(
    "https://amazon-customer-support-ai-production.up.railway.app/analytics"
)

.then(res=>{

setData(res.data);

});

},[]);

if(!data)

return <h2>Loading...</h2>;

return(

<div style={{padding:"30px"}}>

<h1>

Amazon Customer Support Dashboard

</h1>

<DashboardCards data={data}/>

<div
style={{

display:"flex",

gap:"40px",

flexWrap:"wrap"

}}
>

<div style={{width:"450px"}}>

<h2>

Intent Distribution

</h2>

<IntentPieChart

intents={data.intents}

/>

</div>

<div style={{width:"450px"}}>

<h2>

Agent Usage

</h2>

<AgentBarChart

agents={data.agents}

/>

</div>

</div>

</div>

);

}

export default AdminDashboard;