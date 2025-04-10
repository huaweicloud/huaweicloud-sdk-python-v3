# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessPreviewReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configurations': 'Configuration',
        'resource_urn': 'str'
    }

    attribute_map = {
        'configurations': 'configurations',
        'resource_urn': 'resource_urn'
    }

    def __init__(self, configurations=None, resource_urn=None):
        r"""CreateAccessPreviewReqBody

        The model defined in huaweicloud sdk

        :param configurations: 
        :type configurations: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        :param resource_urn: 资源的唯一资源标识符。
        :type resource_urn: str
        """
        
        

        self._configurations = None
        self._resource_urn = None
        self.discriminator = None

        self.configurations = configurations
        self.resource_urn = resource_urn

    @property
    def configurations(self):
        r"""Gets the configurations of this CreateAccessPreviewReqBody.

        :return: The configurations of this CreateAccessPreviewReqBody.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this CreateAccessPreviewReqBody.

        :param configurations: The configurations of this CreateAccessPreviewReqBody.
        :type configurations: :class:`huaweicloudsdkiamaccessanalyzer.v1.Configuration`
        """
        self._configurations = configurations

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this CreateAccessPreviewReqBody.

        资源的唯一资源标识符。

        :return: The resource_urn of this CreateAccessPreviewReqBody.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this CreateAccessPreviewReqBody.

        资源的唯一资源标识符。

        :param resource_urn: The resource_urn of this CreateAccessPreviewReqBody.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

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
        if not isinstance(other, CreateAccessPreviewReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
