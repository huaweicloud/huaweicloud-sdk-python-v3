# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBackupPolicyRequestInfo1:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'policy_id': 'str',
        'operation_definition': 'OperationDefinitionRequestInfo',
        'trigger': 'BackupTriggerRequestInfo1'
    }

    attribute_map = {
        'enabled': 'enabled',
        'policy_id': 'policy_id',
        'operation_definition': 'operation_definition',
        'trigger': 'trigger'
    }

    def __init__(self, enabled=None, policy_id=None, operation_definition=None, trigger=None):
        """UpdateBackupPolicyRequestInfo1

        The model defined in huaweicloud sdk

        :param enabled: 策略是否启用，缺省值：true
        :type enabled: bool
        :param policy_id: 策略ID,若开启防护时开启备份防护，该字段必选
        :type policy_id: str
        :param operation_definition: 
        :type operation_definition: :class:`huaweicloudsdkhss.v5.OperationDefinitionRequestInfo`
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkhss.v5.BackupTriggerRequestInfo1`
        """
        
        

        self._enabled = None
        self._policy_id = None
        self._operation_definition = None
        self._trigger = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if policy_id is not None:
            self.policy_id = policy_id
        if operation_definition is not None:
            self.operation_definition = operation_definition
        if trigger is not None:
            self.trigger = trigger

    @property
    def enabled(self):
        """Gets the enabled of this UpdateBackupPolicyRequestInfo1.

        策略是否启用，缺省值：true

        :return: The enabled of this UpdateBackupPolicyRequestInfo1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateBackupPolicyRequestInfo1.

        策略是否启用，缺省值：true

        :param enabled: The enabled of this UpdateBackupPolicyRequestInfo1.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdateBackupPolicyRequestInfo1.

        策略ID,若开启防护时开启备份防护，该字段必选

        :return: The policy_id of this UpdateBackupPolicyRequestInfo1.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdateBackupPolicyRequestInfo1.

        策略ID,若开启防护时开启备份防护，该字段必选

        :param policy_id: The policy_id of this UpdateBackupPolicyRequestInfo1.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def operation_definition(self):
        """Gets the operation_definition of this UpdateBackupPolicyRequestInfo1.

        :return: The operation_definition of this UpdateBackupPolicyRequestInfo1.
        :rtype: :class:`huaweicloudsdkhss.v5.OperationDefinitionRequestInfo`
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        """Sets the operation_definition of this UpdateBackupPolicyRequestInfo1.

        :param operation_definition: The operation_definition of this UpdateBackupPolicyRequestInfo1.
        :type operation_definition: :class:`huaweicloudsdkhss.v5.OperationDefinitionRequestInfo`
        """
        self._operation_definition = operation_definition

    @property
    def trigger(self):
        """Gets the trigger of this UpdateBackupPolicyRequestInfo1.

        :return: The trigger of this UpdateBackupPolicyRequestInfo1.
        :rtype: :class:`huaweicloudsdkhss.v5.BackupTriggerRequestInfo1`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this UpdateBackupPolicyRequestInfo1.

        :param trigger: The trigger of this UpdateBackupPolicyRequestInfo1.
        :type trigger: :class:`huaweicloudsdkhss.v5.BackupTriggerRequestInfo1`
        """
        self._trigger = trigger

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
        if not isinstance(other, UpdateBackupPolicyRequestInfo1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
