# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewaysByTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'resources': 'list[CoreGatewaysResourceInstanceForTMS]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'resources': 'resources'
    }

    def __init__(self, total_count=None, resources=None):
        r"""ListCoreGatewaysByTagsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释：** 总记录数。 **取值范围：** 非负整数。 
        :type total_count: int
        :param resources: **参数解释：** 根据标签查询网关的资源实例列表。 **取值范围：** 数组长度0-1000。 
        :type resources: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysResourceInstanceForTMS`]
        """
        
        super().__init__()

        self._total_count = None
        self._resources = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if resources is not None:
            self.resources = resources

    @property
    def total_count(self):
        r"""Gets the total_count of this ListCoreGatewaysByTagsResponse.

        **参数解释：** 总记录数。 **取值范围：** 非负整数。 

        :return: The total_count of this ListCoreGatewaysByTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListCoreGatewaysByTagsResponse.

        **参数解释：** 总记录数。 **取值范围：** 非负整数。 

        :param total_count: The total_count of this ListCoreGatewaysByTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def resources(self):
        r"""Gets the resources of this ListCoreGatewaysByTagsResponse.

        **参数解释：** 根据标签查询网关的资源实例列表。 **取值范围：** 数组长度0-1000。 

        :return: The resources of this ListCoreGatewaysByTagsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysResourceInstanceForTMS`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListCoreGatewaysByTagsResponse.

        **参数解释：** 根据标签查询网关的资源实例列表。 **取值范围：** 数组长度0-1000。 

        :param resources: The resources of this ListCoreGatewaysByTagsResponse.
        :type resources: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysResourceInstanceForTMS`]
        """
        self._resources = resources

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreGatewaysByTagsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreGatewaysByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
