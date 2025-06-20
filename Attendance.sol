// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Attendance {
    struct Record {
        string name;
        string timestamp;
    }

    Record[] public logs;

    function markAttendance(string memory name, string memory timestamp) public {
        logs.push(Record(name, timestamp));
    }

    function getAttendanceCount() public view returns (uint) {
        return logs.length;
    }

    function getRecord(uint index) public view returns (string memory, string memory) {
        return (logs[index].name, logs[index].timestamp);
    }
}
