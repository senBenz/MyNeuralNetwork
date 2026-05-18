import torch 
import torch.nn as nn 
import torch.optim as optim 

# x is goin to be our input while the y is going to be the 
#output we want to predict 
# 0 = fail, 1 = pass



X = torch.tensor([
    [1.0, 4.0],   # studied 1h, slept 4h
    [2.0, 5.0],
    [3.0, 6.0],
    [4.0, 7.0],
    [5.0, 8.0],
    [1.0, 3.0],
    [2.0, 3.0],
    [6.0, 8.0],
], dtype=torch.float32)



y = torch.tensor([
    [0.0],  # student 1 failed
    [0.0],
    [1.0],
    [1.0],
    [1.0],
    [0.0],
    [0.0],
    [1.0],], dtype=torch.float32)

model = nn.Sequential(
    nn.Linear(2, 4), 
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)


# after building the model we will
# add the loss function using the Binary Cross ENthropy
# since we are classifying between 2 classes 

# la formule utilisee est [[  loss = -(y × log(pred) + (1-y) × log(1-pred))  ]]
# + the learning rate is set to 0.01 and 
# we are using the Adam optimizer (Adaptive Moment Estimation) which is an adaptive learning rate optimization algorithm 
# that has been designed specifically for training deep neural networks.


loss_function = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


# we will train the model for 1000 epochs

for epoch in range(1000):
    prediction= model(X)
    loss=loss_function(prediction, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 100 == 0:                      
        print(f"Epoch {epoch} | Loss: {loss.item():.4f}")
    
    
    
    

#after trainning the model we will run the tests 
#but before testing we will turn off the gradiant tracking 
#because it consumes memory and we dont need it for testing

with torch.no_grad():
    test = torch.tensor([[5.0, 8.0],   # studied a lot, slept well
                         [1.0, 3.0]])  # studied little, slept little
    
    test_results=model(test)
    
    print("\nPredictions:")
    for i, r in enumerate(test_results):
        prob = r.item()
        label = "PASS test  " if prob > 0.5 else "FAIL test "
        print(f"  Student {i+1}: {prob:.2f} → {label}")
        
        