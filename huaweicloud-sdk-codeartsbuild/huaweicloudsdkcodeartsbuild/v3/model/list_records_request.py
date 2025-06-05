# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_project_id': 'str',
        'page': 'int',
        'limit': 'int',
        'triggers': 'list[str]',
        'branches': 'list[str]',
        'tags': 'list[str]',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'build_project_id': 'build_project_id',
        'page': 'page',
        'limit': 'limit',
        'triggers': 'triggers',
        'branches': 'branches',
        'tags': 'tags',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, build_project_id=None, page=None, limit=None, triggers=None, branches=None, tags=None, from_date=None, to_date=None):
        r"""ListRecordsRequest

        The model defined in huaweicloud sdk

        :param build_project_id: 构建工程项目ID，36位数字、小写字母组合。
        :type build_project_id: str
        :param page: 分页页码，表示从此页开始查询，大于等于0
        :type page: int
        :param limit: 每页显示的条目数量，小于等于100
        :type limit: int
        :param triggers: 需要搜索的触发类型列表
        :type triggers: list[str]
        :param branches: 需要搜索的分支列表
        :type branches: list[str]
        :param tags: 需要搜索的标签列表
        :type tags: list[str]
        :param from_date: 查询起止时间,格式：yyyy-MM-dd HH:mm:ss
        :type from_date: str
        :param to_date: 查询结束时间,格式：yyyy-MM-dd HH:mm:ss
        :type to_date: str
        """
        
        

        self._build_project_id = None
        self._page = None
        self._limit = None
        self._triggers = None
        self._branches = None
        self._tags = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        self.build_project_id = build_project_id
        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit
        if triggers is not None:
            self.triggers = triggers
        if branches is not None:
            self.branches = branches
        if tags is not None:
            self.tags = tags
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def build_project_id(self):
        r"""Gets the build_project_id of this ListRecordsRequest.

        构建工程项目ID，36位数字、小写字母组合。

        :return: The build_project_id of this ListRecordsRequest.
        :rtype: str
        """
        return self._build_project_id

    @build_project_id.setter
    def build_project_id(self, build_project_id):
        r"""Sets the build_project_id of this ListRecordsRequest.

        构建工程项目ID，36位数字、小写字母组合。

        :param build_project_id: The build_project_id of this ListRecordsRequest.
        :type build_project_id: str
        """
        self._build_project_id = build_project_id

    @property
    def page(self):
        r"""Gets the page of this ListRecordsRequest.

        分页页码，表示从此页开始查询，大于等于0

        :return: The page of this ListRecordsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListRecordsRequest.

        分页页码，表示从此页开始查询，大于等于0

        :param page: The page of this ListRecordsRequest.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ListRecordsRequest.

        每页显示的条目数量，小于等于100

        :return: The limit of this ListRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecordsRequest.

        每页显示的条目数量，小于等于100

        :param limit: The limit of this ListRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def triggers(self):
        r"""Gets the triggers of this ListRecordsRequest.

        需要搜索的触发类型列表

        :return: The triggers of this ListRecordsRequest.
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this ListRecordsRequest.

        需要搜索的触发类型列表

        :param triggers: The triggers of this ListRecordsRequest.
        :type triggers: list[str]
        """
        self._triggers = triggers

    @property
    def branches(self):
        r"""Gets the branches of this ListRecordsRequest.

        需要搜索的分支列表

        :return: The branches of this ListRecordsRequest.
        :rtype: list[str]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        r"""Sets the branches of this ListRecordsRequest.

        需要搜索的分支列表

        :param branches: The branches of this ListRecordsRequest.
        :type branches: list[str]
        """
        self._branches = branches

    @property
    def tags(self):
        r"""Gets the tags of this ListRecordsRequest.

        需要搜索的标签列表

        :return: The tags of this ListRecordsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListRecordsRequest.

        需要搜索的标签列表

        :param tags: The tags of this ListRecordsRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def from_date(self):
        r"""Gets the from_date of this ListRecordsRequest.

        查询起止时间,格式：yyyy-MM-dd HH:mm:ss

        :return: The from_date of this ListRecordsRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ListRecordsRequest.

        查询起止时间,格式：yyyy-MM-dd HH:mm:ss

        :param from_date: The from_date of this ListRecordsRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ListRecordsRequest.

        查询结束时间,格式：yyyy-MM-dd HH:mm:ss

        :return: The to_date of this ListRecordsRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ListRecordsRequest.

        查询结束时间,格式：yyyy-MM-dd HH:mm:ss

        :param to_date: The to_date of this ListRecordsRequest.
        :type to_date: str
        """
        self._to_date = to_date

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
        if not isinstance(other, ListRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
