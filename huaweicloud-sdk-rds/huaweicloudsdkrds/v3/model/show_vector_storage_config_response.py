# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVectorStorageConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vector_storage_switch': 'bool'
    }

    attribute_map = {
        'vector_storage_switch': 'vector_storage_switch'
    }

    def __init__(self, vector_storage_switch=None):
        r"""ShowVectorStorageConfigResponse

        The model defined in huaweicloud sdk

        :param vector_storage_switch: **参数解释**：  向量存储开关。true表示已开启向量存储，false表示已关闭向量存储。  **约束限制**：  不涉及。  **取值范围**：  - true - false **默认取值**：  不涉及。
        :type vector_storage_switch: bool
        """
        
        super().__init__()

        self._vector_storage_switch = None
        self.discriminator = None

        if vector_storage_switch is not None:
            self.vector_storage_switch = vector_storage_switch

    @property
    def vector_storage_switch(self):
        r"""Gets the vector_storage_switch of this ShowVectorStorageConfigResponse.

        **参数解释**：  向量存储开关。true表示已开启向量存储，false表示已关闭向量存储。  **约束限制**：  不涉及。  **取值范围**：  - true - false **默认取值**：  不涉及。

        :return: The vector_storage_switch of this ShowVectorStorageConfigResponse.
        :rtype: bool
        """
        return self._vector_storage_switch

    @vector_storage_switch.setter
    def vector_storage_switch(self, vector_storage_switch):
        r"""Sets the vector_storage_switch of this ShowVectorStorageConfigResponse.

        **参数解释**：  向量存储开关。true表示已开启向量存储，false表示已关闭向量存储。  **约束限制**：  不涉及。  **取值范围**：  - true - false **默认取值**：  不涉及。

        :param vector_storage_switch: The vector_storage_switch of this ShowVectorStorageConfigResponse.
        :type vector_storage_switch: bool
        """
        self._vector_storage_switch = vector_storage_switch

    def to_dict(self):
        import warnings
        warnings.warn("ShowVectorStorageConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVectorStorageConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
