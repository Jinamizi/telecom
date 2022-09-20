from django.db import models

# Create your models here.
#changing mgt by organizing data means mccmnc will not be the primary key
class telecom_info(models.Model):
    mccmnc = models.CharField(max_length=6)
    operator=models.TextField()
    country = models.TextField()
    mgt=models.CharField(max_length=15) #should not  be a text field. change data
    ngt = models.CharField(max_length=15, null=True)
    prepaid_OBV= models.BooleanField() #prepaid outbound voice
    prepaid_OBMTV= models.BooleanField(null=True, blank=True) #prepaid Outbound Mobile Terminated Voice
    prepaid_OBD = models.BooleanField(null=True, blank=True) #prepaid Outbound Data
    postpaid_OBV = models.BooleanField(null=True, blank=True) #postpaid Outbound Voice
    postpaid_OBD = models.BooleanField(null=True, blank=True) #postpaid Outbound Data
    one_network = models.BooleanField(null=True, blank=True) #Network is considered one network, Airtel
    code = models.CharField(max_length=10)
    tapcode = models.TextField(null=True, blank=True) #should not  be a text field. change data

    def prepaid(self):
        value = str()
        if self.prepaid_OBV:
            value = "Voice"
        elif self.prepaid_OBMTV:
            value = "Voice MT only"

        if self.prepaid_OBD:
            value = value + " and Data" if value else value #add "and" if voice is also allowed,i.e Voice and Data
        return value if value else "No" #return No if no roaming services allowed.

    def postpaid(self):
        value = str()
        if self.postpaid_OBV:
            value = "Voice"

        if self.postpaid_OBD:
            value = value + " and Data" if value else value #add "and" if voice is also allowed,i.e Voice and Data
        return value if value else "No" #return No if no roaming services allowed.
