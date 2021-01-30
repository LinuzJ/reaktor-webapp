import React, { useState, useEffect } from "react";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Button,
  Box,
  Select,
} from "@chakra-ui/react";

export default function DataTable(props) {
  const [offset, setOffset] = useState(0);
  const [limit, setLimit] = useState(50);
  const [data, setData] = useState([]);
  const [totalItems, setTotal] = useState(0);
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const recieved = await fetch(
        `http://127.0.0.1:5000/${props.category}?o=${offset}&l=${limit}`
      ).then((response) => response.json());
      setData(recieved.data);
      setTotal(recieved.totalItems);
      setColumns(Object.keys(recieved.columns));
    }
    fetchData();
  }, [offset, limit]);

  return (
    <>
      <Table>
        <Thead>
          <Tr>
            {columns.map((key) => {
              return <Th>{key}</Th>;
            })}
          </Tr>
        </Thead>
        <Tbody>
          {data.map((product) => {
            return (
              <Tr>
                {Object.keys(product).map((key) => {
                  return <Td>{product[key]}</Td>;
                })}
              </Tr>
            );
          })}
        </Tbody>
      </Table>

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
          {offset} - {offset + limit} out of a total of {totalItems}
        </strong>{" "}
      </Box>

      <Select
        width="20%"
        value={limit}
        onChange={(e) => {
          setLimit(Number(e.target.value));
        }}
      >
        {[10, 20, 30, 40, 50, 100, 200].map((pageSize) => (
          <option key={pageSize} value={pageSize}>
            Show {pageSize}
          </option>
        ))}
      </Select>
    </>
  );
}
