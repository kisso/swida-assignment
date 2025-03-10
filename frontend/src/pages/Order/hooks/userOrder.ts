import { useQuery } from '@tanstack/vue-query'
import { listOrders } from '@/pages/Order/core/requests.ts'
import { ORDER_QUERY_KEY } from '@/constants/query-keys.ts'
import { computed, type Ref } from 'vue'

export const useOrder = (search: Ref<string | null>, date: Ref<string | null>) => {
  return useQuery({
    queryKey: computed(() => [ORDER_QUERY_KEY, search, date]),
    queryFn: () => listOrders(search?.value, date?.value),
  })
}
