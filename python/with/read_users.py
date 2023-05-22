"""GPT-4:

Using the Abstract Base Class (ABC) module in Python provides several advantages
over relying solely on duck typing:

Explicit contract: By using an abstract base class, you explicitly define a
contract or interface that the implementing classes must adhere to. This
contract serves as documentation and provides a clear understanding of the
expected methods and behavior. It helps developers understand the requirements
of implementing the class correctly.

Enforced interface: With an abstract base class, the @abstractmethod decorator
enforces that the derived classes implement the required methods. If a derived
class fails to implement any of the abstract methods, Python raises a TypeError
at runtime, indicating that the class is incomplete or incorrectly implemented.
This helps catch potential errors early during development.

IDE support and autocompletion: IDEs and code editors can leverage the
information provided by abstract base classes to offer better autocompletion,
code suggestions, and type checking. This enhances developer productivity and
reduces the chances of making mistakes or typos.

Code readability and maintainability: Abstract base classes make the code more
readable and self-documenting. By explicitly defining the expected interface, it
becomes clear to other developers what methods are required for the
implementation. It improves code maintainability by providing a clear separation
of concerns and promoting a more structured and organized codebase.

While duck typing allows you to rely on the presence of specific methods without
explicitly defining interfaces, using an abstract base class adds clarity,
robustness, and enforceability to your code. It makes the code more explicit,
easier to understand, and less prone to errors. It also promotes consistency
among different implementations and facilitates code reuse and extension.
"""
from abc import ABC, abstractmethod

class UserReader(ABC):
    @abstractmethod
    def read_users(self):
        pass


if __name__ == "__main__":
    failing = UserReader()  # ABC instantiation should fail