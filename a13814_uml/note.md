@startuml
skinparam sequenceArrowThickness 2
skinparam roundcorner 20
skinparam maxmessagezie 60
skinparam sequenceParticipant underline

actor StudentClass
participant "AutoAssignClass" as A
participant "PersonerTutorClass" as B

StudentClass -> A: enroll/tranforclass
activate A

A -> B: (create/transfer) auto_assign
activate B

B -> StudentClass: Assign Created
deactivate B
@enduml


----

@startuml
skinparam sequenceArrowThickness 2
skinparam roundcorner 20
skinparam maxmessagezie 60
skinparam sequenceParticipant underline

actor Tutor
participant "AutoAssignClass" as A
participant "StudentClass" as B

Tutor -> A: (search_students/delete_student/alter_student)
activate A

A -> B: (all_student/search_student) request
activate B

B -> AutoAssignClass: operation_result(finshed or failed)
deactivate B
@enduml

--


http://www.plantuml.com/plantuml/uml/RSwnJWCn3CRnFKzXTO81KNLWk04rrnUeH5_0Iao9Ud4Esm74qvChI1Uapjyl_tYlXc8rJqulYMSKpA3qNea3UP7oUNfBuSAa2hkEIAaSGn4cWTss6p9-vORnJD-9u6bx8tj4iHJIZ6pGAYHJOd8EWnM15wkHs0uJghgvanjVhNZLTERhk05KyF_9aKGBavmQbLMDplLPU7W6Fm3-zNZvENsWKSivlwpZ07T128qUJP3rbUGUP3bVRTKjEowwRm_mUo8Shi-ZYzJvFN6iUVe1