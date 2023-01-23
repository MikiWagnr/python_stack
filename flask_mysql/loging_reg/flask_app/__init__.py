from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "You are my sadness and my hope. But mostly, you're my love"

bcrypt = Bcrypt(app)