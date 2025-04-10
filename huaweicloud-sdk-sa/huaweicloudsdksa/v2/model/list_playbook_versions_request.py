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
        'approve_role': 'str',
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
        'approve_role': 'approve_role',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, workspace_id=None, playbook_id=None, status=None, enabled=None, version_type=None, approve_role=None, offset=None, limit=None):
        r"""ListPlaybookVersionsRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param playbook_id: ID of playbook
        :type playbook_id: str
        :param status: 剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED
        :type status: str
        :param enabled: 启用/禁用
        :type enabled: int
        :param version_type: 版本类型， 草稿版本：0  正式版本：1
        :type version_type: int
        :param approve_role: 审核角色
        :type approve_role: str
        :param offset: request offset, from 0
        :type offset: int
        :param limit: request limit size
        :type limit: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._playbook_id = None
        self._status = None
        self._enabled = None
        self._version_type = None
        self._approve_role = None
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
        if approve_role is not None:
            self.approve_role = approve_role
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPlaybookVersionsRequest.

        ID of project

        :return: The project_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPlaybookVersionsRequest.

        ID of project

        :param project_id: The project_id of this ListPlaybookVersionsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListPlaybookVersionsRequest.

        ID of workspace

        :return: The workspace_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListPlaybookVersionsRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this ListPlaybookVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this ListPlaybookVersionsRequest.

        ID of playbook

        :return: The playbook_id of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this ListPlaybookVersionsRequest.

        ID of playbook

        :param playbook_id: The playbook_id of this ListPlaybookVersionsRequest.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def status(self):
        r"""Gets the status of this ListPlaybookVersionsRequest.

        剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED

        :return: The status of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPlaybookVersionsRequest.

        剧本版本状态，编辑中：EDITING  审核中：APPROVING  不通过：UNPASSED 已发布：PUBLISHED

        :param status: The status of this ListPlaybookVersionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def enabled(self):
        r"""Gets the enabled of this ListPlaybookVersionsRequest.

        启用/禁用

        :return: The enabled of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListPlaybookVersionsRequest.

        启用/禁用

        :param enabled: The enabled of this ListPlaybookVersionsRequest.
        :type enabled: int
        """
        self._enabled = enabled

    @property
    def version_type(self):
        r"""Gets the version_type of this ListPlaybookVersionsRequest.

        版本类型， 草稿版本：0  正式版本：1

        :return: The version_type of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ListPlaybookVersionsRequest.

        版本类型， 草稿版本：0  正式版本：1

        :param version_type: The version_type of this ListPlaybookVersionsRequest.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def approve_role(self):
        r"""Gets the approve_role of this ListPlaybookVersionsRequest.

        审核角色

        :return: The approve_role of this ListPlaybookVersionsRequest.
        :rtype: str
        """
        return self._approve_role

    @approve_role.setter
    def approve_role(self, approve_role):
        r"""Sets the approve_role of this ListPlaybookVersionsRequest.

        审核角色

        :param approve_role: The approve_role of this ListPlaybookVersionsRequest.
        :type approve_role: str
        """
        self._approve_role = approve_role

    @property
    def offset(self):
        r"""Gets the offset of this ListPlaybookVersionsRequest.

        request offset, from 0

        :return: The offset of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPlaybookVersionsRequest.

        request offset, from 0

        :param offset: The offset of this ListPlaybookVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPlaybookVersionsRequest.

        request limit size

        :return: The limit of this ListPlaybookVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPlaybookVersionsRequest.

        request limit size

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
