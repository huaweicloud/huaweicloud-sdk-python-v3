# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_group': 'EndpointGroupDetail',
        'request_id': 'str'
    }

    attribute_map = {
        'endpoint_group': 'endpoint_group',
        'request_id': 'request_id'
    }

    def __init__(self, endpoint_group=None, request_id=None):
        """CreateEndpointGroupResponse

        The model defined in huaweicloud sdk

        :param endpoint_group: 
        :type endpoint_group: :class:`huaweicloudsdkga.v1.EndpointGroupDetail`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(CreateEndpointGroupResponse, self).__init__()

        self._endpoint_group = None
        self._request_id = None
        self.discriminator = None

        if endpoint_group is not None:
            self.endpoint_group = endpoint_group
        if request_id is not None:
            self.request_id = request_id

    @property
    def endpoint_group(self):
        """Gets the endpoint_group of this CreateEndpointGroupResponse.

        :return: The endpoint_group of this CreateEndpointGroupResponse.
        :rtype: :class:`huaweicloudsdkga.v1.EndpointGroupDetail`
        """
        return self._endpoint_group

    @endpoint_group.setter
    def endpoint_group(self, endpoint_group):
        """Sets the endpoint_group of this CreateEndpointGroupResponse.

        :param endpoint_group: The endpoint_group of this CreateEndpointGroupResponse.
        :type endpoint_group: :class:`huaweicloudsdkga.v1.EndpointGroupDetail`
        """
        self._endpoint_group = endpoint_group

    @property
    def request_id(self):
        """Gets the request_id of this CreateEndpointGroupResponse.

        请求ID。

        :return: The request_id of this CreateEndpointGroupResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateEndpointGroupResponse.

        请求ID。

        :param request_id: The request_id of this CreateEndpointGroupResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, CreateEndpointGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
