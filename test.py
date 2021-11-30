import casbin

e = casbin.Enforcer('casbin-model.conf', 'casbin-policy.csv')

assert e.enforce("james", "project-001", "update-project")

# assert not e.enforce("james", "project-002", "update-project")

# lily can delete any project.
assert e.enforce("lily", None, "delete-project")

# A projects can be viewed by its members.
assert e.enforce(
    {"is_superuser": False, "id": "101"},
    {"name": "XABC", "members": ["101", "102"]},
    "view-project")

# Super user can do anything.
assert e.enforce({"is_superuser": True, "id": "100"}, None, None)
