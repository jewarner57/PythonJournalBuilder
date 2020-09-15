import datetime
from pathlib import Path
import calendar

now = datetime.datetime.now()
journalStart = now - datetime.timedelta(days=now.weekday())
journalEnd = journalStart + datetime.timedelta(days=4)

print(journalStart.strftime("%m/%d/%Y"))
print(journalEnd.strftime("%m/%d/%Y"))

newFile = open(
    str(journalStart.month)
    + ":"
    + str(journalStart.day)
    + "-"
    + str(journalEnd.month)
    + ":"
    + str(journalEnd.day)
    + " Journal.md",
    "w",
)

newFile.write(
    "## "
    + str(journalStart.year)
    + " Daily Learning Journal : "
    + str(journalStart.month)
    + "/"
    + str(journalStart.day)
    + "-"
    + str(journalEnd.month)
    + "/"
    + str(journalEnd.day)
)


def writeDay(journalDate):
    newFile.write("\n* * *")
    newFile.write(
        "\n### "
        + str(calendar.day_name[journalDate.weekday()])
        + " "
        + str(journalDate.month)
        + "/"
        + str(journalDate.day)
    )
    newFile.write("\n* * *")
    newFile.write("\n#### What did you do today?")
    newFile.write("\n* _")
    newFile.write("\n#### What did learn today?")
    newFile.write("\n* _")
    newFile.write("\n#### 2-3 Questions you still have")
    newFile.write("\n* _")


counter = 0
while counter < 5:
    writeDay(journalStart + datetime.timedelta(days=counter))
    counter += 1


newFile.close()
print("...Done")
