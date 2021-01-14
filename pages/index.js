import DataTable from "../components/table";

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:5000/");
  const data = await res.json();

  return {
    props: {
      data: data,
    },
  };
}

export default function Home(props) {
  return (
    <div>
      <DataTable data={props.data.beanies} />

      {props.data.beanies.map((row) => {
        return <p>{JSON.stringify(row)}</p>;
      })}
    </div>
  );
}
