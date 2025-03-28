import './index.css';
import { useEffect, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';

interface Order {
  number: number;
  expiry: string;
}

function App() {
  const [orders, setOrders] = useState<Order[]>([]);

  const getOrders = () => {
    fetch('/api/orders')
      .then((response) => response.json())
      .then((response: Order[]) => {
        setOrders(
          response
            .filter((order) => {
              const timeTillOrderEnd = new Date(order.expiry).getTime() - Date.now();
              return timeTillOrderEnd > 0;
            })
            .sort((a, b) => b.number - a.number),
        );
      })
      .catch(() => console.error('Something went wrong while fetching the orders.'));
  };

  useEffect(() => {
    getOrders();

    const interval = setInterval(getOrders, (import.meta.env.VITE_ORDER_INTERVAL as number) || 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="main">
      <div className="header-container">
        <a href="https://hubble.cafe">
          <img src="/hubble-logo.png" alt="Hubble Logo" className="logo" />
        </a>
      </div>
      <div className="pickup-container">
        <h1> Ready for Pickup </h1>
      </div>
      <ul className="order-container">
        <AnimatePresence>
          {orders.map((order) => (
            <motion.li
              className="order"
              key={order.number}
              initial={{ scale: 0 }}
              animate={{
                scale: 1,
                transition: { delay: 0.5, type: 'spring', bounce: 0.3 },
              }}
              exit={{
                opacity: 0,
                transition: { delay: 0.5 },
              }}
              layout
            >
              <div className="content">
                <h1>{order.number}</h1>
              </div>
            </motion.li>
          ))}
        </AnimatePresence>
      </ul>
    </div>
  );
}

export default App;
