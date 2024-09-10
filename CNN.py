import numpy as np


# Helper functions
def relu(x):
    return np.maximum(0, x)


def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)


def convolution(image, kernel, stride=1, padding=0):
    image_h, image_w = image.shape
    kernel_h, kernel_w = kernel.shape

    output_h = int((image_h - kernel_h + 2 * padding) / stride) + 1
    output_w = int((image_w - kernel_w + 2 * padding) / stride) + 1

    padded_image = np.pad(image, ((padding, padding), (padding, padding)))

    output = np.zeros((output_h, output_w))

    for y in range(0, output_h):
        for x in range(0, output_w):
            region = padded_image[y * stride: y * stride + kernel_h, x * stride: x * stride + kernel_w]
            output[y, x] = np.sum(region * kernel)

    return output


def max_pooling(image, size=2, stride=2):
    output_h = int((image.shape[0] - size) / stride) + 1
    output_w = int((image.shape[1] - size) / stride) + 1
    output = np.zeros((output_h, output_w))

    for y in range(0, output_h):
        for x in range(0, output_w):
            region = image[y * stride: y * stride + size, x * stride: x * stride + size]
            output[y, x] = np.max(region)

    return output


def flatten(x):
    return x.flatten()


def fully_connected(x, weights, bias):
    return np.dot(weights, x) + bias


# CNN Model
class SimpleCNN:
    def __init__(self):
        # Initialize filters (kernel)
        self.conv_kernel = np.random.randn(3, 3)  # 3x3 filter

        # Fully connected layer parameters
        self.fc_weights = np.random.randn(10, 13 * 13)  # For a 13x13 image after pooling
        self.fc_bias = np.random.randn(10)

    def forward(self, x):
        # Convolutional Layer
        conv_output = convolution(x, self.conv_kernel, stride=1, padding=0)
        conv_output = relu(conv_output)  # Apply ReLU activation

        # Max Pooling Layer
        pooled_output = max_pooling(conv_output, size=2, stride=2)

        # Flatten Layer
        flat_output = flatten(pooled_output)

        # Fully Connected Layer
        fc_output = fully_connected(flat_output, self.fc_weights, self.fc_bias)

        # Output softmax
        output = softmax(fc_output)

        return output


# Test the CNN model
if __name__ == "__main__":
    # Sample 28x28 input image (like from MNIST dataset)
    sample_image = np.random.randn(28, 28)

    # Initialize CNN
    cnn = SimpleCNN()

    # Forward pass
    output = cnn.forward(sample_image)

    print("CNN Output:\n", output)
