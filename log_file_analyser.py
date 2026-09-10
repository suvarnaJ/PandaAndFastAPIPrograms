import pandas as pd

# -----------------------------------------
# Create application.log
# -----------------------------------------

log_entries = [
    "2026-09-10 09:00:01 INFO - Application started",
    "2026-09-10 09:01:12 INFO - Configuration loaded successfully",
    "2026-09-10 09:02:15 INFO - Database connection established",
    "2026-09-10 09:03:21 INFO - User login successful",
    "2026-09-10 09:04:33 WARNING - Memory usage high",
    "2026-09-10 09:05:10 INFO - Cache initialized",
    "2026-09-10 09:06:44 ERROR - Database connection failed",
    "2026-09-10 09:07:02 INFO - Retry successful",
    "2026-09-10 09:08:19 INFO - User profile loaded",
    "2026-09-10 09:09:25 WARNING - Slow response detected",
    "2026-09-10 09:10:31 INFO - Request processed successfully",
    "2026-09-10 09:11:47 ERROR - Payment service unavailable",
    "2026-09-10 09:12:05 INFO - Payment retry initiated",
    "2026-09-10 09:13:16 INFO - Payment completed",
    "2026-09-10 09:14:28 WARNING - CPU usage high",
    "2026-09-10 09:15:40 INFO - Scheduled job started",
    "2026-09-10 09:16:55 ERROR - File processing failed",
    "2026-09-10 09:17:12 INFO - File processing retry successful",
    "2026-09-10 09:18:27 INFO - Scheduled job completed",
    "2026-09-10 09:19:39 WARNING - Disk space running low",
    "2026-09-10 09:20:41 INFO - User logout successful",
    "2026-09-10 09:21:52 ERROR - Authentication service timeout",
    "2026-09-10 09:22:14 INFO - Authentication retry successful",
    "2026-09-10 09:23:29 INFO - New user registered",
    "2026-09-10 09:24:35 WARNING - API rate limit approaching",
    "2026-09-10 09:25:48 INFO - API request completed",
    "2026-09-10 09:26:51 ERROR - Email service failed",
    "2026-09-10 09:27:13 INFO - Email retry successful",
    "2026-09-10 09:28:26 INFO - Report generated",
    "2026-09-10 09:29:38 WARNING - Queue size is high",
    "2026-09-10 09:30:44 INFO - Queue processing completed",
    "2026-09-10 09:31:57 ERROR - External service unavailable",
    "2026-09-10 09:32:20 INFO - External service recovered",
    "2026-09-10 09:33:34 INFO - Backup started",
    "2026-09-10 09:34:49 WARNING - Backup taking longer than expected",
    "2026-09-10 09:35:55 INFO - Backup completed successfully"
]

# Write log entries to application.log
with open("application.log", "w", encoding="utf-8") as file:
    for entry in log_entries:
        file.write(entry + "\n")


# -----------------------------------------
# Read entire log file
# -----------------------------------------

with open("application.log", "r", encoding="utf-8") as file:
    logs = file.readlines()


# -----------------------------------------
# Count total log entries
# -----------------------------------------

total_entries = len(logs)

print("========== LOG ANALYSER ==========")

print("Total log entries:", total_entries)


# -----------------------------------------
# Count ERROR, WARNING and INFO
# -----------------------------------------

error_entries = []

warning_entries = []

info_entries = []


for log in logs:

    if " ERROR - " in log:
        error_entries.append(log.strip())

    elif " WARNING - " in log:
        warning_entries.append(log.strip())

    elif " INFO - " in log:
        info_entries.append(log.strip())


print("ERROR count:", len(error_entries))

print("WARNING count:", len(warning_entries))

print("INFO count:", len(info_entries))


# -----------------------------------------
# Create errors.txt
# -----------------------------------------

with open("errors.txt", "w", encoding="utf-8") as file:

    for error in error_entries:
        file.write(error + "\n")


# -----------------------------------------
# Create warnings.txt
# -----------------------------------------

with open("warnings.txt", "w", encoding="utf-8") as file:

    for warning in warning_entries:
        file.write(warning + "\n")


print("\nerrors.txt created successfully.")

print("warnings.txt created successfully.")


# -----------------------------------------
# BONUS - Pandas Frequency Analysis
# -----------------------------------------

df = pd.DataFrame({
    "log_entry": [log.strip() for log in logs]
})


# Extract log level

df["level"] = df["log_entry"].str.extract(
    r" (INFO|WARNING|ERROR) - "
)


print("\n========== PANDAS FREQUENCY ANALYSIS ==========")

frequency = df["level"].value_counts()

print(frequency)


# Save frequency report

frequency.to_csv(
    "log_frequency_report.csv",
    header=["frequency"]
)

print("\nlog_frequency_report.csv created successfully.")