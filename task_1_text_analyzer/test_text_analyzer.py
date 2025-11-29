from text_analyzer import analyze_text

def test_sample():
    s = "The quick brown fox jumps over the lazy dog the fox"
    out = analyze_text(s)
    assert out["word_count"] == 11  # Changed from 10 to 11
    # average length: lengths = [3,5,5,3,5,4,3,4,3,3,3] sum=41 /11 = 3.727 -> 3.73
    assert abs(out["average_word_length"] - 3.73) < 1e-9  # Changed from 3.80 to 3.73
    assert set(out["longest_words"]) == {"brown", "jumps", "quick"}
    assert out["word_frequency"]["the"] == 3
    assert out["word_frequency"]["fox"] == 2

def test_empty():
    out = analyze_text("")
    assert out["word_count"] == 0
    assert out["average_word_length"] == 0.0
    assert out["longest_words"] == []
    assert out["word_frequency"] == {}

def test_punctuation():
    out = analyze_text("Hello, world! Test...")
    assert out["word_count"] == 3
    assert set(out["longest_words"]) == {"hello", "world"}
    assert out["word_frequency"]["hello"] == 1
    assert out["word_frequency"]["world"] == 1
    assert out["word_frequency"]["test"] == 1

def test_single_word():
    out = analyze_text("Hello")
    assert out["word_count"] == 1
    assert out["average_word_length"] == 5.0
    assert out["longest_words"] == ["hello"]
    assert out["word_frequency"]["hello"] == 1