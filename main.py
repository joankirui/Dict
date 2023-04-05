import json, unittest, datetime,dateutil.parser

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # Split the location string into a dictionary
    location_list = jsonObject["location"].split("/")

    # Create the final result dictionary
    result = {
    "deviceID" : jsonObject["deviceID"],
    "deviceType" : jsonObject["deviceType"],
    "timestamp" : jsonObject["timestamp"],
    "location" : {
      "country": location_list[0],
      "city": location_list[1],
      "area": location_list[2],
      "factory": location_list[3],
      "section": location_list[4]
    },
    "data" : {
      "status": jsonObject["operationStatus"],
      "temperature": jsonObject["temp"]
    }
  }
  # Print the final result
  
    return result


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    
  
    timestamp_str = jsonObject["timestamp"]
    parsed_time = dateutil.parser.parse(timestamp_str)
    timestamp = int(parsed_time.timestamp() * 1000)

    # Create the new dictionary
    final_dict = {
      "deviceID": jsonObject["device"]["id"],
      "deviceType": jsonObject["device"]["type"],
      "timestamp": timestamp,
      "location": {
          "country": jsonObject["country"],
          "city": jsonObject["city"],
          "area": jsonObject["area"],
          "factory": jsonObject["factory"],
          "section": jsonObject["section"]
      },
      "data": jsonObject["data"]
    }

  
    return final_dict
    
def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
