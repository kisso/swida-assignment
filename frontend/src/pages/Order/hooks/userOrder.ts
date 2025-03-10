import { useQuery } from '@tanstack/vue-query'
import { listOrders } from '@/pages/Order/core/requests.ts'
import { ORDER_QUERY_KEY } from '@/constants/query-keys.ts'

export const useOrder = () => {
  return useQuery({
    queryKey: [ORDER_QUERY_KEY],
    queryFn: () => listOrders(),
  })
}
