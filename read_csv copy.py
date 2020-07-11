from series.serializers import SerieSerializer

serializer = SerieSerializer()
print(repr(serializer))
> SerieSerializer():
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=100)
    release_date = DateField()
    rating = IntegerField(required=False)
    category = ChoiceField(choices=(('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')))