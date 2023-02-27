"""
  public static int[] twoSum(int[] nums, int target) {
            int[] indices = new int[2];
            for (int i = 0; i < nums.length; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[i] + nums[j] == target) {
                        indices[0] = i;
                        indices[1] = j;
                        return indices;
                    }
                }
            }
            return null;
        }
}
"""


def two_sum(nums, target):
    indices = [0, 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indices[0] = i
                indices[1] = j
                return indices
    return None


numsArray = [2, 7, 11, 15]
target_Num = 9
result = two_sum(numsArray, target_Num)
print(result)
