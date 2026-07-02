# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDynamicServerlessPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_vcpus': 'str',
        'min_vcpus': 'str',
        'max_vcpus': 'str',
        'available_vcpus': 'list[str]'
    }

    attribute_map = {
        'current_vcpus': 'current_vcpus',
        'min_vcpus': 'min_vcpus',
        'max_vcpus': 'max_vcpus',
        'available_vcpus': 'available_vcpus'
    }

    def __init__(self, current_vcpus=None, min_vcpus=None, max_vcpus=None, available_vcpus=None):
        r"""ShowDynamicServerlessPolicyResponse

        The model defined in huaweicloud sdk

        :param current_vcpus: **参数解释**：  当前动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，大于等于min_vcpus，并且小于等于max_vcpus。未开启动态Serverless时为null。
        :type current_vcpus: str
        :param min_vcpus: **参数解释**：  最小动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且小于等于max_vcpus。未开启动态Serverless时为null。
        :type min_vcpus: str
        :param max_vcpus: **参数解释**：  最大动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且大于等于min_vcpus。未开启动态Serverless时为null。
        :type max_vcpus: str
        :param available_vcpus: **参数解释**：  可选动态Serverless算力列表，不支持动态Serverless的实例该列表为空。  **取值范围**：  不涉及。
        :type available_vcpus: list[str]
        """
        
        super().__init__()

        self._current_vcpus = None
        self._min_vcpus = None
        self._max_vcpus = None
        self._available_vcpus = None
        self.discriminator = None

        if current_vcpus is not None:
            self.current_vcpus = current_vcpus
        if min_vcpus is not None:
            self.min_vcpus = min_vcpus
        if max_vcpus is not None:
            self.max_vcpus = max_vcpus
        if available_vcpus is not None:
            self.available_vcpus = available_vcpus

    @property
    def current_vcpus(self):
        r"""Gets the current_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  当前动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，大于等于min_vcpus，并且小于等于max_vcpus。未开启动态Serverless时为null。

        :return: The current_vcpus of this ShowDynamicServerlessPolicyResponse.
        :rtype: str
        """
        return self._current_vcpus

    @current_vcpus.setter
    def current_vcpus(self, current_vcpus):
        r"""Sets the current_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  当前动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，大于等于min_vcpus，并且小于等于max_vcpus。未开启动态Serverless时为null。

        :param current_vcpus: The current_vcpus of this ShowDynamicServerlessPolicyResponse.
        :type current_vcpus: str
        """
        self._current_vcpus = current_vcpus

    @property
    def min_vcpus(self):
        r"""Gets the min_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  最小动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且小于等于max_vcpus。未开启动态Serverless时为null。

        :return: The min_vcpus of this ShowDynamicServerlessPolicyResponse.
        :rtype: str
        """
        return self._min_vcpus

    @min_vcpus.setter
    def min_vcpus(self, min_vcpus):
        r"""Sets the min_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  最小动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且小于等于max_vcpus。未开启动态Serverless时为null。

        :param min_vcpus: The min_vcpus of this ShowDynamicServerlessPolicyResponse.
        :type min_vcpus: str
        """
        self._min_vcpus = min_vcpus

    @property
    def max_vcpus(self):
        r"""Gets the max_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  最大动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且大于等于min_vcpus。未开启动态Serverless时为null。

        :return: The max_vcpus of this ShowDynamicServerlessPolicyResponse.
        :rtype: str
        """
        return self._max_vcpus

    @max_vcpus.setter
    def max_vcpus(self, max_vcpus):
        r"""Sets the max_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  最大动态Serverless算力。  **取值范围**：  available_vcpus中的可选算力，并且大于等于min_vcpus。未开启动态Serverless时为null。

        :param max_vcpus: The max_vcpus of this ShowDynamicServerlessPolicyResponse.
        :type max_vcpus: str
        """
        self._max_vcpus = max_vcpus

    @property
    def available_vcpus(self):
        r"""Gets the available_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  可选动态Serverless算力列表，不支持动态Serverless的实例该列表为空。  **取值范围**：  不涉及。

        :return: The available_vcpus of this ShowDynamicServerlessPolicyResponse.
        :rtype: list[str]
        """
        return self._available_vcpus

    @available_vcpus.setter
    def available_vcpus(self, available_vcpus):
        r"""Sets the available_vcpus of this ShowDynamicServerlessPolicyResponse.

        **参数解释**：  可选动态Serverless算力列表，不支持动态Serverless的实例该列表为空。  **取值范围**：  不涉及。

        :param available_vcpus: The available_vcpus of this ShowDynamicServerlessPolicyResponse.
        :type available_vcpus: list[str]
        """
        self._available_vcpus = available_vcpus

    def to_dict(self):
        import warnings
        warnings.warn("ShowDynamicServerlessPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDynamicServerlessPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
