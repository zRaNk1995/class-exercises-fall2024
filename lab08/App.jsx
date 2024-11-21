  const carouselStyles = {
        "width": "640px", 
        "border": "solid 1px #000", 
        "margin": "auto"
    };
    const albums = [
        {
           "id": "6BzxX6zkDsYKFJ04ziU5xQ",
           "name": "COWBOY CARTER",
           "image_url": "https://i.scdn.co/image/ab67616d0000b2731572698fff8a1db257a53599",
           "spotify_url": "https://open.spotify.com/album/6BzxX6zkDsYKFJ04ziU5xQ"
        },
        {
           "id": "2UJwKSBUz6rtW4QLK74kQu",
           "name": "BEYONCÉ [Platinum Edition]",
           "image_url": "https://i.scdn.co/image/ab67616d0000b2730d1d6e9325275f104f8e33f3",
           "spotify_url": "https://open.spotify.com/album/2UJwKSBUz6rtW4QLK74kQu"
        }
        ...
     ];

    function albumToJSX(albumJSON) {
        return (
            <div key={albumJSON.id}>
                <img src={albumJSON.image_url} />
                <h3>{albumJSON.name}</h3>
            </div>
        )
    }

    return (
        <div style={carouselStyles}>
            <Carousel dotPosition="top">
                { 
                    albums.map(albumToJSX)
                }
            </Carousel>
        </div>
    );




