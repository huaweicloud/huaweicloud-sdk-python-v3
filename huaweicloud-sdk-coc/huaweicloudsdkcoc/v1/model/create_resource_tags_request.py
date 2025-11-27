# coding: utf-8

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
        'body': 'ResourceTagOperateRequest'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_id=None, body=None):
        r"""CreateResourceTagsRequest

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释：** 资源ID。 **约束限制：** 不涉及。 **取值范围：** 标签对应的资源id。 **默认取值：** 不涉及。
        :type resource_id: str
        :param body: Body of the CreateResourceTagsRequest
        :type body: :class:`huaweicloudsdkcoc.v1.ResourceTagOperateRequest`
        """
        
        

        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateResourceTagsRequest.

        **参数解释：** 资源ID。 **约束限制：** 不涉及。 **取值范围：** 标签对应的资源id。 **默认取值：** 不涉及。

        :return: The resource_id of this CreateResourceTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateResourceTagsRequest.

        **参数解释：** 资源ID。 **约束限制：** 不涉及。 **取值范围：** 标签对应的资源id。 **默认取值：** 不涉及。

        :param resource_id: The resource_id of this CreateResourceTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        r"""Gets the body of this CreateResourceTagsRequest.

        :return: The body of this CreateResourceTagsRequest.
        :rtype: :class:`huaweicloudsdkcoc.v1.ResourceTagOperateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateResourceTagsRequest.

        :param body: The body of this CreateResourceTagsRequest.
        :type body: :class:`huaweicloudsdkcoc.v1.ResourceTagOperateRequest`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
