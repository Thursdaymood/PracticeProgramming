void main(List<String> args) {
  // User myUser = new User(); // similar to java\
  User userOne = User(firstName: "William", lastName: "Smith");

  userPremium userTwo = const userPremium(name: "Sasipa B.", date: "12/3/2023");
  userPremium userThree =
      const userPremium(name: "Sasipa B.", date: "12/3/2023");
  userPremium userFour = userPremium(name: "Sasipa", date: "12/3/2023");

  print(userFour == userThree);
  print(userTwo == userThree);
  print(userOne.hasLongName());
  exampleEncapsulate test1 = exampleEncapsulate(HBD: "1/1/2002", name: "Sin");
  print(test1.getHBD);
  print(test1.getName);

  exampleEncapsulate test2 = exampleEncapsulate(HBD: "2/1/2023", name: "Maple");
  print(test2.getHBD);
  print(test2.getName);

  print(test1._sayHBD("1/1/2002"));
}

////🌠Basic Class
class User {
  late String name;
  // late keyword is used to initialize later on substituting using nullable var.

  //Constructor
  User({
    required String firstName,
    required String lastName,
  }) : name = "$firstName $lastName";

  bool hasLongName() {
    return name.length > 10;
  }
}

////🌠A const keyword
class userPremium {
  // Used const Constructor in case of want a same identical class

  final String name;
  final String date;

  const userPremium({required this.name, required this.date});
}

////🌠A private keyword
class exampleEncapsulate {
  late String _privateHBD;
  late String _privateName;
  // _ is sign of private
  //Private in dart still get that var, method or class
  //in the same file but outside the file it cannot be called\
  exampleEncapsulate({
    required HBD,
    required String name,
  })  : _privateHBD = HBD,
        _privateName = name;

  // Properties ->is the method work sth light-weight
  String getInfo() => "Name: $getName / HBD date: $getHBD";

  //get method
  String get getHBD {
    return this._privateHBD;
  }

  String get getName {
    return this._privateName;
  }

  //set method
  void set setHbd(String user) {
    this._privateHBD = user;
  }

  void set setName(user) {
    this._privateName = user;
  }

  String _sayHBD(String date) {
    if (date == this._privateHBD) {
      return "Happy Birthday!";
    } else {
      return "Have a nice day :)";
    }
  }
}
