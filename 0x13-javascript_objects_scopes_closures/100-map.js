#!/usr/bin/node

const { list } = require("./100-data");

for (let i = 0; i < list.length;i++)
{
    list[i] *= i;
}
return (list);
