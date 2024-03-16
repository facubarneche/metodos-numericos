const myFunc = (x: number) => ((x * 3 / 1.2 +12 ) - 10) * 4.3333

const biseccion = (a: number, b: number, e: number) => {
   let p!: number;

   while(b - a >= e){
      p = (a + b) / 2;
      console.log(p)
      if(myFunc(p) === 0){
         console.log('Se encontró la raiz exacta: ', p)
         return p
      }else if(myFunc(p) > 0){
         b = p;
      }else{
         a = p;
      }
   }
   console.log(p, ' (Raiz aproximada)')
}

biseccion(-100, 100, 0.01)