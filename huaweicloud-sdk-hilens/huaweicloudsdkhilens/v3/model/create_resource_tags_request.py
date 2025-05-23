# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceTagsRequest:

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
        'body': 'TagRequestDetail'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_id=None, resource_type=None, body=None):
        r"""CreateResourceTagsRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID
        :type resource_id: str
        :param resource_type: 资源类型（节点，部署，配置项，密钥）
        :type resource_type: str
        :param body: Body of the CreateResourceTagsRequest
        :type body: :class:`huaweicloudsdkhilens.v3.TagRequestDetail`
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
        r"""Gets the resource_id of this CreateResourceTagsRequest.

        资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID

        :return: The resource_id of this CreateResourceTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateResourceTagsRequest.

        资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID

        :param resource_id: The resource_id of this CreateResourceTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateResourceTagsRequest.

        资源类型（节点，部署，配置项，密钥）

        :return: The resource_type of this CreateResourceTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateResourceTagsRequest.

        资源类型（节点，部署，配置项，密钥）

        :param resource_type: The resource_type of this CreateResourceTagsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        r"""Gets the body of this CreateResourceTagsRequest.

        :return: The body of this CreateResourceTagsRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.TagRequestDetail`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateResourceTagsRequest.

        :param body: The body of this CreateResourceTagsRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.TagRequestDetail`
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
        if not isinstance(other, CreateResourceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
