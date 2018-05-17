Feature: Term frequency and inverse document frequency calculation
  In order to  find the relevance of words in a text
         As a  text analyst
       I want  to know how often the terms appear in the individual files 
               and how seldom over the whole corpus

               
  Scenario: Filtering and counting for a short text
    Given the text to be analyzed is
      """
      § 946 Verbindung mit einem Grundstück
      Wird eine bewegliche Sache mit einem Grundstück dergestalt verbunden, 
      dass sie wesentlicher Bestandteil des Grundstücks wird, so erstreckt 
      sich das Eigentum an dem Grundstück auf diese Sache.
      """
    When search for words to be filtered
    Then we find "an", "auf", "das", "dass", "dem", "des", "diese", "eine"
     And we find "einem", "mit", "sich", "sie", "so", "Wird", "wird"
    When we count the remaining words
    Then we get the following frequencies
       | term           | frequency |
       | "Bestandteil"  |     1     |
       | "bewegliche"   |     1     |
       | "dergestalt"   |     1     |
       | "Eigentum"     |     1     |
       | "erstreckt"    |     1     |
       | "Grundstück"   |     3     |
       | "Grundstücks"  |     1     |
       | "Sache"        |     2     |
       | "Verbindung"   |     1     |
       | "verbunden"    |     1     |
       | "wesentlicher" |     1     |




 # § 433 Vertragstypische Pflichten beim Kaufvertrag
 # (1) Durch den Kaufvertrag wird der Verkäufer einer Sache verpflichtet, dem 
 # Käufer die Sache zu übergeben und das Eigentum an der Sache zu verschaffen. 
 # Der Verkäufer hat dem Käufer die Sache frei von Sach- und Rechtsmängeln zu 
 # verschaffen.
 # (2) Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten Kaufpreis 
 # zu zahlen und die gekaufte Sache abzunehmen.

 # § 964 Vermischung von Bienenschwärmen
 # Ist ein Bienenschwarm in eine fremde besetzte Bienenwohnung eingezogen, 
 # so erstrecken sich das Eigentum und die sonstigen Rechte an den Bienen, 
 # mit denen die Wohnung besetzt war, auf den eingezogenen Schwarm. Das 
 # Eigentum und die sonstigen Rechte an dem eingezogenen Schwarme erlöschen.

 
 # Gesetz über Urheberrecht und verwandte Schutzrechte (Urheberrechtsgesetz)
 # § 5 Amtliche Werke
 # (1) Gesetze, Verordnungen, amtliche Erlasse und Bekanntmachungen sowie 
 # Entscheidungen und amtlich verfaßte Leitsätze zu Entscheidungen genießen
 # keinen urheberrechtlichen Schutz. 
 # (2) Das gleiche gilt für andere amtliche Werke, die im amtlichen Interesse
 # zur allgemeinen Kenntnisnahme veröffentlicht worden sind, mit der Einschränkung,
 # daß die Bestimmungen über Änderungsverbot und Quellenangabe in § 62 Abs. 1 bis 3 
 # und § 63 Abs. 1 und 2 entsprechend anzuwenden sind.
 # (3) Das Urheberrecht an privaten Normwerken wird durch die Absätze 1 und 2 nicht 
 # berührt, wenn Gesetze, Verordnungen, Erlasse oder amtliche Bekanntmachungen auf 
 # sie verweisen, ohne ihren Wortlaut wiederzugeben. In diesem Fall ist der Urheber 
 # verpflichtet, jedem Verleger zu angemessenen Bedingungen ein Recht zur Vervielfältigung
 # und Verbreitung einzuräumen. Ist ein Dritter Inhaber des ausschließlichen Rechts zur 
 # Vervielfältigung und Verbreitung, so ist dieser zur Einräumung des Nutzungsrechts nach
 # Satz 2 verpflichtet.