// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IoTDataStorage {
    struct IoTData {
        uint timestamp;
        string data;
    }

    IoTData[] public dataRecords;

    function storeData(string memory _data) public {
        dataRecords.push(IoTData(block.timestamp, _data));
    }

    function getDataCount() public view returns (uint) {
        return dataRecords.length;
    }

    function getData(uint _index) public view returns (uint, string memory) {
        require(_index < dataRecords.length, "Index out of bounds");
        return (dataRecords[_index].timestamp, dataRecords[_index].data);
    }
}
