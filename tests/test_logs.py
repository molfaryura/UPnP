import pytest


@pytest.mark.order("last")
def test_check_logs_error(log, file_path="logs/test_log.log"):
    """Test to check for errors in the log file."""

    log.info("Testing log file for ERROR entries...")

    try:
        with open(file_path, "r", encoding="utf-8") as log_file:
            logs = log_file.readlines()

            error_logs = [line for line in logs if "ERROR" in str(line.split(" - ")[2])]
            log.info(
                "Error logs found:\n" + "".join(error_logs)
                if error_logs
                else "No ERROR logs found."
            )

        assert not error_logs, f"Found ERROR logs:\n{''.join(error_logs)}"

    except FileNotFoundError:
        pytest.fail(f"Log file not found: {file_path}")
