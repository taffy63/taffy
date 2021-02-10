import 'package:flutter/material.dart';
import 'package:frontend/login_username.dart';
import 'package:http/http.dart' as http;
import 'package:frontend/models/user_models.dart';
import 'dart:convert';

class RegisterPages extends StatefulWidget {
  // final String _Username;
  // final String _Password;

  // RegisterPages(this._Username, this._Password);
  // RegisterPages({Key key, this._Username, this._Password}) : super(key: key);
  @override
  _RegisterPagesState createState() => _RegisterPagesState();
}

class _RegisterPagesState extends State<RegisterPages> {
  // String _Email = '';
  // String _Username = '';
  // String _Firstname = '';
  // String _Lastname = '';
  // String _Password = '';
  // String _Password2 = '';
  String key = '';
  String value = '';

  GlobalKey<FormState> _key = new GlobalKey();
  bool _validate = false;
  String first_name, last_name, username, email, password, password2;

  // final format = DateFormat('dd MMM yyyy');
  // String _value = 'Birthday';
  void navigationPage() {
    Navigator.of(context).pushReplacementNamed('/login');
    // Navigator.of(context).pushReplacement(new MaterialPageRoute(
    //     settings: const RouteSettings(name: '/LoginPage'),
    //     builder: (context) =>
    //         new LoginUsername(username: username, password: password)));
  }

  Future<User> createMember(User user) async {
    Map data = {
      'email': user.email,
      'username': user.username,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'password': user.password,
      'password2': user.password2,
    };
    var url = 'https://taffy.pythonanywhere.com/auth/register/';
    var response = await http.post(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(data),
    );
    if (response.statusCode == 201) {
      // If the server did return a 201 CREATED response,
      // then parse the JSON.
      Map<String, dynamic> result = json.decode(response.body);
      result.forEach((key, value) {
        print("${key = key.toString()}: ${value = value[0]}");
        // return text(key, value.toString());
      });
      navigationPage();

      return User.fromJson(json.decode(response.body));
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.

      print("response.statusCode :${response.statusCode} ");
      // print("response.statusCode :${response.body} ");

      Map<String, dynamic> result = json.decode(response.body);
      result.forEach((key, value) {
        print("${key = key.toString()}: ${value = value[0]}");
        // return text(key, value.toString());
      });
      // List<dynamic> resulted = result[];
      // print(resulted);
      // throw Exception('Failed to Add User');
    }
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        decoration: BoxDecoration(
          color: Colors.white,
        ),
        child: Stack(children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              SafeArea(
                child: GestureDetector(
                  onTap: () {
                    Navigator.pop(context);
                  },
                  child: Container(
                    //color: Colors.grey,
                    margin: EdgeInsets.all(20.0),
                    // child: Icon(
                    //   Icons.arrow_back,
                    //   color: Colors.red[400],
                    // ),
                  ),
                ),
              ),
            ],
          ),
          Container(
            margin: EdgeInsets.fromLTRB(36, 75, 36, 0
                // MediaQuery.of(context).size.height,
                ),
            child: Text(
              "Register Pages",
              textAlign: TextAlign.left,
              style: TextStyle(
                  color: Colors.grey[700],
                  fontSize: 36,
                  fontWeight: FontWeight.bold),
            ),
          ),
          Container(
              margin: EdgeInsets.fromLTRB(
                36,
                120,
                36,
                0,
              ),
              child: ListView(children: <Widget>[
                Container(
                  child: new Form(
                    key: _key,
                    autovalidate: _validate,
                    child: FormUI(),
                  ),
                ),
              ]))
        ]),
      ),
    );
  }

  Widget FormUI() {
    var _text;
    return new Column(
      children: <Widget>[
        new TextFormField(
          decoration: new InputDecoration(
              icon: Icon(Icons.label_rounded), hintText: 'Firstname'),
          // maxLength: 32,
          validator: validateName,
          onSaved: (String val) {
            first_name = val;
          },
        ),
        new SizedBox(height: 20.0),
        new TextFormField(
          decoration: new InputDecoration(
              icon: Icon(Icons.label_rounded), hintText: 'Lastname'),
          // maxLength: 32,
          validator: validateName,
          onSaved: (String val) {
            last_name = val;
          },
        ),
        new SizedBox(height: 20.0),
        new TextFormField(
          decoration: new InputDecoration(
              icon: Icon(Icons.person), hintText: 'Username'),
          maxLength: 150,
          validator: validateUsername,
          onSaved: (String val) {
            username = val;
          },
        ),
        // new TextFormField(
        //     decoration: new InputDecoration(hintText: 'Mobile Number'),
        //     keyboardType: TextInputType.phone,
        //     maxLength: 10,
        //     validator: validateMobile,
        //     onSaved: (String val) {
        //       mobile = val;
        //     }),
        // new SizedBox(height: 20.0),
        new TextFormField(
            decoration:
                new InputDecoration(icon: Icon(Icons.email), hintText: 'Email'),
            keyboardType: TextInputType.emailAddress,
            // maxLength: 32,
            validator: validateEmail,
            onSaved: (String val) {
              email = val;
            }),
        new SizedBox(height: 20.0),
        new TextFormField(
          obscureText: true,
          decoration: new InputDecoration(
              icon: Icon(Icons.vpn_key), hintText: 'Password'),
          // maxLength: 32,
          validator: validatePassword,
          onSaved: (String val) {
            password = val;
          },
        ),
        new SizedBox(height: 20.0),
        new TextFormField(
          obscureText: true,
          decoration: new InputDecoration(
              icon: Icon(Icons.vpn_key), hintText: 'Password (Again)'),
          // maxLength: 32,

          validator: validatePassword,
          onSaved: (String val) {
            password2 = val;
          },
        ),
        new SizedBox(height: 20.0),
        new Text(
          // Map<String, dynamic> result = json.decode(response.body);

          // print(result);
          "................",
          style: TextStyle(fontSize: 20),
        ),

        GestureDetector(
          onTap: () {
            print("Ontap __");
            _sendToServer();
          },
          child: Container(
            width: double.infinity,
            alignment: Alignment.center,
            padding: EdgeInsets.fromLTRB(0, 16, 0, 16),
            margin: EdgeInsets.fromLTRB(24, 20, 24, 10),
            decoration: BoxDecoration(
                gradient: LinearGradient(
                    colors: [Colors.pinkAccent, Colors.black87],
                    begin: Alignment.centerLeft,
                    end: Alignment.centerRight),
                borderRadius: BorderRadius.circular(26)),
            child: Text(
              "Register To Taffy",
              style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 16),
            ),
          ),
        ),
      ],
    );
  }

  String validateName(String value) {
    String patttern = r'(^[a-zA-Z ]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Name is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Name must be a-z and A-Z";
    }
    return null;
  }

  String validateMobile(String value) {
    String patttern = r'(^[0-9]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Mobile is Required";
    } else if (value.length != 10) {
      return "Mobile number must 10 digits";
    } else if (!regExp.hasMatch(value)) {
      return "Mobile Number must be digits";
    }
    return null;
  }

  String validatePassword(String value) {
    String patttern = r'(^[0-9 a-zA-Z]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Password is Required";
    } else if (value.length < 8) {
      return "Password must 8 digits";
    } else if (!regExp.hasMatch(value)) {
      return "Password must be digits";
    }
    return null;
  }

  String validatePassword2(String value) {
    String patttern = r'(^[0-9 a-zA-Z]*$)';
    RegExp regExp = new RegExp(patttern);
    // Sreing patttern2 = r'(^[ ])';
    // RegExp regExp2 = new password2();
    if (value.length == 0) {
      return "Password is Required";
    } else if (value.length < 8) {
      return "Password must 8 digits";
    } else if (!regExp.hasMatch(value)) {
      return "Password must be digits";
      // } else if (!regExp2.hasMatch(value)) {
      // return "Password hasn't  Match";
    }
    return null;
  }

  String validateEmail(String value) {
    String pattern =
        r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
    RegExp regExp = new RegExp(pattern);
    if (value.length == 0) {
      return "Email is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Invalid Email";
    } else {
      return null;
    }
  }

  String validateUsername(String value) {
    String pattern = r'^(^[a-zA-Z @/./+/-/_ 0-9]*$)';
    RegExp regExp = new RegExp(pattern);
    if (value.length == 0) {
      return "Username is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Invalid Username";
    } else {
      return null;
    }
  }

  _sendToServer() {
    if (_key.currentState.validate()) {
      // No any error in validation
      _key.currentState.save();

      createMember(User(
        email: email,
        username: username,
        first_name: first_name,
        last_name: last_name,
        password2: password2,
        password: password,
      ));

      // print("Firstname $first_name");
      // print("Firstname $last_name");
      // print("Username $username");
      // // print("Mobile $mobile");
      // print("Email $email");
      // print("Password $password");
      // print("Password $password2");
    } else {
      // validation error
      setState(() {
        _validate = true;

        print("object validation error");
      });
    }
  }
}