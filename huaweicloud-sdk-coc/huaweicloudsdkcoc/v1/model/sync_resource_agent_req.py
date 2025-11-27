# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncResourceAgentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_infos': 'list[SyncResourceAgentReqResourceInfos]',
        'vendor': 'str'
    }

    attribute_map = {
        'resource_infos': 'resource_infos',
        'vendor': 'vendor'
    }

    def __init__(self, resource_infos=None, vendor=None):
        r"""SyncResourceAgentReq

        The model defined in huaweicloud sdk

        :param resource_infos: **参数解释：** 资源信息。 **约束限制：** 不涉及。 **取值范围：** 选择需要同步的资源对应的资源信息，列表大小1~100之间。 **默认取值：** 不涉及。
        :type resource_infos: list[:class:`huaweicloudsdkcoc.v1.SyncResourceAgentReqResourceInfos`]
        :param vendor: **参数解释：** 云厂商。 **约束限制：** 不涉及。 **取值范围：** - 华为云资源同步时，可以不传。 - 阿里云资源同步时，传ALI。 **默认取值：** 不涉及。
        :type vendor: str
        """
        
        

        self._resource_infos = None
        self._vendor = None
        self.discriminator = None

        if resource_infos is not None:
            self.resource_infos = resource_infos
        if vendor is not None:
            self.vendor = vendor

    @property
    def resource_infos(self):
        r"""Gets the resource_infos of this SyncResourceAgentReq.

        **参数解释：** 资源信息。 **约束限制：** 不涉及。 **取值范围：** 选择需要同步的资源对应的资源信息，列表大小1~100之间。 **默认取值：** 不涉及。

        :return: The resource_infos of this SyncResourceAgentReq.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SyncResourceAgentReqResourceInfos`]
        """
        return self._resource_infos

    @resource_infos.setter
    def resource_infos(self, resource_infos):
        r"""Sets the resource_infos of this SyncResourceAgentReq.

        **参数解释：** 资源信息。 **约束限制：** 不涉及。 **取值范围：** 选择需要同步的资源对应的资源信息，列表大小1~100之间。 **默认取值：** 不涉及。

        :param resource_infos: The resource_infos of this SyncResourceAgentReq.
        :type resource_infos: list[:class:`huaweicloudsdkcoc.v1.SyncResourceAgentReqResourceInfos`]
        """
        self._resource_infos = resource_infos

    @property
    def vendor(self):
        r"""Gets the vendor of this SyncResourceAgentReq.

        **参数解释：** 云厂商。 **约束限制：** 不涉及。 **取值范围：** - 华为云资源同步时，可以不传。 - 阿里云资源同步时，传ALI。 **默认取值：** 不涉及。

        :return: The vendor of this SyncResourceAgentReq.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this SyncResourceAgentReq.

        **参数解释：** 云厂商。 **约束限制：** 不涉及。 **取值范围：** - 华为云资源同步时，可以不传。 - 阿里云资源同步时，传ALI。 **默认取值：** 不涉及。

        :param vendor: The vendor of this SyncResourceAgentReq.
        :type vendor: str
        """
        self._vendor = vendor

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
        if not isinstance(other, SyncResourceAgentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
