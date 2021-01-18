import DataTable from "../components/table";

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:5000/");
  const data = await res.json();
  for (let key in data) {
    data[key] = Object.values(data[key]).slice(0, 20);
  }
  console.log(data);
  return {
    props: {
      data: data,
    },
  };
}

export default function Home(props) {
  return (
    <div>
      <DataTable
        beanies={props.data.beanies}
        facemasks={props.data.facemasks}
        gloves={props.data.gloves}
      />
    </div>
  );
}
