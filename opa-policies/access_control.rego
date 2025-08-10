package nist.access_control

deny[msg] if {
    not input.access_control.role_based
    msg := "RBAC is not implemented."
}
