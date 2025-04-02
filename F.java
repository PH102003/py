public class F {

public static void main(String[] args) {
    int mat[][] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    //nesse caso aqui, tamo pegando a segunda sublista (lembrar que a máquina conta como '0,1,2', ou seja, 3)
    for(int i = 1; i<mat.length; i++){
     if(i == 1){
        for(int j = 0; j < mat[1].length; j++){
            System.out.print(mat[i][j] + " ");
        }
     }   
    }
/*for (int l = 0; l < mat.length; l++) {
        int[] row = mat[l];  // Access the current row
        System.out.println("Row index: " + l + ", Row: " + java.util.Arrays.toString(row));
    }    
}
     */    
    
}
}


