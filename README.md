# **Youtube Transcript Summarizer**
***Objective:*** This is a Search Engine Extension which will make a request to a backend [REST API](https://www.redhat.com/en/topics/api/what-is-a-rest-api) where it will perform NLP and respond with a summarized version of a YouTube transcript.

<img src = "https://user-images.githubusercontent.com/61617780/147524542-598a381c-9cff-49e1-b35b-75b38574b312.png" width="570" height="140">

*Use case Scenario:* YouTube has very large number of videos which has transcripts. Summarization would be especially helpful in the cases where videos are longer in length and different parts might have varying importance. In this sense, Summarization of the video might be useful in saving the viewer’s time. It will help in improving user productivity since they will focus only on the important text spoken in video. 

## :arrow_down_small: Aim
***By our project, we would be building functionality for summarizing those YouTube videos in which captions are added by their owner, to generate a summarized text response through various summarization techniques.***

Our main goal is to save the time of the user who was wasting time on finding useful information about the topic which they are interested in and to save them from click baited videos.
The client could be accessing this API from anywhere (say a Chrome extension) which will request our server, so that we would make summarizer accessible in many ways, and reducing user’s time and effort to get the text summary on the basis of their request.

* **Language Used** - Python, JavaScript, HTML, CSS
* **Concept Used** - [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP)
* **IDE Used** - VSCode
* **Database** - MySQL

## :arrow_down_small: External Libraries Needed
* The summarization is done by first generating the transcript of the video for which if the video has already transcript then it is used with the help of a python library [youtube-transcript-API](https://pypi.org/project/youtube-transcript-api/).
* [Gensim](https://en.wikipedia.org/wiki/Gensim) is a Python library for topic modelling, document indexing and similarity retrieval with large corpora. Target audience is the natural language processing (NLP) and information retrieval (IR) community.

  #### ***Basic Requirements for extension:***
  **Extensions** are small software programs that customize the browsing experience. They enable users to tailor Chrome functionality and behavior to individual preferences. They are built on web technologies such as HTML, CSS and JavaScript.

  * Create a chrome extension application directory containing essential files required as mentioned below:
  <img src = "https://user-images.githubusercontent.com/61617780/147526043-877c6a5a-7c52-4dfb-b10b-10e343e3ebdf.png" width="490" height="150">
  
  * The below diagram indicates the brief role of each of the files for building a chrome extension.
  <img src = "https://user-images.githubusercontent.com/61617780/147526346-b27ecd7c-6a44-4b89-8b7c-f50c95800666.png" width="300" height="250">

### :arrow_down_small: System Architecture
<img src = "https://user-images.githubusercontent.com/61617780/147527817-fa5f94b0-fb7f-49cf-bc22-b15876508d05.png" width="400" height="300">

## 💻: User Interface
> <img src = "https://user-images.githubusercontent.com/61617780/147527137-aed9676a-b376-4c67-876b-b344431b966b.png" width="300" height="200">

The image below shows the front-end of the extension of the summarizer.
> <img src = "https://user-images.githubusercontent.com/61617780/147526800-5745cff7-16f9-4d78-9c1b-22d209e12914.png" width="500" height="250">
> <img src = "https://user-images.githubusercontent.com/61617780/147527016-8018912a-ba75-47e3-baf3-9afe7c0a649a.png" width="500" height="250">

## :speech_balloon: Future Look 
* We'll be working on this summarizer so that it can generate summary of the videos which do not have pre enabled subtitles.

## :black_nib: References
***Websites:*** 
* https://stackoverflow.com/ 
* https://www.javatpoint.com/
* https://medium.com/coding-in-simple-english/how-to-create-chrome-extension-7dd396e884ef
* https://www.crio.do/projects/python-youtube-transcript/
