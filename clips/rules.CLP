(deftemplate Description
    (slot name (type SYMBOL) (default ?NONE))
    (multislot Features)
)
(deftemplate Classification
    (slot name (type SYMBOL) (default ?NONE))
    (slot Class (type SYMBOL) (default ?NONE))
    (slot Flag (type INTEGER) (default 0))
)

(defrule ToRoot
    (Description (name ?x))
    =>
    (assert (Classification (name ?x)
            (Class Someone)))
)

(defrule ToI___
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted yes intuition ? thinking ? judging ?))
    =>
    (assert (Classification (name ?x)
            (Class I___) (Flag 1)))
)
(defrule ToE___
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted no intuition ? thinking ? judging ?))
    =>
    (assert (Classification (name ?x)
            (Class E___) (Flag 1)))
)

(defrule To_N__
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition yes thinking ? judging ?))
    =>
    (assert (Classification (name ?x)
            (Class _N__) (Flag 1)))
)
(defrule To_S__
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition no thinking ? judging ?))
    =>
    (assert (Classification (name ?x)
            (Class _S__) (Flag 1)))
)

(defrule To__T_
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition ? thinking yes judging ?))
    =>
    (assert (Classification (name ?x)
            (Class __T_) (Flag 1)))
)
(defrule To__F_
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition ? thinking no judging ?))
    =>
    (assert (Classification (name ?x)
            (Class __F_) (Flag 1)))
)



(defrule To___J
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition ? thinking ? judging yes))
    =>
    (assert (Classification (name ?x)
            (Class ___J) (Flag 1)))
)
(defrule To___P
    (Classification (name ?x) (Class Someone))
    (Description (name ?x) (Features introverted ? intuition ? thinking ? judging no))
    =>
    (assert (Classification (name ?x)
            (Class ___J) (Flag 1)))
)



(defrule ToInspector
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Inspector) (Flag 1)))
)

(defrule ToCrafter
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Crafter) (Flag 1)))
)

(defrule ToProtector
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Protector) (Flag 1)))
)

(defrule ToArtist
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Artist) (Flag 1)))
)


(defrule ToAdvocate
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Advocate) (Flag 1)))
)

(defrule ToMediator
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Mediator) (Flag 1)))
)

(defrule ToArchitect
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Architect) (Flag 1)))
)

(defrule ToThinker
    (Classification (name ?x) (Class I___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Thinker) (Flag 1)))
)



(defrule ToPersuader
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Persuader) (Flag 1)))
)

(defrule ToDirector
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Director) (Flag 1)))
)

(defrule ToPerformer
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Performer) (Flag 1)))
)

(defrule ToCaregiver
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _S__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Caregiver) (Flag 1)))
)



(defrule ToChampion
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Champion) (Flag 1)))
)

(defrule ToGiver
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __F_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Giver) (Flag 1)))
)

(defrule ToDebater
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___P))
    =>
    (assert (Classification (name ?x)
            (Class Debater) (Flag 1)))
)

(defrule ToCommander
    (Classification (name ?x) (Class E___))
    (Classification (name ?x) (Class _N__))
    (Classification (name ?x) (Class __T_))
    (Classification (name ?x) (Class ___J))
    =>
    (assert (Classification (name ?x)
            (Class Commander) (Flag 1)))
)
