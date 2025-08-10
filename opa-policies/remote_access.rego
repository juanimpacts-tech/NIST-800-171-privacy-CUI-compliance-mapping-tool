package nist.remote_access

deny[msg] if {
    not input.remote_access.enabled
    msg := "Remote access is disabled."
}

deny[msg] if {
    input.remote_access.enabled
    not input.remote_access.mfa
    msg := "MFA is missing for remote access."
}

