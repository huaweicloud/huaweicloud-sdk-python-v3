# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteIpListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'type': 'str',
        'ips': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'ips': 'ips'
    }

    def __init__(self, instance_id=None, type=None, ips=None):
        r"""BlackWhiteIpListRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param type: 规则类型。black - 黑名单， white - 白名单
        :type type: str
        :param ips: ip列表
        :type ips: list[str]
        """
        
        

        self._instance_id = None
        self._type = None
        self._ips = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        self.ips = ips

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BlackWhiteIpListRequest.

        实例id

        :return: The instance_id of this BlackWhiteIpListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BlackWhiteIpListRequest.

        实例id

        :param instance_id: The instance_id of this BlackWhiteIpListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this BlackWhiteIpListRequest.

        规则类型。black - 黑名单， white - 白名单

        :return: The type of this BlackWhiteIpListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BlackWhiteIpListRequest.

        规则类型。black - 黑名单， white - 白名单

        :param type: The type of this BlackWhiteIpListRequest.
        :type type: str
        """
        self._type = type

    @property
    def ips(self):
        r"""Gets the ips of this BlackWhiteIpListRequest.

        ip列表

        :return: The ips of this BlackWhiteIpListRequest.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this BlackWhiteIpListRequest.

        ip列表

        :param ips: The ips of this BlackWhiteIpListRequest.
        :type ips: list[str]
        """
        self._ips = ips

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
        if not isinstance(other, BlackWhiteIpListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
