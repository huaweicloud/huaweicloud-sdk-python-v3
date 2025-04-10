# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'operation_type': 'str',
        'provider_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'start_time': 'str',
        'status': 'str',
        'vault_id': 'str',
        'vault_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'operation_type': 'operation_type',
        'provider_id': 'provider_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'start_time': 'start_time',
        'status': 'status',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, end_time=None, limit=None, offset=None, operation_type=None, provider_id=None, resource_id=None, resource_name=None, start_time=None, status=None, vault_id=None, vault_name=None, enterprise_project_id=None):
        r"""ListOpLogsRequest

        The model defined in huaweicloud sdk

        :param end_time: 任务结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z
        :type end_time: str
        :param limit: 每页显示的条目数量，正整数
        :type limit: int
        :param offset: 偏移值，正整数
        :type offset: int
        :param operation_type: 任务类型
        :type operation_type: str
        :param provider_id: 备份提供商ID
        :type provider_id: str
        :param resource_id: 该任务操作的资源ID
        :type resource_id: str
        :param resource_name: 该任务操作的资源名称
        :type resource_name: str
        :param start_time: 任务开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-01-01T12:00:00Z
        :type start_time: str
        :param status: 任务状态
        :type status: str
        :param vault_id: 存储库ID,该任务操作的资源所属绑定的存储库。
        :type vault_id: str
        :param vault_name: 存储库名称，该任务操作资源所绑定的存储库名称。
        :type vault_name: str
        :param enterprise_project_id: 企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._end_time = None
        self._limit = None
        self._offset = None
        self._operation_type = None
        self._provider_id = None
        self._resource_id = None
        self._resource_name = None
        self._start_time = None
        self._status = None
        self._vault_id = None
        self._vault_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if operation_type is not None:
            self.operation_type = operation_type
        if provider_id is not None:
            self.provider_id = provider_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpLogsRequest.

        任务结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :return: The end_time of this ListOpLogsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpLogsRequest.

        任务结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :param end_time: The end_time of this ListOpLogsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListOpLogsRequest.

        每页显示的条目数量，正整数

        :return: The limit of this ListOpLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpLogsRequest.

        每页显示的条目数量，正整数

        :param limit: The limit of this ListOpLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOpLogsRequest.

        偏移值，正整数

        :return: The offset of this ListOpLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpLogsRequest.

        偏移值，正整数

        :param offset: The offset of this ListOpLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListOpLogsRequest.

        任务类型

        :return: The operation_type of this ListOpLogsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListOpLogsRequest.

        任务类型

        :param operation_type: The operation_type of this ListOpLogsRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ListOpLogsRequest.

        备份提供商ID

        :return: The provider_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ListOpLogsRequest.

        备份提供商ID

        :param provider_id: The provider_id of this ListOpLogsRequest.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListOpLogsRequest.

        该任务操作的资源ID

        :return: The resource_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListOpLogsRequest.

        该任务操作的资源ID

        :param resource_id: The resource_id of this ListOpLogsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListOpLogsRequest.

        该任务操作的资源名称

        :return: The resource_name of this ListOpLogsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListOpLogsRequest.

        该任务操作的资源名称

        :param resource_name: The resource_name of this ListOpLogsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpLogsRequest.

        任务开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-01-01T12:00:00Z

        :return: The start_time of this ListOpLogsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpLogsRequest.

        任务开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-01-01T12:00:00Z

        :param start_time: The start_time of this ListOpLogsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this ListOpLogsRequest.

        任务状态

        :return: The status of this ListOpLogsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOpLogsRequest.

        任务状态

        :param status: The status of this ListOpLogsRequest.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ListOpLogsRequest.

        存储库ID,该任务操作的资源所属绑定的存储库。

        :return: The vault_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ListOpLogsRequest.

        存储库ID,该任务操作的资源所属绑定的存储库。

        :param vault_id: The vault_id of this ListOpLogsRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this ListOpLogsRequest.

        存储库名称，该任务操作资源所绑定的存储库名称。

        :return: The vault_name of this ListOpLogsRequest.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this ListOpLogsRequest.

        存储库名称，该任务操作资源所绑定的存储库名称。

        :param vault_name: The vault_name of this ListOpLogsRequest.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListOpLogsRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :return: The enterprise_project_id of this ListOpLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListOpLogsRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListOpLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListOpLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
