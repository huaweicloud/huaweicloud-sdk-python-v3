# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeSite:

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
        'region_id': 'str',
        'description': 'str',
        'location': 'CreateLocation'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'region_id',
        'description': 'description',
        'location': 'location'
    }

    def __init__(self, name=None, region_id=None, description=None, location=None):
        """CreateEdgeSite

        The model defined in huaweicloud sdk

        :param name: 边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）
        :type name: str
        :param region_id: 边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）
        :type region_id: str
        :param description: 边缘小站描述，最大支持长度为255个字节，不允许包含&lt;&gt;
        :type description: str
        :param location: 
        :type location: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        """
        
        

        self._name = None
        self._region_id = None
        self._description = None
        self._location = None
        self.discriminator = None

        self.name = name
        self.region_id = region_id
        if description is not None:
            self.description = description
        self.location = location

    @property
    def name(self):
        """Gets the name of this CreateEdgeSite.

        边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :return: The name of this CreateEdgeSite.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEdgeSite.

        边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :param name: The name of this CreateEdgeSite.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this CreateEdgeSite.

        边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :return: The region_id of this CreateEdgeSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateEdgeSite.

        边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :param region_id: The region_id of this CreateEdgeSite.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def description(self):
        """Gets the description of this CreateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :return: The description of this CreateEdgeSite.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :param description: The description of this CreateEdgeSite.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        """Gets the location of this CreateEdgeSite.

        :return: The location of this CreateEdgeSite.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateEdgeSite.

        :param location: The location of this CreateEdgeSite.
        :type location: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        """
        self._location = location

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
        if not isinstance(other, CreateEdgeSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
