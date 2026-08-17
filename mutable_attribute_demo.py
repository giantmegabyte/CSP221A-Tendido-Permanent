def demonstrate_mutable_class_attribute_trap():
    print("=== Mutable Class Attribute Trap Demo ===")

    class BuggyRobotLog:
        tasks_done = []  # BUG: 

        def __init__(self, name):
            self.name = name

        def log_task(self, task):
            self.tasks_done.append(task)  

    buggy_a = BuggyRobotLog("A")
    buggy_b = BuggyRobotLog("B")
    buggy_a.log_task("sweep floor")
    buggy_b.log_task("fly survey")

    print("Buggy version — both instances share one list:")
    print(f"  buggy_a.tasks_done = {buggy_a.tasks_done}")
    print(f"  buggy_b.tasks_done = {buggy_b.tasks_done}")
    print(f"  same object? {buggy_a.tasks_done is buggy_b.tasks_done}")

    class FixedRobotLog:
        def __init__(self, name):
            self.name = name
            self.tasks_done = []  

        def log_task(self, task):
            self.tasks_done.append(task)

    fixed_a = FixedRobotLog("A")
    fixed_b = FixedRobotLog("B")
    fixed_a.log_task("sweep floor")
    fixed_b.log_task("fly survey")

    print("\nFixed version — each instance has its own list:")
    print(f"  fixed_a.tasks_done = {fixed_a.tasks_done}")
    print(f"  fixed_b.tasks_done = {fixed_b.tasks_done}")
    print(f"  same object? {fixed_a.tasks_done is fixed_b.tasks_done}")


if __name__ == "__main__":
    demonstrate_mutable_class_attribute_trap()