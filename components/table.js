import React from "react";
import { Table, Thead, Tbody, Tr, Th, Td, chakra, Box } from "@chakra-ui/react";
import { TriangleDownIcon, TriangleUpIcon } from "@chakra-ui/icons";
import { useTable, useSortBy } from "react-table";

export default function DataTable(props) {
  const dataset = props.data.slice(0, 4);
  console.log(dataset);
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
      name: "ÖISJE ROOM",
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
  } = useTable({ columns, data });

  return (
    <>
      <Table {...getTableProps()}>
        <Thead>
          {headerGroups.map((headerGroup) => (
            <Tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <Th {...column.getHeaderProps()}>{column.render("Header")}</Th>
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
                  <Td
                    {...cell.getCellProps()}
                    isNumeric={cell.column.isNumeric}
                  >
                    {cell.render("Cell")}
                  </Td>
                ))}
              </Tr>
            );
          })}
        </Tbody>
      </Table>
    </>
  );
}
