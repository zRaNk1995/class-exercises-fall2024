import java.util.HashSet;

public class ContainsPair {

    public static boolean hasDuplicate(int[] array) {
        // Create a HashSet to keep track of seen integers
        HashSet<Integer> seenNumbers = new HashSet<>();

        // Iterate through each element in the array
        for (int num : array) {
            // Check if the number is already in the HashSet
            if (seenNumbers.contains(num)) {
                // Found a duplicate
                return true;
            }
            // Add the number to the HashSet
            seenNumbers.add(num);
        }

        // No duplicates found
        return false;
    }

    public static void main(String[] args) {
        // Test the function with an example array
        int[] array = {1, 2, 3, 4, 5, 3};
	int[] arrayTwo = {1,2,3,4,5};

        if (hasDuplicate(array)) {
            System.out.println("Array contains duplicates.");
        } else {
            System.out.println("Array does not contain duplicates.");
		}

	if(hasDuplicate(arrayTwo)) {
		System.out.println("Array contains duplicates. ");
	} else {
		System.out.println("No duplicates found.");
	}

}
}


