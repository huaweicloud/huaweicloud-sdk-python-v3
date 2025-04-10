# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapInstanceListNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'sub_net_id': 'str',
        'security_group_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'sub_net_id': 'sub_net_id',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, vpc_id=None, sub_net_id=None, security_group_id=None):
        r"""HtapInstanceListNetwork

        The model defined in huaweicloud sdk

        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param sub_net_id: 子网ID。
        :type sub_net_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        """
        
        

        self._vpc_id = None
        self._sub_net_id = None
        self._security_group_id = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if sub_net_id is not None:
            self.sub_net_id = sub_net_id
        if security_group_id is not None:
            self.security_group_id = security_group_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HtapInstanceListNetwork.

        虚拟私有云ID。

        :return: The vpc_id of this HtapInstanceListNetwork.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HtapInstanceListNetwork.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this HtapInstanceListNetwork.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def sub_net_id(self):
        r"""Gets the sub_net_id of this HtapInstanceListNetwork.

        子网ID。

        :return: The sub_net_id of this HtapInstanceListNetwork.
        :rtype: str
        """
        return self._sub_net_id

    @sub_net_id.setter
    def sub_net_id(self, sub_net_id):
        r"""Sets the sub_net_id of this HtapInstanceListNetwork.

        子网ID。

        :param sub_net_id: The sub_net_id of this HtapInstanceListNetwork.
        :type sub_net_id: str
        """
        self._sub_net_id = sub_net_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this HtapInstanceListNetwork.

        安全组ID。

        :return: The security_group_id of this HtapInstanceListNetwork.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this HtapInstanceListNetwork.

        安全组ID。

        :param security_group_id: The security_group_id of this HtapInstanceListNetwork.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, HtapInstanceListNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
