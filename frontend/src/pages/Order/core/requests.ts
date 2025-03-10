import api from '@/api/common.ts'
import type { PaginationResponse, SingleResponse } from '@/api/responses.ts'
import type { Order, OrderDTO } from '@/pages/Order/data/models.ts'

export const listOrders = async (): Promise<Order[]> => {
  const response = await api.get<PaginationResponse<Order>>('/orders', {
    params: {
      // customer_name: search,
      // created_at: date,
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
