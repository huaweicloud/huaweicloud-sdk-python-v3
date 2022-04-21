# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonPoolsWithBorderGroupDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip_pools': 'list[str]',
        'public_border_group': 'str'
    }

    attribute_map = {
        'publicip_pools': 'publicip_pools',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, publicip_pools=None, public_border_group=None):
        """CommonPoolsWithBorderGroupDict

        The model defined in huaweicloud sdk

        :param publicip_pools: 同组的公共池列表
        :type publicip_pools: list[str]
        :param public_border_group: 分组：中心还是边缘
        :type public_border_group: str
        """
        
        

        self._publicip_pools = None
        self._public_border_group = None
        self.discriminator = None

        if publicip_pools is not None:
            self.publicip_pools = publicip_pools
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def publicip_pools(self):
        """Gets the publicip_pools of this CommonPoolsWithBorderGroupDict.

        同组的公共池列表

        :return: The publicip_pools of this CommonPoolsWithBorderGroupDict.
        :rtype: list[str]
        """
        return self._publicip_pools

    @publicip_pools.setter
    def publicip_pools(self, publicip_pools):
        """Sets the publicip_pools of this CommonPoolsWithBorderGroupDict.

        同组的公共池列表

        :param publicip_pools: The publicip_pools of this CommonPoolsWithBorderGroupDict.
        :type publicip_pools: list[str]
        """
        self._publicip_pools = publicip_pools

    @property
    def public_border_group(self):
        """Gets the public_border_group of this CommonPoolsWithBorderGroupDict.

        分组：中心还是边缘

        :return: The public_border_group of this CommonPoolsWithBorderGroupDict.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this CommonPoolsWithBorderGroupDict.

        分组：中心还是边缘

        :param public_border_group: The public_border_group of this CommonPoolsWithBorderGroupDict.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, CommonPoolsWithBorderGroupDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
