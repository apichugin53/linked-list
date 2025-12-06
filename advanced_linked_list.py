from typing import Optional

class AdvancedLinkedList:
    def print_ll_from_tail(self):
        """
        Метод выводит элементы списка в обратном порядке,
        начиная с последнего элемента.
        """
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        print("Список выведен с конца")
    
    def insert_at_index(self, index: int, data):
        """
        Вставляет новый узел по заданному индексу.
        
        :param index: Индекс места вставки
        :param data: Данные нового узла
        """
        if index <= 0 or self.head is None:
            return self.insert_at_head(data)
        elif index >= self.len_ll():
            return self.insert_at_tail(data)
        
        new_node = Node(data)
        current_node = self.head
        position = 0
        
        while position != index and current_node is not None:
            previous_node = current_node
            current_node = current_node.next_node
            position += 1
            
        previous_node.next_node = new_node
        new_node.prev_node = previous_node
        new_node.next_node = current_node
        if current_node is not None:
            current_node.prev_node = new_node
        print(f"Вставка выполнена успешно. Новый узел {new_node.data} находится на позиции {index}.")
    
    def remove_node_index(self, index: int):
        """
        Удаляет узел по указанному индексу.
        
        :param index: Индекс удаляемого узла
        """
        if index < 0 or self.head is None:
            raise IndexError("Индекс вне диапазона")
        
        if index == 0:
            return self.remove_from_head()
        elif index == self.len_ll() - 1:
            return self.remove_from_tail()
        
        current_node = self.head
        position = 0
        
        while position != index and current_node is not None:
            previous_node = current_node
            current_node = current_node.next_node
            position += 1
        
        if current_node is None:
            raise IndexError("Индекс вне диапазона")
        
        previous_node.next_node = current_node.next_node
        if current_node.next_node is not None:
            current_node.next_node.prev_node = previous_node
        print(f"Удалён узел с данными {current_node.data}, находился на позиции {index}.")
        del current_node
    
    def remove_node_data(self, target_data):
        """
        Удаляет узел по значению данных.
        
        :param target_data: Значение данных узла для удаления
        """
        current_node = self.head
        found = False
        
        while current_node is not None:
            if current_node.data == target_data:
                found = True
                break
            current_node = current_node.next_node
        
        if not found:
            raise ValueError(f"Нет узла с данными '{target_data}'")
        
        if current_node.prev_node is not None:
            current_node.prev_node.next_node = current_node.next_node
        else:
            self.head = current_node.next_node
        
        if current_node.next_node is not None:
            current_node.next_node.prev_node = current_node.prev_node
        else:
            self.tail = current_node.prev_node
        
        print(f"Удалён узел с данными {target_data}.")
        del current_node
    
    def len_ll(self):
        """
        Возвращает количество узлов в списке.
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count
    
    def contains_from_head(self, target_data):
        """
        Проверяет наличие указанного значения в списке, проходя от головы.
        
        :param target_data: Данные искомого узла
        :return: bool - присутствует ли значение в списке?
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == target_data:
                return True
            current_node = current_node.next_node
        return False
    
    def contains_from_tail(self, target_data):
        """
        Проверяет наличие указанного значения в списке, проходя от хвоста.
        
        :param target_data: Данные искомого узла
        :return: bool - присутствует ли значение в списке?
        """
        current_node = self.tail
        while current_node is not None:
            if current_node.data == target_data:
                return True
            current_node = current_node.prev_node
        return False
    
    def contains_from(self, target_data, from_head=True):
        """
        Универсальная проверка наличия значения в списке, позволяющая выбрать направление обхода.
        
        :param target_data: Данные искомого узла
        :param from_head: Флаг направления проверки (True - от головы, False - от хвоста)
        :return: bool - присутствует ли значение в списке?
        """
        if from_head:
            return self.contains_from_head(target_data)
        else:
            return self.contains_from_tail(target_data)