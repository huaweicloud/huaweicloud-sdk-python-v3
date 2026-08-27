# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'diff_parameters': 'list[GroupParameterDiffInfo]',
        'skipped_parameter_names': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'diff_parameters': 'diff_parameters',
        'skipped_parameter_names': 'skipped_parameter_names'
    }

    def __init__(self, name=None, diff_parameters=None, skipped_parameter_names=None):
        r"""UpgradeConfigurationResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  参数模板名称。  **取值范围**：  不涉及。
        :type name: str
        :param diff_parameters: **参数解释**：  差异参数列表。
        :type diff_parameters: list[:class:`huaweicloudsdkgaussdb.v3.GroupParameterDiffInfo`]
        :param skipped_parameter_names: **参数解释**：  执行更新操作被跳过的参数名称列表（原值与目标值相同）。
        :type skipped_parameter_names: list[str]
        """
        
        super().__init__()

        self._name = None
        self._diff_parameters = None
        self._skipped_parameter_names = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if diff_parameters is not None:
            self.diff_parameters = diff_parameters
        if skipped_parameter_names is not None:
            self.skipped_parameter_names = skipped_parameter_names

    @property
    def name(self):
        r"""Gets the name of this UpgradeConfigurationResponse.

        **参数解释**：  参数模板名称。  **取值范围**：  不涉及。

        :return: The name of this UpgradeConfigurationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpgradeConfigurationResponse.

        **参数解释**：  参数模板名称。  **取值范围**：  不涉及。

        :param name: The name of this UpgradeConfigurationResponse.
        :type name: str
        """
        self._name = name

    @property
    def diff_parameters(self):
        r"""Gets the diff_parameters of this UpgradeConfigurationResponse.

        **参数解释**：  差异参数列表。

        :return: The diff_parameters of this UpgradeConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.GroupParameterDiffInfo`]
        """
        return self._diff_parameters

    @diff_parameters.setter
    def diff_parameters(self, diff_parameters):
        r"""Sets the diff_parameters of this UpgradeConfigurationResponse.

        **参数解释**：  差异参数列表。

        :param diff_parameters: The diff_parameters of this UpgradeConfigurationResponse.
        :type diff_parameters: list[:class:`huaweicloudsdkgaussdb.v3.GroupParameterDiffInfo`]
        """
        self._diff_parameters = diff_parameters

    @property
    def skipped_parameter_names(self):
        r"""Gets the skipped_parameter_names of this UpgradeConfigurationResponse.

        **参数解释**：  执行更新操作被跳过的参数名称列表（原值与目标值相同）。

        :return: The skipped_parameter_names of this UpgradeConfigurationResponse.
        :rtype: list[str]
        """
        return self._skipped_parameter_names

    @skipped_parameter_names.setter
    def skipped_parameter_names(self, skipped_parameter_names):
        r"""Sets the skipped_parameter_names of this UpgradeConfigurationResponse.

        **参数解释**：  执行更新操作被跳过的参数名称列表（原值与目标值相同）。

        :param skipped_parameter_names: The skipped_parameter_names of this UpgradeConfigurationResponse.
        :type skipped_parameter_names: list[str]
        """
        self._skipped_parameter_names = skipped_parameter_names

    def to_dict(self):
        import warnings
        warnings.warn("UpgradeConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpgradeConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
