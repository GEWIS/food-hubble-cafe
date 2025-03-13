import './index.css'
import { useState} from 'react';
import {useInterval} from "usehooks-ts";
import Order from "./Order";

function App() {
    const [orders, setOrders] = useState<number[]>([])

    useInterval(
        () => {
            fetch('/api/getOrders')
                .then(response => response.json())
                .then(response => setOrders(response.orders))
                .catch((e) => console.error(e))
        },
        import.meta.env.VITE_ORDER_INTERVAL
    )

    return (
        <div className="main">
            <div className="order-container">
                <img src="/hubble-logo.png" alt="Hubble Logo" width="80%" className={"logo"}/>
                {
                    orders.map((order, i) => (
                        <Order
                            key={i}
                            orderNumber={order}
                        />
                    ))
                }
            </div>
        </div>
    );
}

export default App;
