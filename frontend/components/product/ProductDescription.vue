<script lang="ts" setup>
const props = defineProps<{
  description: string
}>()

const isExpand = ref(false)
</script>

<template>
  <div class="max-w-[900px]">
    <div class="relative">
      <div v-html="description" class="leading-8 text-gray-600" :class="isExpand ? '' : 'h-96 overflow-hidden'">
      </div>
      <!-- <div v-if="!isExpand" class="absolute bottom-0 h-32 w-full bg-gradient-to-b from-white/60 to-gray-100/40">
      </div> -->
    </div>
    <div>
      <span class="text-orange-500 underline cursor-pointer" @click="isExpand = !isExpand">
        {{ isExpand ? 'Thu gọn' : 'Xem thêm' }}
      </span>
    </div>
  </div>
</template>
