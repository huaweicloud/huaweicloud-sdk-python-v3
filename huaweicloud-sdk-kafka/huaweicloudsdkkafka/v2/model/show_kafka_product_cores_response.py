# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaProductCoresResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'core_num': 'int',
        'total_extend_storage_space': 'int'
    }

    attribute_map = {
        'core_num': 'core_num',
        'total_extend_storage_space': 'total_extend_storage_space'
    }

    def __init__(self, core_num=None, total_extend_storage_space=None):
        r"""ShowKafkaProductCoresResponse

        The model defined in huaweicloud sdk

        :param core_num: **参数解释**： 核数。 **取值范围**： 不涉及。
        :type core_num: int
        :param total_extend_storage_space: **参数解释**： 需要扩容的存储空间。 **取值范围**： 不涉及。
        :type total_extend_storage_space: int
        """
        
        super().__init__()

        self._core_num = None
        self._total_extend_storage_space = None
        self.discriminator = None

        if core_num is not None:
            self.core_num = core_num
        if total_extend_storage_space is not None:
            self.total_extend_storage_space = total_extend_storage_space

    @property
    def core_num(self):
        r"""Gets the core_num of this ShowKafkaProductCoresResponse.

        **参数解释**： 核数。 **取值范围**： 不涉及。

        :return: The core_num of this ShowKafkaProductCoresResponse.
        :rtype: int
        """
        return self._core_num

    @core_num.setter
    def core_num(self, core_num):
        r"""Sets the core_num of this ShowKafkaProductCoresResponse.

        **参数解释**： 核数。 **取值范围**： 不涉及。

        :param core_num: The core_num of this ShowKafkaProductCoresResponse.
        :type core_num: int
        """
        self._core_num = core_num

    @property
    def total_extend_storage_space(self):
        r"""Gets the total_extend_storage_space of this ShowKafkaProductCoresResponse.

        **参数解释**： 需要扩容的存储空间。 **取值范围**： 不涉及。

        :return: The total_extend_storage_space of this ShowKafkaProductCoresResponse.
        :rtype: int
        """
        return self._total_extend_storage_space

    @total_extend_storage_space.setter
    def total_extend_storage_space(self, total_extend_storage_space):
        r"""Sets the total_extend_storage_space of this ShowKafkaProductCoresResponse.

        **参数解释**： 需要扩容的存储空间。 **取值范围**： 不涉及。

        :param total_extend_storage_space: The total_extend_storage_space of this ShowKafkaProductCoresResponse.
        :type total_extend_storage_space: int
        """
        self._total_extend_storage_space = total_extend_storage_space

    def to_dict(self):
        import warnings
        warnings.warn("ShowKafkaProductCoresResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowKafkaProductCoresResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
