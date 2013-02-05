def getting_data():
  '''Downloads the elevator status for grand central station 
  and gives the fraction of elevators that are down due to repair.
  '''
  import untangle
  from fractions import Fraction
  doc = untangle.parse("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
  outages = doc.NYCOutages.outage
  repair_count = 0
  for outage in outages:
    if outage.reason.cdata == 'REPAIR':
      repair_count += 1
  return Fraction(repair_count, len(outages))