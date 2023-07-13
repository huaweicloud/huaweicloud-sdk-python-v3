# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownlinkVpc:

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
        'virsubnet_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id'
    }

    def __init__(self, vpc_id=None, virsubnet_id=None):
        """DownlinkVpc

        The model defined in huaweicloud sdk

        :param vpc_id: 私网NAT网关实例所属VPC的ID。
        :type vpc_id: str
        :param virsubnet_id: 私网NAT网关实例所属子网的ID。
        :type virsubnet_id: str
        """
        
        

        self._vpc_id = None
        self._virsubnet_id = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DownlinkVpc.

        私网NAT网关实例所属VPC的ID。

        :return: The vpc_id of this DownlinkVpc.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DownlinkVpc.

        私网NAT网关实例所属VPC的ID。

        :param vpc_id: The vpc_id of this DownlinkVpc.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this DownlinkVpc.

        私网NAT网关实例所属子网的ID。

        :return: The virsubnet_id of this DownlinkVpc.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this DownlinkVpc.

        私网NAT网关实例所属子网的ID。

        :param virsubnet_id: The virsubnet_id of this DownlinkVpc.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

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
        if not isinstance(other, DownlinkVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
