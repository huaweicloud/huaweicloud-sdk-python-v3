# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpdProjectIssuesRequest:

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
        'is_backlog': 'bool',
        'issue_type': 'str',
        'src_domain_id': 'str',
        'view': 'str',
        'body': 'SearchIpdIssuesRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'is_backlog': 'is_backlog',
        'issue_type': 'issue_type',
        'src_domain_id': 'src_domain_id',
        'view': 'view',
        'body': 'body'
    }

    def __init__(self, project_id=None, is_backlog=None, issue_type=None, src_domain_id=None, view=None, body=None):
        r"""ListIpdProjectIssuesRequest

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param is_backlog: 是否backlog查询
        :type is_backlog: bool
        :param issue_type: 工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]
        :type issue_type: str
        :param src_domain_id: 提出项目Id
        :type src_domain_id: str
        :param view: 视图模式[tree,list]
        :type view: str
        :param body: Body of the ListIpdProjectIssuesRequest
        :type body: :class:`huaweicloudsdkprojectman.v4.SearchIpdIssuesRequestBody`
        """
        
        

        self._project_id = None
        self._is_backlog = None
        self._issue_type = None
        self._src_domain_id = None
        self._view = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if is_backlog is not None:
            self.is_backlog = is_backlog
        self.issue_type = issue_type
        if src_domain_id is not None:
            self.src_domain_id = src_domain_id
        if view is not None:
            self.view = view
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ListIpdProjectIssuesRequest.

        devcloud项目的32位id

        :return: The project_id of this ListIpdProjectIssuesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListIpdProjectIssuesRequest.

        devcloud项目的32位id

        :param project_id: The project_id of this ListIpdProjectIssuesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_backlog(self):
        r"""Gets the is_backlog of this ListIpdProjectIssuesRequest.

        是否backlog查询

        :return: The is_backlog of this ListIpdProjectIssuesRequest.
        :rtype: bool
        """
        return self._is_backlog

    @is_backlog.setter
    def is_backlog(self, is_backlog):
        r"""Sets the is_backlog of this ListIpdProjectIssuesRequest.

        是否backlog查询

        :param is_backlog: The is_backlog of this ListIpdProjectIssuesRequest.
        :type is_backlog: bool
        """
        self._is_backlog = is_backlog

    @property
    def issue_type(self):
        r"""Gets the issue_type of this ListIpdProjectIssuesRequest.

        工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]

        :return: The issue_type of this ListIpdProjectIssuesRequest.
        :rtype: str
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        r"""Sets the issue_type of this ListIpdProjectIssuesRequest.

        工作项分类：[Epic,FE,IR,RR,SR,US,AR,Bug,Task]

        :param issue_type: The issue_type of this ListIpdProjectIssuesRequest.
        :type issue_type: str
        """
        self._issue_type = issue_type

    @property
    def src_domain_id(self):
        r"""Gets the src_domain_id of this ListIpdProjectIssuesRequest.

        提出项目Id

        :return: The src_domain_id of this ListIpdProjectIssuesRequest.
        :rtype: str
        """
        return self._src_domain_id

    @src_domain_id.setter
    def src_domain_id(self, src_domain_id):
        r"""Sets the src_domain_id of this ListIpdProjectIssuesRequest.

        提出项目Id

        :param src_domain_id: The src_domain_id of this ListIpdProjectIssuesRequest.
        :type src_domain_id: str
        """
        self._src_domain_id = src_domain_id

    @property
    def view(self):
        r"""Gets the view of this ListIpdProjectIssuesRequest.

        视图模式[tree,list]

        :return: The view of this ListIpdProjectIssuesRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListIpdProjectIssuesRequest.

        视图模式[tree,list]

        :param view: The view of this ListIpdProjectIssuesRequest.
        :type view: str
        """
        self._view = view

    @property
    def body(self):
        r"""Gets the body of this ListIpdProjectIssuesRequest.

        :return: The body of this ListIpdProjectIssuesRequest.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SearchIpdIssuesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListIpdProjectIssuesRequest.

        :param body: The body of this ListIpdProjectIssuesRequest.
        :type body: :class:`huaweicloudsdkprojectman.v4.SearchIpdIssuesRequestBody`
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
        if not isinstance(other, ListIpdProjectIssuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
