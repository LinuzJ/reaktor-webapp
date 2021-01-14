import { Table, Thead, Tbody, Tr, Th, Td, chakra } from "@chakra-ui/react";
import { TriangleDownIcon, TriangleUpIcon } from "@chakra-ui/icons";
import { useTable, useSortBy } from "react-table";

export default function DataTable(props) {
  console.log(props.data);
  const dataset = props.data;

  const data = [
    {
      color: ["blue"],
      id: "5af6de2f306eabb2b67cba6",
      manufacturer: "abiplos",
      name: "LEASOPREV ROOM",
      price: 25,
      type: "beanies",
    },
    {
      color: ["yellow"],
      id: "441a9e1b86b62a7a92197b",
      manufacturer: "abiplos",
      name: "UPJE SWEET",
      price: 42,
      type: "beanies",
    },
    {
      color: ["grey"],
      id: "9766d4d22e96bd93a1ddab4",
      manufacturer: "hennex",
      name: "HEMILKOL BRIGHT",
      price: 283,
      type: "beanies",
    },
    {
      color: ["red"],
      id: "e2de9c75d1ee834bf4bcd",
      manufacturer: "niksleh",
      name: "\u00d6ISJE ROOM",
      price: 40,
      type: "beanies",
    },
  ];
  const columns = [
    {
      Header: "Name",
      accessor: "name",
    },
    {
      Header: "Color",
      accessor: "color",
    },
    {
      Header: "Manufacturer",
      accessor: "manufacturer",
    },
    {
      Header: "Price",
      accessor: "price",
    },
    {
      Header: "Type",
      accessor: "type",
    },
    {
      Header: "ID",
      accessor: "id",
    },
  ];

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable({ columns, data }, useSortBy);

  return (
    <Table {...getTableProps()}>
      <Thead>
        {headerGroups.map((headerGroup) => (
          <Tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map((column) => (
              <Th
                {...column.getHeaderProps(column.getSortByToggleProps())}
                isNumeric={column.isNumeric}
              >
                {column.render("Header")}
                <chakra.span pl="4">
                  {column.isSorted ? (
                    column.isSortedDesc ? (
                      <TriangleDownIcon aria-label="sorted descending" />
                    ) : (
                      <TriangleUpIcon aria-label="sorted ascending" />
                    )
                  ) : null}
                </chakra.span>
              </Th>
            ))}
          </Tr>
        ))}
      </Thead>
      <Tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <Tr {...row.getRowProps()}>
              {row.cells.map((cell) => (
                <Td {...cell.getCellProps()} isNumeric={cell.column.isNumeric}>
                  {cell.render("Cell")}
                </Td>
              ))}
            </Tr>
          );
        })}
      </Tbody>
    </Table>
  );
}
