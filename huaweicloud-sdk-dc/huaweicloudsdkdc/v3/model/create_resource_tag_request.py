# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceTagRequest:

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
        'body': 'CreateResourceTagRequestBody'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_id=None, resource_type=None, body=None):
        r"""CreateResourceTagRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源实例ID
        :type resource_id: str
        :param resource_type: - 专线服务资源类型，包括dc-directconnect/dc-vgw/dc-vif - dc-directconnect: 专线物理连接 - dc-vgw： 虚拟网关 - dc-vif： 虚拟接口
        :type resource_type: str
        :param body: Body of the CreateResourceTagRequest
        :type body: :class:`huaweicloudsdkdc.v3.CreateResourceTagRequestBody`
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
        r"""Gets the resource_id of this CreateResourceTagRequest.

        资源实例ID

        :return: The resource_id of this CreateResourceTagRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateResourceTagRequest.

        资源实例ID

        :param resource_id: The resource_id of this CreateResourceTagRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateResourceTagRequest.

        - 专线服务资源类型，包括dc-directconnect/dc-vgw/dc-vif - dc-directconnect: 专线物理连接 - dc-vgw： 虚拟网关 - dc-vif： 虚拟接口

        :return: The resource_type of this CreateResourceTagRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateResourceTagRequest.

        - 专线服务资源类型，包括dc-directconnect/dc-vgw/dc-vif - dc-directconnect: 专线物理连接 - dc-vgw： 虚拟网关 - dc-vif： 虚拟接口

        :param resource_type: The resource_type of this CreateResourceTagRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        r"""Gets the body of this CreateResourceTagRequest.

        :return: The body of this CreateResourceTagRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateResourceTagRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateResourceTagRequest.

        :param body: The body of this CreateResourceTagRequest.
        :type body: :class:`huaweicloudsdkdc.v3.CreateResourceTagRequestBody`
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
        if not isinstance(other, CreateResourceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
