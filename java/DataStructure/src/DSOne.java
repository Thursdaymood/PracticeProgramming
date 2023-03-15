
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.PriorityQueue;

public class DSOne {
	static Scanner scan = new Scanner(System.in);
	public static void main(String[] args) {
		// String[] details = {"Stack", "Queue", "PriorityQueue", "ArrayList", "LinkedList",};
		// referenceStudy();
		// detailsInDSOne(details);
		

		
	} 
	public static void one_Stack() {
		//-------------------------------------------------
		/* Stack (LIFO - Last-in First-out)
		 * push(x)	add item
		 * pop(x)	remove
		 * peek()	know the previous pushed item
		 * empty()	return the boolean check item in stack
		 * search(x)	return 1 means the stack has x, -1 means opposite
		 *///-------------------------------------------------
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
		//-------------------------------------------------
		/* Queue (FIFO First-In First-Out)
		 * offer	enqueue/add item
		 * poll		dequeue/remove
		 * peek		check the last enqueued element 
		 *///------------------------------------------------- 
		
		// 	Cannot create queue as an object cause it's just interface
		// 	The queue inherits collection class so we can use method that normally use
		//in array or set
		Queue<String> queueOne = new LinkedList<String>();
		queueOne.offer("Mind");
		queueOne.offer("Sin");
		queueOne.offer("Aye");
		queueOne.offer("Spy");
		
		System.out.println(queueOne);
		String user = queueOne.peek();
		System.out.println(user);
		
		// The poll method doesn't cause an exception as pop method
		// But the element can cause as exception if the data doesn't exist in queue
		queueOne.poll();
		queueOne.poll();
		System.out.println(queueOne);
		
		//Example of using other method in collection class
		System.out.println("Emptiness of queueOne: " + queueOne.isEmpty());
		System.out.println("Size in queueOne: " + queueOne.size());
		System.out.print("Enter the name to search: ");
		String name = scan.next();
		
		if(queueOne.contains(name)) {
			System.out.println(name + "exists in queue.");
			
		}
		else {
			System.out.println(name + " doesn't exist in queue.");
		}
		
		
		
	}
	
	public static void three_PriorityQueue() {
		/*	Note : the Priority Queue is the extension of queue
		 * The difference between Queue and Priority Queue is 
		 * O(n) -> Priority Queue is slower than queue
		 * Algorithm -> PQ consider the higher priority first, but Q follows FIFO  
		 * 
		 */
		Queue<String> specialQ = new PriorityQueue<>();
		// Queue<Double> specialQ = new PriorityQueue<>(Collections.reverseOrder());
		// Make it reverse
		
		specialQ.offer("Chocolate");
		specialQ.offer("Banana");
		specialQ.offer("Lime");
		specialQ.offer("Vanilla");
		specialQ.offer("Rainbow");
		
		while(!specialQ.isEmpty()) {
			// Alphabet priority
			System.out.println(specialQ.poll());
		}
		
		
	}
	public static void four_ArrayList() {
		//-------------------------------------------------
		/*	ArrayList
		 * 
		 * 
		 *///-------------------------------------------------
	}
	public static void five_LinkedList() {
		//-------------------------------------------------
		/* 		LinkedList the algorithm of LL mimic from stack and queue, 
		 * it was made to solve the disadvantage of the ArrayList's complexity 
		 * of inserting and deleting
		 * add(index, x)				insert the element at the specific
		 * add(x)						insert to the end of this list
		 * addAll(index, Collections<>)	insert all element in collection starting in specific position
		 * addAll(Collection<>)			insert the all element at the end of LinkedList
		 * addFirst(x), offerFirst()	insert in the first position
		 * addLast(x), offer()			insert in the last element
		 * clear()						clear all the element in LL
		 * clone()						clone LL
		 * element()					retrieve the first element
		 * indexOf(x)							return the index of element
		 * get(index), getFirst(), getLast()	retrieve element
		 * poll(), pollFirst(), pollLast()		retrieve and remove the first element
		 * set(index, x)				replace the element
		 * size()						return the number of elements
		 *///-------------------------------------------------
		LinkedList<String> lineOne = new LinkedList<String>();
		
		lineOne.add("A");
		lineOne.add("B");
		lineOne.add("C");
		lineOne.add("D");
		lineOne.add("E");
		lineOne.add("F");
		
		System.out.print("Enter the index to get element: " );
		int userOne = scan.nextInt();
		System.out.println();
		if(userOne < lineOne.size()) {
			System.out.println(lineOne.get(userOne));
		}else {
			System.out.println("Out of index");
		}
		System.out.println();
		
		
		System.out.print("Enter the index to remove element: ");
		int userTwo = scan.nextInt();
		System.out.println();
		if(userTwo < lineOne.size()) {
			System.out.println(lineOne.remove(userTwo));
		}else {
			System.out.println("Out of index");
		}
		
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
	

