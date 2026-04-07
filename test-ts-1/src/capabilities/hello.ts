/**
 * Hello capability handler — minimal entitled capability (TypeScript).
 */

export interface HelloRequest {
  name?: string;
}

export interface HelloResponse {
  message: string;
}

export default async function handler(
  request: HelloRequest
): Promise<HelloResponse> {
  const name =
    request?.name != null && String(request.name).trim() !== ""
      ? String(request.name)
      : "world";
  return { message: `Hello, ${name}!` };
}
