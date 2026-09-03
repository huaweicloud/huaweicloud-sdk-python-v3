# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDatabasePrecheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_item': 'str',
        'check_description': 'str',
        'check_object': 'str',
        'check_status': 'str'
    }

    attribute_map = {
        'check_item': 'check_item',
        'check_description': 'check_description',
        'check_object': 'check_object',
        'check_status': 'check_status'
    }

    def __init__(self, check_item=None, check_description=None, check_object=None, check_status=None):
        r"""UpgradeDatabasePrecheckResult

        The model defined in huaweicloud sdk

        :param check_item: **参数解释**：  升级预检查项目。  **取值范围**：  - Upgrade permission check：升级权限检查。 - Instance version check：实例源版本检查。 - Resource check：资源检查。 - Upgrade feature compatibility check：升级特性兼容性检查。
        :type check_item: str
        :param check_description: **参数解释**：  升级预检查项说明。  **取值范围**：  不涉及。
        :type check_description: str
        :param check_object: **参数解释**：  升级预检查对象。  **取值范围**：  不涉及。
        :type check_object: str
        :param check_status: **参数解释**：  升级预检查项的检查状态。  **取值范围**：  - passed：检查通过。 - failed：检查失败。
        :type check_status: str
        """
        
        

        self._check_item = None
        self._check_description = None
        self._check_object = None
        self._check_status = None
        self.discriminator = None

        self.check_item = check_item
        self.check_description = check_description
        self.check_object = check_object
        self.check_status = check_status

    @property
    def check_item(self):
        r"""Gets the check_item of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项目。  **取值范围**：  - Upgrade permission check：升级权限检查。 - Instance version check：实例源版本检查。 - Resource check：资源检查。 - Upgrade feature compatibility check：升级特性兼容性检查。

        :return: The check_item of this UpgradeDatabasePrecheckResult.
        :rtype: str
        """
        return self._check_item

    @check_item.setter
    def check_item(self, check_item):
        r"""Sets the check_item of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项目。  **取值范围**：  - Upgrade permission check：升级权限检查。 - Instance version check：实例源版本检查。 - Resource check：资源检查。 - Upgrade feature compatibility check：升级特性兼容性检查。

        :param check_item: The check_item of this UpgradeDatabasePrecheckResult.
        :type check_item: str
        """
        self._check_item = check_item

    @property
    def check_description(self):
        r"""Gets the check_description of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项说明。  **取值范围**：  不涉及。

        :return: The check_description of this UpgradeDatabasePrecheckResult.
        :rtype: str
        """
        return self._check_description

    @check_description.setter
    def check_description(self, check_description):
        r"""Sets the check_description of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项说明。  **取值范围**：  不涉及。

        :param check_description: The check_description of this UpgradeDatabasePrecheckResult.
        :type check_description: str
        """
        self._check_description = check_description

    @property
    def check_object(self):
        r"""Gets the check_object of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查对象。  **取值范围**：  不涉及。

        :return: The check_object of this UpgradeDatabasePrecheckResult.
        :rtype: str
        """
        return self._check_object

    @check_object.setter
    def check_object(self, check_object):
        r"""Sets the check_object of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查对象。  **取值范围**：  不涉及。

        :param check_object: The check_object of this UpgradeDatabasePrecheckResult.
        :type check_object: str
        """
        self._check_object = check_object

    @property
    def check_status(self):
        r"""Gets the check_status of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项的检查状态。  **取值范围**：  - passed：检查通过。 - failed：检查失败。

        :return: The check_status of this UpgradeDatabasePrecheckResult.
        :rtype: str
        """
        return self._check_status

    @check_status.setter
    def check_status(self, check_status):
        r"""Sets the check_status of this UpgradeDatabasePrecheckResult.

        **参数解释**：  升级预检查项的检查状态。  **取值范围**：  - passed：检查通过。 - failed：检查失败。

        :param check_status: The check_status of this UpgradeDatabasePrecheckResult.
        :type check_status: str
        """
        self._check_status = check_status

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
        if not isinstance(other, UpgradeDatabasePrecheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
