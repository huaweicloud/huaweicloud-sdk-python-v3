# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteApplicationEndpointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_urn': 'str'
    }

    attribute_map = {
        'endpoint_urn': 'endpoint_urn'
    }

    def __init__(self, endpoint_urn=None):
        r"""DeleteApplicationEndpointRequest

        The model defined in huaweicloud sdk

        :param endpoint_urn: Endpoint的唯一资源标识，可通过[查询Application的Endpoint列表](smn_api_58004.xml)获取该标识。
        :type endpoint_urn: str
        """
        
        

        self._endpoint_urn = None
        self.discriminator = None

        self.endpoint_urn = endpoint_urn

    @property
    def endpoint_urn(self):
        r"""Gets the endpoint_urn of this DeleteApplicationEndpointRequest.

        Endpoint的唯一资源标识，可通过[查询Application的Endpoint列表](smn_api_58004.xml)获取该标识。

        :return: The endpoint_urn of this DeleteApplicationEndpointRequest.
        :rtype: str
        """
        return self._endpoint_urn

    @endpoint_urn.setter
    def endpoint_urn(self, endpoint_urn):
        r"""Sets the endpoint_urn of this DeleteApplicationEndpointRequest.

        Endpoint的唯一资源标识，可通过[查询Application的Endpoint列表](smn_api_58004.xml)获取该标识。

        :param endpoint_urn: The endpoint_urn of this DeleteApplicationEndpointRequest.
        :type endpoint_urn: str
        """
        self._endpoint_urn = endpoint_urn

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
        if not isinstance(other, DeleteApplicationEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
