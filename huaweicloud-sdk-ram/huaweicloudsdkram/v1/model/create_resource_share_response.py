# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceShareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share': 'ResourceShare'
    }

    attribute_map = {
        'resource_share': 'resource_share'
    }

    def __init__(self, resource_share=None):
        r"""CreateResourceShareResponse

        The model defined in huaweicloud sdk

        :param resource_share: 
        :type resource_share: :class:`huaweicloudsdkram.v1.ResourceShare`
        """
        
        super(CreateResourceShareResponse, self).__init__()

        self._resource_share = None
        self.discriminator = None

        if resource_share is not None:
            self.resource_share = resource_share

    @property
    def resource_share(self):
        r"""Gets the resource_share of this CreateResourceShareResponse.

        :return: The resource_share of this CreateResourceShareResponse.
        :rtype: :class:`huaweicloudsdkram.v1.ResourceShare`
        """
        return self._resource_share

    @resource_share.setter
    def resource_share(self, resource_share):
        r"""Sets the resource_share of this CreateResourceShareResponse.

        :param resource_share: The resource_share of this CreateResourceShareResponse.
        :type resource_share: :class:`huaweicloudsdkram.v1.ResourceShare`
        """
        self._resource_share = resource_share

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
        if not isinstance(other, CreateResourceShareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
