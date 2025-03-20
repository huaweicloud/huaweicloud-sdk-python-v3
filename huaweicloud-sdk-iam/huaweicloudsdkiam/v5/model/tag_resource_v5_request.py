# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagResourceV5Request:

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
        'resource_type': 'str',
        'body': 'Tags'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_id=None, resource_type=None, body=None):
        """TagResourceV5Request

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type resource_id: str
        :param resource_type: 资源类型，可以为“信任委托”（agency）或“IAM用户”（user）。
        :type resource_type: str
        :param body: Body of the TagResourceV5Request
        :type body: :class:`huaweicloudsdkiam.v5.Tags`
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._body = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def resource_id(self):
        """Gets the resource_id of this TagResourceV5Request.

        资源ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The resource_id of this TagResourceV5Request.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this TagResourceV5Request.

        资源ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param resource_id: The resource_id of this TagResourceV5Request.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this TagResourceV5Request.

        资源类型，可以为“信任委托”（agency）或“IAM用户”（user）。

        :return: The resource_type of this TagResourceV5Request.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TagResourceV5Request.

        资源类型，可以为“信任委托”（agency）或“IAM用户”（user）。

        :param resource_type: The resource_type of this TagResourceV5Request.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this TagResourceV5Request.

        :return: The body of this TagResourceV5Request.
        :rtype: :class:`huaweicloudsdkiam.v5.Tags`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this TagResourceV5Request.

        :param body: The body of this TagResourceV5Request.
        :type body: :class:`huaweicloudsdkiam.v5.Tags`
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
        if not isinstance(other, TagResourceV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
