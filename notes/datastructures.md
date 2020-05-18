1. list :[mutable]
  insertion order is required to preserve
  duplicates are allowed
  heterogeneous objects are allowed
  growable in nature

2. tuple :[immutable][read only version of list]
  insertion order is required to preserve
  duplicates are allowed
  heterogeneous objects are allowed
  growable in nature

3.set: [mutable]
  insertion order not preserved
  duplicates are not allowed
  heterogeneous objects are allowed
  growable in nature
  set will accept only one argument
  s = set()
  s = set(10,02,03) ==> invalid
  s.add(10)
  s.add('abc')
  s = {10,abc}

4. frozenset :[immutable]
  insertion order not preserved
  duplicates are not allowed
  heterogeneous objects are allowed
  growable in nature

5.dictionary:[mutable]
  order not preserved

6.range():[immutable]
  range(10) ==> 0 to 9
  range[2:8] ==> 2,3,4,5,6,7
  range[0,10,2] ==> 0,2,4,6,8
