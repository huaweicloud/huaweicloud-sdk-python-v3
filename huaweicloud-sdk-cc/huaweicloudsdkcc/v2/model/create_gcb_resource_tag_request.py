# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGcbResourceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'body': 'CreateGcbTagRequestBody'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_id=None, body=None):
        """CreateGcbResourceTagRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源唯一标识符。
        :type resource_id: str
        :param body: Body of the CreateGcbResourceTagRequest
        :type body: :class:`huaweicloudsdkcc.v2.CreateGcbTagRequestBody`
        """
        
        

        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_id(self):
        """Gets the resource_id of this CreateGcbResourceTagRequest.

        资源唯一标识符。

        :return: The resource_id of this CreateGcbResourceTagRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CreateGcbResourceTagRequest.

        资源唯一标识符。

        :param resource_id: The resource_id of this CreateGcbResourceTagRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        """Gets the body of this CreateGcbResourceTagRequest.

        :return: The body of this CreateGcbResourceTagRequest.
        :rtype: :class:`huaweicloudsdkcc.v2.CreateGcbTagRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateGcbResourceTagRequest.

        :param body: The body of this CreateGcbResourceTagRequest.
        :type body: :class:`huaweicloudsdkcc.v2.CreateGcbTagRequestBody`
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
        if not isinstance(other, CreateGcbResourceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
