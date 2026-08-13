# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTargetFlavorsResponse(SdkResponse):

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
        'flavors': 'list[FlavorInfoResponse]',
        'change_mode': 'str'
    }

    attribute_map = {
        'count': 'count',
        'flavors': 'flavors',
        'change_mode': 'change_mode'
    }

    def __init__(self, count=None, flavors=None, change_mode=None):
        r"""ListTargetFlavorsResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 规格数量。 **取值范围**： 不涉及。
        :type count: int
        :param flavors: **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。
        :type flavors: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        :param change_mode: **参数解释**： 规格变更模式。 **取值范围**： online：在线模式； offline：离线模式； all：在线模式、离线模式都支持。
        :type change_mode: str
        """
        
        super().__init__()

        self._count = None
        self._flavors = None
        self._change_mode = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if flavors is not None:
            self.flavors = flavors
        if change_mode is not None:
            self.change_mode = change_mode

    @property
    def count(self):
        r"""Gets the count of this ListTargetFlavorsResponse.

        **参数解释**： 规格数量。 **取值范围**： 不涉及。

        :return: The count of this ListTargetFlavorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTargetFlavorsResponse.

        **参数解释**： 规格数量。 **取值范围**： 不涉及。

        :param count: The count of this ListTargetFlavorsResponse.
        :type count: int
        """
        self._count = count

    @property
    def flavors(self):
        r"""Gets the flavors of this ListTargetFlavorsResponse.

        **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。

        :return: The flavors of this ListTargetFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ListTargetFlavorsResponse.

        **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。

        :param flavors: The flavors of this ListTargetFlavorsResponse.
        :type flavors: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        """
        self._flavors = flavors

    @property
    def change_mode(self):
        r"""Gets the change_mode of this ListTargetFlavorsResponse.

        **参数解释**： 规格变更模式。 **取值范围**： online：在线模式； offline：离线模式； all：在线模式、离线模式都支持。

        :return: The change_mode of this ListTargetFlavorsResponse.
        :rtype: str
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        r"""Sets the change_mode of this ListTargetFlavorsResponse.

        **参数解释**： 规格变更模式。 **取值范围**： online：在线模式； offline：离线模式； all：在线模式、离线模式都支持。

        :param change_mode: The change_mode of this ListTargetFlavorsResponse.
        :type change_mode: str
        """
        self._change_mode = change_mode

    def to_dict(self):
        import warnings
        warnings.warn("ListTargetFlavorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTargetFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
