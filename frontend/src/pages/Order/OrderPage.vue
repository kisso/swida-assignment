<script setup lang="ts">
import { ref } from 'vue'
import OrderForm from '@/pages/Order/components/OrderForm.vue'
import OrderDeleteModal from '@/pages/Order/components/OrderDeleteModal.vue'
import type { Order } from '@/pages/Order/data/models.ts'
import { useOrder } from '@/pages/Order/hooks/userOrder.ts'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import { formattedDate } from '@/utils.ts'

// Filtering
const searchInput = ref('')
const dateInput = ref('')

const searchQuery = ref('')
const dateQuery = ref('')

const handleDateChange = (date: Date | null) => {
  if (date) {
    // Convert to YYYY-MM-DD format
    dateInput.value = date.toISOString().split('T')[0]
  } else {
    dateInput.value = ''
  }
}

const applyFilter = () => {
  searchQuery.value = searchInput.value
  dateQuery.value = dateInput.value
  console.log(searchQuery.value)
  refetchData()
}

const resetFilter = () => {
  searchInput.value = ''
  dateInput.value = ''
  searchQuery.value = ''
  dateQuery.value = ''
  refetchData()
}

// API
const {
  data: orderData,
  isLoading: orderLoading,
  error: orderError,
  refetch: refetchData,
} = useOrder(searchQuery, dateQuery)

// Modals
const showDeletionModal = ref(false)
const selectedOrder = ref<Order | null>(null)
const openDeleteModal = (order: Order) => {
  showDeletionModal.value = true
  selectedOrder.value = order
}
</script>

<template>
  <div class="flex flex-col gap-3 items-start">
    <h2 class="text-3xl font-bold mb-2">Swida Orders</h2>
    <OrderForm />
    <OrderDeleteModal
      v-model:showDeletionModal="showDeletionModal"
      :selected-order="selectedOrder"
    />

    <!-- Filter Section -->
    <div class="flex flex-row items-center gap-4">
      <input
        type="text"
        v-model="searchInput"
        placeholder="Search by order number or customer name"
        class="border p-2 rounded w-sm"
      />
      <VueDatePicker
        class="max-w-80"
        v-model="dateInput"
        :enable-time-picker="false"
        @update:model-value="handleDateChange"
      />
      <button class="bg-blue-500 text-white px-10 py-2 rounded" @click="applyFilter">Filter</button>
      <button
        v-if="searchQuery || dateQuery"
        class="bg-red-500 text-white px-10 py-2 rounded"
        @click="resetFilter"
      >
        Reset
      </button>
    </div>

    <!-- Table Section -->
    <div class="w-full">
      <p v-if="orderError" class="text-red-500">{{ orderError }}</p>

      <p v-if="orderLoading">Loading orders...</p>
      <div v-if="orderData && orderData.length > 0">
        <!-- Table -->
        <table class="w-full border border-black">
          <thead>
            <tr class="border border-black bg-gray-200">
              <th class="px-4 py-2">Order Nr.</th>
              <th class="px-4 py-2">Date</th>
              <th class="px-4 py-2">Customer</th>
              <th class="px-4 py-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="order in orderData" :key="order.id">
              <tr class="border border-black">
                <td class="px-4 py-2 text-center">{{ order.order_number }}</td>
                <td class="px-4 py-2 text-center">
                  {{ formattedDate(order.date) }}
                </td>
                <td class="px-4 py-2 text-center">{{ order.customer_name }}</td>
                <td class="flex flex-row justify-center gap-2 px-4 py-2 text-center">
                  <button
                    class="bg-red-500 text-white px-4 py-1 rounded"
                    @click="openDeleteModal(order)"
                  >
                    D
                  </button>
                </td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>
      <p v-else-if="!orderLoading" class="text-gray-500">No orders available.</p>
    </div>
  </div>
</template>
