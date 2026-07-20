function DashboardCards({ data }) {

    return (

        <div
            style={{
                display: "flex",
                gap: "20px",
                marginBottom: "30px",
                flexWrap: "wrap"
            }}
        >

            <div className="card">

                <h3>Total Messages</h3>

                <h1>{data.total_messages}</h1>

            </div>

            <div className="card">

                <h3>Total Sessions</h3>

                <h1>{data.total_sessions}</h1>

            </div>

            <div className="card">

                <h3>Total Agents Used</h3>

                <h1>{data.agents.length}</h1>

            </div>

        </div>

    );

}

export default DashboardCards;