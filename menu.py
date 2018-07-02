salir = False

while not salir:
    print("Seleccione estructura de Datos")
    print ("1. Lista")
    print ("2. Btree")
    print ("3. AVLtree")
    print ("4. 2-3tree")
    print ("5. Hash")
    print ("6. Salir")
    opcion = input("Ingrese una opcion")

    if opcion == 1:
        import list.py
        list = List()
        print("Que desea hacer?")
        print("1. Ingresar")
        print("2. Buscar")
        print("3. Imprimir")
        print("4. Eliminar")
        print("5. Salir")
        do = input("ingrese una opcion")

        if do == 1:
            nombre = input("Ingrese nombre")
            apellido = input("Ingrese apellido")
            telefono = input("Ingrese telefono")
            mail = input ("Ingrese mail")
            list.insert_last(nombre,apellido,telefono,mail)

        if do == 2:
            nombre = input("Ingrese nombre")
            list.search(nombre)

        if do == 3:
            list.print_list

        if do == 4:
            nombre = input("Ingrese nombre")
            list.delete_node(nombre)
        if do == 5:
            salir = True

    if opcion == 2:
        import btree.py
        tree = BST()
        print("Que desea hacer?")
        print("1. Ingresar")
        print("2. Buscar")
        print("3. Imprimir")
        print("4. Eliminar")
        print("5. Salir")
        do = input("ingrese una opcion")

        if do == 1:
            nombre = input("Ingrese nombre")
            apellido = input("Ingrese apellido")
            telefono = input("Ingrese telefono")
            mail = input ("Ingrese mail")
            tree.insert(nombre,apellido,telefono,mail)

        if do == 2:
            apellido = ingrese("apellido")
            telefono = ingrese("telefono")
            tree.find(apellido, telefono)

        if do == 3:
            tree.in_order

        if do == 4:
            nombre = input("Ingrese nombre")
            apellido = input("Ingrese apellido")
            telefono = input("Ingrese telefono")
            mail = input ("Ingrese mail")
            tree.delete_node(nombre, apellido, telefono, mail)
        if do == 5:
            salir = True
    if opcion == 3:
        import avltree.py
        tree = AVLTree()
        print("Que desea hacer?")
        print("1. Ingresar")
        print("2. Buscar")
        print("3. Imprimir")
        print("4. Eliminar")
        print("5. Salir")
        do = input("ingrese una opcion")

        if do == 1:
            nombre = input("Ingrese nombre")
            apellido = input("Ingrese apellido")
            telefono = input("Ingrese telefono")
            mail = input ("Ingrese mail")
            tree.insert(nombre,apellido,telefono,mail)

        if do == 2:
            print("no disponible")

        if do == 3:
            tree.display()

        if do == 4:
            nombre = input("Ingrese nombre")
            apellido = input("Ingrese apellido")
            tree.delete(nombre, apellido)
        if do == 5:
            salir = True

        if opcion == 4:
            import twothreetree.py

            print("Que desea hacer?")
            print("1. Ingresar")
            print("2. Buscar")
            print("3. Imprimir")
            print("4. Eliminar")
            print("5. Salir")
            do = input("ingrese una opcion")

            if do == 1:
                nombre = input("Ingrese nombre")
                apellido = input("Ingrese apellido")
                telefono = input("Ingrese telefono")
                mail = input ("Ingrese mail")
                tree._add(nombre,apellido,telefono,mail)

            if do == 2:
                apellido = input("Ingrese apellido")
                tree._find(apellido)

            if do == 3:
                tree.preorder()

            if do == 4:
                print("no disponible")
            if do == 5:
                salir = True

        if opcion == 5:
            import hash.py
            hash = HashMap()
            print("Que desea hacer?")
            print("1. Ingresar")
            print("2. Buscar")
            print("3. Imprimir")
            print("4. Eliminar")
            print("5. Salir")
            do = input("ingrese una opcion")

            if do == 1:
                nombre = input("Ingrese nombre")
                apellido = input("Ingrese apellido")
                telefono = input("Ingrese telefono")
                mail = input ("Ingrese mail")
                hash.add(nombre,apellido,telefono,mail)

            if do == 2:
                mail = input ("Ingrese mail")
                list.get(mail)

            if do == 3:
                hash.print_()

            if do == 4:
                mail = input ("Ingrese mail")
                hash.delete(mail)

            if do == 5:
                salir = True
