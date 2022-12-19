# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookAuditLogsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'body': 'AuditLogInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, body=None):
        """ListPlaybookAuditLogsRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param offset: offset
        :type offset: int
        :param limit: limit
        :type limit: int
        :param sort_key: sort_key
        :type sort_key: str
        :param sort_dir: sort_dir. asc, desc
        :type sort_dir: str
        :param body: Body of the ListPlaybookAuditLogsRequest
        :type body: :class:`huaweicloudsdksa.v2.AuditLogInfo`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.offset = offset
        self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this ListPlaybookAuditLogsRequest.

        ID of project

        :return: The project_id of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPlaybookAuditLogsRequest.

        ID of project

        :param project_id: The project_id of this ListPlaybookAuditLogsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListPlaybookAuditLogsRequest.

        ID of workspace

        :return: The workspace_id of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListPlaybookAuditLogsRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this ListPlaybookAuditLogsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        """Gets the offset of this ListPlaybookAuditLogsRequest.

        offset

        :return: The offset of this ListPlaybookAuditLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPlaybookAuditLogsRequest.

        offset

        :param offset: The offset of this ListPlaybookAuditLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPlaybookAuditLogsRequest.

        limit

        :return: The limit of this ListPlaybookAuditLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPlaybookAuditLogsRequest.

        limit

        :param limit: The limit of this ListPlaybookAuditLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPlaybookAuditLogsRequest.

        sort_key

        :return: The sort_key of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPlaybookAuditLogsRequest.

        sort_key

        :param sort_key: The sort_key of this ListPlaybookAuditLogsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPlaybookAuditLogsRequest.

        sort_dir. asc, desc

        :return: The sort_dir of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPlaybookAuditLogsRequest.

        sort_dir. asc, desc

        :param sort_dir: The sort_dir of this ListPlaybookAuditLogsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def body(self):
        """Gets the body of this ListPlaybookAuditLogsRequest.

        :return: The body of this ListPlaybookAuditLogsRequest.
        :rtype: :class:`huaweicloudsdksa.v2.AuditLogInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListPlaybookAuditLogsRequest.

        :param body: The body of this ListPlaybookAuditLogsRequest.
        :type body: :class:`huaweicloudsdksa.v2.AuditLogInfo`
        """
        self._body = body

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
        if not isinstance(other, ListPlaybookAuditLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
