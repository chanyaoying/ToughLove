import tensorflow as tf
from util import PositionalEncoding
from util import MultiHeadAttentionLayer
from util import create_padding_mask
from util import create_look_ahead_mask
from preprocessing import preprocess_sentence
import pickle

tokenizer_name = 'tokenizer_v0(chatbot.h5).pkl'
model_name = 'chatbot.h5'

with open(tokenizer_name, 'rb') as handle:
    tokenizer = pickle.load(handle)

START_TOKEN, END_TOKEN = [tokenizer.vocab_size], [tokenizer.vocab_size + 1]
VOCAB_SIZE = tokenizer.vocab_size + 2
MAX_LENGTH = 40

def evaluate(sentence):
    sentence = preprocess_sentence(sentence)

    sentence = tf.expand_dims(
        START_TOKEN + tokenizer.encode(sentence) + END_TOKEN, axis=0
    )

    output = tf.expand_dims(START_TOKEN, 0)

    for i in range(MAX_LENGTH):
        predictions = model(inputs=[sentence, output], training=False)

        # select the last word from the seq_len dimension
        predictions = predictions[:, -1:, :]
        predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

        # return the result if the predicted_id is equal to the end token
        if tf.equal(predicted_id, END_TOKEN[0]):
            break

        # concatenated the predicted_id to the output which is given to the decoder
        # as its input.
        output = tf.concat([output, predicted_id], axis=-1)

    return tf.squeeze(output, axis=0)


def predict(sentence):
    prediction = evaluate(sentence)
    predicted_sentence = tokenizer.decode(
        [i for i in prediction if i < tokenizer.vocab_size]
    )
    return predicted_sentence

# load tensorflow model

model = tf.keras.models.load_model(model_name,
    custom_objects={
            "PositionalEncoding": PositionalEncoding,
            "MultiHeadAttentionLayer": MultiHeadAttentionLayer,
        }, compile=False)

