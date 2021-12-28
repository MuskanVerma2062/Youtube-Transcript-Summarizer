from django.shortcuts import render
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi
from gensim.summarization import summarize
# from polls.models import Summary
import pymysql

def index(request):
    return render(request, 'polls/index.html')
    #return HttpResponse('Hello World !!!')

def createSummary(request):
    if request.method == 'POST':
        # fetched_data = Summary.objects.all()
        # print(Summary.objects.all())
        # if url in fetched_data:
        #     sum  = Summary.objects.get(video_link=url)
        #     summary = sum.summary
        
        try:
            url = request.POST.get('url')
            print(url)
            url = url.split('=')[1]
            # url = 'oBt53YbR9Kk'
            con=pymysql.connect(host="localhost",user="root",password="",database="transcriptsummarizer")
            cur=con.cursor()
            cur.execute("select summary from summarydetails where video_link=%s",url)
            existingurl=cur.fetchone()
            if existingurl:
                summary = existingurl[0]
            else:
                # transcript = YouTubeTranscriptApi.get_transcripts(['oBt53YbR9Kk'], languages=['de', 'en'])
                transcript = YouTubeTranscriptApi.get_transcripts([url], languages=['de', 'en'])
                result = ''
                for i in transcript[0][url]:
                # for i in transcript[0]['oBt53YbR9Kk']:
                    result += ' ' + i['text']
                l = len(result)//10
                summary=''
                i=0
                for x in range(10):
                    summary += summarize(result[i:l+i], word_count = 50).replace("\n"," ")
                    i+=l
                    print(i)
                cur.execute("insert into summarydetails (video_link, summary) values (%s,%s)",
                            (
                                url,
                                summary
                            ))
                con.commit()
                print(summary)

        except IndexError:
            summary = 'Enter Valid/Complete URL'

        except Exception as e:
            summary = 'Subtitles are disabled for this video'
                # summary = summarize(result[:1000], word_count = 500)
                # s = Summary(video_link=url, summary=summary)
                # s.save()
                # summary='hello'
                # Summary.objects.create(video_link=url, summary=summary)
        finally:
            con.close()    
        
        print(summary,len(summary))
    return JsonResponse({'summ': summary})


# Create your views here.
