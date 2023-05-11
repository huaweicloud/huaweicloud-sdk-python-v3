# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'availability_zone': 'str',
        'region': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'region': 'region',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, name=None, availability_zone=None, region=None, limit=None, offset=None):
        """ListTemplatesRequest

        The model defined in huaweicloud sdk

        :param name: 模板名称
        :type name: str
        :param availability_zone: 可用区
        :type availability_zone: str
        :param region: Region ID
        :type region: str
        :param limit: 分页大小，不传值默认为50
        :type limit: int
        :param offset: 偏移量，不传值默认为0
        :type offset: int
        """
        
        

        self._name = None
        self._availability_zone = None
        self._region = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if region is not None:
            self.region = region
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        """Gets the name of this ListTemplatesRequest.

        模板名称

        :return: The name of this ListTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTemplatesRequest.

        模板名称

        :param name: The name of this ListTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListTemplatesRequest.

        可用区

        :return: The availability_zone of this ListTemplatesRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListTemplatesRequest.

        可用区

        :param availability_zone: The availability_zone of this ListTemplatesRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def region(self):
        """Gets the region of this ListTemplatesRequest.

        Region ID

        :return: The region of this ListTemplatesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListTemplatesRequest.

        Region ID

        :param region: The region of this ListTemplatesRequest.
        :type region: str
        """
        self._region = region

    @property
    def limit(self):
        """Gets the limit of this ListTemplatesRequest.

        分页大小，不传值默认为50

        :return: The limit of this ListTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTemplatesRequest.

        分页大小，不传值默认为50

        :param limit: The limit of this ListTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTemplatesRequest.

        偏移量，不传值默认为0

        :return: The offset of this ListTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTemplatesRequest.

        偏移量，不传值默认为0

        :param offset: The offset of this ListTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
