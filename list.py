class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert_last(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node = Node(nombre)
            self.tail.next = node
            self.tail = node

    def insert_first(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node = Node(nombre, apellido, telefono, mail)
            node.next = self.head
            self.head = node

    def delete_node(self,nombre):
        if self.empty():
            print("Lista vacia")
        if self.head.nombre == nombre:
            print ("encontrado")
            temp = self.head
            self.head = self.head.next
            temp.next = None
        else:
            temp = self.head
            while temp:
                if nombre == temp.next.nombre:
                    print("encontrado")
                    temp2 = temp
                    temp.next = temp.next.next
                    temp2.next = None

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            seguir = True
            while seguir:
                print(i, temp.nombre, temp.apellido, temp.telefono, temp.mail)
                temp = temp.next
                i += 1
                if temp == None:
                    break
