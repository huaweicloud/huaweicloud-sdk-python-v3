# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddResourceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str',
        'body': 'ResourceTagRequest'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_type=None, resource_id=None, body=None):
        r"""BatchAddResourceTagRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - auditInstance
        :type resource_type: str
        :param resource_id: 资源ID。可在查询实例列表接口的resource_id字段获取。
        :type resource_id: str
        :param body: Body of the BatchAddResourceTagRequest
        :type body: :class:`huaweicloudsdkdbss.v1.ResourceTagRequest`
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        r"""Gets the resource_type of this BatchAddResourceTagRequest.

        资源类型。 - auditInstance

        :return: The resource_type of this BatchAddResourceTagRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this BatchAddResourceTagRequest.

        资源类型。 - auditInstance

        :param resource_type: The resource_type of this BatchAddResourceTagRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BatchAddResourceTagRequest.

        资源ID。可在查询实例列表接口的resource_id字段获取。

        :return: The resource_id of this BatchAddResourceTagRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BatchAddResourceTagRequest.

        资源ID。可在查询实例列表接口的resource_id字段获取。

        :param resource_id: The resource_id of this BatchAddResourceTagRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        r"""Gets the body of this BatchAddResourceTagRequest.

        :return: The body of this BatchAddResourceTagRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.ResourceTagRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchAddResourceTagRequest.

        :param body: The body of this BatchAddResourceTagRequest.
        :type body: :class:`huaweicloudsdkdbss.v1.ResourceTagRequest`
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
        if not isinstance(other, BatchAddResourceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
