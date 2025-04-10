# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApicInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_instances': 'list[ApigInstanceDTO]'
    }

    attribute_map = {
        'gateway_instances': 'gateway_instances'
    }

    def __init__(self, gateway_instances=None):
        r"""ListApicInstancesResponse

        The model defined in huaweicloud sdk

        :param gateway_instances: 网关实例
        :type gateway_instances: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigInstanceDTO`]
        """
        
        super(ListApicInstancesResponse, self).__init__()

        self._gateway_instances = None
        self.discriminator = None

        if gateway_instances is not None:
            self.gateway_instances = gateway_instances

    @property
    def gateway_instances(self):
        r"""Gets the gateway_instances of this ListApicInstancesResponse.

        网关实例

        :return: The gateway_instances of this ListApicInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigInstanceDTO`]
        """
        return self._gateway_instances

    @gateway_instances.setter
    def gateway_instances(self, gateway_instances):
        r"""Sets the gateway_instances of this ListApicInstancesResponse.

        网关实例

        :param gateway_instances: The gateway_instances of this ListApicInstancesResponse.
        :type gateway_instances: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigInstanceDTO`]
        """
        self._gateway_instances = gateway_instances

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
        if not isinstance(other, ListApicInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
