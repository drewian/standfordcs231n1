import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(X.shape[0]):
    curr_class = y[i]
    f = np.dot(X[i, :], W)
    f = np.exp(f)
    f = f / np.sum(f)
    loss -= np.log(f[curr_class])
    ys = np.zeros((W.shape[1], ))
    ys[curr_class] = 1
    dW += np.matmul(X[i, :].reshape(1, 3073).transpose(), (f - ys).reshape(10, 1).transpose())
        
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  dW /= W.shape[0]
  loss /= W.shape[0]
  loss +=  0.5 * reg * np.sum(W ** 2)
  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = np.dot(X, W)
  exp_scores = np.exp(scores)
  normalized = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
  loss = np.sum(-np.log(normalized[range(X.shape[0]), y])) / W.shape[0]
  normalized[range(X.shape[0]), y] -= 1
  dW = np.dot(X.transpose(), normalized) / W.shape[0]
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
