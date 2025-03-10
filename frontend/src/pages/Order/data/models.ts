export interface Waypoint {
  id: string
  address: string
  waypoint_type: string
  sequence: number
  date: string
  created_at: string
}

export interface Order {
  id: string
  order_number: string
  customer_name: string
  date: string
  created_at: string
  waypoints: Waypoint[]
}

export interface OrderDTO {
  customer_name: string
  date: string
}
