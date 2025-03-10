<script setup lang="ts">
import type { Order } from '@/pages/Order/data/models.ts'

const props = defineProps<{ order: Order }>()
</script>

<template>
  <button class="bg-green-500 text-white px-4 py-1 rounded mb-2">Add Waypoint</button>
  <table class="w-full bg-gray-200">
    <thead>
      <tr class="border border-black">
        <th class="px-4 py-2">Sequence</th>
        <th class="px-4 py-2">Type</th>
        <th class="px-4 py-2">Address</th>
      </tr>
    </thead>
    <tbody>
      <template v-for="waypoint in props.order.waypoints" :key="waypoint.id">
        <tr class="border border-black">
          <td class="px-4 py-2 text-center">{{ waypoint.sequence }}</td>
          <td class="px-4 py-2 text-center">{{ waypoint.waypoint_type }}</td>
          <td class="px-4 py-2 text-center">{{ waypoint.address }}</td>
        </tr>
      </template>
    </tbody>
  </table>
</template>
