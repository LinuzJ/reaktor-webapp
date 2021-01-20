import DataTable from "../components/table";
import Layout from "../components/layout";
export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:5000/");
  const data = await res.json();
  for (let key in data) {
    data[key] = Object.values(data[key]).slice(0, 200);
  }
  return {
    props: {
      data: data,
    },
  };
}

export default function Facemasks(props) {
  return (
    <Layout>
      <DataTable tableData={props.data.facemasks} />
    </Layout>
  );
}
