# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdHostnameEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname'
    }

    def __init__(self, id=None, hostname=None):
        """IdHostnameEntry

        The model defined in huaweicloud sdk

        :param id: 防护域名ID
        :type id: str
        :param hostname: 防护域名
        :type hostname: str
        """
        
        

        self._id = None
        self._hostname = None
        self.discriminator = None

        self.id = id
        self.hostname = hostname

    @property
    def id(self):
        """Gets the id of this IdHostnameEntry.

        防护域名ID

        :return: The id of this IdHostnameEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdHostnameEntry.

        防护域名ID

        :param id: The id of this IdHostnameEntry.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this IdHostnameEntry.

        防护域名

        :return: The hostname of this IdHostnameEntry.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this IdHostnameEntry.

        防护域名

        :param hostname: The hostname of this IdHostnameEntry.
        :type hostname: str
        """
        self._hostname = hostname

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
        if not isinstance(other, IdHostnameEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
