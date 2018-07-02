# -*- coding: utf-8 -*-

class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombe = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.left = None
        self.right = None
        self.parent = None # Añadimos el atributo parent para facilitar la eliminación de un nodo

class BST:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, nombre, apellido, telefono,mail, node):
        if telefono < node.telefono:
            if node.left == None:
                node.left = Node(nombre, apellido, telefono, mail)
                node.left.parent = node
            else:
                self._insert(nombre, apellido, telefono, mail, node.left)
        elif telefono > node.telefono:
            if node.right == None:
                node.right = Node(nombre, apellido, telefono, mail)
                node.right.parent = node
            else:
                self._insert(nombre, apellido, telefono, mail, node.right)
        else:
            print("Value is already in the Tree")

    def insert(self, nombre, apellido, telefono, mail):
        if self.empty():
            self.root = Node(nombre, apellido, telefono, mail)
        else:
            self._insert(nombre, apellido, telefono, mail, self.root)

    def _find(self, apellido, telefono):
        if node == None:
            return None
        elif apellido == node.apellido:
            return node
        elif telefono < node.telefono and node.left != None:
            return self._find(apellido, telefono, node.left)
        elif telefono > node.telefono and node.right != none:
            return self._find(apellido, telefono, node.right)

    def find(self, apellido, telefono):
        if self.empty():
            return None
        else:
            return self._find(apellido, telefono, self.root)

    def delete(self, nombre, apellido, telefono, mail): #Implementar
        if self.empty():
            return None
        return self.delete_node(self.find(nombre, apellido, telefono, mail))

    def delete_node(self, node):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent # Get the parent of the node to be deleted
        node_children = number_children(node)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # Replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(node.right) # Get the inorder successor of the deleted node
            node.telefono = successor.telefono # Copy the value
            self.delete_node(successor)

    def in_order(self, node): #Implementar
        if node==None:
            pass
        else:
            self.in_order(node.left)
            print(node.telefono)
            self.in_order(node.nombre, node.apellido, node.telefono, node.mail)

    def post_order(self, node): #Implementar
        if node==None:
            pass
        else:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.nombre, node.apellido, node.telefono, node.mail)

    def pre_order(self, node): #Implementar
        if node==None:
            pass
        else:
            print(node.nombre, node.apellido, node.telefono, node.mail)
            self.in_order(node.left)
            self.in_order(node.right)

    def leaf_number(self): #Implementar
        pass


    def _tree_height(self, current, height):
        if current == None:
            return height
        left_height = self._tree_height(current.left, height+1)
        right_height = self._tree_height(current.right, height+1)
        return max(left_height, right_height)

    def tree_height(self): #Implementar
        if self.empty():
            return 0
        else:
            return self._tree_height(self.root, 0)

    def node_height(self, telefono): #Implementar
        node = self.root
        height = 0
        if self.find(telefono):
            height += 1
            while node.telefono != telefono:
                if telefono < node.telefono:
                    node = node.left
                else:
                    node = node.right
                height += 1
            return height
        return False

    def find_minimum(self): #Implementar
        if self.empty():
            return None
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current

    def find_maximum(self): #Implementar
        if self.empty():
            return None
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current
