import tkinter as tk
import calendar
from datetime import datetime

class SimpleCalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calendar")

        # Labels and Entry Fields
        tk.Label(master, text="Enter Date (YYYY-MM-DD):").pack()
        self.entry_date = tk.Entry(master)
        self.entry_date.pack()

        tk.Label(master, text="Enter Event Description:").pack()
        self.entry_event = tk.Entry(master)
        self.entry_event.pack()

        # Buttons
        self.add_button = tk.Button(master, text="Add Event", command=self.add_event)
        self.add_button.pack()

        self.show_button = tk.Button(master, text="Show Month", command=self.show_month)
        self.show_button.pack()

        # Text Output Area
        self.text = tk.Text(master, height=20, width=50)
        self.text.pack()

        self.events = {}  # Dictionary to store events

    def add_event(self):
        """Adds an event to a specific date."""
        date_str = self.entry_date.get().strip()
        event = self.entry_event.get().strip()

        if not date_str or not event:
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', "Error: Date and event description cannot be empty.\n")
            return

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]

            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', f"Event added for {date_str}: {event}\n")

            self.entry_date.delete(0, tk.END)
            self.entry_event.delete(0, tk.END)

        except ValueError:
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', "Error: Invalid date format. Use YYYY-MM-DD.\n")

    def show_month(self):
        """Displays a month calendar and lists events below it."""
        date_str = self.entry_date.get().strip()

        if not date_str:
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', "Error: Please enter a valid date (YYYY-MM-DD) to view a month.\n")
            return

        try:
            year, month = map(int, date_str.split('-')[:2])
            cal = calendar.monthcalendar(year, month)
            output = f"\n{calendar.month_name[month]} {year}\n\n"
            output += "Mon Tue Wed Thu Fri Sat Sun\n"

            for week in cal:
                for day in week:
                    if day == 0:
                        output += "    "
                    else:
                        current_date = datetime(year, month, day).date()
                        if current_date in self.events:
                            output += f"{day:2}* "
                        else:
                            output += f"{day:2}  "
                output += "\n"

            # List the events below the calendar
            output += "\nEvents for this month:\n"
            event_found = False
            for date, events in sorted(self.events.items()):
                if date.year == year and date.month == month:
                    event_found = True
                    output += f"\n{date.strftime('%Y-%m-%d')}:\n"
                    for event in events:
                        output += f" - {event}\n"

            if not event_found:
                output += "No events for this month.\n"

            # Display in text box
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', output)

        except ValueError:
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', "Error: Invalid date format. Use YYYY-MM-DD.\n")


if __name__ == "__main__":
    root = tk.Tk()
    gui = SimpleCalendarGUI(root)
    root.mainloop()
