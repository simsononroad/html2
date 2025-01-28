import pytest
from bs4 import BeautifulSoup

# Segédfüggvény a HTML tartalom betöltéséhez
def load_html():
    with open("fuzfa.html", "r", encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser")

# 1. feladat: Ellenőrizd a nyelv beállítását
def test_language_setting():
    soup = load_html()
    assert soup.html.get("lang") == "hu", "A nyelv beállítása nem magyar."

# 2. feladat: Ellenőrizd a böngészőfülen megjelenő címet
def test_browser_tab_title():
    soup = load_html()
    assert soup.title.text == "Két fűzfa", "A böngészőfülön nem a 'Két fűzfa' felirat jelenik meg."

# 3. feladat: Ellenőrizd a főcímet
def test_main_heading():
    soup = load_html()
    h1 = soup.find("h1")
    assert h1 is not None, "Nem található egyes szintű főcím (h1)."
    assert h1.text == "Két fűzfa", "A főcím tartalma nem 'Két fűzfa'."

# 4. feladat: Ellenőrizd a bekezdések számát
def test_paragraph_count():
    soup = load_html()
    paragraphs = soup.find_all("p")
    assert len(paragraphs) == 3, "Nem pontosan 3 bekezdés található."

# 5. feladat: Ellenőrizd a bekezdések alcímeit
def test_subheadings():
    soup = load_html()
    h2_elements = soup.find_all("h2")
    assert len(h2_elements) == 3, "Nem pontosan 3 darab kettes szintű fejezetcím található."

    expected_h2_texts = [
        "1 bekezdés: A jövedelem",
        "2 bekezdés: A kollégium",
        "3 bekezdés: Az orákulum"
    ]
    for i, h2 in enumerate(h2_elements):
        assert h2.text == expected_h2_texts[i], f"A {i+1}. alcím szövege nem megfelelő."

# 6. feladat: Ellenőrizd a harmadik bekezdésben a kiemelt szöveget
def test_emphasized_text_in_third_paragraph():
    soup = load_html()
    paragraphs = soup.find_all("p")
    third_paragraph = paragraphs[2]
    em_element = third_paragraph.find("em")
    assert em_element is not None, "A harmadik bekezdésben nem található kiemelt szöveg."
    assert em_element.text == "bevette magát", "A kiemelt szöveg tartalma nem 'bevette magát'."
    assert em_element.get('style') == "font-style:normal; font-weight:bold;", "A kiemelés stílusa nem megfelelő"
    

# 7. feladat: Ellenőrizd a második bekezdésben a dőlt szöveget
def test_italic_text_in_second_paragraph():
    soup = load_html()
    paragraphs = soup.find_all("p")
    second_paragraph = paragraphs[1]
    i_element = second_paragraph.find("i")
    assert i_element is not None, "A második bekezdésben nem található dőlt szöveg."
    assert i_element.text == "időszerint", "A dőlt szöveg tartalma nem 'időszerint'."

# 8. feladat: Ellenőrizd a kommentet
def test_html_comment():
    soup = load_html()
    comment = soup.find(string=lambda text: isinstance(text, str) and "Vizsgafeladat" in text)
    assert comment is not None, "Nem található a 'Vizsgafeladat' szöveg a megjegyzésben."


if __name__ == "__main__":
    pytest.main()