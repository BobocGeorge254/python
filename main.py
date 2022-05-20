f = open("input.in", "r")
g = open("output.out", "w")

Entities = []
numberOfEntities = int(f.readline())
numeClasa = f.readline()
for i in range (numberOfEntities) :
    (dataType, entity, whatever) = f.readline().split()
    Entities.append( (dataType, entity, whatever) )

def Constructor() :
    print (numeClasa, end = "",file = g)
    print("(", end = "", file = g)
    step = 1
    for tuple in Entities :
        print (f"{tuple[0]} {tuple[1]}", end = "", file = g)
        if tuple[0] == "int" or tuple[0] == "float" :
            print (" = 0", end = "", file = g)
        if tuple[0] == "string" :
            print ("= \"\" ", end = "", file = g)
        if "vector" in tuple[0] :
            print ("= {} ", end = "", file = g)
        if (step != numberOfEntities) :
            print(",", end = "", file = g)
        else :
            print (")", end = "",file = g)
        step = step + 1
    print("{", file = g)
    for tuple in Entities :
        print (f"this -> {tuple[1]} = {tuple[1]} ;", file = g)
    print ("}", file = g)



def Main() :
    print("void citire(istream&);", file = g)
    print("void afisare(ostream&);", file = g)
    print(f"friend istream& operator>> (istream&, {numeClasa}&);", file = g)
    print(f"friend ostream& operator<< (ostream&, {numeClasa}&);", file = g )
    for tuple in Entities :
        if "vector" not in tuple[0] :
            print(f"{tuple[0]} get_{tuple[1]} () ;",file = g)
        else :
            length = len(tuple[0])
            dataType = tuple[0][7: length-1]
            print(f"{dataType}* get_{tuple[1]} () ;", file = g)
    for tuple in Entities :
        print (f"void set_{tuple[1]} ({tuple[0]}) ;", file = g)

def Citire() :
    print(f"void {numeClasa}" , file = g ,end = "" )
    print(f"::citire(istream& in)", file = g, end = "")
    print ("{", file = g)
    for tuple in Entities :
        if "vector" not in tuple[0] :
            print (f"cout << \"{tuple[1]}\"  ; ", file = g)
            print (f"in >> this -> {tuple[1]} ;" , file = g)
        else :
            print (f"for (int i = 0 ; i < nrElemente ; ++i)", file = g, end = "")
            print ("{", file = g)
            print (f"cout << \"{tuple[1]}\" ", file = g)
            print(f"in >> this -> {tuple[1]}[i] ;", file=g)
            print("}", file = g)
    print ("}", file = g)
    print(file = g)
    print(f"istream& operator>> (istream& in, {numeClasa} " , file = g , end = "")
    print ("&ob) {", file = g)
    print ("ob.citire(in);", file = g)
    print("return in; ", file = g ) ;
    print("}", file = g)

def Afisare() :
    print(f"void {numeClasa}", file=g, end="")
    print(f"::afisare(ostream& out)", file=g, end="")
    print("{", file=g)
    for tuple in Entities:
        if "vector" not in tuple[0]:
            print(f"out << \"{tuple[1]}\"  << this -> {tuple[1]} << endl ; ", file=g)
        else:
            print(f"for (int i = 0 ; i < nrElemente ; ++i)", file=g, end="")
            print(f"cout << \"{tuple[1]}\" << this -> {tuple[1]}[i] << endl", file=g)
    print("}", file=g)
    print(file = g)
    print(f"ostream& operator<< (ostream& out, {numeClasa} ", file=g, end="")
    print("&ob) {", file=g)
    print("ob.afisare(out);", file=g)
    print("return out; ", file=g);
    print("}", file=g)

def Setter() :
    for tuple in Entities :
        print (f"void {numeClasa}::set_{tuple[1]} ({tuple[0]} info)", file = g, end = "")
        print ("{", file = g)
        if "vector" not in tuple[0] :
            print (f"this -> {tuple[1]} = info ;", file = g)
        else :
            print("for ( int i = 0 ; i < nrElemente ; ++i )", file = g)
            print (f"this -> {tuple[1]}[i] = info[i] ;", file = g)
        print("}", file = g)

def Getter() :
    for tuple in Entities :
        if "vector" not in tuple[0] :
            print(f"{tuple[0]} {numeClasa}::get_{tuple[1]} ()", file = g, end = "")
        else :
            length = len(tuple[0])
            dataType = tuple[0][7: length-1]
            print(f"{dataType}* {numeClasa}::get_{tuple[1]} ()", file = g, end = "")
        print ("{", file = g)
        print (f"return {tuple[1]} ;", file = g)
        print("}", file = g)


print (f"class {numeClasa}", end ="", file = g)
print ("{", file = g)
for tuple in Entities :
    print (*tuple, file = g)
print("public:", file = g)
Constructor()
Main()
print("};", file = g)
print("//Citire", file = g)
Citire()
print('\n\n',file = g)
print("//Afisare", file = g)
Afisare()
print('\n\n',file = g)
print("//Setteri", file = g)
Setter()
print("//Getteri", file = g)
print('\n\n',file = g)
Getter()
