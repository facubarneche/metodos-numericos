var myFunc = function (x) { return ((x * 3 / 1.2 + 12) - 10) * 4.3333; };
var biseccion = function (a, b, e) {
    var p;
    while (b - a >= e) {
        p = (a + b) / 2;
        console.log(p);
        if (myFunc(p) === 0) {
            console.log('Se encontró la raiz exacta: ', p);
            return p;
        }
        else if (myFunc(p) > 0) {
            b = p;
        }
        else {
            a = p;
        }
    }
    console.log(p, ' (Raiz aproximada)');
};
biseccion(-100, 100, 0.01);
