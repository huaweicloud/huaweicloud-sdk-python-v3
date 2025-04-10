# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PassengerTravelItemList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traveler_name': 'str',
        'id_number': 'str',
        'travel_date': 'str',
        'departure_location': 'str',
        'arrival_location': 'str',
        '_class': 'str',
        'transportation_type': 'str'
    }

    attribute_map = {
        'traveler_name': 'traveler_name',
        'id_number': 'id_number',
        'travel_date': 'travel_date',
        'departure_location': 'departure_location',
        'arrival_location': 'arrival_location',
        '_class': 'class',
        'transportation_type': 'transportation_type'
    }

    def __init__(self, traveler_name=None, id_number=None, travel_date=None, departure_location=None, arrival_location=None, _class=None, transportation_type=None):
        r"""PassengerTravelItemList

        The model defined in huaweicloud sdk

        :param traveler_name: 出行人。 
        :type traveler_name: str
        :param id_number: 有效身份证件号。 
        :type id_number: str
        :param travel_date: 出行日期。 
        :type travel_date: str
        :param departure_location: 出发地。 
        :type departure_location: str
        :param arrival_location: 到达地。 
        :type arrival_location: str
        :param _class: 等级。 
        :type _class: str
        :param transportation_type: 交通工具类型。 
        :type transportation_type: str
        """
        
        

        self._traveler_name = None
        self._id_number = None
        self._travel_date = None
        self._departure_location = None
        self._arrival_location = None
        self.__class = None
        self._transportation_type = None
        self.discriminator = None

        if traveler_name is not None:
            self.traveler_name = traveler_name
        if id_number is not None:
            self.id_number = id_number
        if travel_date is not None:
            self.travel_date = travel_date
        if departure_location is not None:
            self.departure_location = departure_location
        if arrival_location is not None:
            self.arrival_location = arrival_location
        if _class is not None:
            self._class = _class
        if transportation_type is not None:
            self.transportation_type = transportation_type

    @property
    def traveler_name(self):
        r"""Gets the traveler_name of this PassengerTravelItemList.

        出行人。 

        :return: The traveler_name of this PassengerTravelItemList.
        :rtype: str
        """
        return self._traveler_name

    @traveler_name.setter
    def traveler_name(self, traveler_name):
        r"""Sets the traveler_name of this PassengerTravelItemList.

        出行人。 

        :param traveler_name: The traveler_name of this PassengerTravelItemList.
        :type traveler_name: str
        """
        self._traveler_name = traveler_name

    @property
    def id_number(self):
        r"""Gets the id_number of this PassengerTravelItemList.

        有效身份证件号。 

        :return: The id_number of this PassengerTravelItemList.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        r"""Sets the id_number of this PassengerTravelItemList.

        有效身份证件号。 

        :param id_number: The id_number of this PassengerTravelItemList.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def travel_date(self):
        r"""Gets the travel_date of this PassengerTravelItemList.

        出行日期。 

        :return: The travel_date of this PassengerTravelItemList.
        :rtype: str
        """
        return self._travel_date

    @travel_date.setter
    def travel_date(self, travel_date):
        r"""Sets the travel_date of this PassengerTravelItemList.

        出行日期。 

        :param travel_date: The travel_date of this PassengerTravelItemList.
        :type travel_date: str
        """
        self._travel_date = travel_date

    @property
    def departure_location(self):
        r"""Gets the departure_location of this PassengerTravelItemList.

        出发地。 

        :return: The departure_location of this PassengerTravelItemList.
        :rtype: str
        """
        return self._departure_location

    @departure_location.setter
    def departure_location(self, departure_location):
        r"""Sets the departure_location of this PassengerTravelItemList.

        出发地。 

        :param departure_location: The departure_location of this PassengerTravelItemList.
        :type departure_location: str
        """
        self._departure_location = departure_location

    @property
    def arrival_location(self):
        r"""Gets the arrival_location of this PassengerTravelItemList.

        到达地。 

        :return: The arrival_location of this PassengerTravelItemList.
        :rtype: str
        """
        return self._arrival_location

    @arrival_location.setter
    def arrival_location(self, arrival_location):
        r"""Sets the arrival_location of this PassengerTravelItemList.

        到达地。 

        :param arrival_location: The arrival_location of this PassengerTravelItemList.
        :type arrival_location: str
        """
        self._arrival_location = arrival_location

    @property
    def _class(self):
        r"""Gets the _class of this PassengerTravelItemList.

        等级。 

        :return: The _class of this PassengerTravelItemList.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        r"""Sets the _class of this PassengerTravelItemList.

        等级。 

        :param _class: The _class of this PassengerTravelItemList.
        :type _class: str
        """
        self.__class = _class

    @property
    def transportation_type(self):
        r"""Gets the transportation_type of this PassengerTravelItemList.

        交通工具类型。 

        :return: The transportation_type of this PassengerTravelItemList.
        :rtype: str
        """
        return self._transportation_type

    @transportation_type.setter
    def transportation_type(self, transportation_type):
        r"""Sets the transportation_type of this PassengerTravelItemList.

        交通工具类型。 

        :param transportation_type: The transportation_type of this PassengerTravelItemList.
        :type transportation_type: str
        """
        self._transportation_type = transportation_type

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
        if not isinstance(other, PassengerTravelItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
