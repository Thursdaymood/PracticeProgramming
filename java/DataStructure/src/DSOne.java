
import java.util.Stack;

public class DSOne {

	public static void main(String[] args) {
		referenceStudy();
	}
	
	public void one_Stack() {
		
		/* Stack /LIFO - Last-in First-out/
		 * push()	add item
		 * pop()	remove
		 * peak()	know the previous pushed item
		 * empty()	return the boolean check item in stack
		 * search(x)	return 1 means the stack has x, -1 means opposite
		 */
		Stack<String> stackTest = new Stack<String>();
		
		System.out.println("Check stack's capacity: "+stackTest.empty());
		stackTest.push("Minecraft");
		
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
	

}
