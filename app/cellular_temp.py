from copy import copy
def get_J_and_C(C_dict, D, h, d_t, width, height):

    C_list = []
    C = []
    index = 0
    for k, v in C_dict.items():

        if (index+1)%4 == 0:
            C_list.append(v)
            if len(C_list) == height:
                C.append(C_list)
                C_list = []
        index += 1

    J = 0
    print()
    for i in range(width):
        for j in range(height):

            if i == 0:
                if j == 0:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ((- 2*C[i][j] + C[i+1][j])/h**2 + (- 2*C[i][j] + C[i][j+1])/h**2 )*d_t

                if j == height-1:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ((- 2*C[i][j] + C[i+1][j])/h**2 + (C[i][j-1] - 2*C[i][j])/h**2 )*d_t

                else:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ((- 2*C[i][j] + C[i+1][j])/h**2 + (C[i][j-1] - 2*C[i][j] + C[i][j+1])/h**2 )*d_t


            elif i == width-1:
                
                if j == 0:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j])/h**2 + (- 2*C[i][j] + C[i][j+1])/h**2 )*d_t

                if j == height-1:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j])/h**2 + (C[i][j-1] - 2*C[i][j])/h**2 )*d_t

                else:
                    C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j])/h**2 + (C[i][j-1] - 2*C[i][j] + C[i][j+1])/h**2 )*d_t

            elif j == 0:
                C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j] + C[i+1][j]) / h**2 + (- 2*C[i][j] + C[i][j+1]) / h**2 )*d_t

            elif j == height-1:
                C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j] + C[i+1][j]) / h**2 + (C[i][j-1] - 2*C[i][j]) / h**2 )*d_t

            else:
                C_dict[str((width*i+j)*4+3)] = C[i][j] + D * ( (C[i-1][j] - 2*C[i][j] + C[i+1][j]) / h**2 + (C[i][j-1] - 2*C[i][j] + C[i][j+1]) / h**2 )*d_t

            J += C_dict[str((width*i+j)*4+3)]

    return J, C_dict
