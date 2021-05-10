# coding: utf-8

import pprint
import re

import six





class ListInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'name': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'edgecloud_id': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'name': 'name',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'edgecloud_id': 'edgecloud_id',
        'site_id': 'site_id'
    }

    def __init__(self, offset=None, limit=None, status=None, name=None, area=None, province=None, city=None, edgecloud_id=None, site_id=None):
        """ListInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._name = None
        self._area = None
        self._province = None
        self._city = None
        self._edgecloud_id = None
        self._site_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if edgecloud_id is not None:
            self.edgecloud_id = edgecloud_id
        if site_id is not None:
            self.site_id = site_id

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.


        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.


        :param offset: The offset of this ListInstancesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.


        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.


        :param limit: The limit of this ListInstancesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListInstancesRequest.


        :return: The status of this ListInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesRequest.


        :param status: The status of this ListInstancesRequest.
        :type: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.


        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.


        :param name: The name of this ListInstancesRequest.
        :type: str
        """
        self._name = name

    @property
    def area(self):
        """Gets the area of this ListInstancesRequest.


        :return: The area of this ListInstancesRequest.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ListInstancesRequest.


        :param area: The area of this ListInstancesRequest.
        :type: str
        """
        self._area = area

    @property
    def province(self):
        """Gets the province of this ListInstancesRequest.


        :return: The province of this ListInstancesRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this ListInstancesRequest.


        :param province: The province of this ListInstancesRequest.
        :type: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this ListInstancesRequest.


        :return: The city of this ListInstancesRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ListInstancesRequest.


        :param city: The city of this ListInstancesRequest.
        :type: str
        """
        self._city = city

    @property
    def edgecloud_id(self):
        """Gets the edgecloud_id of this ListInstancesRequest.


        :return: The edgecloud_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._edgecloud_id

    @edgecloud_id.setter
    def edgecloud_id(self, edgecloud_id):
        """Sets the edgecloud_id of this ListInstancesRequest.


        :param edgecloud_id: The edgecloud_id of this ListInstancesRequest.
        :type: str
        """
        self._edgecloud_id = edgecloud_id

    @property
    def site_id(self):
        """Gets the site_id of this ListInstancesRequest.


        :return: The site_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListInstancesRequest.


        :param site_id: The site_id of this ListInstancesRequest.
        :type: str
        """
        self._site_id = site_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
