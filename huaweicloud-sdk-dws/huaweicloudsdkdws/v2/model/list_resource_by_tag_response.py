# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceByTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'resources': 'list[TagFilter]'
    }

    attribute_map = {
        'count': 'count',
        'resources': 'resources'
    }

    def __init__(self, count=None, resources=None):
        r"""ListResourceByTagResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type count: int
        :param resources: **参数解释**： 资源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type resources: list[:class:`huaweicloudsdkdws.v2.TagFilter`]
        """
        
        super().__init__()

        self._count = None
        self._resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if resources is not None:
            self.resources = resources

    @property
    def count(self):
        r"""Gets the count of this ListResourceByTagResponse.

        **参数解释**： 标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The count of this ListResourceByTagResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListResourceByTagResponse.

        **参数解释**： 标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param count: The count of this ListResourceByTagResponse.
        :type count: int
        """
        self._count = count

    @property
    def resources(self):
        r"""Gets the resources of this ListResourceByTagResponse.

        **参数解释**： 资源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The resources of this ListResourceByTagResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TagFilter`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListResourceByTagResponse.

        **参数解释**： 资源信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param resources: The resources of this ListResourceByTagResponse.
        :type resources: list[:class:`huaweicloudsdkdws.v2.TagFilter`]
        """
        self._resources = resources

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceByTagResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListResourceByTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
