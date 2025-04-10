# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryIssueTreeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'int',
        'service_types': 'list[int]',
        'parent_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'filter': 'IssueListFilterInfo',
        'tracker_id': 'str',
        'module_id': 'str',
        'task_uri': 'str',
        'include_sub_issue': 'bool'
    }

    attribute_map = {
        'service_type': 'service_type',
        'service_types': 'service_types',
        'parent_id': 'parent_id',
        'page_number': 'page_number',
        'page_size': 'page_size',
        'filter': 'filter',
        'tracker_id': 'tracker_id',
        'module_id': 'module_id',
        'task_uri': 'task_uri',
        'include_sub_issue': 'include_sub_issue'
    }

    def __init__(self, service_type=None, service_types=None, parent_id=None, page_number=None, page_size=None, filter=None, tracker_id=None, module_id=None, task_uri=None, include_sub_issue=None):
        r"""QueryIssueTreeInfo

        The model defined in huaweicloud sdk

        :param service_type: 服务类型
        :type service_type: int
        :param service_types: 服务类型集合
        :type service_types: list[int]
        :param parent_id: 父节点id
        :type parent_id: str
        :param page_number: 页码
        :type page_number: int
        :param page_size: 每页数量
        :type page_size: int
        :param filter: 
        :type filter: :class:`huaweicloudsdkcloudtest.v1.IssueListFilterInfo`
        :param tracker_id: trackerId
        :type tracker_id: str
        :param module_id: 模块id
        :type module_id: str
        :param task_uri: 任务udi
        :type task_uri: str
        :param include_sub_issue: 是否统计子需求的用例数，默认true
        :type include_sub_issue: bool
        """
        
        

        self._service_type = None
        self._service_types = None
        self._parent_id = None
        self._page_number = None
        self._page_size = None
        self._filter = None
        self._tracker_id = None
        self._module_id = None
        self._task_uri = None
        self._include_sub_issue = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type
        if service_types is not None:
            self.service_types = service_types
        if parent_id is not None:
            self.parent_id = parent_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if filter is not None:
            self.filter = filter
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if module_id is not None:
            self.module_id = module_id
        if task_uri is not None:
            self.task_uri = task_uri
        if include_sub_issue is not None:
            self.include_sub_issue = include_sub_issue

    @property
    def service_type(self):
        r"""Gets the service_type of this QueryIssueTreeInfo.

        服务类型

        :return: The service_type of this QueryIssueTreeInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this QueryIssueTreeInfo.

        服务类型

        :param service_type: The service_type of this QueryIssueTreeInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def service_types(self):
        r"""Gets the service_types of this QueryIssueTreeInfo.

        服务类型集合

        :return: The service_types of this QueryIssueTreeInfo.
        :rtype: list[int]
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        r"""Sets the service_types of this QueryIssueTreeInfo.

        服务类型集合

        :param service_types: The service_types of this QueryIssueTreeInfo.
        :type service_types: list[int]
        """
        self._service_types = service_types

    @property
    def parent_id(self):
        r"""Gets the parent_id of this QueryIssueTreeInfo.

        父节点id

        :return: The parent_id of this QueryIssueTreeInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this QueryIssueTreeInfo.

        父节点id

        :param parent_id: The parent_id of this QueryIssueTreeInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def page_number(self):
        r"""Gets the page_number of this QueryIssueTreeInfo.

        页码

        :return: The page_number of this QueryIssueTreeInfo.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this QueryIssueTreeInfo.

        页码

        :param page_number: The page_number of this QueryIssueTreeInfo.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this QueryIssueTreeInfo.

        每页数量

        :return: The page_size of this QueryIssueTreeInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QueryIssueTreeInfo.

        每页数量

        :param page_size: The page_size of this QueryIssueTreeInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def filter(self):
        r"""Gets the filter of this QueryIssueTreeInfo.

        :return: The filter of this QueryIssueTreeInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IssueListFilterInfo`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this QueryIssueTreeInfo.

        :param filter: The filter of this QueryIssueTreeInfo.
        :type filter: :class:`huaweicloudsdkcloudtest.v1.IssueListFilterInfo`
        """
        self._filter = filter

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this QueryIssueTreeInfo.

        trackerId

        :return: The tracker_id of this QueryIssueTreeInfo.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this QueryIssueTreeInfo.

        trackerId

        :param tracker_id: The tracker_id of this QueryIssueTreeInfo.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def module_id(self):
        r"""Gets the module_id of this QueryIssueTreeInfo.

        模块id

        :return: The module_id of this QueryIssueTreeInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this QueryIssueTreeInfo.

        模块id

        :param module_id: The module_id of this QueryIssueTreeInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def task_uri(self):
        r"""Gets the task_uri of this QueryIssueTreeInfo.

        任务udi

        :return: The task_uri of this QueryIssueTreeInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this QueryIssueTreeInfo.

        任务udi

        :param task_uri: The task_uri of this QueryIssueTreeInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def include_sub_issue(self):
        r"""Gets the include_sub_issue of this QueryIssueTreeInfo.

        是否统计子需求的用例数，默认true

        :return: The include_sub_issue of this QueryIssueTreeInfo.
        :rtype: bool
        """
        return self._include_sub_issue

    @include_sub_issue.setter
    def include_sub_issue(self, include_sub_issue):
        r"""Sets the include_sub_issue of this QueryIssueTreeInfo.

        是否统计子需求的用例数，默认true

        :param include_sub_issue: The include_sub_issue of this QueryIssueTreeInfo.
        :type include_sub_issue: bool
        """
        self._include_sub_issue = include_sub_issue

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
        if not isinstance(other, QueryIssueTreeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
