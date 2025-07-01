https://github.com/ravindrakush11/Python-OOPs

# pydantic

The potential confusion around the term "validation" arises from the fact that, strictly speaking, Pydantic's primary focus doesn't align precisely with the dictionary definition of "validation":
validation
noun the action of checking or proving the validity or accuracy of something.



In Pydantic, the term "validation" refers to the process of instantiating a model (or other type) that adheres to specified types and constraints. Pydantic guarantees the types and constraints of the output, not the input data. This distinction becomes apparent when considering that Pydantic's ValidationError is raised when data cannot be successfully parsed into a model instance.
