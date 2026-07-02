# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayWorkloadIdentity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urn': 'str'
    }

    attribute_map = {
        'urn': 'urn'
    }

    def __init__(self, urn=None):
        r"""CoreGatewayWorkloadIdentity

        The model defined in huaweicloud sdk

        :param urn: 工作负载标识的统一资源名称。
        :type urn: str
        """
        
        

        self._urn = None
        self.discriminator = None

        if urn is not None:
            self.urn = urn

    @property
    def urn(self):
        r"""Gets the urn of this CoreGatewayWorkloadIdentity.

        工作负载标识的统一资源名称。

        :return: The urn of this CoreGatewayWorkloadIdentity.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this CoreGatewayWorkloadIdentity.

        工作负载标识的统一资源名称。

        :param urn: The urn of this CoreGatewayWorkloadIdentity.
        :type urn: str
        """
        self._urn = urn

    def to_dict(self):
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
        if not isinstance(other, CoreGatewayWorkloadIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
