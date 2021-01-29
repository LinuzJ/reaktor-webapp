import React, { useMemo, useState, useEffect } from "react";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  chakra,
  Button,
  Box,
  Select,
  Input,
} from "@chakra-ui/react";

import { useTable } from "react-table";

export default function DataTable(props) {
  const [offset, setOffset] = useState(0);
  const [limit, setLimit] = useState(50);
  const [data, setData] = useState([]);
  const [totalItems, setTotal] = useState(0);

  useEffect(() => {
    async function fetchData() {
      const recieved = await fetch(
        `http://127.0.0.1:5000/${props.category}?o=${offset}&l=${limit}`
      ).then((response) => response.json());
      setData(recieved.data);
      setTotal(recieved.totalItems);
    }
    fetchData();
  }, [offset, limit]);

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
    {
      Header: "Availability",
      accessor: "availability",
    },
  ];
  console.log(data);
  // const {
  //   getTableProps,
  //   getTableBodyProps,
  //   headerGroups,
  //   rows,
  //   prepareRow,
  // } = useTable({ columns, data });

  return (
    <Box>
      <Table>
        <Thead></Thead>
      </Table>

      {/* <Table {...getTableProps()}>
        <Thead>
          {headerGroups.map((headerGroup) => (
            <Tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <Th
                  {...column.getHeaderProps(column)}
                  isNumeric={column.isNumeric}
                >
                  {column.render("Header")}
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
      </Table> */}
      <Box
        display="flex"
        flex-direction="row"
        justifyContent="space-between"
        p="20px"
        alignItems="center"
      >
        <Button
          onClick={() => {
            if (offset - limit < 0) {
              setOffset(offset - limit);
            } else {
              setOffset(0);
            }
          }}
        >
          {"<"}
        </Button>
        <Button
          onClick={() => {
            if (offset + limit > totalItems) {
              setOffset(totalItems - limit);
            } else {
              setOffset(offset + limit);
            }
          }}
        >
          {">"}
        </Button>
      </Box>
      <Box>
        Displaying{" "}
        <strong>
          {limit} out of {totalItems}
        </strong>{" "}
      </Box>
      <Input
        width="20%"
        type="number"
        placeholder=" Go to page: "
        onChange={(e) => {
          const page = e.target.value ? Number(e.target.value) - 1 : 0;
          gotoPage(page);
        }}
      />
      <Select
        width="20%"
        value={limit}
        onChange={(e) => {
          setLimit(Number(e.target.value));
        }}
      >
        {[10, 20, 30, 40, 50].map((pageSize) => (
          <option key={pageSize} value={pageSize}>
            Show {pageSize}
          </option>
        ))}
      </Select>
    </Box>
  );
}
