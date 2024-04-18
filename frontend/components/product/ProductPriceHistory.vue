<script lang="ts" setup>
import { VisXYContainer, VisLine, VisAxis, VisScatter, VisTooltip, VisCrosshair } from '@unovis/vue'
import { Position, Scatter, Line } from '@unovis/ts'
import { format, differenceInMonths } from 'date-fns'
import type { ProductBase } from '@/types'

interface PriceHistory {
  price: number[],
  price_ts: number[]
}
const props = defineProps<{
  productData: ProductBase
}>()

const { data: priceHistory } = await useAPI<PriceHistory>(`/v1/products/${props.productData.product_base_id}/price-history`)

const data = priceHistory.value!.price.map((p, i) => {
  return { x: priceHistory.value!.price_ts[i], y: p }
})
const x = (d: any, i: number) => i
const y = (d: any) => d.y

function tickXFormat(tick: number) {
  return format(new Date(data[tick].x), 'dd-MM-yyyy')
}
function tickYFormat(d: number) {
  return `${d / 1000}k`
}
const triggers = {
  // [Line.selectors.line]: (d: any) => `<div>Ngày ${d.x}</div> <div>${d.y} ₫</div>`,
  [Scatter.selectors.point]: (d: any) => `<div class="rounded text-sm font-medium">
    <div>Ngày ${format(new Date(d.x), 'dd-MM-yyyy')}</div> <div class="text-center">${d.y.toLocaleString('de-DE')} ₫</div>
  </div>`
}
</script>

<template>
  <div v-if="priceHistory" class="mt-4 flex flex-col lg:flex-row">
    <div class="flex-1 border border-orange-500 rounded-lg px-4 py-4">
      <div class="flex justify-between">
        <span class="text-orange-500 text-lg font-medium">Biến động giá
        </span>
        <div>
          <div>
            <span class="text-sm">Giá hiện tại: </span>
            <span class="text-lg font-medium">{{ productData.price.toLocaleString('de-DE') }} ₫</span>
          </div>
          <div class="mt-1 text-sm">
            <span class="">Từ </span>
            <span class="bg-gray-200 px-2 py-1">{{ format(priceHistory.price_ts[0], 'dd-MM-yyyy') }}</span>
            <span class="ml-4 ">Đến </span>
            <span class="bg-gray-200 px-2 py-1">{{ format(priceHistory.price_ts[priceHistory.price_ts.length - 1],
    'dd-MM-yyyy') }}</span>
          </div>
        </div>
      </div>
      <div class="mb-3 text-sm">
        <span>Cao nhất: </span>
        <span class="text-red-500">{{ Math.max(...priceHistory.price).toLocaleString('de-DE') }} ₫</span>
        <span class="ml-4">Thấp nhất: </span>
        <span class="text-green-500">{{ Math.min(...priceHistory.price).toLocaleString('de-DE') }} ₫</span>
      </div>
      <VisXYContainer :data="data" class="w-full">
        <VisLine color="#9ca3af" :x="x" :y="y" />
        <VisScatter color="#9ca3af" :x="x" :y="y" />
        <VisAxis type="x" :x="x" :tickFormat="tickXFormat" :gridLine="false" />
        <VisAxis type="y" :tickFormat="tickYFormat" :gridLine="false" />
        <VisTooltip :triggers="triggers" :horizontalPlacement="Position.Center" />
      </VisXYContainer>
    </div>
    <div class="ml-4 w-full max-w-sm space-y-6">
      <div class=" p-4 border border-orange-500 rounded">
        <ul class="list-disc list-inside">
          <li>Tổng thời gian biến động giá: <span>{{ differenceInMonths(new
    Date(priceHistory.price_ts[priceHistory.price_ts.length - 1]), new
    Date(priceHistory.price_ts[0])) }}</span> tháng</li>
          <li>Số lần thay đổi giá: <span>{{ (new Set(priceHistory.price)).size }}</span> lần</li>
        </ul>
      </div>
      <div class="p-4 pr-8 border border-orange-500 rounded bg-amber-50">
        <p class="mb-2 text-2xl font-semibold">Gợi ý dành cho bạn</p>
        <p class="mb-4">
          Tiện ích Mua Thông Minh giúp bạn xem tất cả các mức giá trong quá khứ của mọi sản phẩm (Shopee, Tiki, Lazada,
          Sendo). <strong>Tiết kiệm gấp đôi</strong>
        </p>
        <div class="mb-4 flex justify-center items-center gap-4">
          <ModalExtensionVideo />
          <a href="https://www.beecost.com/install?pub=lsg_widget" target="_blank"><span
              class="text-white p-2 bg-orange-500 rounded cursor-pointer">Xem thêm chi tiết</span></a>
        </div>
      </div>
    </div>
  </div>
</template>
