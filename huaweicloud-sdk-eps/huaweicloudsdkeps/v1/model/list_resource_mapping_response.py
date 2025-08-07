# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceMappingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_mapping': 'dict(str, str)'
    }

    attribute_map = {
        'resource_mapping': 'resource_mapping'
    }

    def __init__(self, resource_mapping=None):
        r"""ListResourceMappingResponse

        The model defined in huaweicloud sdk

        :param resource_mapping: 资源类型映射
        :type resource_mapping: dict(str, str)
        """
        
        super(ListResourceMappingResponse, self).__init__()

        self._resource_mapping = None
        self.discriminator = None

        if resource_mapping is not None:
            self.resource_mapping = resource_mapping

    @property
    def resource_mapping(self):
        r"""Gets the resource_mapping of this ListResourceMappingResponse.

        资源类型映射

        :return: The resource_mapping of this ListResourceMappingResponse.
        :rtype: dict(str, str)
        """
        return self._resource_mapping

    @resource_mapping.setter
    def resource_mapping(self, resource_mapping):
        r"""Sets the resource_mapping of this ListResourceMappingResponse.

        资源类型映射

        :param resource_mapping: The resource_mapping of this ListResourceMappingResponse.
        :type resource_mapping: dict(str, str)
        """
        self._resource_mapping = resource_mapping

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
        if not isinstance(other, ListResourceMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
