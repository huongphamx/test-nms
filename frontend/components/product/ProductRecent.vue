<script lang="ts" setup>
const recentProducts = [
  {
    "product_base_id": "2__272274823",
    "name": "Home and Garden - Thước Nivo Laser đa năng (US Quality)",
    "price": 168000.0,
    "price_before_discount": 168000.0,
    "url_thumbnail": "https:\/\/vn-live-01.slatic.net\/p\/70bbdc89404f2ccd5a72148285064772.jpg",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "2__272274823",
      "classify_price": "best",
      "current_price": 168000.0,
      "ratio": 0.0,
      "min_price": 168000.0,
      "max_price": 210000.0,
      "avg_price": 176195.12,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__18391356780__972724310",
    "name": "Set 14 Đi Ốt Điều Chỉnh ZMM 3V-39V Tổng Cộng Với 14 Loại 20 LL34 1206",
    "price": 51444.0,
    "price_before_discount": null,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/cn-11134207-7qukw-ljrxmhkzc45045",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__18391356780__972724310",
      "classify_price": "normal",
      "current_price": 51444.0,
      "ratio": -1.0,
      "min_price": 51444.0,
      "max_price": 51444.0,
      "avg_price": 51444.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__23174615060__795612574",
    "name": "Bông Tai Tròn Đính Đá Zircon Toàn Diện Phong Cách Âu Mỹ Cho Nam",
    "price": 69875.0,
    "price_before_discount": 99821.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/sg-11134201-7qvda-livbxb8rtgeh20",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 2,
    "price_insight": {
      "product_base_id": "1__23174615060__795612574",
      "classify_price": "best",
      "current_price": 69875.0,
      "ratio": 0.0,
      "min_price": 69875.0,
      "max_price": 99821.0,
      "avg_price": 71072.84,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__3213399477__23658745",
    "name": "Set 3 món Trung Hoa cho bé trai 9-14kg",
    "price": 260000.0,
    "price_before_discount": 260000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/fc3bc909b746cf54ca329885ebf21d6a",
    "is_official_shop": false,
    "rating_count": 3,
    "rating_avg": 5.0,
    "historical_sold": 14,
    "price_insight": {
      "product_base_id": "1__3213399477__23658745",
      "classify_price": "bad",
      "current_price": 260000.0,
      "ratio": 1.0,
      "min_price": 230000.0,
      "max_price": 260000.0,
      "avg_price": 259042.55,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__400350793__14766789",
    "name": "Kính gọng Bibi thời trang - unisex cho nam và nữ",
    "price": 95000.0,
    "price_before_discount": null,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/5c071ea877e5ad995041ecd58e9d270d",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 2,
    "price_insight": {
      "product_base_id": "1__400350793__14766789",
      "classify_price": "normal",
      "current_price": 95000.0,
      "ratio": -1.0,
      "min_price": 95000.0,
      "max_price": 95000.0,
      "avg_price": 95000.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__6414620487__63049533",
    "name": "[Ảnh Thât+Video]Khuôn Silicon Đổ Socola\/Thạch\/Kẹo Lollipop\/Kẹochipchip Hình Love",
    "price": 35000.0,
    "price_before_discount": 45000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/083b99b0848f01571442bcb4b528bf36",
    "is_official_shop": false,
    "rating_count": 2,
    "rating_avg": 3.5,
    "historical_sold": 8,
    "price_insight": {
      "product_base_id": "1__6414620487__63049533",
      "classify_price": "bad",
      "current_price": 35000.0,
      "ratio": 0.75,
      "min_price": 5000.0,
      "max_price": 45000.0,
      "avg_price": 27099.01,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__8597895460__269181513",
    "name": "Hạt điều rang muối Xuân An Nuts đóng lon\/hộp tròn xếp 500g",
    "price": 199000.0,
    "price_before_discount": 199000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/ff48be24b1a561c3a849c0ee09ab80f6",
    "is_official_shop": false,
    "rating_count": 2,
    "rating_avg": 3.5,
    "historical_sold": 2,
    "price_insight": {
      "product_base_id": "1__8597895460__269181513",
      "classify_price": "bad",
      "current_price": 199000.0,
      "ratio": 1.0,
      "min_price": 143000.0,
      "max_price": 199000.0,
      "avg_price": 193146.42,
      "delta_price": null
    }
  },
  {
    "product_base_id": "2__1297515472",
    "name": "Dao thái thịt Scanpan Classic 20cm 92502000",
    "price": 740000.0,
    "price_before_discount": 892000.0,
    "url_thumbnail": "https:\/\/vn-live-01.slatic.net\/p\/29ce9a7be90cac652dfe0c9cf1342e79.jpg",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "2__1297515472",
      "classify_price": "normal",
      "current_price": 740000.0,
      "ratio": -1.0,
      "min_price": 740000.0,
      "max_price": 740000.0,
      "avg_price": 740000.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__10205197710__168215956",
    "name": "Bàn Học Cho Bé-Bàn Học Đôi nhựa cao cấp [Hàng Chính Hãng]-MIỄN PHÍ GIAO HÀNG HCM",
    "price": 1750000.0,
    "price_before_discount": 2187500.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/2786cff8d6aa3ad4df5959ce699489e7",
    "is_official_shop": false,
    "rating_count": 1,
    "rating_avg": 5.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__10205197710__168215956",
      "classify_price": "good",
      "current_price": 1750000.0,
      "ratio": 0.2,
      "min_price": 1640625.0,
      "max_price": 2187500.0,
      "avg_price": 1793818.6,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__14105654221__394843676",
    "name": "Quần Áo Khách Đặt",
    "price": 445000.0,
    "price_before_discount": null,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/1d94ecf964bff64bbea3751f76af0e78",
    "is_official_shop": false,
    "rating_count": 7,
    "rating_avg": 5.0,
    "historical_sold": 11,
    "price_insight": {
      "product_base_id": "1__14105654221__394843676",
      "classify_price": "bad",
      "current_price": 445000.0,
      "ratio": 0.5413534,
      "min_price": 85000.0,
      "max_price": 750000.0,
      "avg_price": 349594.6,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1423876046__84989368",
    "name": "Sim số đẹp Viettel",
    "price": 300000.0,
    "price_before_discount": null,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/f39455044d2051ec41a36c2eb05c51cb",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 8,
    "price_insight": {
      "product_base_id": "1__1423876046__84989368",
      "classify_price": "normal",
      "current_price": 300000.0,
      "ratio": -1.0,
      "min_price": 300000.0,
      "max_price": 300000.0,
      "avg_price": 300000.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1446550281__50089617",
    "name": "Kem đánh răng Aquafresh Family Protection Fresh & Minty 100ml của Anh mua tại Mỹ",
    "price": 105000.0,
    "price_before_discount": 105000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/e67edb7844769d1f84ec21ab5f405d88",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__1446550281__50089617",
      "classify_price": "normal",
      "current_price": 105000.0,
      "ratio": -1.0,
      "min_price": 105000.0,
      "max_price": 105000.0,
      "avg_price": 105000.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1522012205__6389384",
    "name": "Váy xòe xịn, áo chất nỉ dày, váy nhung ( size 2-6T)",
    "price": 145000.0,
    "price_before_discount": 145000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/9d1c454fd35f010dada35faf35e40dfa",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__1522012205__6389384",
      "classify_price": "bad",
      "current_price": 145000.0,
      "ratio": 1.0,
      "min_price": 87000.0,
      "max_price": 145000.0,
      "avg_price": 124726.85,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1586719870__35559884",
    "name": "Túi chườm nóng Belly well NIP",
    "price": 256000.0,
    "price_before_discount": 256000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/d15c7d601aaa86e68242f05b394c93c1",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__1586719870__35559884",
      "classify_price": "bad",
      "current_price": 256000.0,
      "ratio": 1.0,
      "min_price": 204800.0,
      "max_price": 256000.0,
      "avg_price": 252421.5,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1646474398__102524249",
    "name": "Đồng Hồ Nữ Mặt Đính Đá Sang Chảnh Hiệu Bs",
    "price": 200000.0,
    "price_before_discount": 200000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/00eda47f1ad0287a986a75d0ecbd3de1",
    "is_official_shop": false,
    "rating_count": 1,
    "rating_avg": 5.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__1646474398__102524249",
      "classify_price": "bad",
      "current_price": 200000.0,
      "ratio": 0.5555556,
      "min_price": 100000.0,
      "max_price": 280000.0,
      "avg_price": 189747.47,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__17223842595__297238203",
    "name": "Khuôn cơm Loại Đẹp khuôn ép cơm tạo hình ngộ nghĩnh cho bé ăn dặm – AD11",
    "price": 11000.0,
    "price_before_discount": 11000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/6f5e544fc5ed5775dfe91d6287ef52ff",
    "is_official_shop": false,
    "rating_count": 1,
    "rating_avg": 1.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__17223842595__297238203",
      "classify_price": "bad",
      "current_price": 11000.0,
      "ratio": 1.0,
      "min_price": 8500.0,
      "max_price": 11000.0,
      "avg_price": 8985.074,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__17523846476__297238203",
    "name": "Túi nhai ăn dặm 3 chi tiết chống hóc cao cấp cho bé – AD10",
    "price": 60000.0,
    "price_before_discount": 60000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/29e0034bb5893747b78f15d3d2f5d5c0",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__17523846476__297238203",
      "classify_price": "bad",
      "current_price": 60000.0,
      "ratio": 1.0,
      "min_price": 39000.0,
      "max_price": 60000.0,
      "avg_price": 43074.625,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__18209449468__419901534",
    "name": "[Mã SKAMLTS0811 giảm 15K đơn 0Đ] [Phụ Kiện] Máy Xay Sinh Tố Goldsun BL-GYT463G - 1.25L",
    "price": 105000.0,
    "price_before_discount": 105000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/ffb65cd6b7ae0c13108df1410a3a4038",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__18209449468__419901534",
      "classify_price": "bad",
      "current_price": 105000.0,
      "ratio": 1.0,
      "min_price": 97000.0,
      "max_price": 105000.0,
      "avg_price": 104691.664,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__10442321048__453946630",
    "name": "Đũa gỗ Lát hoa Việt Nam an toàn, sang trọng",
    "price": 20000.0,
    "price_before_discount": 20000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/b1d21d1d3d43c496d1c00d8dc6b4e9b7",
    "is_official_shop": false,
    "rating_count": 2,
    "rating_avg": 5.0,
    "historical_sold": 4,
    "price_insight": {
      "product_base_id": "1__10442321048__453946630",
      "classify_price": "normal",
      "current_price": 20000.0,
      "ratio": -1.0,
      "min_price": 20000.0,
      "max_price": 20000.0,
      "avg_price": 20000.0,
      "delta_price": null
    }
  },
  {
    "product_base_id": "1__1988120059__4950856",
    "name": "Khuyên tai giả cổ hình xinh xắn",
    "price": 18000.0,
    "price_before_discount": 18000.0,
    "url_thumbnail": "https:\/\/cf.shopee.vn\/file\/94d27f15d78325a401b75ce4c78b1797",
    "is_official_shop": false,
    "rating_count": 0,
    "rating_avg": 0.0,
    "historical_sold": 1,
    "price_insight": {
      "product_base_id": "1__1988120059__4950856",
      "classify_price": "bad",
      "current_price": 18000.0,
      "ratio": 0.6923077,
      "min_price": 9000.0,
      "max_price": 22000.0,
      "avg_price": 17831.578,
      "delta_price": null
    }
  }
]
</script>

<template>
  <div class="px-4 lg:px-0">
    <div class="text-lg font-semibold">Gợi ý hôm nay</div>
    <div
      class="mt-2 flex whitespace-nowrap overflow-auto lg:whitespace-normal lg:grid lg:grid-cols-5 gap-3 scrollbar-hide">
      <div v-for="product in recentProducts" class="w-36 lg:w-56">
        <img :src="product.url_thumbnail" alt="" class="w-36 h-36 lg:w-56 lg:h-56">
        <div class="mt-2 w-full  text-xs md:text-base line-clamp-2">{{ product.name }}</div>
        <div class="text-sm md:text-base lg:text-lg text-red-500 font-semibold">
          {{ product.price.toLocaleString('de-DE') }} ₫
        </div>
      </div>
    </div>
  </div>
</template>
