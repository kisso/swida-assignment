import api from '@/api/common.ts'
import type { PaginationResponse, SingleResponse } from '@/api/responses.ts'
import type { Order, OrderDTO, Waypoint, WaypointDTO } from '@/pages/Order/data/models.ts'

export const listOrders = async (search: string | null, date: string | null): Promise<Order[]> => {
  const response = await api.get<PaginationResponse<Order>>('/orders', {
    params: {
      text_query: search || undefined,
      date: date || undefined,
    },
  })

  return response.data.items
}

export const createOrder = async (body: OrderDTO) => {
  const response = await api.post<SingleResponse<Order>>('/orders', body)
  return response.data.response
}

export const deleteOrder = async (orderId: string) => {
  await api.delete(`/orders/${orderId}`)
}

export const createWaypoint = async (orderId: string, body: WaypointDTO) => {
  const response = await api.post<SingleResponse<Waypoint>>(`/orders/${orderId}/waypoints`, body)
  return response.data.response
}
