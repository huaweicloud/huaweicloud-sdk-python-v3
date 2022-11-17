# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRemoveEndpointServicePermissionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_endpoint_service_id': 'str',
        'body': 'BatchRemovePermissionRequest'
    }

    attribute_map = {
        'vpc_endpoint_service_id': 'vpc_endpoint_service_id',
        'body': 'body'
    }

    def __init__(self, vpc_endpoint_service_id=None, body=None):
        """BatchRemoveEndpointServicePermissionsRequest

        The model defined in huaweicloud sdk

        :param vpc_endpoint_service_id: 终端节点服务的ID。
        :type vpc_endpoint_service_id: str
        :param body: Body of the BatchRemoveEndpointServicePermissionsRequest
        :type body: :class:`huaweicloudsdkvpcep.v1.BatchRemovePermissionRequest`
        """
        
        

        self._vpc_endpoint_service_id = None
        self._body = None
        self.discriminator = None

        self.vpc_endpoint_service_id = vpc_endpoint_service_id
        if body is not None:
            self.body = body

    @property
    def vpc_endpoint_service_id(self):
        """Gets the vpc_endpoint_service_id of this BatchRemoveEndpointServicePermissionsRequest.

        终端节点服务的ID。

        :return: The vpc_endpoint_service_id of this BatchRemoveEndpointServicePermissionsRequest.
        :rtype: str
        """
        return self._vpc_endpoint_service_id

    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, vpc_endpoint_service_id):
        """Sets the vpc_endpoint_service_id of this BatchRemoveEndpointServicePermissionsRequest.

        终端节点服务的ID。

        :param vpc_endpoint_service_id: The vpc_endpoint_service_id of this BatchRemoveEndpointServicePermissionsRequest.
        :type vpc_endpoint_service_id: str
        """
        self._vpc_endpoint_service_id = vpc_endpoint_service_id

    @property
    def body(self):
        """Gets the body of this BatchRemoveEndpointServicePermissionsRequest.

        :return: The body of this BatchRemoveEndpointServicePermissionsRequest.
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchRemovePermissionRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchRemoveEndpointServicePermissionsRequest.

        :param body: The body of this BatchRemoveEndpointServicePermissionsRequest.
        :type body: :class:`huaweicloudsdkvpcep.v1.BatchRemovePermissionRequest`
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
        if not isinstance(other, BatchRemoveEndpointServicePermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
