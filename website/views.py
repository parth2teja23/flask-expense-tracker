from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Expense, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        description = request.form.get("description")
        amount = request.form.get("amount")
        category = request.form.get("category")

        if not description or not amount or not category:
            flash("All fields are required!", category="error")
        else:
            new_expense = Expense(
                description=description,
                amount=float(amount),
                category=category,
                user_id=current_user.id
            )
            db.session.add(new_expense)
            db.session.commit()
            flash("Expense added successfully!", category="success")

    return render_template("home.html", user=current_user)

@views.route("/edit-expense/<int:id>", methods=["POST"])
@login_required
def edit_expense(id):
    expense = Expense.query.get(id)
    if expense and expense.user_id == current_user.id:
        expense.description = request.form.get("description")
        expense.amount = float(request.form.get("amount"))
        expense.category = request.form.get("category")
        db.session.commit()
        flash("Expense updated successfully!", category="success")
    else:
        flash("Unauthorized action!", category="error")
    return redirect(url_for("views.home"))

@views.route("/delete-expense/<int:id>", methods=["POST"])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense and expense.user_id == current_user.id:
        db.session.delete(expense)
        db.session.commit()
        flash("Expense deleted successfully!", category="success")
    else:
        flash("Unauthorized action!", category="error")
    return redirect(url_for("views.home"))
