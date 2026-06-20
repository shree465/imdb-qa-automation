from pages.imdb_search_page import IMDBSearchPage

def test_imdb_data_integrity(setup_browser):
    driver = setup_browser
    imdb_page = IMDBSearchPage(driver)
    
    imdb_page.open_page()
    imdb_page.apply_filters_and_search()
    
    # Text Validation Logic
    target_movie = "Off Campus"
    
    print(f"\n[INFO] Checking if '{target_movie}' is displayed on the results page...")
    is_displayed = imdb_page.is_movie_displayed(target_movie)
    
    if is_displayed:
        print(f"\n--- SUCCESS: '{target_movie}' found on screen! ---")
    else:
        print(f"\n--- FAILED: '{target_movie}' is missing! ---")
        
    # Asli PyTest Assertion
    assert is_displayed, f"Bug: The movie '{target_movie}' did not appear in the search results. Check URL: {driver.current_url}"
    