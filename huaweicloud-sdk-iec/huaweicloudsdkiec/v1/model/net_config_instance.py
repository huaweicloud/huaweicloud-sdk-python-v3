# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetConfigInstance:

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
        'subnets': 'list[SubnetConfig]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnets': 'subnets'
    }

    def __init__(self, vpc_id=None, subnets=None):
        r"""NetConfigInstance

        The model defined in huaweicloud sdk

        :param vpc_id: 边缘网络ID。
        :type vpc_id: str
        :param subnets: 待创建边缘实例子网信息。  需要指定vpcid对应VPC下已创建的子网（subnet）的网络ID，UUID格式。
        :type subnets: list[:class:`huaweicloudsdkiec.v1.SubnetConfig`]
        """
        
        

        self._vpc_id = None
        self._subnets = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnets = subnets

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this NetConfigInstance.

        边缘网络ID。

        :return: The vpc_id of this NetConfigInstance.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this NetConfigInstance.

        边缘网络ID。

        :param vpc_id: The vpc_id of this NetConfigInstance.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnets(self):
        r"""Gets the subnets of this NetConfigInstance.

        待创建边缘实例子网信息。  需要指定vpcid对应VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :return: The subnets of this NetConfigInstance.
        :rtype: list[:class:`huaweicloudsdkiec.v1.SubnetConfig`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        r"""Sets the subnets of this NetConfigInstance.

        待创建边缘实例子网信息。  需要指定vpcid对应VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :param subnets: The subnets of this NetConfigInstance.
        :type subnets: list[:class:`huaweicloudsdkiec.v1.SubnetConfig`]
        """
        self._subnets = subnets

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
        if not isinstance(other, NetConfigInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
