#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#places.py

import random, string

#lifted direct from my other NaNoGenMo 2019 project, 'Fictionalia'.

property_subjects = [["2019_10_11.txt", ["St Leonards-on-Sea, East Sussex", "St Leonards"]],
                     ["2019_10_04.txt", ["Croydon, south London", "Croydon"]],
                     ["2019_09_27.txt", ["New Ash Green, Kent", "New Ash Green"]],
                     ["2019_09_20.txt", ["Buxton, Derbyshire", "Buxton"]],
                     ["2019_09_13.txt", ["Lancaster, Lancashire", "Lancaster"]],
                     ["2019_09_06.txt", ["Ormeau, Belfast", "Ormeau"]],
                     ["2019_08_30.txt", ["Ventnor, Isle of Wight", "Ventnor"]],
                     ["2019_08_23.txt", ["West Kirby, Merseyside", "West Kirby"]],
                     ["2019_08_16.txt", ["Helmsley, North Yorkshire", "Helmsley"]],
                     ["2019_08_09.txt", ["Chichester, West Sussex", "Chichester"]],
                     ["2019_08_02.txt", ["Bermondsey, south-east London", "Bermondsey"]],
                     ["2019_07_26.txt", ["Cardigan, Ceredigion", "Cardigan"]],
                     ["2019_07_19.txt", ["Hemel Hempstead, Hertfordshire", "Hemel Hempstead"]],
                     ["2019_07_12.txt", ["Whitley Bay, Tyne and Wear", "Whitley Bay"]],
                     ["2019_07_05.txt", ["Thurso and Dunnet Bay, Caithness", "Thurso and Dunnet Bay"]],
                     ["2019_06_28.txt", ["Brighton, East Sussex:", "Brighton"]],
                     ["2019_06_21.txt", ["Grimsby and Cleethorpes, Lincolnshire", "Grimsby and Cleethorpes"]],
                     ["2019_06_14.txt", ["Kendal, Cumbria", "Kendal"]],
                     ["2019_06_07.txt", ["Bognor Regis, West Sussex", "Bognor Regis"]],
                     ["2019_05_31.txt", ["Didsbury, south Manchester", "Didsbury"]],
                     ["2019_05_17.txt", ["Hertford, Hertfordshire", "Hertford"]],
                     ["2019_05_10.txt", ["Hornsey, north London", "Hornsey"]],
                     ["2019_05_03.txt", ["Oswestry, Shropshire", "Oswestry"]],
                     ["2019_04_26.txt", ["Ripon, North Yorkshire", "Ripon"]],
                     ["2019_04_19.txt", ["Ely, Cambridgeshire", "Ely"]],
                     ["2019_04_05.txt", ["Whitstable, Kent", "Whitstable"]],
                     ["2019_03_29.txt", ["Brecon, Powys", "Brecon"]],
                     ["2019_03_22.txt", ["Winchester, Hampshire", "Winchester"]],
                     ["2019_03_08.txt", ["Brentford, west London", "Brentford"]],
                     ["2019_03_01.txt", ["Stirling", "Stirling"]],
                     ["2019_02_22.txt", ["Cromer, Norfolk", "Cromer"]],
                     ["2019_02_15.txt", ["Bedford", "Bedford"]],
                     ["2019_02_08.txt", ["Clitheroe, Lancashire", "Clitheroe"]],
                     ["2019_02_01.txt", ["Anglesey/Ynys Môn, Wales", "Anglesey/Ynys Môn"]],
                     ["2019_01_25.txt", ["Sherborne, Dorset", "Sherborne"]],###
                     ["2019_01_18.txt", ["Somers Town and Euston, north London", "Somers Town"]],
                     ["2019_01_11.txt", ["King's Lynn, Norfolk", "King's Lynn"]],
                     ["2019_01_04.txt", ["Warwick, Warwickshire", "Warwick"]],
                     ["2018_12_28.txt", ["Great Malvern and the Malvern hills", "Great Malvern"]],
                     ["2018_12_14.txt", ["Littlehampton, West Sussex", "Littlehampton"]],
                     ["2018_12_07.txt", ["Bangor, County Down", "Bangor"]],
                     ["2018_11_30.txt", ["Chester, Cheshire", "Chester"]],
                     ["2018_11_23.txt", ["Gospel Oak, north London", "Gospel Oak"]],
                     ["2018_11_16.txt", ["Portobello, Edinburgh", "Portobello"]],
                     ["2018_11_09.txt", ["Colchester, Essex", "Colchester"]],
                     ["2018_11_02.txt", ["Wimborne Minster", "Wimborne Minster"]],
                     ["2018_10_26.txt", ["Worcester", "Worcester"]],
                     ["2018_10_12.txt", ["Abergavenny, Monmouthshire", "Abergavenny"]],
                     ["2018_10_05.txt", ["Deal, Kent", "Deal"]],
                     ["2018_09_28.txt", ["Grange-Over-Sands, Cumbria", "Grange-Over-Sands"]],
                     ["2018_09_21.txt", ["Leytonstone", "Leytonstone"]],
                     ["2018_09_14.txt", ["Lewes, East Sussex", "Lewes"]],
                     ["2018_09_07.txt", ["Southwold, Suffolk", "Southwold"]],  ###
                     ["2018_08_24.txt", ["Callander and the Trossachs", "Callander"]],
                     ["2018_08_17.txt", ["Openshaw", "Openshaw"]],
                     ["2018_08_03.txt", ["Bury St Edmunds, Suffolk", "Bury"]],
                     ["2018_07_27.txt", ["Weston-super-Mare, Somerset", "Weston-super-Mare"]],
                     ["2018_07_20.txt", ["Ramsbottom, Greater Manchester", "Ramsbottom"]],
                     ["2018_07_13.txt", ["Halifax, West Yorkshire", "Halifax"]],
                     ["2018_07_06.txt", ["Lampeter, Ceredigion", "Lampeter"]],
                     ["2018_06_29.txt", ["Surrey Quays, London", "Surrey Quays"]],
                     ["2018_06_22.txt", ["St Andrews", "St Andrews"]],
                     ["2018_06_15.txt", ["Ipswich, Suffolk", "Ipswich"]],
                     ["2018_06_08.txt", ["Ouseburn, Newcastle upon Tyne", "Ouseburn"]],
                     ["2018_06_01.txt", ["Dorking, Surrey", "Dorking"]],
                     ["2018_05_11.txt", ["Truro, Cornwall", "Truro"]],
                     ["2018_04_20.txt", ["Stockport, Greater Manchester", "Stockport"]],
                     ["2018_04_13.txt", ["King's Cross, London", "King's Cross"]],
                     ["2018_04_06.txt", ["Tenterden, Kent", "Tenterden"]],
                     ["2018_03_30.txt", ["Warrington, Cheshire", "Warrington"]],
                     ["2018_03_23.txt", ["Eastbourne, East Sussex", "Eastbourne"]],
                     ["2018_03_16.txt", ["Spalding, Lincolnshire", "Spalding"]],
                     ["2018_03_02.txt", ["Exeter, Devon", "Exeter"]],
                     ["2018_02_23.txt", ["Hebden Bridge, West Yorks", "Hebden Bridge"]],
                     ["2018_02_09.txt", ["Deptford, south-east London", "Deptford"]],
                     ["2018_02_02.txt", ["Stroud, Gloucestershire", "Stroud"]],
                     ["2018_01_26.txt", ["Beverley, east Yorkshire", "Beverley"]],
                     ["2018_01_19.txt", ["Finnieston, Glasgow", "Finnieston"]],
                     ["2018_01_12.txt", ["Louth, Lincolnshire", "Louth"]],
                     ["2018_01_05.txt", ["Lichfield, Staffordshire", "Lichfield"]],
                     ["2017_12_29.txt", ["Romford, east London", "Romford"]],
                     ["2017_12_22.txt", ["Bexhill-on-Sea, East Sussex", "Bexhill-on-Sea"]],
                     ["2017_12_15.txt", ["Pwllheli", "Pwllheli"]],
                     ["2017_12_08.txt", ["Kelso, Roxburghshire", "Kelso"]],
                     ["2017_12_01.txt", ["Whitby, North Yorkshire", "Whitby"]],
                     ["2017_11_24.txt", ["Hereford", "Hereford"]],
                     ["2017_11_17.txt", ["Stamford, Lincolnshire", "Stamford"]],
                     ["2017_11_10.txt", ["Frome, Somerset", "Frome"]],
                     ["2017_11_03.txt", ["Windsor & Eton, Berkshire", "Windsor & Eton"]],
                     ["2017_10_27.txt", ["Lincoln", "Lincoln"]],
                     ["2017_10_20.txt", ["Berwick-upon-Tweed, Northumberland", "Berwick-upon-Tweed"]],
                     ["2017_10_06.txt", ["Dollis Hill, north-west London", "Dollis Hill"]],
                     ["2017_10_01.txt", ["Arundel, West Sussex", "Arundel"]],
                     ["2017_09_29.txt", ["Boscastle, Cornwall", "Boscastle"]],
                     ["2017_09_22.txt", ["Kintyre peninsula, Argyll and Bute", "Kintyre"]],
                     ["2017_09_08.txt", ["Diss, Norfolk", "Diss, Norfolk"]],
                     ["2017_08_25.txt", ["Kingston upon Hull, Yorkshire", "Kingston upon Hull"]],
                     ["2017_08_17.txt", ["Rochester, Kent", "Rochester"]],
                     ["2017_08_11.txt", ["Preston, Lancashire", "Preston"]],
                     ["2017_08_04.txt", ["Herne Bay, Kent", "Herne Bay"]],
                     ### property_subjects (AUTO-GENERATED) ###
                     ["2017_07_28.txt", ["Brockley, south-east London", "Brockley"]],
                     ["2017_07_21.txt", ["Canvey Island, Essex", "Canvey Island"]],
                     ["2017_07_14.txt", ["Ballycastle, County Antrim", "Ballycastle"]],
                     ["2017_07_07.txt", ["Hove, East Sussex", "Hove"]],
                     ["2017_06_30.txt", ["Aylsham, Norfolk", "Aylsham"]],
                     ["2017_06_23.txt", ["Cambridge", "Cambridge"]],
                     ["2017_06_16.txt", ["Helensburgh, Argyll & Bute", "Helensburgh"]],
                     ["2017_06_09.txt", ["Beaconsfield, Bucks", "Beaconsfield"]],
                     ["2017_06_02.txt", ["Dorchester-on-Thames, Oxfordshire", "Dorchester-on-Thames"]],
                     ["2017_05_26.txt", ["Ilford, east London", "Ilford"]],
                     ["2017_05_19.txt", ["Rothbury, Northumberland", "Rothbury"]],
                     ["2017_05_12.txt", ["Thetford, Norfolk", "Thetford"]],
                     ["2017_05_05.txt", ["Blaenafon, Gwent", "Blaenafon"]],
                     ["2017_04_21.txt", ["the Isle of Portland, Dorset", "the Isle of Portland"]],
                     ["2017_04_14.txt", ["Crediton, Devon", "Crediton"]],
                     ["2017_04_07.txt", ["Kirkcaldy, Fife", "Kirkcaldy"]],
                     ["2017_04_01.txt", ["Framplington, Suffolk", "Framplington"]],
                     ["2017_03_24.txt", ["Petworth and Pulborough, West Sussex", "Petworth and Pulborough"]],
                     ["2017_03_17.txt", ["Rhayader & the Elan valley, Powys", "Rhayader"]],
                     ["2017_03_03.txt", ["Hither Green, London", "Hither Green"]],
                     ["2017_02_24.txt", ["the Torridge valley, Devon", "the Torridge valley"]],
                     ["2017_02_17.txt", ["Bishop's Castle, Shropshire", "Bishop's Castle"]],
                     ["2017_02_10.txt", ["Kirkwall and Orkney", "Kirkwall and Orkney"]],
                     ["2017_02_03.txt", ["Ashbourne, Derbyshire", "Ashbourne"]],
                     ["2017_01_27.txt", ["Newport, Isle of Wight", "Newport"]],
                     ["2017_01_20.txt", ["Scarborough, North Yorkshire", "Scarborough"]],
                     ["2017_01_13.txt", ["Streatham, south-west London", "Streatham"]],
                     ["2017_01_06.txt", ["Durham, County Durham", "Durham"]],
                     ["2016_12_16.txt", ["Fishguard and Newport, Pembrokeshire", "Fishguard and Newport"]],
                     ["2016_12_09.txt", ["Dover, Kent", "Dover"]],
                     ["2016_12_02.txt", ["Rye, East Sussex", "Rye"]],
                     ["2016_11_25.txt", ["St Albans", "St Albans"]],
                     ["2016_11_18.txt", ["Harringay, north London", "Harringay"]],
                     ["2016_11_11.txt", ["Stranraer and the Rhinns, Dumfries and Galloway", "Stranraer"]],
                     ["2016_11_04.txt", ["Ottery St Mary, Devon", "Ottery St Mary"]],
                     ["2016_10_28.txt", ["Worthing, West Sussex", "Worthing"]],
                     ["2016_10_21.txt", ["Hotwells, Bristol", "Hotwells"]],
                     ["2016_10_14.txt", ["Perth, Perthshire", "Perth"]],
                     ["2016_10_07.txt", ["Canterbury, Kent", "Canterbury"]],
                     ["2016_09_30.txt", ["Aberaeron, Ceredigion", "Aberaeron"]],
                     ["2016_09_23.txt", ["Lambeth, London", "Lambeth"]],
                     ["2016_09_16.txt", ["Luton, Bedfordshire", "Luton"]],
                     ["2016_09_09.txt", ["Bowness and Windermere", "Bowness and Windermere"]],
                     ["2016_09_02.txt", ["Saltaire", "Saltaire"]],
                     ["2016_08_19.txt", ["Lowestoft, Suffolk", "Lowestoft"]],
                     ["2016_08_12.txt", ["Lanark", "Lanark"]],
                     ["2016_08_05.txt", ["Okehampton, Devon", "Okehampton"]],
                     ["2016_07_29.txt", ["Monmouth and the lower Wye valley", "Monmouth"]],
                     ["2016_07_22.txt", ["Abingdon, Oxfordshire", "Abingdon"]],
                     ["2016_07_15.txt", ["Plumstead, south-east London", "Plumstead"]],
                     ["2016_07_08.txt", ["Princes Risborough, Buckinghamshire", "Princes Risborough"]],
                     ["2016_06_24.txt", ["Paisley, Renfrewshire", "Paisley"]],
                     ["2016_06_17.txt", ["Henley-on-Thames, Oxfordshire", "Henley"]],
                     ["2016_06_10.txt", ["Lynton and Lynmouth, north Devon", "Lynton and Lynmouth"]],
                     ["2016_06_03.txt", ["Shrewsbury, Shropshire", "Shrewsbury"]],
                     ["2016_05_27.txt", ["Westerham, West Malling and the West Kent Downs", "Westerham"]],
                     ["2016_05_20.txt", ["Leigh-on-Sea", "Leigh"]],
                     ["2016_05_13.txt", ["South Norwood and Thornton Heath, south London", "South Norwood"]],
                     ["2016_05_06.txt", ["The Marches", "The Marches"]],
                     ["2016_04_29.txt", ["Northumberland", "Northumberland"]],
                     ["2016_04_22.txt", ["Ripley, Derbyshire", "Ripley"]],
                     ["2016_04_15.txt", ["Barnstaple, Devon", "Barnstaple"]],
                     ["2016_04_08.txt", ["Llanrwst, Conwy", "Llanrwst"]],
                     ["2016_04_01.txt", ["Winchcombe, Gloucestershire", "Winchcombe"]],
                     ["2016_03_25.txt", ["Great Yarmouth", "Great Yarmouth"]],
                     ["2016_03_18.txt", ["Steyning, West Sussex", "Steyning"]],
                     ["2016_03_04.txt", ["Moretonhampstead and east Dartmoor, Devon", "Moretonhampstead"]],
                     ["2016_02_26.txt", ["Alston, Cumbria", "Alston"]],
                     ["2016_02_19.txt", ["Glasgow Southside", "Glasgow Southside"]],
                     ["2016_02_12.txt", ["Abbey Wood, south-east London", "Abbey Wood"]],
                     ["2016_02_05.txt", ["Slaithwaite and the Colne Valley, West Yorkshire", "Slaithwaite"]],
                     ["2016_01_29.txt", ["Solihull, West Midlands", "Solihull"]],
                     ["2016_01_22.txt", ["Farnham, Surrey", "Farnham"]],
                     ["2016_01_15.txt", ["Braunton, Croyde and Woolacombe, Devon", "Braunton"]],
                     ["2016_01_01.txt", ["the Nadder valley, Wiltshire", "the Nadder valley"]],
                     ["2015_12_18.txt", ["Jesmond, Newcastle upon Tyne", "Jesmond"]],
                     ["2015_12_11.txt", ["Happisburgh, Norfolk", "Happisburgh"]],
                     ["2015_12_04.txt", ["Tottenham, north London", "Tottenham"]],
                     ["2015_11_27.txt", ["Chepstow, Monmouthshire", "Chepstow"]],
                     ["2015_11_20.txt", ["Tadcaster, north Yorkshire", "Tadcaster"]],
                     ["2015_11_13.txt", ["Soho, central London", "Soho"]],
                     ["2015_11_06.txt", ["Melton Mowbray, Leicestershire", "Melton Mowbray"]],
                     ["2015_10_30.txt", ["Eyemouth and St Abbs Head, Berwickshire", "Eyemouth"]],
                     ["2015_10_23.txt", ["Church Stretton and the Shropshire Hills, Shropshire", "Church Stretton"]],
                     ["2015_10_16.txt", ["Ramsgate, Kent", "Ramsgate"]],
                     ["2015_10_09.txt", ["Falmouth, Cornwall", "Falmouth"]],
                     ["2015_10_02.txt", ["Holmfirth, West Yorkshire", "Holmfirth"]],
                     ["2015_09_25.txt", ["Sydenham, south-east London", "Sydenham"]],
                     ["2015_09_18.txt", ["Pevensey and Pevensey Bay, East Sussex", "Pevensey"]],
                     ["2015_09_11.txt", ["Tynemouth, Tyne & Wear", "Tynemouth"]],
                     ["2015_09_04.txt", ["St Asaph, Denbighshire", "St Asaph"]],
                     ["2015_08_28.txt", ["Lyme Regis, Dorset", "Lyme Regis"]],
                     ["2015_08_21.txt", ["Devizes, Wiltshire", "Devizes"]],
                     ["2015_08_14.txt", ["the Forest of Dean, Gloucestershire", "the Forest of Dean"]],
                     ["2015_08_07.txt", ["Marlow, Buckinghamshire", "Marlow"]],
                     ["2015_07_31.txt", ["Barnet, north-west London", "Barnet"]],
                     ["2015_07_24.txt", ["Nantwich, Cheshire", "Nantwich"]],
                     ["2015_07_17.txt", ["The Marches", "the Marches"]],
                     ["2015_07_10.txt", ["Welshpool, Powys", "Welshpool"]],
                     ["2015_07_03.txt", ["Dorchester, Dorset", "Dorchester"]],
                     ["2019_10_18.txt", ["Dumfries, Dumfries & Galloway", "Dumfries"]],
                     ["2019_10_26.txt", ["Tavistock, Devon", "Tavistock"]],
                     ["2019_11_02.txt", ["Walton-on-the-Naze, Essex", "Walton-on-the-Naze"]],
                     #["", ["", ""]],
                     #["", ["", ""]],
                     ]


def get_random_place():
    p = random.choice(property_subjects)
    place = p[1][0]
    if string.find(place, " and ") > -1:
        if string.find(place, ", ") > -1:
            places, county = string.split(place, ", ", maxsplit=1)
            if string.find(places, " and ") > -1:
                p2 = string.split(places, " and ")
                p3 = random.choice(p2)
                place = "%s, %s" % (p3, county)
    return place

if __name__ == "__main__":
    print get_random_place()


    