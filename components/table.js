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
  Badge,
} from "@chakra-ui/react";

export default function DataTable(props) {
  const [offset, setOffset] = useState(0);
  const [limit, setLimit] = useState(10);
  const [data, setData] = useState([]);
  const [totalItems, setTotal] = useState(0);
  const [columns, setColumns] = useState([]);
  const [error, setError] = useState("");

  useEffect(async () => {
    if (props.category !== undefined) {
      const recieved = await fetch(
        `/api/${props.category}?offset=${offset}&limit=${limit}`
      ).then((response) => {
        if (response.status === 200) {
          return response.json();
        }
      });
      if (recieved) {
        setData(recieved.data);
        setTotal(recieved.totalItems);
        setColumns(Object.keys(recieved.columns));
      } else {
        setError("Loading data failed...");
      }
    }
  }, [offset, limit, props.category]);

  return (
    <Box margin="1% 10% 1% 10%">
      {error ? <Badge colorScheme="red">{error}</Badge> : ""}
      <Table>
        <Thead>
          <Tr>
            {columns.map((key) => {
              if (key === "type") {
                {
                }
              } else {
                return <Th>{key}</Th>;
              }
            })}
          </Tr>
        </Thead>
        <Tbody>
          {data.map((product) => {
            return (
              <Tr>
                {Object.keys(product).map((key) => {
                  if (key === "type") {
                    {
                    }
                  } else if (key === "price") {
                    return <Td>{product[key]}€</Td>;
                  } else if (Array.isArray(product[key])) {
                    return <Td>{product[key].join(", ")}</Td>;
                  } else {
                    return <Td>{product[key]}</Td>;
                  }
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
        alignItems="center"
      >
        <Box
          display="flex"
          flex-direction="row"
          justifyContent="space-between"
          p="20px"
          m="20px"
          alignItems="center"
        >
          <Button
            onClick={() => {
              if (offset - limit <= 0) {
                setOffset(0);
              } else {
                setOffset(offset - limit);
              }
            }}
          >
            {"<"}
          </Button>
          <Button
            onClick={() => {
              if (offset + limit >= totalItems) {
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
          width="15%"
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
      </Box>
    </Box>
  );
}
