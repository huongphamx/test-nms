<script lang="ts" setup>
const props = withDefaults(defineProps<{
  score: number
  size: 'lg' | 'sm'
}>(), {
  size: 'lg'
})

const fillStarNum = computed(() => Math.floor(props.score))
const isHalfStar = computed(() => props.score - fillStarNum.value > 0.5)
const starNum = computed(() => Math.floor(5 - props.score))
</script>

<template>
  <div class="flex gap-1 items-center text-amber-400">
    <UIcon v-for="n in fillStarNum" :key="n" name="i-ph-star-fill" :class="size === 'lg' ? 'w-5 h-5' : 'w-3 h-3'" />
    <UIcon v-if="isHalfStar" name="i-ph-star-half-fill" :class="size === 'lg' ? 'w-5 h-5' : 'w-3 h-3'" />
    <UIcon v-for="n in starNum" :key="n" name="i-ph-star" :class="size === 'lg' ? 'w-5 h-5' : 'w-3 h-3'" />
  </div>
</template>
