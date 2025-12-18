# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareParameterGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'str',
        'source_name': 'str',
        'target_id': 'str',
        'target_name': 'str',
        'parameters': 'list[ParamGroupParameterDiffV3]'
    }

    attribute_map = {
        'source_id': 'source_id',
        'source_name': 'source_name',
        'target_id': 'target_id',
        'target_name': 'target_name',
        'parameters': 'parameters'
    }

    def __init__(self, source_id=None, source_name=None, target_id=None, target_name=None, parameters=None):
        r"""CompareParameterGroupsResponse

        The model defined in huaweicloud sdk

        :param source_id: **参数解释**：  源参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type source_id: str
        :param source_name: **参数解释**：  源参数组名称。  **参数范围**：  不涉及。
        :type source_name: str
        :param target_id: **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type target_id: str
        :param target_name: **参数解释**：  目标参数组名称。  **参数范围**：  不涉及。
        :type target_name: str
        :param parameters: **参数解释**：  比较参数组返回相关信息的集合。  **参数范围**：  不涉及。
        :type parameters: list[:class:`huaweicloudsdkddm.v1.ParamGroupParameterDiffV3`]
        """
        
        super().__init__()

        self._source_id = None
        self._source_name = None
        self._target_id = None
        self._target_name = None
        self._parameters = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        if target_id is not None:
            self.target_id = target_id
        if target_name is not None:
            self.target_name = target_name
        if parameters is not None:
            self.parameters = parameters

    @property
    def source_id(self):
        r"""Gets the source_id of this CompareParameterGroupsResponse.

        **参数解释**：  源参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The source_id of this CompareParameterGroupsResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this CompareParameterGroupsResponse.

        **参数解释**：  源参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param source_id: The source_id of this CompareParameterGroupsResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_name(self):
        r"""Gets the source_name of this CompareParameterGroupsResponse.

        **参数解释**：  源参数组名称。  **参数范围**：  不涉及。

        :return: The source_name of this CompareParameterGroupsResponse.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this CompareParameterGroupsResponse.

        **参数解释**：  源参数组名称。  **参数范围**：  不涉及。

        :param source_name: The source_name of this CompareParameterGroupsResponse.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def target_id(self):
        r"""Gets the target_id of this CompareParameterGroupsResponse.

        **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The target_id of this CompareParameterGroupsResponse.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this CompareParameterGroupsResponse.

        **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param target_id: The target_id of this CompareParameterGroupsResponse.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        r"""Gets the target_name of this CompareParameterGroupsResponse.

        **参数解释**：  目标参数组名称。  **参数范围**：  不涉及。

        :return: The target_name of this CompareParameterGroupsResponse.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this CompareParameterGroupsResponse.

        **参数解释**：  目标参数组名称。  **参数范围**：  不涉及。

        :param target_name: The target_name of this CompareParameterGroupsResponse.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def parameters(self):
        r"""Gets the parameters of this CompareParameterGroupsResponse.

        **参数解释**：  比较参数组返回相关信息的集合。  **参数范围**：  不涉及。

        :return: The parameters of this CompareParameterGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ParamGroupParameterDiffV3`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CompareParameterGroupsResponse.

        **参数解释**：  比较参数组返回相关信息的集合。  **参数范围**：  不涉及。

        :param parameters: The parameters of this CompareParameterGroupsResponse.
        :type parameters: list[:class:`huaweicloudsdkddm.v1.ParamGroupParameterDiffV3`]
        """
        self._parameters = parameters

    def to_dict(self):
        import warnings
        warnings.warn("CompareParameterGroupsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CompareParameterGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
