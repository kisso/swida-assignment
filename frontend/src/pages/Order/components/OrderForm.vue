<script setup lang="ts">
import { ref } from 'vue'
import { z } from 'zod'
import { useField, useForm } from 'vee-validate'
import type { OrderDTO } from '@/pages/Order/data/models.ts'
import { useMutation, useQueryClient } from '@tanstack/vue-query'
import { ORDER_QUERY_KEY } from '@/constants/query-keys.ts'
import { createOrder } from '@/pages/Order/core/requests.ts'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import { toTypedSchema } from '@vee-validate/zod'

const showModal = ref(false)
const queryClient = useQueryClient()

// Zod Schema for Validation
const orderSchema = toTypedSchema(
  z.object({
    customer_name: z.string().min(3, 'Customer name must be at least 3 characters long'),
    date: z
      .date({ invalid_type_error: 'Please select a valid date' })
      .transform((date) => date.toISOString()),
  }),
)

const { handleSubmit, errors, resetForm } = useForm({
  validationSchema: orderSchema,
})

const { value: customerName } = useField<string>('customer_name')
const { value: date } = useField<Date | null>('date')

// Order create mutation
const createOrderMutation = useMutation({
  mutationFn: async (orderData: OrderDTO) => createOrder(orderData),
  onSuccess: () => {
    resetForm()
    queryClient.invalidateQueries({ queryKey: [ORDER_QUERY_KEY] }) // Refresh order list
    showModal.value = false
  },
})

const handleCreate = handleSubmit((values) => {
  createOrderMutation.mutate(values)
})

const openModal = () => {
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  resetForm()
}
</script>

<template>
  <button class="bg-green-500 text-white px-10 py-2 rounded" @click="openModal">
    Create Order
  </button>

  <div
    v-if="showModal"
    class="fixed inset-0 flex items-center justify-center bg-gray-200/90 z-9999"
  >
    <div class="bg-white p-6 border rounded shadow-lg w-96">
      <h2 class="text-lg font-semibold mb-4">Create New Order</h2>

      <form @submit.prevent="handleCreate">
        <!-- Customer name -->
        <div class="mb-4">
          <label for="customer_name" class="block text-gray-700">Customer Name</label>
          <input
            ref="customer-name-input"
            v-model="customerName"
            id="customer_name"
            type="text"
            class="w-full border p-2 rounded"
          />
          <span class="text-red-500 text-sm">{{ errors.customer_name }}</span>
        </div>

        <!-- Date -->
        <div class="mb-4">
          <label for="date" class="block text-gray-700">Date</label>
          <VueDatePicker v-model="date" id="date" class="w-full" />
          <span class="text-red-500 text-sm">{{ errors.date }}</span>
        </div>

        <!-- Buttons -->
        <div class="flex justify-end gap-2">
          <button
            type="button"
            class="bg-gray-400 text-white px-4 py-2 rounded"
            @click="closeModal"
          >
            Cancel
          </button>
          <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded">
            Create Order
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
