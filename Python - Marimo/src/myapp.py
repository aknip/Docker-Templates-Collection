import marimo

__generated_with = "0.10.17"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Marimo

        - Build and edit an app in Marimo
        - Re-use the app in a webservice, worker or app: Use `service.py` (in the same directory)
        - Test this via the terminal inside of Marimo (left bottom): `python src/service.py`

        """
    )
    return


@app.cell
def _():
    print('App running...')
    return


@app.cell
def _():
    def calculate(var1):
        print('calculating...')
        return(var1*10)
    return (calculate,)


@app.cell
def _(calculate):
    result = calculate(4711)
    print('Result: ' + str(result))
    return (result,)


if __name__ == "__main__":
    app.run()
