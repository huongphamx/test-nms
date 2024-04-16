<script lang="ts" setup>
interface RelatedProduct {
  historical_sold: number;
  is_official_shop: boolean;
  name: string;
  price: number;
  price_insight: PriceInsight;
  product_base_id: string;
  rating_avg: number;
  rating_count: number;
  url_thumbnail: string;
}

interface PriceInsight {
  avg_price: number;
  classify_price: string;
  current_price: number;
  delta_price: number | null;
  max_price: number;
  min_price: number;
  product_base_id: string;
  ratio: number;
}

const relatedProducts: RelatedProduct[] = [
  {
    "product_base_id": "1__7370776212__299794970",
    "url_thumbnail": "https://cf.shopee.vn/file/f55f5a69b9e54e4152617aff992771f8",
    "name": "Duc98 FHDT Bộ hub chia 4 cổng USB 3.0 - ORICO MH4PU - chính hãng bảo hành lỗi 1 đổi 1 !!! 50 MHB12",
    "price": 259000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__7370776212__299794970",
      "classify_price": "normal",
      "current_price": 259000,
      "ratio": -1,
      "min_price": 259000,
      "max_price": 259000,
      "avg_price": 259000,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__13848730793__545226246",
    "url_thumbnail": "https://cf.shopee.vn/file/daab7ed13eadad643d398a5e0f186aa8",
    "name": "Hub chia USB7 cổng có công tắc giá rẻ.",
    "price": 47900,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__13848730793__545226246",
      "classify_price": "normal",
      "current_price": 47900,
      "ratio": -1,
      "min_price": 47900,
      "max_price": 47900,
      "avg_price": 47900,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__13951953339__253482297",
    "url_thumbnail": "https://cf.shopee.vn/file/712c88935312a04a026d93631ec7988e",
    "name": "Bộ Chia USB 3.0 10 Cổng ACASIS HS710 Nguồn Rời 12V 4A - HUB USB 10 Port chính hãng - Hapuhouse",
    "price": 2200000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__13951953339__253482297",
      "classify_price": "bad",
      "current_price": 2200000,
      "ratio": 1,
      "min_price": 1100000,
      "max_price": 2200000,
      "avg_price": 1252777.8,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__9943772020__291306617",
    "url_thumbnail": "https://cf.shopee.vn/file/477e60b632bd06496903e57cb5974b24",
    "name": "[Freeship toàn quốc từ 50k] Hub 8 Fan High low",
    "price": 75000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__9943772020__291306617",
      "classify_price": "normal",
      "current_price": 75000,
      "ratio": -1,
      "min_price": 75000,
      "max_price": 75000,
      "avg_price": 75000,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__13548704707__545226246",
    "url_thumbnail": "https://cf.shopee.vn/file/4f36a490a26bd874167d15f1d66e96a5",
    "name": "Hub chia USB 4 cổng có công tắc",
    "price": 36900,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__13548704707__545226246",
      "classify_price": "normal",
      "current_price": 36900,
      "ratio": -1,
      "min_price": 36900,
      "max_price": 36900,
      "avg_price": 36900,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__10021466032__348231963",
    "url_thumbnail": "https://cf.shopee.vn/file/5ace1ad5db9dd8c39e133d49b6ba22be",
    "name": "Usb Flash Drive 32 Gb Dạng Xoay Mới",
    "price": 106000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__10021466032__348231963",
      "classify_price": "bad",
      "current_price": 106000,
      "ratio": 1,
      "min_price": 53000,
      "max_price": 106000,
      "avg_price": 103393.445,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__6352771017__68044915",
    "url_thumbnail": "https://cf.shopee.vn/file/af1d9bc9dbad90d69396e9ee32e139cb",
    "name": "[ Giá Quá Sốc ] Hub USB 4 cổng hình ổ điện có công tắc",
    "price": 91000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__6352771017__68044915",
      "classify_price": "bad",
      "current_price": 91000,
      "ratio": 1,
      "min_price": 58500,
      "max_price": 91000,
      "avg_price": 90121.625,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__11418992387__133533704",
    "url_thumbnail": "https://cf.shopee.vn/file/9acf9137ccd46377715e4237c8e4c81e",
    "name": "cổng Chuyển HyperDrive HDMI 4K60HZ 4IN1 USBC HUB",
    "price": 1450000,
    "is_official_shop": false,
    "rating_count": 1,
    "rating_avg": 5,
    "historical_sold": 2,
    "price_insight": {
      "product_base_id": "1__11418992387__133533704",
      "classify_price": "no_comment",
      "current_price": 1450000,
      "ratio": 0.45945945,
      "min_price": 1280000,
      "max_price": 1650000,
      "avg_price": 1441031.9,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__12604955082__408599709",
    "url_thumbnail": "https://cf.shopee.vn/file/00820fc89a54a5cbdfad3c1bcb6014e0",
    "name": "coco.a Thẻ nhớ 128GB CF Lexar Professional 1066X 160M/s, Thẻ tray",
    "price": 7740000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__12604955082__408599709",
      "classify_price": "normal",
      "current_price": 7740000,
      "ratio": -1,
      "min_price": 7740000,
      "max_price": 7740000,
      "avg_price": 7740000,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__9526523070__395959636",
    "url_thumbnail": "https://cf.shopee.vn/file/580fc08876d6fc5d127bc1dcf6f75bf9",
    "name": "Bộ Chuyển Đổi Usb Sang Rj45 Ethernet Lan + 3 Cổng Usb",
    "price": 418000,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__9526523070__395959636",
      "classify_price": "bad",
      "current_price": 418000,
      "ratio": 1,
      "min_price": 331800,
      "max_price": 418000,
      "avg_price": 412929.4,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__5888303262__162014995",
    "url_thumbnail": "https://cf.shopee.vn/file/8af3d16b6cc32939e9ac0b2685934d37",
    "name": "Silicone Keyboard Cover Skin Protector for Lenovo Ideapad 320-14 320s-15 120s-14 330C-14 S130-14 340C-14 330S-14 V320-14 V330-14",
    "price": 29498,
    "is_official_shop": false,
    "rating_count": 2,
    "rating_avg": 5,
    "historical_sold": 5,
    "price_insight": {
      "product_base_id": "1__5888303262__162014995",
      "classify_price": "best",
      "current_price": 29498,
      "ratio": 0,
      "min_price": 29498,
      "max_price": 36872,
      "avg_price": 30071.533,
      "delta_price": -7374
    }
  },
  {
    "product_base_id": "1__6264057718__218619340",
    "url_thumbnail": "https://cf.shopee.vn/file/8536ef8672942809d62547fd6d7042d4",
    "name": "Hub Chia Usb USB gồm 4 Cổng (4 Port) Hình Ổ Điện",
    "price": 16900,
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0,
    "historical_sold": 0,
    "price_insight": {
      "product_base_id": "1__6264057718__218619340",
      "classify_price": "normal",
      "current_price": 16900,
      "ratio": -1,
      "min_price": 16900,
      "max_price": 16900,
      "avg_price": 16900,
      "delta_price": null
    }
  }
]

</script>

<template>
  <div>
    <div class="text-lg font-semibold">Sản phẩm liên quan</div>
    <div class="flex gap-2 flex-wrap">
      <div v-for="product in relatedProducts" :key="product.product_base_id" class="w-56 ">
        <img :src="product.url_thumbnail" alt="" class="w-56 h-56">
        <div>
          <div class="text-lg font-semibold">{{ product.name }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
