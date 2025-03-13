import './index.css'

export interface OrderProps {
    orderNumber: number
}

export default function Order({ orderNumber} : OrderProps) {
    return (
        <div className="order">
            <h1>{orderNumber}</h1>
        </div>
    )
}