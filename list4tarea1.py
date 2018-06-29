class Node():
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombe = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def insert_last(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node = Node(nombre, apellido, telefono, mail)
            self.tail.next_node = node
            self.tail = node

    def insert_first(self,nombre, apellido, telefono, mail):
        if self.empty():
            self.head = Node(nombre, apellido, telefono, mail)
            self.tail = self.head
        else:
            node = Node(nombre, apellido, telefono, mail)
            node.next_node = self.head
            self.head = node

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            seguir = True
            while seguir:
                print("Nodo {} contiene el número {}".format(i, temp.data))
                temp = temp.next_node
                i += 1
                if temp == None:
                    break
    def erase_node(self,telefono):
        if self.head is not None:
            if telefono == self.head.telefono
                aux = self.head
                self.head = self.head.next
                aux.next = None
            else:
                aux = self.head
                while aux:
                    if aux.next.data == dato
                        aux2 = aux.next
                        aux.next = aux2.next
                        aux2.next = None
                        aux2 = None
