def abrir_google(page){
    page.gets("https://www.google.com/")
    print(page.title())
    assert "Google" in page.title()
}