# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItineraryList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'departure_station': 'str',
        'destination_station': 'str',
        'carrier': 'str',
        'flight': 'str',
        'cabin_class': 'str',
        'date': 'str',
        'time': 'str',
        'fare_basis': 'str',
        'effective_date': 'str',
        'expiry_date': 'str',
        'baggage_allowance': 'str'
    }

    attribute_map = {
        'departure_station': 'departure_station',
        'destination_station': 'destination_station',
        'carrier': 'carrier',
        'flight': 'flight',
        'cabin_class': 'cabin_class',
        'date': 'date',
        'time': 'time',
        'fare_basis': 'fare_basis',
        'effective_date': 'effective_date',
        'expiry_date': 'expiry_date',
        'baggage_allowance': 'baggage_allowance'
    }

    def __init__(self, departure_station=None, destination_station=None, carrier=None, flight=None, cabin_class=None, date=None, time=None, fare_basis=None, effective_date=None, expiry_date=None, baggage_allowance=None):
        r"""ItineraryList

        The model defined in huaweicloud sdk

        :param departure_station: 始发站。 
        :type departure_station: str
        :param destination_station: 目的站。 
        :type destination_station: str
        :param carrier: 承运人。 
        :type carrier: str
        :param flight: 航班号。 
        :type flight: str
        :param cabin_class: 座位等级。 
        :type cabin_class: str
        :param date: 日期。 
        :type date: str
        :param time: 时间。 
        :type time: str
        :param fare_basis: 客票类别。 
        :type fare_basis: str
        :param effective_date: 客票生效日期。 
        :type effective_date: str
        :param expiry_date: 有效截止日期。 
        :type expiry_date: str
        :param baggage_allowance: 免费行李。 
        :type baggage_allowance: str
        """
        
        

        self._departure_station = None
        self._destination_station = None
        self._carrier = None
        self._flight = None
        self._cabin_class = None
        self._date = None
        self._time = None
        self._fare_basis = None
        self._effective_date = None
        self._expiry_date = None
        self._baggage_allowance = None
        self.discriminator = None

        if departure_station is not None:
            self.departure_station = departure_station
        if destination_station is not None:
            self.destination_station = destination_station
        if carrier is not None:
            self.carrier = carrier
        if flight is not None:
            self.flight = flight
        if cabin_class is not None:
            self.cabin_class = cabin_class
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if fare_basis is not None:
            self.fare_basis = fare_basis
        if effective_date is not None:
            self.effective_date = effective_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if baggage_allowance is not None:
            self.baggage_allowance = baggage_allowance

    @property
    def departure_station(self):
        r"""Gets the departure_station of this ItineraryList.

        始发站。 

        :return: The departure_station of this ItineraryList.
        :rtype: str
        """
        return self._departure_station

    @departure_station.setter
    def departure_station(self, departure_station):
        r"""Sets the departure_station of this ItineraryList.

        始发站。 

        :param departure_station: The departure_station of this ItineraryList.
        :type departure_station: str
        """
        self._departure_station = departure_station

    @property
    def destination_station(self):
        r"""Gets the destination_station of this ItineraryList.

        目的站。 

        :return: The destination_station of this ItineraryList.
        :rtype: str
        """
        return self._destination_station

    @destination_station.setter
    def destination_station(self, destination_station):
        r"""Sets the destination_station of this ItineraryList.

        目的站。 

        :param destination_station: The destination_station of this ItineraryList.
        :type destination_station: str
        """
        self._destination_station = destination_station

    @property
    def carrier(self):
        r"""Gets the carrier of this ItineraryList.

        承运人。 

        :return: The carrier of this ItineraryList.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        r"""Sets the carrier of this ItineraryList.

        承运人。 

        :param carrier: The carrier of this ItineraryList.
        :type carrier: str
        """
        self._carrier = carrier

    @property
    def flight(self):
        r"""Gets the flight of this ItineraryList.

        航班号。 

        :return: The flight of this ItineraryList.
        :rtype: str
        """
        return self._flight

    @flight.setter
    def flight(self, flight):
        r"""Sets the flight of this ItineraryList.

        航班号。 

        :param flight: The flight of this ItineraryList.
        :type flight: str
        """
        self._flight = flight

    @property
    def cabin_class(self):
        r"""Gets the cabin_class of this ItineraryList.

        座位等级。 

        :return: The cabin_class of this ItineraryList.
        :rtype: str
        """
        return self._cabin_class

    @cabin_class.setter
    def cabin_class(self, cabin_class):
        r"""Sets the cabin_class of this ItineraryList.

        座位等级。 

        :param cabin_class: The cabin_class of this ItineraryList.
        :type cabin_class: str
        """
        self._cabin_class = cabin_class

    @property
    def date(self):
        r"""Gets the date of this ItineraryList.

        日期。 

        :return: The date of this ItineraryList.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ItineraryList.

        日期。 

        :param date: The date of this ItineraryList.
        :type date: str
        """
        self._date = date

    @property
    def time(self):
        r"""Gets the time of this ItineraryList.

        时间。 

        :return: The time of this ItineraryList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ItineraryList.

        时间。 

        :param time: The time of this ItineraryList.
        :type time: str
        """
        self._time = time

    @property
    def fare_basis(self):
        r"""Gets the fare_basis of this ItineraryList.

        客票类别。 

        :return: The fare_basis of this ItineraryList.
        :rtype: str
        """
        return self._fare_basis

    @fare_basis.setter
    def fare_basis(self, fare_basis):
        r"""Sets the fare_basis of this ItineraryList.

        客票类别。 

        :param fare_basis: The fare_basis of this ItineraryList.
        :type fare_basis: str
        """
        self._fare_basis = fare_basis

    @property
    def effective_date(self):
        r"""Gets the effective_date of this ItineraryList.

        客票生效日期。 

        :return: The effective_date of this ItineraryList.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        r"""Sets the effective_date of this ItineraryList.

        客票生效日期。 

        :param effective_date: The effective_date of this ItineraryList.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this ItineraryList.

        有效截止日期。 

        :return: The expiry_date of this ItineraryList.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this ItineraryList.

        有效截止日期。 

        :param expiry_date: The expiry_date of this ItineraryList.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def baggage_allowance(self):
        r"""Gets the baggage_allowance of this ItineraryList.

        免费行李。 

        :return: The baggage_allowance of this ItineraryList.
        :rtype: str
        """
        return self._baggage_allowance

    @baggage_allowance.setter
    def baggage_allowance(self, baggage_allowance):
        r"""Sets the baggage_allowance of this ItineraryList.

        免费行李。 

        :param baggage_allowance: The baggage_allowance of this ItineraryList.
        :type baggage_allowance: str
        """
        self._baggage_allowance = baggage_allowance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ItineraryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
