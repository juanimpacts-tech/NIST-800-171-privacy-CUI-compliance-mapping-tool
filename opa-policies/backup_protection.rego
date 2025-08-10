package nist.backup_protection

deny[msg] if {
    not input.backup_protection.encrypted
    msg := "Backups are not encrypted."
}

deny[msg] if {
    input.backup_protection.encrypted
    not input.backup_protection.fips_compliant
    msg := "Backups are encrypted but not FIPS 140-2 compliant."
}
