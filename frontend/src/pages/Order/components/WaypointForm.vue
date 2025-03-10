<script setup lang="ts">
import { ref } from 'vue'
import { z } from 'zod'
import { useField, useForm } from 'vee-validate'
import type { Order, WaypointDTO } from '@/pages/Order/data/models.ts'
import { useMutation, useQueryClient } from '@tanstack/vue-query'
import '@vuepic/vue-datepicker/dist/main.css'
import { toTypedSchema } from '@vee-validate/zod'
import { createWaypoint } from '@/pages/Order/core/requests.ts'
import { ORDER_QUERY_KEY } from '@/constants/query-keys.ts'

const props = defineProps<{ order: Order }>()
const showModal = ref(false)
const queryClient = useQueryClient()

// Zod Schema for Validation
const options = [
  { value: 'pickup', label: 'Pickup' },
  { value: 'delivery', label: 'Delivery' },
]

const waypointSchema = toTypedSchema(
  z.object({
    address: z.string().min(3, 'Customer name must be at least 3 characters long'),
    waypoint_type: z.enum(['pickup', 'delivery'], {
      errorMap: () => ({ message: 'Please select a waypoint type' }),
    }),
  }),
)

const { handleSubmit, errors, resetForm } = useForm({
  validationSchema: waypointSchema,
})

const { value: address } = useField<string>('address')
const { value: waypointType } = useField<string>('waypoint_type')

// Waypoint create mutation
const createWaypointMutation = useMutation({
  mutationFn: async (waypointData: WaypointDTO) => createWaypoint(props.order.id, waypointData),
  onSuccess: () => {
    resetForm()
    queryClient.invalidateQueries({ queryKey: [ORDER_QUERY_KEY] }) // Refresh order list
    showModal.value = false
  },
})

const handleCreate = handleSubmit((values) => {
  createWaypointMutation.mutate(values)
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
  <button class="bg-green-500 text-white px-10 py-2 rounded mb-2" @click="openModal">
    Add Waypoint
  </button>

  <div
    v-if="showModal"
    class="fixed inset-0 flex items-center justify-center bg-gray-200/90 z-9999"
  >
    <div class="bg-white p-6 border rounded shadow-lg w-96">
      <h2 class="text-lg font-semibold mb-4">Add Waypoint</h2>

      <form @submit.prevent="handleCreate">
        <!-- Customer name -->
        <div class="mb-4">
          <label for="address" class="block text-gray-700">Address</label>
          <input v-model="address" id="address" type="text" class="w-full border p-2 rounded" />
          <span class="text-red-500 text-sm">{{ errors.address }}</span>
        </div>

        <!-- WaypointType -->
        <div class="mb-4">
          <label for="waypoint_type" class="block text-gray-700">Waypoint Type</label>
          <select v-model="waypointType" id="waypoint_type" class="w-full border p-2 rounded">
            <option v-for="option in options" :key="option.value" :value="option.value">
              {{ option.label }}
            </option>
          </select>
          <span class="text-red-500 text-sm">{{ errors.waypoint_type }}</span>
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
            Create Waypoint
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
