from ddgs import DDGS

def get_live_moodboard(query, num_images=25):
    try:
        with DDGS() as ddgs:
            results = ddgs.images(
                query,
                region="wt-wt",
                safesearch="on",
                size="Medium",
                type_image="photo",
                max_results=num_images
            )
            return [res['image'] for res in results[:num_images]]
    except Exception as e:
        print(f"Scraping error: {e}")
        return []