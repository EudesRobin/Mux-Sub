FROM python:3.5
MAINTAINER Benoit Brayer <https://github.com/M0dM>

# Dependencies 
RUN wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | apt-key add -
RUN echo 'deb http://mkvtoolnix.download/debian/jessie/ ./' >> /etc/apt/sources.list.d/mkvtoolnix.list
RUN apt-get update && apt-get -y install mkvtoolnix --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Prepare directories
RUN mkdir -p /usr/src/mux-mkv_srt/source

# Copy script & entypoint to app directory
COPY mux.py /usr/src/mux-mkv_srt/mux.py
COPY entrypoint.sh /usr/src/mux-mkv_srt/entrypoint.sh
RUN chmod +x /usr/src/mux-mkv_srt/mux.py /usr/src/mux-mkv_srt/entrypoint.sh

# Volume will receive the video & subtitle files
VOLUME ["/usr/src/mux-mkv_srt/source"]

# Entrypoint workdir
WORKDIR /usr/src/mux-mkv_srt

ENTRYPOINT ["/usr/src/mux-mkv_srt/entrypoint.sh"]
