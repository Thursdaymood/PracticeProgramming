void main(List<String> args) {
  ////🌼 Basic collection
  //basicCollection();
  ////🌼 Transformation
  //exampleTrans();
  ////🌼 If,For,Spread with collection
  //exampleIFS();
  ////🌼 Enum
  //exampleEnum();
  ////🌼 pubPackage
}

void basicCollection() {
  // Collections in dart
  // 4 kinds -> List, Set, Map, Queue

  // now it's dynamic type
  List elements = ["F", "H", "He", "O", "Ca"];
  //var elements = ["F", "H", "He", "O", "Ca"];
  //final elements = ["F", "H", "He", "O", "Ca"];

  // Notice that should not use a dynamic type as much as possible
  // Assign type
  List<String> transitionElements = ["Fe", "Au"];

  // Example of
  <int>[1, 2, 3];

  // Alike json
  // Mostly use dynamic type with Map
  // assign type of key & value
  Map<String, dynamic> firstMap = {
    "name": "John",
    "age": 23,
    "registered": true
  };

  Set<int> mySet = {1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5};
  print(mySet.length);
}

void exampleTrans() {
  var drinks = ["Water", "Cola", "Juice", "Beer", "Wine"];

  // Iterable variable
  //var drinkLen = drinks.map((drinks) => drinks.length); // Similar to tuple
  var drinkLen = drinks.map((drinks) => drinks.length).toList();
  print(drinkLen);

  var drinksFilter = drinks.where((drinks) => drinks.length == 4).toList();
  print(drinksFilter);

  //drinksFilter.forEach((element) => print(element));
  drinksFilter.forEach(print);

  for (final i in drinks) {
    print(i);
  }
}

void exampleIFS() {
  bool isSignIn = true;
  var test1 = <String>[
    "This is a fake content",
    if (isSignIn) "Sign Out" else "Sign In",
  ];
  var test2 = <String>[
    for (int i = 0; i < 5; i++) i.toString(),
    for (final num in [1, 2, 3]) num.toString(),
  ];

  // Spread Operator
  final list1 = ["Hello", "there"];
  final list2 = ["what", "up"];
  var test3 = <String>[...list1, ...list2];

  print(test1);
  print(test2);
  print(test3);
}

// Enum allow to enumerate a certain sequence of element
enum AccountType { free, premium, vip } //PascalCase
// Actually enum can use carmel case but in normal it uses pascalCase

// the AccountType an have only three value
void exampleEnum() {
  AccountType userAccountType = AccountType.premium;
  print(userAccountType.index);
  print(AccountType.values[0]);

  switch (userAccountType) {
    case AccountType.free:
      print("0 USD");
      break;

    case AccountType.premium:
      print("20 USD");
      break;

    case AccountType.vip:
      print("30 USD");
      break;

    default:
      break;
  }
}

void pubPackage() {
  //pedantic package is for bettering the quality of the code that you write
  // linting package etc.
  // can check in pub.dev
}
