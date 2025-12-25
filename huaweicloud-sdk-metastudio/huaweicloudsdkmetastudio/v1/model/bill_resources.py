# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillResources:

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
        'resource_nums': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_nums': 'resource_nums'
    }

    def __init__(self, resource_type=None, resource_nums=None):
        r"""BillResources

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 当前支持的形象资源类型如下： * 2D_DIGITAL_HUMAN_BASIC：形象制作基础版 * 2D_DIGITAL_HUMAN_ADVANCED：形象制作高级版 * 2D_DIGITAL_HUMAN_FLEXUS：形象制作FLEXUS版  当前支持的声音资源类型如下： * VOICE_BASIC: 声音制作基础版 * VOICE_MIDDLE: 声音制作进阶版 * VOICE_ADVANCE：声音制作高级版 * VOICE_THIRD_PARTY：声音制作第三方出门问问 * VOICE_THIRD_PARTY_LJZN: 声音制作第三方逻辑智能 * VOICE_FLEXUS: 声音制作Flexus版资源
        :type resource_type: str
        :param resource_nums: 资源数量。
        :type resource_nums: int
        """
        
        

        self._resource_type = None
        self._resource_nums = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_nums is not None:
            self.resource_nums = resource_nums

    @property
    def resource_type(self):
        r"""Gets the resource_type of this BillResources.

        资源类型。 当前支持的形象资源类型如下： * 2D_DIGITAL_HUMAN_BASIC：形象制作基础版 * 2D_DIGITAL_HUMAN_ADVANCED：形象制作高级版 * 2D_DIGITAL_HUMAN_FLEXUS：形象制作FLEXUS版  当前支持的声音资源类型如下： * VOICE_BASIC: 声音制作基础版 * VOICE_MIDDLE: 声音制作进阶版 * VOICE_ADVANCE：声音制作高级版 * VOICE_THIRD_PARTY：声音制作第三方出门问问 * VOICE_THIRD_PARTY_LJZN: 声音制作第三方逻辑智能 * VOICE_FLEXUS: 声音制作Flexus版资源

        :return: The resource_type of this BillResources.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this BillResources.

        资源类型。 当前支持的形象资源类型如下： * 2D_DIGITAL_HUMAN_BASIC：形象制作基础版 * 2D_DIGITAL_HUMAN_ADVANCED：形象制作高级版 * 2D_DIGITAL_HUMAN_FLEXUS：形象制作FLEXUS版  当前支持的声音资源类型如下： * VOICE_BASIC: 声音制作基础版 * VOICE_MIDDLE: 声音制作进阶版 * VOICE_ADVANCE：声音制作高级版 * VOICE_THIRD_PARTY：声音制作第三方出门问问 * VOICE_THIRD_PARTY_LJZN: 声音制作第三方逻辑智能 * VOICE_FLEXUS: 声音制作Flexus版资源

        :param resource_type: The resource_type of this BillResources.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_nums(self):
        r"""Gets the resource_nums of this BillResources.

        资源数量。

        :return: The resource_nums of this BillResources.
        :rtype: int
        """
        return self._resource_nums

    @resource_nums.setter
    def resource_nums(self, resource_nums):
        r"""Sets the resource_nums of this BillResources.

        资源数量。

        :param resource_nums: The resource_nums of this BillResources.
        :type resource_nums: int
        """
        self._resource_nums = resource_nums

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
        if not isinstance(other, BillResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
