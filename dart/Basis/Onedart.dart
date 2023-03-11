import 'dart:html';
import 'dart:indexed_db';

void main(List<String> args) {
  //// Remember the syntax is quite similar to C# and Java

  //🚩Variable & primitive type
  //exampleAssignVar();
  //🚩Null & Non-null types
  //exampleNull_NonNull();
  //🚩Null & Non-null types
  exampleOperator();
  //🚩Control Flow
  //exampleControlFlow();
}

void exampleAssignVar() {
  // Assign the variable
  // 7 data types -> String, Number(Integer, Double),
  //List, Boolean, Runes, Symbols, dynamic

  // String
  String firstName = "Sasipa";
  String lastName = "B.";
  print(firstName + " " + lastName);

  //Number
  num member_in_family = 4;

  int age = 20;
  print("I'm " + age.toString() + " years old.");

  double height = 156;
  print(height.toString() + "cm.");

  //lIST
  List favorite_food;
  favorite_food = [
    "pizza",
    "curry & rice",
    1
  ]; // can store many type of data in one list
  print(favorite_food);
  List beverage = ["cola", "coffee", "water", "juice"];

  //Boolean
  bool like_Pizza = true;

  // Map
  Map family = {1: "sister", 2: "mom & dad"};

  //Runes
  var heart = "\u2665";
  print(heart);

  // Symbols
  var symbols = "#num";
  print(symbols);

  // Dynamic var. -> can be every type
  dynamic sth = "Candy";
  sth = true;
  sth = "caramel";

  // Constant keyword
  final String nickName = "Sin";
  String university, faculty, department;
}

void exampleNull_NonNull() {
  // Null easily describe
  //is a universal non-value variable(don't hold anything!)

  String? impossible = null;
  //String? impossible;

  print(impossible);
  print(impossible?.length);
  //  when the complier detect null variable(?)
  //it will short circuit and execute that is null
  //  Resolve the runtime error which is null var is hard
  //to detect in pov of programmer

  //Example of error detected by (?)
  String? possible = "ABC";
  print(possible?.length);
  // display the error but still print the output
}

void exampleOperator() {
  // Assignment Operator
  // Arithmetic Op.
  double num1 = 100.455;
  double num2 = 1456;
  print(num2 /= num1);

  // Unary Operator
  int num3 = 1;
  print(num3++); // the value before increment
  print(-num3); // The value before decrement

  String phoneA = "Apple";
  //Test Op.
  if (phoneA is String) {
    print("Oh well!");
  } else {
    print("So many type of OS");
  }
  //Relational Op.
  num3 = 10;
  while (num3 != 0) {
    print("Hello");
    num3 -= 1;
  }

  //Logical Op.
  List team = ["A", "B", "C", "D"];
  print((team.length != 0) && (num3 != 0));

  //Bitwise Op.
  int A = 1001;
  int B = 0011;
  print(A & B);

  // Conditional
  bool isEqual = 5 != 10;
  bool checkup = num3 == 3;
  String merging = checkup.toString() + " " + isEqual.toString();
  print(merging);
  //String myString = "Hello" + " " + isEqual.toString();
  String myString = "Hello $isEqual";
  print(myString);

  myString = "Hello ${5 + 5 / 2 + 123}";
  print(myString);

  // Cascade
}

void exampleControlFlow() {
  int num = 5;

  //Iteration Statement
  for (int i = 0; i < 8; i++) {
    num -= 1;
    i++;
  }

  while (num != 100) {
    num += 1;
  }

  // Selection Statement
  if (!(num != 5)) {
    print("Chocolate is my life");
  } else if (num > 5) {
    print("Boba tea as well");
  } else {
    print("Pizza healing me");
  }

  switch (num <= 100) {
    //Cannot do any operation in case statement
    case true:
      {
        print("It's me");
      }
      break;

    case false:
      {
        print("I'm the problem is me");
      }
      break;
  }
  switch (num) {
    case 1:
      {
        print(num);
      }
      break;
    case 100:
      {
        print("Yeah");
      }
      break;
    default:
      print("Oh greez");
  }
  int count = 0;
  while (true) {
    print(count);
    if (count == 99) {
      continue;
    }
    if (count == 100) {
      print("Hooya");
      break;
    }
    count += 1;
  }
  bool myBool = true;

  do {
    print("Wow that is the new thing");
  } while (!(myBool)); // 
}
