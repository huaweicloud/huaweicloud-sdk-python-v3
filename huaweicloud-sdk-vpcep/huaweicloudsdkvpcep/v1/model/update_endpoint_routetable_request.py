# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointRoutetableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_endpoint_id': 'str',
        'body': 'UpdateEndpointRoutetableRequestBody'
    }

    attribute_map = {
        'vpc_endpoint_id': 'vpc_endpoint_id',
        'body': 'body'
    }

    def __init__(self, vpc_endpoint_id=None, body=None):
        """UpdateEndpointRoutetableRequest

        The model defined in huaweicloud sdk

        :param vpc_endpoint_id: 终端节点的ID。
        :type vpc_endpoint_id: str
        :param body: Body of the UpdateEndpointRoutetableRequest
        :type body: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableRequestBody`
        """
        
        

        self._vpc_endpoint_id = None
        self._body = None
        self.discriminator = None

        self.vpc_endpoint_id = vpc_endpoint_id
        if body is not None:
            self.body = body

    @property
    def vpc_endpoint_id(self):
        """Gets the vpc_endpoint_id of this UpdateEndpointRoutetableRequest.

        终端节点的ID。

        :return: The vpc_endpoint_id of this UpdateEndpointRoutetableRequest.
        :rtype: str
        """
        return self._vpc_endpoint_id

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, vpc_endpoint_id):
        """Sets the vpc_endpoint_id of this UpdateEndpointRoutetableRequest.

        终端节点的ID。

        :param vpc_endpoint_id: The vpc_endpoint_id of this UpdateEndpointRoutetableRequest.
        :type vpc_endpoint_id: str
        """
        self._vpc_endpoint_id = vpc_endpoint_id

    @property
    def body(self):
        """Gets the body of this UpdateEndpointRoutetableRequest.

        :return: The body of this UpdateEndpointRoutetableRequest.
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEndpointRoutetableRequest.

        :param body: The body of this UpdateEndpointRoutetableRequest.
        :type body: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateEndpointRoutetableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
