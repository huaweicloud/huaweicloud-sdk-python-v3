# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetBackupPolicyFailedRecordResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'error_message': 'error_message'
    }

    def __init__(self, instance_id=None, error_message=None):
        r"""BatchSetBackupPolicyFailedRecordResult

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **取值范围**: 不涉及。
        :type instance_id: str
        :param error_message: **参数解释**: 错误信息。 **取值范围**: 不涉及。
        :type error_message: str
        """
        
        

        self._instance_id = None
        self._error_message = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if error_message is not None:
            self.error_message = error_message

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchSetBackupPolicyFailedRecordResult.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **取值范围**: 不涉及。

        :return: The instance_id of this BatchSetBackupPolicyFailedRecordResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchSetBackupPolicyFailedRecordResult.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this BatchSetBackupPolicyFailedRecordResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def error_message(self):
        r"""Gets the error_message of this BatchSetBackupPolicyFailedRecordResult.

        **参数解释**: 错误信息。 **取值范围**: 不涉及。

        :return: The error_message of this BatchSetBackupPolicyFailedRecordResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this BatchSetBackupPolicyFailedRecordResult.

        **参数解释**: 错误信息。 **取值范围**: 不涉及。

        :param error_message: The error_message of this BatchSetBackupPolicyFailedRecordResult.
        :type error_message: str
        """
        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchSetBackupPolicyFailedRecordResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
