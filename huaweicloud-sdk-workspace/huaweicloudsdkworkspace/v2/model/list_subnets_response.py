# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnets': 'list[SubnetInfo]',
        'subnet_size': 'int'
    }

    attribute_map = {
        'subnets': 'subnets',
        'subnet_size': 'subnet_size'
    }

    def __init__(self, subnets=None, subnet_size=None):
        r"""ListSubnetsResponse

        The model defined in huaweicloud sdk

        :param subnets: 子网列表。
        :type subnets: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        :param subnet_size: 子网数量。
        :type subnet_size: int
        """
        
        super().__init__()

        self._subnets = None
        self._subnet_size = None
        self.discriminator = None

        if subnets is not None:
            self.subnets = subnets
        if subnet_size is not None:
            self.subnet_size = subnet_size

    @property
    def subnets(self):
        r"""Gets the subnets of this ListSubnetsResponse.

        子网列表。

        :return: The subnets of this ListSubnetsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        r"""Sets the subnets of this ListSubnetsResponse.

        子网列表。

        :param subnets: The subnets of this ListSubnetsResponse.
        :type subnets: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        """
        self._subnets = subnets

    @property
    def subnet_size(self):
        r"""Gets the subnet_size of this ListSubnetsResponse.

        子网数量。

        :return: The subnet_size of this ListSubnetsResponse.
        :rtype: int
        """
        return self._subnet_size

    @subnet_size.setter
    def subnet_size(self, subnet_size):
        r"""Sets the subnet_size of this ListSubnetsResponse.

        子网数量。

        :param subnet_size: The subnet_size of this ListSubnetsResponse.
        :type subnet_size: int
        """
        self._subnet_size = subnet_size

    def to_dict(self):
        import warnings
        warnings.warn("ListSubnetsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubnetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
