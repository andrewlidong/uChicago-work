let results queen =
 
  let show board =
    let foo v =
      for i = 1 to queen do
        print_string (if i=v then " 0" else " x");
      done;
      print_newline() in
    List.iter foo board;
    print_newline() in
 
  let rec safe a b c = function
    | [] -> true
    | x::t -> x<>a && x<>b && x<>c && safe a (b+1) (c-1) t in
 
  let rec loop col p =
    for i = 1 to queen
    do
      if safe i (i+1) (i-1) p then
        let p' = i::p in
        if col = queen then show p'
        else loop (col+1) p'
    done in
 
  loop 1 [] in
 
let queen =
  if Array.length Sys.argv > 1
  then int_of_string Sys.argv.(1)
  else 8 in
 
results queen;
