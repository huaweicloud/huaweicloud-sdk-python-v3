# coding: utf-8

import pprint
import re

import six





class OperationLog:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str',
        'created_at': 'str',
        'ended_at': 'str',
        'error_info': 'OpErrorInfo',
        'extra_info': 'OpExtraInfo',
        'id': 'str',
        'operation_type': 'str',
        'policy_id': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'started_at': 'str',
        'status': 'str',
        'updated_at': 'str',
        'vault_id': 'str',
        'vault_name': 'str'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'created_at': 'created_at',
        'ended_at': 'ended_at',
        'error_info': 'error_info',
        'extra_info': 'extra_info',
        'id': 'id',
        'operation_type': 'operation_type',
        'policy_id': 'policy_id',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'started_at': 'started_at',
        'status': 'status',
        'updated_at': 'updated_at',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name'
    }

    def __init__(self, checkpoint_id=None, created_at=None, ended_at=None, error_info=None, extra_info=None, id=None, operation_type=None, policy_id=None, project_id=None, provider_id=None, started_at=None, status=None, updated_at=None, vault_id=None, vault_name=None):
        """OperationLog - a model defined in huaweicloud sdk"""
        
        

        self._checkpoint_id = None
        self._created_at = None
        self._ended_at = None
        self._error_info = None
        self._extra_info = None
        self._id = None
        self._operation_type = None
        self._policy_id = None
        self._project_id = None
        self._provider_id = None
        self._started_at = None
        self._status = None
        self._updated_at = None
        self._vault_id = None
        self._vault_name = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        self.created_at = created_at
        if ended_at is not None:
            self.ended_at = ended_at
        self.error_info = error_info
        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        if operation_type is not None:
            self.operation_type = operation_type
        if policy_id is not None:
            self.policy_id = policy_id
        self.project_id = project_id
        if provider_id is not None:
            self.provider_id = provider_id
        self.started_at = started_at
        self.status = status
        self.updated_at = updated_at
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this OperationLog.

        备份记录id

        :return: The checkpoint_id of this OperationLog.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this OperationLog.

        备份记录id

        :param checkpoint_id: The checkpoint_id of this OperationLog.
        :type: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def created_at(self):
        """Gets the created_at of this OperationLog.

        创建时间,例如: \"2020-02-23T01:00:32Z\"

        :return: The created_at of this OperationLog.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OperationLog.

        创建时间,例如: \"2020-02-23T01:00:32Z\"

        :param created_at: The created_at of this OperationLog.
        :type: str
        """
        self._created_at = created_at

    @property
    def ended_at(self):
        """Gets the ended_at of this OperationLog.

        任务结束时间,例如: \"2020-02-23T01:00:32Z\"

        :return: The ended_at of this OperationLog.
        :rtype: str
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this OperationLog.

        任务结束时间,例如: \"2020-02-23T01:00:32Z\"

        :param ended_at: The ended_at of this OperationLog.
        :type: str
        """
        self._ended_at = ended_at

    @property
    def error_info(self):
        """Gets the error_info of this OperationLog.


        :return: The error_info of this OperationLog.
        :rtype: OpErrorInfo
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this OperationLog.


        :param error_info: The error_info of this OperationLog.
        :type: OpErrorInfo
        """
        self._error_info = error_info

    @property
    def extra_info(self):
        """Gets the extra_info of this OperationLog.


        :return: The extra_info of this OperationLog.
        :rtype: OpExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this OperationLog.


        :param extra_info: The extra_info of this OperationLog.
        :type: OpExtraInfo
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this OperationLog.

        任务id

        :return: The id of this OperationLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationLog.

        任务id

        :param id: The id of this OperationLog.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """Gets the operation_type of this OperationLog.

        任务类型

        :return: The operation_type of this OperationLog.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this OperationLog.

        任务类型

        :param operation_type: The operation_type of this OperationLog.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def policy_id(self):
        """Gets the policy_id of this OperationLog.

        策略ID

        :return: The policy_id of this OperationLog.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this OperationLog.

        策略ID

        :param policy_id: The policy_id of this OperationLog.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def project_id(self):
        """Gets the project_id of this OperationLog.

        项目ID

        :return: The project_id of this OperationLog.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this OperationLog.

        项目ID

        :param project_id: The project_id of this OperationLog.
        :type: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this OperationLog.

        备份提供商ID。用于区分备份对象。

        :return: The provider_id of this OperationLog.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this OperationLog.

        备份提供商ID。用于区分备份对象。

        :param provider_id: The provider_id of this OperationLog.
        :type: str
        """
        self._provider_id = provider_id

    @property
    def started_at(self):
        """Gets the started_at of this OperationLog.

        任务开始时间,例如: \"2020-02-23T01:00:32Z\"

        :return: The started_at of this OperationLog.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this OperationLog.

        任务开始时间,例如: \"2020-02-23T01:00:32Z\"

        :param started_at: The started_at of this OperationLog.
        :type: str
        """
        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this OperationLog.

        任务状态

        :return: The status of this OperationLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OperationLog.

        任务状态

        :param status: The status of this OperationLog.
        :type: str
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this OperationLog.

        修改时间,例如: \"2020-02-23T01:00:32Z\"

        :return: The updated_at of this OperationLog.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OperationLog.

        修改时间,例如: \"2020-02-23T01:00:32Z\"

        :param updated_at: The updated_at of this OperationLog.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def vault_id(self):
        """Gets the vault_id of this OperationLog.

        任务操作资源所属存储库ID

        :return: The vault_id of this OperationLog.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this OperationLog.

        任务操作资源所属存储库ID

        :param vault_id: The vault_id of this OperationLog.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        """Gets the vault_name of this OperationLog.

        任务操作资源所属存储库名称

        :return: The vault_name of this OperationLog.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        """Sets the vault_name of this OperationLog.

        任务操作资源所属存储库名称

        :param vault_name: The vault_name of this OperationLog.
        :type: str
        """
        self._vault_name = vault_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OperationLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
