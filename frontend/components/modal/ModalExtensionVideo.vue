<script lang="ts" setup>
const isOpen = ref(false)
</script>

<template>
  <div>
    <span class="cursor-pointer text-xs" @click="isOpen = true">Video hướng dẫn</span>
    <UModal :model-value="isOpen" :ui="{ width: 'sm:max-w-4xl' }">
      <div class="p-2">
        <div class="text-end">
          <UButton icon="i-ph-x" :padded="false" color="gray" variant="ghost" @click="isOpen = false" />
        </div>
        <iframe width="853" height="480" src="https://www.youtube.com/embed/GICCaUZ-Zcw?si=uKCZPx7QOfzYmKuj"
          title="YouTube video player" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
    </UModal>
  </div>
</template>
