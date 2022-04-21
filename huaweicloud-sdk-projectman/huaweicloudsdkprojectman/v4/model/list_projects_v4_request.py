# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectsV4Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'search': 'str',
        'project_type': 'str',
        'sort': 'str',
        'archive': 'str',
        'query_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'project_type': 'project_type',
        'sort': 'sort',
        'archive': 'archive',
        'query_type': 'query_type'
    }

    def __init__(self, offset=None, limit=None, search=None, project_type=None, sort=None, archive=None, query_type=None):
        """ListProjectsV4Request

        The model defined in huaweicloud sdk

        :param offset: 偏移量 从0开始
        :type offset: int
        :param limit: 条数 最小1条,最大1000
        :type limit: int
        :param search: 模糊查询项目名称或描述,不支持通配符等高级查询
        :type search: str
        :param project_type: 项目类型 scrum|xboard
        :type project_type: str
        :param sort: 排序条件 默认创建时间降序(name|created_on)(asc|desc)
        :type sort: str
        :param archive: 是否归档 true已归档|false未归档
        :type archive: str
        :param query_type: 默认返回当前用户参与的项目列表,domain_projects租户下的所有项目列表,absent返回当前用户未参与的租户项目列表
        :type query_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._search = None
        self._project_type = None
        self._sort = None
        self._archive = None
        self._query_type = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if search is not None:
            self.search = search
        if project_type is not None:
            self.project_type = project_type
        if sort is not None:
            self.sort = sort
        if archive is not None:
            self.archive = archive
        if query_type is not None:
            self.query_type = query_type

    @property
    def offset(self):
        """Gets the offset of this ListProjectsV4Request.

        偏移量 从0开始

        :return: The offset of this ListProjectsV4Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectsV4Request.

        偏移量 从0开始

        :param offset: The offset of this ListProjectsV4Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProjectsV4Request.

        条数 最小1条,最大1000

        :return: The limit of this ListProjectsV4Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectsV4Request.

        条数 最小1条,最大1000

        :param limit: The limit of this ListProjectsV4Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        """Gets the search of this ListProjectsV4Request.

        模糊查询项目名称或描述,不支持通配符等高级查询

        :return: The search of this ListProjectsV4Request.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListProjectsV4Request.

        模糊查询项目名称或描述,不支持通配符等高级查询

        :param search: The search of this ListProjectsV4Request.
        :type search: str
        """
        self._search = search

    @property
    def project_type(self):
        """Gets the project_type of this ListProjectsV4Request.

        项目类型 scrum|xboard

        :return: The project_type of this ListProjectsV4Request.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this ListProjectsV4Request.

        项目类型 scrum|xboard

        :param project_type: The project_type of this ListProjectsV4Request.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def sort(self):
        """Gets the sort of this ListProjectsV4Request.

        排序条件 默认创建时间降序(name|created_on)(asc|desc)

        :return: The sort of this ListProjectsV4Request.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListProjectsV4Request.

        排序条件 默认创建时间降序(name|created_on)(asc|desc)

        :param sort: The sort of this ListProjectsV4Request.
        :type sort: str
        """
        self._sort = sort

    @property
    def archive(self):
        """Gets the archive of this ListProjectsV4Request.

        是否归档 true已归档|false未归档

        :return: The archive of this ListProjectsV4Request.
        :rtype: str
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this ListProjectsV4Request.

        是否归档 true已归档|false未归档

        :param archive: The archive of this ListProjectsV4Request.
        :type archive: str
        """
        self._archive = archive

    @property
    def query_type(self):
        """Gets the query_type of this ListProjectsV4Request.

        默认返回当前用户参与的项目列表,domain_projects租户下的所有项目列表,absent返回当前用户未参与的租户项目列表

        :return: The query_type of this ListProjectsV4Request.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListProjectsV4Request.

        默认返回当前用户参与的项目列表,domain_projects租户下的所有项目列表,absent返回当前用户未参与的租户项目列表

        :param query_type: The query_type of this ListProjectsV4Request.
        :type query_type: str
        """
        self._query_type = query_type

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
        if not isinstance(other, ListProjectsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
