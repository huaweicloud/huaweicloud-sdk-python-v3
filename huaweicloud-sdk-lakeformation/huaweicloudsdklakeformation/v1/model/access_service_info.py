# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessServiceInfo:

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
        'description': 'str',
        'grant': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'grant': 'grant'
    }

    def __init__(self, name=None, description=None, grant=None):
        """AccessServiceInfo

        The model defined in huaweicloud sdk

        :param name: 接入服务名称。最大长度为20个字符。
        :type name: str
        :param description: 接入服务描述。最大长度为500个字符。
        :type description: str
        :param grant: 是否授权。值为true或false。
        :type grant: bool
        """
        
        

        self._name = None
        self._description = None
        self._grant = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if grant is not None:
            self.grant = grant

    @property
    def name(self):
        """Gets the name of this AccessServiceInfo.

        接入服务名称。最大长度为20个字符。

        :return: The name of this AccessServiceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessServiceInfo.

        接入服务名称。最大长度为20个字符。

        :param name: The name of this AccessServiceInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AccessServiceInfo.

        接入服务描述。最大长度为500个字符。

        :return: The description of this AccessServiceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessServiceInfo.

        接入服务描述。最大长度为500个字符。

        :param description: The description of this AccessServiceInfo.
        :type description: str
        """
        self._description = description

    @property
    def grant(self):
        """Gets the grant of this AccessServiceInfo.

        是否授权。值为true或false。

        :return: The grant of this AccessServiceInfo.
        :rtype: bool
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this AccessServiceInfo.

        是否授权。值为true或false。

        :param grant: The grant of this AccessServiceInfo.
        :type grant: bool
        """
        self._grant = grant

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
        if not isinstance(other, AccessServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
