export interface Compare {
  data: CompareData;
  message: null;
  message_type: null;
  status: string;
}

export interface CompareData {
  products: CompareDataProduct[];
}

export interface CompareDataProduct {
  historical_sold?: number;
  is_official_shop?: boolean;
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