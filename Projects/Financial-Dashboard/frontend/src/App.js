import React, { useState, useEffect } from 'react';
import Chart from './components/Chart';
import Table from './components/Table';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('/api/data')
            .then(res => res.json())
            .then(data => setData(data));
    }, []);

    return (
        <div>
            <h1>Financial Dashboard</h1>
            {data ? (
                <>
                    <Chart data={data} />
                    <Table data={data} />
                </>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;
