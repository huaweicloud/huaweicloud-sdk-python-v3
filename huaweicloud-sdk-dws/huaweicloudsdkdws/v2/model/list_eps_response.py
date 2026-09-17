# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[SysTagResp]',
        'count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'count': 'count'
    }

    def __init__(self, resources=None, count=None):
        r"""ListEpsResponse

        The model defined in huaweicloud sdk

        :param resources: **参数解释**： 集群及关联的企业项目信息。 **取值范围**： 不涉及。
        :type resources: list[:class:`huaweicloudsdkdws.v2.SysTagResp`]
        :param count: **参数解释**： 分页总条数。 **取值范围**： 大于等于0
        :type count: int
        """
        
        super().__init__()

        self._resources = None
        self._count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if count is not None:
            self.count = count

    @property
    def resources(self):
        r"""Gets the resources of this ListEpsResponse.

        **参数解释**： 集群及关联的企业项目信息。 **取值范围**： 不涉及。

        :return: The resources of this ListEpsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.SysTagResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListEpsResponse.

        **参数解释**： 集群及关联的企业项目信息。 **取值范围**： 不涉及。

        :param resources: The resources of this ListEpsResponse.
        :type resources: list[:class:`huaweicloudsdkdws.v2.SysTagResp`]
        """
        self._resources = resources

    @property
    def count(self):
        r"""Gets the count of this ListEpsResponse.

        **参数解释**： 分页总条数。 **取值范围**： 大于等于0

        :return: The count of this ListEpsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListEpsResponse.

        **参数解释**： 分页总条数。 **取值范围**： 大于等于0

        :param count: The count of this ListEpsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListEpsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListEpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
