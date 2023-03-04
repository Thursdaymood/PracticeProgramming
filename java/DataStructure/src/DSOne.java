
import java.util.Stack;

public class DSOne {
	
	public static void main(String[] args) {
		String[] details = {"Stack", "Queue"};
		referenceStudy();
		detailsInDSOne(details);
	}
	
	public static void one_Stack() {
		
		/* Stack /LIFO - Last-in First-out/
		 * push()	add item
		 * pop()	remove
		 * peek()	know the previous pushed item
		 * empty()	return the boolean check item in stack
		 * search(x)	return 1 means the stack has x, -1 means opposite
		 */
		Stack<String> stackTest = new Stack<String>();
		
		System.out.println("Check stack's capacity: "+stackTest.empty());
		System.out.println("Start pushing");
		stackTest.push("Minecraft");
		stackTest.push("The sims");
		stackTest.push("Far cry");
		stackTest.push("The bubble");
		System.out.println("Check stack's capacity: "+stackTest.empty());
		System.out.println("This string was pushed previously: "+stackTest.peek());
		
		String game = stackTest.pop(); //it will remove the previous item in stack out
		
//		//Study case about the memory and using the stack
//		for (int i = 0 ; i < 1000000000 ; i++) {
//			stackTest.push("Papa's");
//			// it will display an error OutoOfMemoryError
//			// due to java heap the memory
//		}
		
	}
	
	public static void two_Queue() {
		
		
	}
	
	public static void referenceStudy() {
		 
		 theLine(30);
		 System.out.println("    "+"Lecture from Bro Code");
		 System.out.println("    URL: \"https://www.youtube.com/watch?v=CBYHwZcbD-s\"");
		 theLine(30);
	}
	public static void theLine(int num) {
		
		for(int i = 0 ; i < num ; i++) {
			System.out.print("-");
		}
		System.out.println();
	}
	
	public static void detailsInDSOne(String[] details) {
		System.out.print("Contents : ");
		for (int i = 0 ; i < details.length ; i++) {
			System.out.print(details[i] +", ");
		}
		}
	
	
	
//The end of the class		
}
	

