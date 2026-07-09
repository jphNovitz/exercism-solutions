       IDENTIFICATION DIVISION.
       PROGRAM-ID. LEAP.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
            01 WS-YEAR  PIC 9(4).
            01 WS-RESULT  PIC 9(4).
            01 WS-Q     PIC 9(4).
            01 WS-R4    PIC 9(4).
            01 WS-R100  PIC 9(4).
            01 WS-R400  PIC 9(4).
       PROCEDURE DIVISION.
       LEAP.
           DISPLAY "Year : " WITH NO ADVANCING.
           ACCEPT WS-YEAR.
           DIVIDE WS-YEAR BY 4 GIVING WS-Q REMAINDER WS-R4.
           DIVIDE WS-YEAR BY 100 GIVING WS-Q REMAINDER WS-R100.
           DIVIDE WS-YEAR BY 400 GIVING WS-Q REMAINDER WS-R400.
           IF WS-Q = 0 AND (WS-R100 NOT = 0 OR WS-R400 = 0)
              DISPLAY "LEAP"
           STOP RUN.

         CONTINUE.
       LEAP-EXIT.
         EXIT.
