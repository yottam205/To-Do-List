import pytest
from project import add_task, edit_tasks, done_tasks, end_or_menu

def main():
    test_add_task()
    test_edit_tasks()
    test_done_tasks()
    end_or_menu()

def test_add_task(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "wash the dishes")
    tasks, count = add_task([], 0)
    assert tasks == [{"No.": 1, "Task": "wash the dishes", "Status": "Not Done"}] and count == 1

def test_edit_tasks(monkeypatch):
    inputs = iter(["1", "do the laundry", "n", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tasks = [{"No.": 1, "Task": "wash the dishes", "Status": "Not Done"}]
    count = 1
    with pytest.raises(SystemExit) as excinfo:
        edit_tasks(tasks, count)
    assert str(excinfo.value) == "Thanks a lot, Byeeeeeeeee"


def test_done_tasks(monkeypatch):
    inputs = iter(["1", "9"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    tasks = [{"No.": 1, "Task": "do the laundry", "Status": "Not Done"}]
    new_tasks, count = done_tasks(tasks, 1)
    assert new_tasks == [{"No.": 1, "Task": "do the laundry", "Status": "Done"}] and count == 1

def test_end_or_menu(monkeypatch):
    inputs = iter(["5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit) as excinfo:
        end_or_menu()
    assert str(excinfo.value) == "Thanks a lot, Byeeeeeeeee"


if __name__ == "__main__":
    main()