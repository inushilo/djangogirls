from django.shortcuts import render
from .models import Ranking
from .forms import RankingForm
import requests
from bs4 import BeautifulSoup
from django.utils import timezone

# Create your views here.
def ranking_list(request):
    rankings = Ranking.objects.distinct().values('ranking_name','ranking_num')
    return render(request, 'ranking/ranking_list.html', {'rankings':rankings})

def ranking_detail(request, ranking_name):
    rankings = Ranking.objects.filter(ranking_name=ranking_name).order_by('rank')
    return render(request, 'ranking/ranking_detail.html', {'rankings': rankings})

def download_ranking(request):
    if request.method == "POST":
      form = RankingForm(request.POST)
      if form.is_valid():
        ranking = form.save(commit=False)
        req = requests.get("https://game-i.daa.jp/?GooglePlay%E3%82%A2%E3%83%97%E3%83%AA%E6%9C%88%E9%96%93%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0")
        req.encoding = req.apparent_encoding # 日本語の文字化け防止
        bsObj = BeautifulSoup(req.text,"html.parser")
        items = bsObj.find_all("td")
        Rank = 1; cnt = 0; flg = False; finish_Rank = ranking.ranking_num
        for item in items:
          if str(Rank) == item.get_text():
            flg = True
          if flg:
            if cnt == 0:
              rank = int(item.get_text())
            elif cnt == 2:
              app_name = item.get_text()
            elif cnt == 3:
              download_value = item.get_text().replace(",","")
            cnt += 1
            if cnt == 4:
              created_date = timezone.now()
              Ranking.objects.create(ranking_name=ranking.ranking_name, ranking_num=ranking.ranking_num, rank=rank, app_name=app_name, download_value=download_value, created_date=created_date)
              cnt = 0
              flg = False
              Rank += 1
          if Rank > finish_Rank:
            break
        rankings = Ranking.objects.distinct().values('ranking_name','ranking_num')
        return render(request, 'ranking/ranking_list.html', {'rankings':rankings})
    else:
      form = RankingForm()
      return render(request, 'ranking/form.html', {'form':form})

def ranking_delete(request, ranking_name):
    ranking = Ranking.objects.filter(ranking_name=ranking_name)
    ranking.delete()
    rankings = Ranking.objects.distinct().values('ranking_name','ranking_num')
    return render(request, 'ranking/ranking_list.html', {'rankings':rankings})
# Create your views here.
