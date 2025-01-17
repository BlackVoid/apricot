from .ldap_organizational_person import LDAPOrganizationalPerson


class LDAPInetOrgPerson(LDAPOrganizationalPerson):
    """
    A person belonging to an internet/intranet directory service

    OID: 2.16.840.1.113730.3.2.2
    Object class: Structural
    Parent: organizationalPerson
    Schema: rfc2798
    """

    cn: str
    displayName: str  # noqa: N815
    givenName: str  # noqa: N815
    sn: str

    def names(self) -> list[str]:
        return [*super().names(), "inetOrgPerson"]
