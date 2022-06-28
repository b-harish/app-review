# app-review
App to find contradicting app reviews from corpus of reviews uploaded.

This app supports authentication.

**Steps to run this app**
* Install the pip packages attached in requirements.txt
* To use this app, create '.streamlit/secrets.toml' file.
* Add below text to the file. Replace _username_ and _password_ appropriately.
```
[passwords]
username = "password"
```
* In the terminal, run `streamlit run app_review.py`

## Bonus Questions
(1) Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 

**Answer**:

In my current project, we are using a UI component which is like a **table** with **sorting** functionality.
There are scenarios where the data is of parent-child nature. So we have a **nested table**. What it means is
that sometimes a row can/cannot have children rows. So **sorting** feature was not provided to this nested table
UI component. Since we are following Agile (2-week per sprint), senior folks said that we need a sepearte story
and this feature to be analyzed because this is of nested nature. But I saw no difference between regular table sort
and nested table sort. I just modified the original **mergesort** algorithm and made it work within an hour. 
This is something that I am happy about in my small experience. Still could have solved by others but at that moment
only I could think of this simple idea.

(2) Formally, a vector space V' is a subspace of a vector space V if

1. V' is a vector space
2. every element of V′ is also an element of V.

Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
* The set of pairs (a, a + 1) for all real a
* The set of pairs (a, b) for all real a ≥ b
* The set of pairs (a, 2a) for all real a
* The set of pairs (a, b) for all non-negative real a,b

**Answer**:
* (a, a+1) is **not a subspace of V** because (0, 0) cannot be in the V'

* (a, b) for all real a >= b
    * (0, 0) exists
    * (2, 1) + (9, 9) = (11, 10) in the vector space
    * -5(1, -2) = (-5, 10) **not closed under multiplication.**
    * **Not a a subspace of V**

* (a, 2a) for all real a
    * (0, 0) exists
    * (5, 10) + (6, 12) => (11, 22) in the vector space.
    * (-9, -18) + (4, 8) => (-5, -10) in the vector space.
    * 3(5, 10) => (15, 30) in the vector space.
    * **a subspace of V**

* (a, b) for all non-negative real a, b
    * (0, 0) exists
    * (2, 2) + (4, 4) => (6, 6) in the vector space
    * -1(2, 2) => (-2, -2) not in vector space
    * **Not a subspace of V**
