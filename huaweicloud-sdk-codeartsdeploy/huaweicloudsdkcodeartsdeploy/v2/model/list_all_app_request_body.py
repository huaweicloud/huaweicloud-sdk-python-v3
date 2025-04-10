# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllAppRequestBody:

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
        'page': 'int',
        'size': 'int',
        'sort_name': 'str',
        'sort_by': 'str',
        'states': 'list[str]',
        'group_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page': 'page',
        'size': 'size',
        'sort_name': 'sort_name',
        'sort_by': 'sort_by',
        'states': 'states',
        'group_id': 'group_id'
    }

    def __init__(self, project_id=None, page=None, size=None, sort_name=None, sort_by=None, states=None, group_id=None):
        r"""ListAllAppRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param page: 分页页码， 表示从此页开始查询， page大于等于1
        :type page: int
        :param size: 每页显示的条目数量，size小于等于100
        :type size: int
        :param sort_name: 排序字段的名称，当前仅支持name和startTime
        :type sort_name: str
        :param sort_by: 排序顺序，正序（ASC）或者逆序（DESC)
        :type sort_by: str
        :param states: 应用状态列表，支持查询以下状态： abort: 部署中止 failed: 部署失败 not_started: 取消执行 pending: 排队中 running: 正在部署 succeeded: 部署成功 timeout: 部署超时 not_executed: 未执行 
        :type states: list[str]
        :param group_id: 应用的分组id，传入no_grouped为查询未分组的应用
        :type group_id: str
        """
        
        

        self._project_id = None
        self._page = None
        self._size = None
        self._sort_name = None
        self._sort_by = None
        self._states = None
        self._group_id = None
        self.discriminator = None

        self.project_id = project_id
        self.page = page
        self.size = size
        if sort_name is not None:
            self.sort_name = sort_name
        if sort_by is not None:
            self.sort_by = sort_by
        if states is not None:
            self.states = states
        if group_id is not None:
            self.group_id = group_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAllAppRequestBody.

        项目id

        :return: The project_id of this ListAllAppRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAllAppRequestBody.

        项目id

        :param project_id: The project_id of this ListAllAppRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page(self):
        r"""Gets the page of this ListAllAppRequestBody.

        分页页码， 表示从此页开始查询， page大于等于1

        :return: The page of this ListAllAppRequestBody.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListAllAppRequestBody.

        分页页码， 表示从此页开始查询， page大于等于1

        :param page: The page of this ListAllAppRequestBody.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ListAllAppRequestBody.

        每页显示的条目数量，size小于等于100

        :return: The size of this ListAllAppRequestBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListAllAppRequestBody.

        每页显示的条目数量，size小于等于100

        :param size: The size of this ListAllAppRequestBody.
        :type size: int
        """
        self._size = size

    @property
    def sort_name(self):
        r"""Gets the sort_name of this ListAllAppRequestBody.

        排序字段的名称，当前仅支持name和startTime

        :return: The sort_name of this ListAllAppRequestBody.
        :rtype: str
        """
        return self._sort_name

    @sort_name.setter
    def sort_name(self, sort_name):
        r"""Sets the sort_name of this ListAllAppRequestBody.

        排序字段的名称，当前仅支持name和startTime

        :param sort_name: The sort_name of this ListAllAppRequestBody.
        :type sort_name: str
        """
        self._sort_name = sort_name

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListAllAppRequestBody.

        排序顺序，正序（ASC）或者逆序（DESC)

        :return: The sort_by of this ListAllAppRequestBody.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListAllAppRequestBody.

        排序顺序，正序（ASC）或者逆序（DESC)

        :param sort_by: The sort_by of this ListAllAppRequestBody.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def states(self):
        r"""Gets the states of this ListAllAppRequestBody.

        应用状态列表，支持查询以下状态： abort: 部署中止 failed: 部署失败 not_started: 取消执行 pending: 排队中 running: 正在部署 succeeded: 部署成功 timeout: 部署超时 not_executed: 未执行 

        :return: The states of this ListAllAppRequestBody.
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this ListAllAppRequestBody.

        应用状态列表，支持查询以下状态： abort: 部署中止 failed: 部署失败 not_started: 取消执行 pending: 排队中 running: 正在部署 succeeded: 部署成功 timeout: 部署超时 not_executed: 未执行 

        :param states: The states of this ListAllAppRequestBody.
        :type states: list[str]
        """
        self._states = states

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAllAppRequestBody.

        应用的分组id，传入no_grouped为查询未分组的应用

        :return: The group_id of this ListAllAppRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAllAppRequestBody.

        应用的分组id，传入no_grouped为查询未分组的应用

        :param group_id: The group_id of this ListAllAppRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, ListAllAppRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
