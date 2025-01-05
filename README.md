# Anonymous Ring Signature-Based Age Verification

A Python implementation of ring signatures for anonymous age verification. Inspired by [Australia's newly implemented age verification laws](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd2425/25bd39), this project enables proving age eligibility without revealing personal identity. It demonstrates key cryptographic concepts like anonymity and group-based verification.


## Ring Signatures
*Notes from [NIST - Privacy-Enhancing Cryptography](https://csrc.nist.gov/projects/pec/pec-tools)*

A group or a ring signature (here jointly denoted as GRS, though having relevant distinctions), allow a party to sign a message m on behalf of a group GG of possible signatories. The signature can be verified as having been produced by a member of the group, without revealing who.

![<img>(https://csrc.nist.gov/csrc/media/Projects/pec/pec-tools-figs/pec-tool-GRS.jpg)</img>](https://csrc.nist.gov/csrc/media/Projects/pec/pec-tools-figs/pec-tool-GRS.jpg)