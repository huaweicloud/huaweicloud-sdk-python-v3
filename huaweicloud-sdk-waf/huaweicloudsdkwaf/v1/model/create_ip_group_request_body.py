# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpGroupRequestBody:

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
        'ips': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ips': 'ips',
        'description': 'description'
    }

    def __init__(self, name=None, ips=None, description=None):
        """CreateIpGroupRequestBody

        The model defined in huaweicloud sdk

        :param name: 地址组名称
        :type name: str
        :param ips: 以逗号分隔的ip或ip段
        :type ips: str
        :param description: 地址组描述
        :type description: str
        """
        
        

        self._name = None
        self._ips = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.ips = ips
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CreateIpGroupRequestBody.

        地址组名称

        :return: The name of this CreateIpGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIpGroupRequestBody.

        地址组名称

        :param name: The name of this CreateIpGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        """Gets the ips of this CreateIpGroupRequestBody.

        以逗号分隔的ip或ip段

        :return: The ips of this CreateIpGroupRequestBody.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this CreateIpGroupRequestBody.

        以逗号分隔的ip或ip段

        :param ips: The ips of this CreateIpGroupRequestBody.
        :type ips: str
        """
        self._ips = ips

    @property
    def description(self):
        """Gets the description of this CreateIpGroupRequestBody.

        地址组描述

        :return: The description of this CreateIpGroupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIpGroupRequestBody.

        地址组描述

        :param description: The description of this CreateIpGroupRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateIpGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
