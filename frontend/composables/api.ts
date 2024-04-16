import type { UseFetchOptions } from 'nuxt/app'
import { defu } from 'defu'

export function useAPI<T>(url: string, options: UseFetchOptions<T> = {}) {
  const config = useRuntimeConfig()

  const defaults: UseFetchOptions<T> = {
    baseURL: config.public.apiBase,
    // cache request
    key: url,
  }

  // for nice deep defaults, please use unjs/defu
  const params = defu(options, defaults)

  return useFetch(url, params)
}
