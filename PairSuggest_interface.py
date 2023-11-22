import tkinter as tk
from tkinter import messagebox

class EmployeePairingApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplicação para criação de duplas")

        self.persons_list = []
        self.threshold = 20

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Aplicação para criação de duplas")
        self.label.pack()

        self.add_button = tk.Button(self.master, text="Inserir um trabalhador", command=self.add_person)
        self.add_button.pack()

        self.show_button = tk.Button(self.master, text="Mostrar trabalhadores", command=self.show_persons)
        self.show_button.pack()

        self.pair_button = tk.Button(self.master, text="Fazer pares", command=self.pair_employees)
        self.pair_button.pack()

        self.delete_button = tk.Button(self.master, text="Eliminar trabalhador", command=self.delete_person_window)
        self.delete_button.pack()

        self.exit_button = tk.Button(self.master, text="Sair", command=self.master.destroy)
        self.exit_button.pack()

    def add_person(self):
        add_person_window = tk.Toplevel(self.master)
        add_person_window.title("Inserir um trabalhador")

        name_label = tk.Label(add_person_window, text="Nome:")
        name_label.pack()
        name_entry = tk.Entry(add_person_window)
        name_entry.pack()

        preferences_label = tk.Label(add_person_window, text="Preferências (1 to 10):")
        preferences_label.pack()

        preferences_entries = []
        topics = ["Esporte", "Cinema", "Cozinha", "Leitura", "Jogos", "Música"]
        for topic in topics:
            label = tk.Label(add_person_window, text=f"{topic}:")
            label.pack()
            entry = tk.Entry(add_person_window)
            entry.pack()
            preferences_entries.append(entry)


        submit_button = tk.Button(add_person_window, text="Submit", command=lambda: self.submit_person(add_person_window, name_entry.get(), preferences_entries))
        submit_button.pack()

    def submit_person(self, add_person_window, name, preferences_entries):
        try:
            new_person_scores = [self.validate_score(entry.get()) for entry in preferences_entries]
            new_person_format = {'name': name, 'preferences': new_person_scores}
            self.persons_list.append(new_person_format)
            add_person_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Input inválido.")

    def validate_score(self, score_str):
        score = int(score_str)
        if 1 <= score <= 10:
            return score
        else:
            raise ValueError("Valor deve estar entre 1 e 10.")

    def show_persons(self):
        if not self.persons_list:
            messagebox.showinfo("Não há trabalhadores.", "Não há trabalhadores para mostrar.")
            return

        persons_window = tk.Toplevel(self.master)
        persons_window.title("Informação dos trabalhadores")

        for person in self.persons_list:
            tk.Label(persons_window, text=f"{person['name']}: {person['preferences']}").pack()


    def pair_employees(self):
        if len(self.persons_list) < 2:
            messagebox.showinfo("Não há trabalhadores suficientes.", "Não há trabalhadores suficientes para formar duplas.")
            return

        similar_pairs, unpaired_indices = self.find_similar_pairs()

        pairs_window = tk.Toplevel(self.master)
        pairs_window.title("Trabalhadores com e sem dupla")

        if not similar_pairs:
            tk.Label(pairs_window, text="Nenhuma dupla foi encontrada.").pack()
        else:
            tk.Label(pairs_window, text="Trabalhadores com dupla:").pack()
            for pair in similar_pairs:
                tk.Label(pairs_window, text=f"{pair[0]} e {pair[1]}").pack()

        if unpaired_indices:
            tk.Label(pairs_window, text="Trabalhadores sem dupla:").pack()
            for idx in unpaired_indices:
                tk.Label(pairs_window, text=f"{self.persons_list[idx]['name']} não pôde formar dupla.").pack()




    def delete_person_window(self):
        delete_person_window = tk.Toplevel(self.master)
        delete_person_window.title("Eliminar trabalhador")


        name_label = tk.Label(delete_person_window, text="Nome:")
        name_label.pack()
        name_entry = tk.Entry(delete_person_window)
        name_entry.pack()


        submit_button = tk.Button(delete_person_window, text="Submit", command=lambda: self.delete_person(delete_person_window, name_entry.get()))
        submit_button.pack()

    def delete_person(self, delete_person_window, name):
        for person in self.persons_list:
            if person['name'] == name:
                self.persons_list.remove(person)
                messagebox.showinfo("Sucesso", f"{name} removido.")
                delete_person_window.destroy() 
                return
        messagebox.showinfo("Error", f"{name} não encontrado.")

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = self.merge_sort(arr[:mid])
        right, inv_right = self.merge_sort(arr[mid:])
        merged, inv_split = self.merge(left, right)

        inversions = inv_left + inv_right + inv_split
        return merged, inversions

    def merge(self, left, right):
        result = []
        inversions = 0
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inversions += len(left) - i
                j += 1

        result += left[i:]
        result += right[j:]

        return result, inversions

    def count_inversions(self, arr):
        _, inversions = self.merge_sort(arr)
        return inversions

    def are_similar_taste(self, person1, person2, threshold):
        combined_preferences = person1['preferences'] + person2['preferences']
        inversions = self.count_inversions(combined_preferences)
        return inversions <= threshold

    def find_similar_pairs(self):
        similar_pairs = []
        unpaired_indices = list(range(len(self.persons_list)))

        for i, person1 in enumerate(self.persons_list):
            for j, person2 in enumerate(self.persons_list):
                if i < j:  
                    if self.are_similar_taste(person1, person2, self.threshold):
                        similar_pairs.append((person1['name'], person2['name']))

                        if i in unpaired_indices:
                            unpaired_indices.remove(i)
                        if j in unpaired_indices:
                            unpaired_indices.remove(j)

        return similar_pairs, unpaired_indices

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeePairingApp(root)
    root.mainloop()
