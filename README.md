# Anonymous Ring Signature-Based Age Verification
Inspired by [Australia's newly implemented age verification laws](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd2425/25bd39), this project aims to deliver a proof of concept for a Python-based ring signature scheme for anonymous age verification.


## Ring Signatures
*Notes from [NIST - Privacy-Enhancing Cryptography](https://csrc.nist.gov/projects/pec/pec-tools)*

A ring signature allows a person to sign a message on behalf of a group of possible signatories. The signature can be verified as having been produced by a member of the group, without revealing who the signer is.

![<img>(https://csrc.nist.gov/csrc/media/Projects/pec/pec-tools-figs/pec-tool-GRS.jpg)</img>](https://csrc.nist.gov/csrc/media/Projects/pec/pec-tools-figs/pec-tool-GRS.jpg)