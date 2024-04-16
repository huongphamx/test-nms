<script lang="ts" setup>
import { VisXYContainer, VisLine, VisAxis, VisScatter } from '@unovis/vue'

const priceHistory = {
  "price": [
    449000,
    449000,
    669000,
    569000,
    608790,
    608790,
    526890,
    579000,
    579000,
    521100,
    526890,
    479470,
    408590,
    579000,
    669000,
    541890,
    669000,
    608790,
    669000,
    608790,
    669000,
    579000,
    526890,
    519000,
    472290,
    472290,
    519000,
    472290,
    409000,
    409000,
    579000,
    499000,
    579000,
    521100,
    579000,
    449000,
    579000,
    579000,
    526890,
    526890
  ],
  "price_ts": [
    1690701772000,
    1691016312000,
    1691739068000,
    1692906553000,
    1694077694000,
    1694683479000,
    1695301822000,
    1696491003000,
    1696705615000,
    1696808827000,
    1697268491000,
    1697365322000,
    1697451652000,
    1698415404000,
    1699499902000,
    1699606303000,
    1699702544000,
    1700792606000,
    1700984211000,
    1701320363000,
    1702201102000,
    1702449529000,
    1702556199000,
    1703217855000,
    1704363612576,
    1704483574000,
    1704682208000,
    1705198052000,
    1706386329000,
    1706958955000,
    1707263809000,
    1707805310000,
    1708005598000,
    1709197629000,
    1709385726000,
    1710562709000,
    1711676230879,
    1711915231714,
    1712914245691,
    1713230415514
  ]
}

const data = priceHistory.price.map((p, i) => {
  return { x: priceHistory.price_ts[i], y: p }
})
const x = (d: any) => d.x
const y = (d: any) => d.y
</script>

<template>
  <div class="mt-4 flex">
    <div class="flex-1 border border-orange-500 rounded-lg px-4 py-4">
      <div class="mb-3">
        <span class="text-orange-500 text-lg font-medium">Biến động giá
        </span>
      </div>
      <VisXYContainer :data="data" class="w-full">
        <VisLine :x="x" :y="y" />
        <VisScatter :x="x" :y="y" />
        <VisAxis type="x" :gridLine="false" />
        <VisAxis type="y" :gridLine="false" />
      </VisXYContainer>
    </div>
    <div class="ml-auto w-full max-w-sm">

    </div>
  </div>
</template>
