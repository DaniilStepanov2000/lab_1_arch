from flask import Flask, render_template, request, redirect
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session

from database import Hospital, engine, LogisticCompany, Doctors, University

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("base.html")


@app.route("/hospitals", methods=["GET"])
def hospitals():
    with Session(engine) as session:
        stmt = select(Hospital)
        hospitals = session.scalars(stmt).all()
    return render_template("data.html", info=hospitals)


@app.route("/add_hospitals", methods=["GET", "POST"])
def add_hospitals():
    if request.method == "POST":
        data = request.form.to_dict()
        with Session(engine) as session:
            stmt = insert(Hospital).values(
                address=data.get("h_address"),
                country=data.get("h_country"),
                city=data.get("h_city"),
                count_employees=int(data.get("h_count_employees")),
                )
            session.execute(stmt)
            session.commit()
            return redirect("hospitals")
    return render_template("add_hospitals.html")


@app.route("/delete_hospitals", methods=["GET", "POST"])
def delete_hospitals():
    if request.method == "POST":
        data = request.form.to_dict()
        with Session(engine) as session:
            stmt = delete(Hospital).where(
                Hospital.id == int(data.get("h_id")),
            )
            session.execute(stmt)
            session.commit()
            return redirect("hospitals")
    return render_template("delete_hospitals.html")


@app.route("/update_hospitals", methods=["GET", "POST"])
def update_hospitals():
    if request.method == "POST":
        data = request.form.to_dict()
        update_values = {}
        for key, value in data.items():
            if not value:
                continue
            else:
                update_values[key] = value

        with Session(engine) as session:
            stmt = update(Hospital).where(
                Hospital.id == int(data.get("id")),
            ).values(
                   update_values
            )
            session.execute(stmt)
            session.commit()
            return redirect("hospitals")
    return render_template("update_hospitals.html")


@app.route("/logistic_companies", methods=["GET"])
def logistic_companies():
    with Session(engine) as session:
        stmt = select(LogisticCompany)
        logistic_companies = session.scalars(stmt).all()
    return render_template("logistic_companies.html", info=logistic_companies)


@app.route("/doctors", methods=["GET"])
def doctors():
    with Session(engine) as session:
        stmt = select(Doctors)
        doctors = session.scalars(stmt).all()
    return render_template("doctors.html", info=doctors)


@app.route("/patients", methods=["GET"])
def patients():
    with Session(engine) as session:
        stmt = select(Doctors)
        patients = session.scalars(stmt).all()
    return render_template("patients.html", info=patients)


@app.route("/universities", methods=["GET"])
def universities():
    with Session(engine) as session:
        stmt = select(University)
        patients = session.scalars(stmt).all()
    return render_template("university.html", info=patients)


if __name__ == "__main__":
    app.run()
