# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupPolicyInfoResponse(SdkResponse):

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
        'id': 'str',
        'name': 'str',
        'operation_type': 'str',
        'operation_definition': 'OperationDefinitionInfo',
        'trigger': 'BackupTriggerInfo'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'operation_type': 'operation_type',
        'operation_definition': 'operation_definition',
        'trigger': 'trigger'
    }

    def __init__(self, enabled=None, id=None, name=None, operation_type=None, operation_definition=None, trigger=None):
        """ShowBackupPolicyInfoResponse

        The model defined in huaweicloud sdk

        :param enabled: 策略是否启用
        :type enabled: bool
        :param id: 策略ID
        :type id: str
        :param name: 策略名称
        :type name: str
        :param operation_type: 备份类型。备份（backup）、复制(replication)，包含如下2种。   - backup ：备份。   - replication ：复制。
        :type operation_type: str
        :param operation_definition: 
        :type operation_definition: :class:`huaweicloudsdkhss.v5.OperationDefinitionInfo`
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkhss.v5.BackupTriggerInfo`
        """
        
        super(ShowBackupPolicyInfoResponse, self).__init__()

        self._enabled = None
        self._id = None
        self._name = None
        self._operation_type = None
        self._operation_definition = None
        self._trigger = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_definition is not None:
            self.operation_definition = operation_definition
        if trigger is not None:
            self.trigger = trigger

    @property
    def enabled(self):
        """Gets the enabled of this ShowBackupPolicyInfoResponse.

        策略是否启用

        :return: The enabled of this ShowBackupPolicyInfoResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ShowBackupPolicyInfoResponse.

        策略是否启用

        :param enabled: The enabled of this ShowBackupPolicyInfoResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ShowBackupPolicyInfoResponse.

        策略ID

        :return: The id of this ShowBackupPolicyInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowBackupPolicyInfoResponse.

        策略ID

        :param id: The id of this ShowBackupPolicyInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowBackupPolicyInfoResponse.

        策略名称

        :return: The name of this ShowBackupPolicyInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowBackupPolicyInfoResponse.

        策略名称

        :param name: The name of this ShowBackupPolicyInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def operation_type(self):
        """Gets the operation_type of this ShowBackupPolicyInfoResponse.

        备份类型。备份（backup）、复制(replication)，包含如下2种。   - backup ：备份。   - replication ：复制。

        :return: The operation_type of this ShowBackupPolicyInfoResponse.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ShowBackupPolicyInfoResponse.

        备份类型。备份（backup）、复制(replication)，包含如下2种。   - backup ：备份。   - replication ：复制。

        :param operation_type: The operation_type of this ShowBackupPolicyInfoResponse.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_definition(self):
        """Gets the operation_definition of this ShowBackupPolicyInfoResponse.

        :return: The operation_definition of this ShowBackupPolicyInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.OperationDefinitionInfo`
        """
        return self._operation_definition

    @operation_definition.setter
    def operation_definition(self, operation_definition):
        """Sets the operation_definition of this ShowBackupPolicyInfoResponse.

        :param operation_definition: The operation_definition of this ShowBackupPolicyInfoResponse.
        :type operation_definition: :class:`huaweicloudsdkhss.v5.OperationDefinitionInfo`
        """
        self._operation_definition = operation_definition

    @property
    def trigger(self):
        """Gets the trigger of this ShowBackupPolicyInfoResponse.

        :return: The trigger of this ShowBackupPolicyInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.BackupTriggerInfo`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ShowBackupPolicyInfoResponse.

        :param trigger: The trigger of this ShowBackupPolicyInfoResponse.
        :type trigger: :class:`huaweicloudsdkhss.v5.BackupTriggerInfo`
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
        if not isinstance(other, ShowBackupPolicyInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
