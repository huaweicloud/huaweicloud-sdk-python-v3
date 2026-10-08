# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayCloudServiceApiTargetConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'payload': 'str'
    }

    attribute_map = {
        'payload': 'payload'
    }

    def __init__(self, payload=None):
        r"""CoreGatewayCloudServiceApiTargetConfiguration

        The model defined in huaweicloud sdk

        :param payload: OpenAPI规范文档内容（JSON或YAML格式的内联内容）。
        :type payload: str
        """
        
        

        self._payload = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload

    @property
    def payload(self):
        r"""Gets the payload of this CoreGatewayCloudServiceApiTargetConfiguration.

        OpenAPI规范文档内容（JSON或YAML格式的内联内容）。

        :return: The payload of this CoreGatewayCloudServiceApiTargetConfiguration.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        r"""Sets the payload of this CoreGatewayCloudServiceApiTargetConfiguration.

        OpenAPI规范文档内容（JSON或YAML格式的内联内容）。

        :param payload: The payload of this CoreGatewayCloudServiceApiTargetConfiguration.
        :type payload: str
        """
        self._payload = payload

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
        if not isinstance(other, CoreGatewayCloudServiceApiTargetConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
