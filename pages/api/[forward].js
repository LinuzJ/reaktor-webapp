export default async function handler(req, res) {
  const category = req.query.forward;
  const offset = req.query.offset;
  const limit = req.query.limit;

  const data = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_API}${category}?o=${offset}&l=${limit}`
  ).then((response) => response.json());
  if (data) {
    res.status(200).json(data);
  } else {
    res.status(404);
  }
}
