# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'is_update_param_group_version': 'bool'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'is_update_param_group_version': 'is_update_param_group_version'
    }

    def __init__(self, instance_ids=None, is_update_param_group_version=None):
        r"""ApplyConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 实例ID列表。列表长度限制在10以内。
        :type instance_ids: list[str]
        :param is_update_param_group_version: **参数解释**：  是否更新实例参数组版本，更新后实例规格变更时默认的规格参数值会以最新版本的为准。  **约束限制**：  不涉及。  **取值范围**：  - true：是。 - false：否。  **默认取值**：    false。
        :type is_update_param_group_version: bool
        """
        
        

        self._instance_ids = None
        self._is_update_param_group_version = None
        self.discriminator = None

        self.instance_ids = instance_ids
        if is_update_param_group_version is not None:
            self.is_update_param_group_version = is_update_param_group_version

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this ApplyConfigurationRequestBody.

        实例ID列表。列表长度限制在10以内。

        :return: The instance_ids of this ApplyConfigurationRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this ApplyConfigurationRequestBody.

        实例ID列表。列表长度限制在10以内。

        :param instance_ids: The instance_ids of this ApplyConfigurationRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def is_update_param_group_version(self):
        r"""Gets the is_update_param_group_version of this ApplyConfigurationRequestBody.

        **参数解释**：  是否更新实例参数组版本，更新后实例规格变更时默认的规格参数值会以最新版本的为准。  **约束限制**：  不涉及。  **取值范围**：  - true：是。 - false：否。  **默认取值**：    false。

        :return: The is_update_param_group_version of this ApplyConfigurationRequestBody.
        :rtype: bool
        """
        return self._is_update_param_group_version

    @is_update_param_group_version.setter
    def is_update_param_group_version(self, is_update_param_group_version):
        r"""Sets the is_update_param_group_version of this ApplyConfigurationRequestBody.

        **参数解释**：  是否更新实例参数组版本，更新后实例规格变更时默认的规格参数值会以最新版本的为准。  **约束限制**：  不涉及。  **取值范围**：  - true：是。 - false：否。  **默认取值**：    false。

        :param is_update_param_group_version: The is_update_param_group_version of this ApplyConfigurationRequestBody.
        :type is_update_param_group_version: bool
        """
        self._is_update_param_group_version = is_update_param_group_version

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
        if not isinstance(other, ApplyConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
