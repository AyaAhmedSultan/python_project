import hashlib
from db import connect

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hash_password(password)))
        conn.commit()
        print("✅ Registered successfully.")
    except Exception as e:
        print("❌ Registration failed:", e)
    finally:
        cur.close()
        conn.close()

def login_user(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, hash_password(password)))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user[0] if user else None

def apply_loan(user_id, amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO loans (user_id, amount, balance) VALUES (%s, %s, %s)", (user_id, amount, amount))
    conn.commit()
    cur.close()
    conn.close()
    print("💰 Loan applied successfully.")

def make_payment(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, balance FROM loans WHERE user_id = %s", (user_id,))
    loans = cur.fetchall()
    if not loans:
        print("⚠️ No active loans.")
        return
    print("\nYour Loans:")
    for idx, (loan_id, balance) in enumerate(loans):
        print(f"{idx+1}. Loan ID: {loan_id}, Balance: ${balance:.2f}")

    try:
        choice = int(input("Choose loan number to pay: ")) - 1
        loan_id, current_balance = loans[choice]
        amount = float(input("Enter payment amount: "))
        if amount > current_balance:
            print("❌ Payment exceeds loan balance.")
            return

        cur.execute("UPDATE loans SET balance = balance - %s WHERE id = %s", (amount, loan_id))
        cur.execute("INSERT INTO payments (loan_id, amount) VALUES (%s, %s)", (loan_id, amount))
        conn.commit()
        print("✅ Payment successful.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        conn.close()

def check_balance(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, balance FROM loans WHERE user_id = %s", (user_id,))
    loans = cur.fetchall()
    if not loans:
        print("📭 No loans found.")
    else:
        print("\n💼 Loan Balances:")
        for loan_id, balance in loans:
            print(f"Loan ID: {loan_id}, Balance: ${balance:.2f}")
    cur.close()
    conn.close()

def view_payment_history(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM loans WHERE user_id = %s", (user_id,))
    loan_ids = [row[0] for row in cur.fetchall()]
    if not loan_ids:
        print("📭 No loans found.")
        return

    print("\n📄 Payment History:")
    for loan_id in loan_ids:
        cur.execute("SELECT amount, paid_at FROM payments WHERE loan_id = %s", (loan_id,))
        payments = cur.fetchall()
        if payments:
            print(f"\nLoan ID {loan_id}:")
            for amount, paid_at in payments:
                print(f" - ${amount:.2f} on {paid_at}")
        else:
            print(f"\nLoan ID {loan_id}: No payments made.")
    cur.close()
    conn.close()
