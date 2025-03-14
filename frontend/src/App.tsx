import './index.css';
import { useEffect, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';

interface Order {
  number: number;
  startTime: string;
  timeoutSeconds: number;
}

function App() {
  const [orders, setOrders] = useState<Order[]>([]);

  useEffect(() => {
    const interval = setInterval(
      () => {
        fetch('/api/getOrders')
          .then((response) => response.json())
          .then((response: Order[]) => {
            setOrders(
              response.filter((order) => {
                const timeTillOrderEnd = new Date(order.startTime).getTime() + order.timeoutSeconds * 1000 - Date.now();
                return timeTillOrderEnd > 0;
              }),
            );
          })
          .catch((e) => console.error(e));
      },
      (import.meta.env.VITE_ORDER_INTERVAL as number) || 5000,
    );

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="main">
      <div className="header-container">
        <img src="/hubble-logo.png" alt="Hubble Logo" className={'logo'} />
        <h1> Ready for pickup </h1>
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
                transition: { delay: 0.5, type: 'spring' },
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
