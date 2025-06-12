

# Algorand Smart Contracts – Beginner Examples

This repository contains a collection of beginner-friendly smart contracts written in [Algopy](https://github.com/algorandfoundation/algopy), demonstrating common patterns and functionalities on the Algorand blockchain using ARC-4 compliant syntax.

---

## 1. 🔐 `Creator Only` – Authorized Caller Check

**Purpose**: Only allow the creator of the contract to call certain methods.

```python
assert Txn.sender == Global.creator_address
```

**Method**:

* `check()` → Ensures only the creator can execute it, logs a message upon success.
[check the contract here](./projects/beginner-contract/smart_contracts/creator_only/contract.py)
---

## 2. 🧮 `First Person` – One-Time Callable Function

**Purpose**: Allows a method to be called only once by any user.

**Methods**:

* `call()` → Can be called only once. Sets counter from 0 to 1.
* `reset()` → Only the creator can reset the counter back to 0.
[check the contract here](./projects/beginner-contract/smart_contracts/first_person_only/contract.py)
---

## 3. 🔄 `Global Storage` – Track Last Modifier

**Purpose**: Adds increment and decrement capabilities while storing the last address that modified the counter.

**Methods**:

* `increment()` → Increases counter, logs sender.
* `decrement()` → Decreases counter if non-zero, logs sender.
* `get()` → Returns the current counter.
* `get_address()` → Returns the last address that changed the value.
[check the contract here](./projects/beginner-contract/smart_contracts/global_storage/contract.py)
---

## 4. 🗃️ `LocalStorage` – Per-User Local State

**Purpose**: Store, retrieve, and delete a `UInt64` value per account using local state.

**Methods**:

* `set_value(account, value)` → Sets a number in local state.
* `get_value(account)` → Retrieves stored number.
* `clear_value(account)` → Deletes stored number from local state.
[check the contract here](./projects/beginner-contract/smart_contracts/local_storage/contract.py)
Each user must opt-in to store data locally.

---

## 5. 💸 `Token Faucet` – Send Algo from Contract to Caller

**Purpose**: Sends 1 Algo from the contract account to the caller if balance is sufficient.

**Method**:

* `fund()` → Checks contract balance and sends 1 Algo to the caller if sufficient funds exist.
[check the contract here](./projects/beginner-contract/smart_contracts/token_faucet/contract.py)
---

## 6. 📦 `Whitelist Access` – Dynamic Array with BoxMap

**Purpose**: Manages a dynamic list of addresses associated with a string key using Algorand Boxes.

**Methods**:

* `add(name, account)` → Only creator can add an account under a given name. Prevents duplicates.
* `check(name, account)` → Returns `True` if the account exists under the name.
[check the contract here](./projects/beginner-contract/smart_contracts/whitelist_access/contract.py)

📌 This example uses `BoxMap` and `DynamicArray` from Algopy for scalable, on-chain lists.

---

## 🛠️ Setup & Build

Make sure you have:

* [AlgoKit](https://github.com/algorandfoundation/algokit-cli) installed
* Python ≥ 3.10
* Activated your project's virtual environment and installed dependencies

### Build Example:

```bash
algokit project run build
```

### Deploy / Test:

Use `algokit localnet` or `goal` CLI for deploying and interacting with the contracts.

---
