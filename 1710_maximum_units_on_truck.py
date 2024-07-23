class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort by boxtypes[i][1]
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        weight = 0
        no_of_boxes = 0
        i = 0
        # print(boxTypes)
        while weight < truckSize and i < len(boxTypes):
            box = boxTypes[i]
            no_of_boxes += box[1]
            weight += 1
            boxTypes[i][0] -= 1
            if box[0] == 0:
                i += 1
        return no_of_boxes