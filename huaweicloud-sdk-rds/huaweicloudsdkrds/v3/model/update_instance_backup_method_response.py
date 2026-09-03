# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceBackupMethodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_method': 'str'
    }

    attribute_map = {
        'backup_method': 'backup_method'
    }

    def __init__(self, backup_method=None):
        r"""UpdateInstanceBackupMethodResponse

        The model defined in huaweicloud sdk

        :param backup_method: **参数解释**：  成功修改后的备份方式。  **约束限制**：  不涉及。
        :type backup_method: str
        """
        
        super().__init__()

        self._backup_method = None
        self.discriminator = None

        if backup_method is not None:
            self.backup_method = backup_method

    @property
    def backup_method(self):
        r"""Gets the backup_method of this UpdateInstanceBackupMethodResponse.

        **参数解释**：  成功修改后的备份方式。  **约束限制**：  不涉及。

        :return: The backup_method of this UpdateInstanceBackupMethodResponse.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this UpdateInstanceBackupMethodResponse.

        **参数解释**：  成功修改后的备份方式。  **约束限制**：  不涉及。

        :param backup_method: The backup_method of this UpdateInstanceBackupMethodResponse.
        :type backup_method: str
        """
        self._backup_method = backup_method

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInstanceBackupMethodResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateInstanceBackupMethodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
