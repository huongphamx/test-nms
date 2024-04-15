export interface ProductDetailResponse {
  data: Data;
  status: string;
}

export interface Data {
  product_base: ProductBase;
}

export interface ProductBase {
  attributes: Attribute[];
  brand: Brand;
  categories: Category[];
  category_base_id: string;
  comment_count: number;
  currency: string;
  description: string;
  historical_sold: number;
  is_adult: boolean;
  is_official_shop: boolean;
  like_count: number;
  name: string;
  platform_id: number;
  price: number;
  price_before_discount: number;
  price_insight: PriceInsight;
  product_base_id: string;
  product_id_platform: number;
  rating_avg: number;
  rating_count: number;
  rating_detail: number[];
  shop_base_id: string;
  shop_id_platform: string;
  shop_location: Brand;
  sold: number;
  status: number;
  url_images: string[];
  url_thumbnail: string;
  variations: Variation[];
}

export interface Attribute {
  id: string;
  name: string;
  value: string;
}

export interface Brand {
  name: string;
  parent_id: null;
  relative_path: string;
  slug: string;
  stemming_name: string;
  url_thumbnail: null | string;
}

export interface Category {
  cat_level: number;
  category_base_id: string;
  name: string;
  parent_category_id: null | string;
  relative_path: null;
  slug: string;
  url_thumbnail: string;
}

export interface PriceInsight {
  avg_price: number;
  classify_price: string;
  current_price: number;
  delta_price: number;
  max_price: number;
  min_price: number;
  product_base_id: string;
  ratio: number;
}

export interface Variation {
  name: string;
  options: string[];
}
