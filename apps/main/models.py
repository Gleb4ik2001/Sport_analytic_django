from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    """Sport model"""
    name = models.CharField(
        verbose_name='название спорта',
        max_length=100,
        unique=True
    )
    image = models.ImageField(
        verbose_name='фото',
        upload_to='sports/'
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'спорт'
        verbose_name_plural = 'спорты'
        ordering = ('name',)
    
class Country(models.Model):
    """Country model"""
    name = models.CharField(
        verbose_name='название страны',
        max_length=100,
        unique=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
        ordering = ('name',)

class Team(models.Model):
    """Team model"""
    name = models.CharField(
        verbose_name='название команды',
        max_length=100
    )
    logo = models.ImageField(
        verbose_name='логотип',
        upload_to='logos/'
    )
    country = models.ForeignKey(
        to=Country,
        verbose_name='страна',
        related_name='team_to_country',
        on_delete= models.PROTECT,
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'
        ordering = ('name',)

class Player(models.Model):
    """Player model"""
    team = models.ForeignKey(
        to=Team, 
        on_delete=models.PROTECT,
        verbose_name='команда'
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=100
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=100
    )
    photo = models.ImageField(
        verbose_name='фото',
        upload_to='players/'
    )
    position = models.CharField(
        verbose_name='позиция',
        max_length=100
    )
    age = models.PositiveIntegerField(
        verbose_name='возраст'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} .Возраст: {self.age}'

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'
        ordering = ('first_name','last_name',)

class Author(models.Model):
    user = models.OneToOneField(
        verbose_name='автор',
        to=User,
        related_name='author_to_user',
        on_delete=models.PROTECT
    )
    def __str__(self) -> str:
        return self.user
    
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural ='авторы'
        ordering = ('user',)

class Game(models.Model):
    """Game model"""
    team1 = models.ForeignKey(        
        to=Team,
        verbose_name='команда 1',
        related_name='games_as_team1', 
        on_delete=models.PROTECT
    )
    team2 = models.ForeignKey(        
        to=Team,
        verbose_name='команда 2',
        related_name='games_as_team2', 
        on_delete=models.PROTECT
    )
    date_time = models.DateTimeField(
        verbose_name='дата игры/матча',
    )
    venue = models.CharField(
        verbose_name='место проведения',
        max_length=100
    )
    result = models.CharField(
        verbose_name='результат матча',
        max_length=100
    )

    def __str__(self) -> str:
        return f'{self.team1} VS {self.team2} result: {self.result}'

class Stat(models.Model):
    """Stat model"""
    player = models.ForeignKey(        
        to=Player, 
        verbose_name='игрок',
        on_delete=models.PROTECT
    )
    team = models.ForeignKey(        
        to=Team, 
        verbose_name='команда',
        on_delete=models.PROTECT
    )
    game = models.ForeignKey(        
        to=Game,
        verbose_name='игра',
        on_delete=models.PROTECT
    )
    goals = models.PositiveIntegerField(
        verbose_name='голы',
        null=True,
        blank=True
    )
    points = models.PositiveIntegerField(
        verbose_name='очки',
        null=True,
        blank=True
    )
    games_played = models.PositiveIntegerField(
        verbose_name='игр сыграно',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.player}:{self.team}: {self.game} .Goals: {self.goals}'

    class Meta:
        verbose_name = 'ститистика'
        verbose_name_plural = 'статистики'
        ordering = ('player','goals',)

class News(models.Model):
    """News model"""
    title = models.CharField(
        verbose_name='заголовок',
        max_length=100
    )
    content = models.TextField(
        verbose_name='статья'
    )
    author = models.ForeignKey(        
        to=Author,
        verbose_name='автор',
        related_name='news_to_author',
        on_delete=models.PROTECT
    )
    publication_date = models.DateField(
        verbose_name='дата публикации',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f'Заголовок: {self.title} Автор: {self.author}'

class Analysis(models.Model):
    game = models.ForeignKey(   
        to=Game, 
        verbose_name='игра',
        on_delete=models.PROTECT
    )
    team = models.ForeignKey(
        to=Team,
        verbose_name='команда',
        on_delete=models.PROTECT
    )
    statistics = models.ForeignKey(  
        to=Stat, 
        verbose_name='статистика',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'Игра: {self.game} Команда: {self.team} Статистика: {self.statistics}'
    
    class Meta:
        verbose_name = 'анализ'
        verbose_name_plural = 'анализы'
        ordering = ('game',)

