after executing the python code the result were : 

Epoch 0 | Loss: 0.7917

Epoch 100 | Loss: 0.3568

Epoch 200 | Loss: 0.1798

Epoch 300 | Loss: 0.1078

Epoch 400 | Loss: 0.0686

Epoch 500 | Loss: 0.0455

Epoch 600 | Loss: 0.0316

Epoch 700 | Loss: 0.0229

Epoch 800 | Loss: 0.0174

Epoch 900 | Loss: 0.0137




Predictions:
  Student 1: 1.00 → PASS test  
  Student 2: 0.01 → FAIL test 



## the predictions were made over these two  sample of students:
          torch.tensor([[5.0, 8.0],   # studied a lot, slept well
                         [1.0, 3.0]])  # barely studied, barely slept
## and they were just right as expected 

## the  neural network visualization looks like this : 

<img width="1558" height="1320" alt="image" src="https://github.com/user-attachments/assets/707b1adb-d8f5-4862-ad43-120df1772d0c" />

  
