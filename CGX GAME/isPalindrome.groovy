public class PalindromeChecker {

    public static boolean isPalindrome(String str) {
        // Remove non-alphanumeric characters and convert to lowercase
        String cleanStr = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        int left = 0;
        int right = cleanStr.length() - 1;

        while (left < right) {
            if (cleanStr.charAt(left) != cleanStr.charAt(right)) {
                return false; // Characters don't match
            }
            left++;
            right--;
        }

        return true; // All characters matched
    }

    public static void main(String[] args) {
        String testString1 = "racecar";
        String testString2 = "hello";
        String testString3 = "A man, a plan, a canal: Panama";

        System.out.println(testString1 + " is a palindrome: " + isPalindrome(testString1)); // Output: racecar is a palindrome: true
        System.out.println(testString2 + " is a palindrome: " + isPalindrome(testString2)); // Output: hello is a palindrome: false
        System.out.println(testString3 + " is a palindrome: " + isPalindrome(testString3)); // Output: A man, a plan, a canal: Panama is a palindrome: true
    }
}
