import React from 'react';

function Table({ data }) {
    return (
        <table border="1">
            <thead>
                <tr>
                    <th>Type</th>
                    <th>Values</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Expenses</td>
                    <td>{data.expenses.join(', ')}</td>
                </tr>
                <tr>
                    <td>Revenue</td>
                    <td>{data.revenue.join(', ')}</td>
                </tr>
                <tr>
                    <td>Profit</td>
                    <td>{data.profit.join(', ')}</td>
                </tr>
            </tbody>
        </table>
    );
}

export default Table;
