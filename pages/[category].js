import DataTable from "../components/table";
import Layout from "../components/layout";
import { useRouter } from "next/router";

export default function Category(props) {
  const router = useRouter();
  const { category } = router.query;
  return (
    <Layout category={category}>
      <DataTable category={category} />
    </Layout>
  );
}
