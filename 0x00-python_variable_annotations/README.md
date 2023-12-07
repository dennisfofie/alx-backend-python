This module provides runtime support for type hints. The most fundamental support consists of the types Any, Union, Callable, TypeVar, and Generic. For a full specification, please see PEP 484. For a simplified introduction to type hints, see PEP 483.

The function below takes and returns a string and is annotated as follows:

def greeting(name: str) -> str:
return 'Hello ' + name
In the function greeting, the argument name is expected to be of type str and the return type str. Subtypes are accepted as arguments.

New features are frequently added to the typing module. The typing_extensions package provides backports of these new features to older versions of Python.

For a summary of deprecated features and a deprecation timeline, please see Deprecation Timeline of Major Features.

See also For a quick overview of type hints, refer to this cheat sheet.
The “Type System Reference” section of https://mypy.readthedocs.io/ – since the Python typing system is standardised via PEPs, this reference should broadly apply to most Python type checkers, although some parts may still be specific to mypy.

The documentation at https://typing.readthedocs.io/ serves as useful reference for type system features, useful typing related tools and typing best practices.

Relevant PEPs
Since the initial introduction of type hints in PEP 484 and PEP 483, a number of PEPs have modified and enhanced Python’s framework for type annotations. These include:

PEP 526: Syntax for Variable Annotations
Introducing syntax for annotating variables outside of function definitions, and ClassVar

PEP 544: Protocols: Structural subtyping (static duck typing)
Introducing Protocol and the @runtime_checkable decorator

PEP 585: Type Hinting Generics In Standard Collections
Introducing types.GenericAlias and the ability to use standard library classes as generic types

PEP 586: Literal Types
Introducing Literal

PEP 589: TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
Introducing TypedDict

PEP 591: Adding a final qualifier to typing
Introducing Final and the @final decorator

PEP 593: Flexible function and variable annotations
Introducing Annotated

PEP 604: Allow writing union types as X | Y
Introducing types.UnionType and the ability to use the binary-or operator | to signify a union of types

PEP 612: Parameter Specification Variables
Introducing ParamSpec and Concatenate

PEP 613: Explicit Type Aliases
Introducing TypeAlias

PEP 646: Variadic Generics
Introducing TypeVarTuple

PEP 647: User-Defined Type Guards
Introducing TypeGuard

PEP 655: Marking individual TypedDict items as required or potentially missing
Introducing Required and NotRequired

PEP 673: Self type
Introducing Self

PEP 675: Arbitrary Literal String Type
Introducing LiteralString

PEP 681: Data Class Transforms
Introducing the @dataclass_transform decorator

Type aliases
A type alias is defined by assigning the type to the alias. In this example, Vector and list[float] will be treated as interchangeable synonyms:

Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.

new_vector = scale(2.0, [1.0, -4.2, 5.4])
Type aliases are useful for simplifying complex type signatures. For example:

from collections.abc import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
...

# The static type checker will treat the previous type signature as

# being exactly equivalent to this one.

def broadcast_message(
message: str,
servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
...
Note that None as a type hint is a special case and is replaced by type(None).
