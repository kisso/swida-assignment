<script setup lang="ts">
import type { Order } from '@/pages/Order/data/models.ts'
import { ORDER_QUERY_KEY } from '@/constants/query-keys.ts'
import { useMutation, useQueryClient } from '@tanstack/vue-query'
import { deleteOrder } from '@/pages/Order/core/requests.ts'

const showDeletionModal = defineModel<boolean>('showDeletionModal')
const props = defineProps<{ selectedOrder: Order | null }>()
const queryClient = useQueryClient()

// Order delete mutation
const deleteMutation = useMutation({
  mutationFn: deleteOrder,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: [ORDER_QUERY_KEY] }) // Refresh order list
    showDeletionModal.value = false
  },
})

const handleDelete = () => {
  if (props.selectedOrder?.id) {
    deleteMutation.mutate(props.selectedOrder.id)
  }
}

const closeModal = () => {
  showDeletionModal.value = false
}
</script>

<template>
  <div
    v-if="showDeletionModal"
    class="fixed inset-0 flex items-center justify-center bg-gray-200/90 z-9999"
  >
    <div class="bg-white p-6 border rounded shadow-lg w-96">
      <h2 class="text-lg font-semibold mb-4">
        Do you really want to delete order nr.: {{ props.selectedOrder?.order_number }}?
      </h2>

      <form @submit.prevent="handleDelete">
        <div class="flex justify-end gap-2">
          <button
            type="button"
            class="bg-gray-400 text-white px-4 py-2 rounded"
            @click="closeModal"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="bg-red-500 text-white px-4 py-2 rounded"
            :disabled="!props.selectedOrder"
          >
            Delete
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
