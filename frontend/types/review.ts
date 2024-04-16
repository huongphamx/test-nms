export interface ReviewResponse {
  data: ReviewData;
  status: string;
}

export interface ReviewData {
  reviews: Review[];
}

export interface Review {
  comments: Comment[] | null;
  content: string;
  created_at_platform: number;
  images: string[] | null;
  platform_id: number;
  product_base_id: string;
  rating: number;
  review_base_id: string;
  title: null;
  user_url_image: string;
  user_username: string;
}

export interface Comment {
  comment: string;
  created_at: number;
}
