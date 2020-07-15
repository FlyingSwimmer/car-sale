from sale.models import Offer


def get_user_offers(user_id, ad_id=None, since_date=None):
    user_offers = Offer.objects.filter(user__id=user_id)
    if ad_id is not None:
        user_offers = user_offers.filter(advertisement__id=ad_id)
    if since_date is not None:
        user_offers = user_offers.filter(creation_date__gte=since_date)
    return user_offers
