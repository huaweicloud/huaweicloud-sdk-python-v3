# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'playbook_id': 'str',
        'status': 'str',
        'enabled': 'int',
        'version_type': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'playbook_id': 'playbook_id',
        'status': 'status',
        'enabled': 'enabled',
        'version_type': 'version_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, workspace_id=None, playbook_id=None, status=None, enabled=None, version_type=None, offset=None, limit=None):
        """ListPlaybookVersionsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param playbook_id: 剧本ID
        :type playbook_id: str
        :param status: 剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED
        :type status: str
        :param enabled: 启用/禁用
        :type enabled: int
        :param version_type: 版本类型， 草稿版本：0  正式版本：1
        :type version_type: int
        :param offset: 分页查询参数。用于指定查询结果的起始位置，从0开始
        :type offset: int
        :param limit: 分页查询参数，用于指定一次查询最多的结果数，从1开始
        :type limit: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._playbook_id = None
        self._status = None
        self._enabled = None
        self._version_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.playbook_id = playbook_id
        if status is not None:
            self.status = status
        if enabled is not None:
            self.enabled = enabled
        if version_type is not None:
            self.version_type = version_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ListPlaybookVersionsRequest.

        项目ID

        :return: The project_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPlaybookVersionsRequest.

        项目ID

        :param project_id: The project_id of this ListPlaybookVersionsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListPlaybookVersionsRequest.

        工作空间ID

        :return: The workspace_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListPlaybookVersionsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListPlaybookVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def playbook_id(self):
        """Gets the playbook_id of this ListPlaybookVersionsRequest.

        剧本ID

        :return: The playbook_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this ListPlaybookVersionsRequest.

        剧本ID

        :param playbook_id: The playbook_id of this ListPlaybookVersionsRequest.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def status(self):
        """Gets the status of this ListPlaybookVersionsRequest.

        剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED

        :return: The status of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPlaybookVersionsRequest.

        剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED

        :param status: The status of this ListPlaybookVersionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def enabled(self):
        """Gets the enabled of this ListPlaybookVersionsRequest.

        启用/禁用

        :return: The enabled of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListPlaybookVersionsRequest.

        启用/禁用

        :param enabled: The enabled of this ListPlaybookVersionsRequest.
        :type enabled: int
        """
        self._enabled = enabled

    @property
    def version_type(self):
        """Gets the version_type of this ListPlaybookVersionsRequest.

        版本类型， 草稿版本：0  正式版本：1

        :return: The version_type of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this ListPlaybookVersionsRequest.

        版本类型， 草稿版本：0  正式版本：1

        :param version_type: The version_type of this ListPlaybookVersionsRequest.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def offset(self):
        """Gets the offset of this ListPlaybookVersionsRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :return: The offset of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPlaybookVersionsRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :param offset: The offset of this ListPlaybookVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPlaybookVersionsRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :return: The limit of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPlaybookVersionsRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :param limit: The limit of this ListPlaybookVersionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPlaybookVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
