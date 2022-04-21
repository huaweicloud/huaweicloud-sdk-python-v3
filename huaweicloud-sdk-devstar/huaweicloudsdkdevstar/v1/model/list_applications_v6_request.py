# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsV6Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'attention': 'bool',
        'region_id': 'str',
        'keyword': 'str',
        'project_id': 'str',
        'topic_id': 'str',
        'is_created_by_self': 'bool',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'attention': 'attention',
        'region_id': 'region_id',
        'keyword': 'keyword',
        'project_id': 'project_id',
        'topic_id': 'topic_id',
        'is_created_by_self': 'is_created_by_self',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, attention=None, region_id=None, keyword=None, project_id=None, topic_id=None, is_created_by_self=None, sort_key=None, sort_dir=None, limit=None, offset=None):
        """ListApplicationsV6Request

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param attention: 是否查询我关注的应用
        :type attention: bool
        :param region_id: 区域id，从控制台获取方法请参见: [获取区域ID](https://console.huaweicloud.com/iam/?region&#x3D;cn-north-1&amp;locale&#x3D;zh-cn#/iam/projects)
        :type region_id: str
        :param keyword: 搜索关键字,支持按名称和描述搜索，默认null
        :type keyword: str
        :param project_id: 所属DevCloud项目id，从 [项目列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;DevStar&amp;api&#x3D;ListProjectsV4) 查询。
        :type project_id: str
        :param topic_id: 主题id,场景或者部署方式分类id
        :type topic_id: str
        :param is_created_by_self: 是否查询由我创建
        :type is_created_by_self: bool
        :param sort_key: 排序字段, name：应用名称,created_at:创建时间,updated_at:更新时间
        :type sort_key: list[str]
        :param sort_dir: 排序方式, desc:降序, asc:升序
        :type sort_dir: list[str]
        :param limit: 每页显示的条目数量,默认10
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询,默认0
        :type offset: int
        """
        
        

        self._x_language = None
        self._attention = None
        self._region_id = None
        self._keyword = None
        self._project_id = None
        self._topic_id = None
        self._is_created_by_self = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if attention is not None:
            self.attention = attention
        if region_id is not None:
            self.region_id = region_id
        if keyword is not None:
            self.keyword = keyword
        if project_id is not None:
            self.project_id = project_id
        if topic_id is not None:
            self.topic_id = topic_id
        if is_created_by_self is not None:
            self.is_created_by_self = is_created_by_self
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListApplicationsV6Request.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this ListApplicationsV6Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListApplicationsV6Request.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this ListApplicationsV6Request.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def attention(self):
        """Gets the attention of this ListApplicationsV6Request.

        是否查询我关注的应用

        :return: The attention of this ListApplicationsV6Request.
        :rtype: bool
        """
        return self._attention

    @attention.setter
    def attention(self, attention):
        """Sets the attention of this ListApplicationsV6Request.

        是否查询我关注的应用

        :param attention: The attention of this ListApplicationsV6Request.
        :type attention: bool
        """
        self._attention = attention

    @property
    def region_id(self):
        """Gets the region_id of this ListApplicationsV6Request.

        区域id，从控制台获取方法请参见: [获取区域ID](https://console.huaweicloud.com/iam/?region=cn-north-1&locale=zh-cn#/iam/projects)

        :return: The region_id of this ListApplicationsV6Request.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListApplicationsV6Request.

        区域id，从控制台获取方法请参见: [获取区域ID](https://console.huaweicloud.com/iam/?region=cn-north-1&locale=zh-cn#/iam/projects)

        :param region_id: The region_id of this ListApplicationsV6Request.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def keyword(self):
        """Gets the keyword of this ListApplicationsV6Request.

        搜索关键字,支持按名称和描述搜索，默认null

        :return: The keyword of this ListApplicationsV6Request.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListApplicationsV6Request.

        搜索关键字,支持按名称和描述搜索，默认null

        :param keyword: The keyword of this ListApplicationsV6Request.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def project_id(self):
        """Gets the project_id of this ListApplicationsV6Request.

        所属DevCloud项目id，从 [项目列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=DevStar&api=ListProjectsV4) 查询。

        :return: The project_id of this ListApplicationsV6Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListApplicationsV6Request.

        所属DevCloud项目id，从 [项目列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=DevStar&api=ListProjectsV4) 查询。

        :param project_id: The project_id of this ListApplicationsV6Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def topic_id(self):
        """Gets the topic_id of this ListApplicationsV6Request.

        主题id,场景或者部署方式分类id

        :return: The topic_id of this ListApplicationsV6Request.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this ListApplicationsV6Request.

        主题id,场景或者部署方式分类id

        :param topic_id: The topic_id of this ListApplicationsV6Request.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def is_created_by_self(self):
        """Gets the is_created_by_self of this ListApplicationsV6Request.

        是否查询由我创建

        :return: The is_created_by_self of this ListApplicationsV6Request.
        :rtype: bool
        """
        return self._is_created_by_self

    @is_created_by_self.setter
    def is_created_by_self(self, is_created_by_self):
        """Sets the is_created_by_self of this ListApplicationsV6Request.

        是否查询由我创建

        :param is_created_by_self: The is_created_by_self of this ListApplicationsV6Request.
        :type is_created_by_self: bool
        """
        self._is_created_by_self = is_created_by_self

    @property
    def sort_key(self):
        """Gets the sort_key of this ListApplicationsV6Request.

        排序字段, name：应用名称,created_at:创建时间,updated_at:更新时间

        :return: The sort_key of this ListApplicationsV6Request.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListApplicationsV6Request.

        排序字段, name：应用名称,created_at:创建时间,updated_at:更新时间

        :param sort_key: The sort_key of this ListApplicationsV6Request.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListApplicationsV6Request.

        排序方式, desc:降序, asc:升序

        :return: The sort_dir of this ListApplicationsV6Request.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListApplicationsV6Request.

        排序方式, desc:降序, asc:升序

        :param sort_dir: The sort_dir of this ListApplicationsV6Request.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListApplicationsV6Request.

        每页显示的条目数量,默认10

        :return: The limit of this ListApplicationsV6Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApplicationsV6Request.

        每页显示的条目数量,默认10

        :param limit: The limit of this ListApplicationsV6Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListApplicationsV6Request.

        偏移量，表示从此偏移量开始查询,默认0

        :return: The offset of this ListApplicationsV6Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApplicationsV6Request.

        偏移量，表示从此偏移量开始查询,默认0

        :param offset: The offset of this ListApplicationsV6Request.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListApplicationsV6Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
