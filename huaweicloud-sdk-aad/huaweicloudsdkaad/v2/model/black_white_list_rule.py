# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteListRule:

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
        'type': 'int',
        'ip': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'ip': 'ip',
        'domain_id': 'domain_id'
    }

    def __init__(self, id=None, type=None, ip=None, domain_id=None):
        r"""BlackWhiteListRule

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param type: 0-黑名单，1-白名单
        :type type: int
        :param ip: ip
        :type ip: str
        :param domain_id: 域名id
        :type domain_id: str
        """
        
        

        self._id = None
        self._type = None
        self._ip = None
        self._domain_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if ip is not None:
            self.ip = ip
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this BlackWhiteListRule.

        id

        :return: The id of this BlackWhiteListRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BlackWhiteListRule.

        id

        :param id: The id of this BlackWhiteListRule.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this BlackWhiteListRule.

        0-黑名单，1-白名单

        :return: The type of this BlackWhiteListRule.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BlackWhiteListRule.

        0-黑名单，1-白名单

        :param type: The type of this BlackWhiteListRule.
        :type type: int
        """
        self._type = type

    @property
    def ip(self):
        r"""Gets the ip of this BlackWhiteListRule.

        ip

        :return: The ip of this BlackWhiteListRule.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this BlackWhiteListRule.

        ip

        :param ip: The ip of this BlackWhiteListRule.
        :type ip: str
        """
        self._ip = ip

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BlackWhiteListRule.

        域名id

        :return: The domain_id of this BlackWhiteListRule.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BlackWhiteListRule.

        域名id

        :param domain_id: The domain_id of this BlackWhiteListRule.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, BlackWhiteListRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
