# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateUpdateApiTestCaseVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'type': 'str',
        'author': 'str',
        'name': 'str',
        'rank': 'int',
        'last_modifier': 'str',
        'last_modified': 'datetime',
        'last_modified_timestamp': 'int',
        'last_change_time': 'datetime',
        'version_uri': 'str',
        'origin_uri': 'str',
        'parent_uri': 'str',
        'parent_path': 'str',
        'creation_version_uri': 'str',
        'creation_date': 'datetime',
        'creation_date_timestamp': 'int',
        'author_name': 'str',
        'comment': 'str',
        'number': 'str',
        'success_list': 'list[TestCaseVo]',
        'failed_list': 'list[TestCaseInfo]'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type',
        'author': 'author',
        'name': 'name',
        'rank': 'rank',
        'last_modifier': 'last_modifier',
        'last_modified': 'last_modified',
        'last_modified_timestamp': 'last_modified_timestamp',
        'last_change_time': 'last_change_time',
        'version_uri': 'version_uri',
        'origin_uri': 'origin_uri',
        'parent_uri': 'parent_uri',
        'parent_path': 'parent_path',
        'creation_version_uri': 'creation_version_uri',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'author_name': 'author_name',
        'comment': 'comment',
        'number': 'number',
        'success_list': 'success_list',
        'failed_list': 'failed_list'
    }

    def __init__(self, uri=None, type=None, author=None, name=None, rank=None, last_modifier=None, last_modified=None, last_modified_timestamp=None, last_change_time=None, version_uri=None, origin_uri=None, parent_uri=None, parent_path=None, creation_version_uri=None, creation_date=None, creation_date_timestamp=None, author_name=None, comment=None, number=None, success_list=None, failed_list=None):
        r"""BatchCreateUpdateApiTestCaseVo

        The model defined in huaweicloud sdk

        :param uri: 资源URI
        :type uri: str
        :param type: 资源类型
        :type type: str
        :param author: 创建人
        :type author: str
        :param name: 名称
        :type name: str
        :param rank: 级别
        :type rank: int
        :param last_modifier: 最后修改人
        :type last_modifier: str
        :param last_modified: 最后修改时间
        :type last_modified: datetime
        :param last_modified_timestamp: 修改时间时间戳
        :type last_modified_timestamp: int
        :param last_change_time: 最后变更时间
        :type last_change_time: datetime
        :param version_uri: 版本URI
        :type version_uri: str
        :param origin_uri: 源资源URI
        :type origin_uri: str
        :param parent_uri: 父资源URI
        :type parent_uri: str
        :param parent_path: 父资源路径
        :type parent_path: str
        :param creation_version_uri: 创建版本URI
        :type creation_version_uri: str
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param creation_date_timestamp: 创建时间时间戳
        :type creation_date_timestamp: int
        :param author_name: 创建人名称
        :type author_name: str
        :param comment: 备注
        :type comment: str
        :param number: 编号
        :type number: str
        :param success_list: 创建成功的用例列表
        :type success_list: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        :param failed_list: 创建失败的用例列表
        :type failed_list: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`]
        """
        
        

        self._uri = None
        self._type = None
        self._author = None
        self._name = None
        self._rank = None
        self._last_modifier = None
        self._last_modified = None
        self._last_modified_timestamp = None
        self._last_change_time = None
        self._version_uri = None
        self._origin_uri = None
        self._parent_uri = None
        self._parent_path = None
        self._creation_version_uri = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._author_name = None
        self._comment = None
        self._number = None
        self._success_list = None
        self._failed_list = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if author is not None:
            self.author = author
        if name is not None:
            self.name = name
        if rank is not None:
            self.rank = rank
        if last_modifier is not None:
            self.last_modifier = last_modifier
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if last_change_time is not None:
            self.last_change_time = last_change_time
        if version_uri is not None:
            self.version_uri = version_uri
        if origin_uri is not None:
            self.origin_uri = origin_uri
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if parent_path is not None:
            self.parent_path = parent_path
        if creation_version_uri is not None:
            self.creation_version_uri = creation_version_uri
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if author_name is not None:
            self.author_name = author_name
        if comment is not None:
            self.comment = comment
        if number is not None:
            self.number = number
        if success_list is not None:
            self.success_list = success_list
        if failed_list is not None:
            self.failed_list = failed_list

    @property
    def uri(self):
        r"""Gets the uri of this BatchCreateUpdateApiTestCaseVo.

        资源URI

        :return: The uri of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this BatchCreateUpdateApiTestCaseVo.

        资源URI

        :param uri: The uri of this BatchCreateUpdateApiTestCaseVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def type(self):
        r"""Gets the type of this BatchCreateUpdateApiTestCaseVo.

        资源类型

        :return: The type of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchCreateUpdateApiTestCaseVo.

        资源类型

        :param type: The type of this BatchCreateUpdateApiTestCaseVo.
        :type type: str
        """
        self._type = type

    @property
    def author(self):
        r"""Gets the author of this BatchCreateUpdateApiTestCaseVo.

        创建人

        :return: The author of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this BatchCreateUpdateApiTestCaseVo.

        创建人

        :param author: The author of this BatchCreateUpdateApiTestCaseVo.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        r"""Gets the name of this BatchCreateUpdateApiTestCaseVo.

        名称

        :return: The name of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateUpdateApiTestCaseVo.

        名称

        :param name: The name of this BatchCreateUpdateApiTestCaseVo.
        :type name: str
        """
        self._name = name

    @property
    def rank(self):
        r"""Gets the rank of this BatchCreateUpdateApiTestCaseVo.

        级别

        :return: The rank of this BatchCreateUpdateApiTestCaseVo.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        r"""Sets the rank of this BatchCreateUpdateApiTestCaseVo.

        级别

        :param rank: The rank of this BatchCreateUpdateApiTestCaseVo.
        :type rank: int
        """
        self._rank = rank

    @property
    def last_modifier(self):
        r"""Gets the last_modifier of this BatchCreateUpdateApiTestCaseVo.

        最后修改人

        :return: The last_modifier of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        r"""Sets the last_modifier of this BatchCreateUpdateApiTestCaseVo.

        最后修改人

        :param last_modifier: The last_modifier of this BatchCreateUpdateApiTestCaseVo.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_modified(self):
        r"""Gets the last_modified of this BatchCreateUpdateApiTestCaseVo.

        最后修改时间

        :return: The last_modified of this BatchCreateUpdateApiTestCaseVo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this BatchCreateUpdateApiTestCaseVo.

        最后修改时间

        :param last_modified: The last_modified of this BatchCreateUpdateApiTestCaseVo.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        r"""Gets the last_modified_timestamp of this BatchCreateUpdateApiTestCaseVo.

        修改时间时间戳

        :return: The last_modified_timestamp of this BatchCreateUpdateApiTestCaseVo.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        r"""Sets the last_modified_timestamp of this BatchCreateUpdateApiTestCaseVo.

        修改时间时间戳

        :param last_modified_timestamp: The last_modified_timestamp of this BatchCreateUpdateApiTestCaseVo.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_change_time(self):
        r"""Gets the last_change_time of this BatchCreateUpdateApiTestCaseVo.

        最后变更时间

        :return: The last_change_time of this BatchCreateUpdateApiTestCaseVo.
        :rtype: datetime
        """
        return self._last_change_time

    @last_change_time.setter
    def last_change_time(self, last_change_time):
        r"""Sets the last_change_time of this BatchCreateUpdateApiTestCaseVo.

        最后变更时间

        :param last_change_time: The last_change_time of this BatchCreateUpdateApiTestCaseVo.
        :type last_change_time: datetime
        """
        self._last_change_time = last_change_time

    @property
    def version_uri(self):
        r"""Gets the version_uri of this BatchCreateUpdateApiTestCaseVo.

        版本URI

        :return: The version_uri of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this BatchCreateUpdateApiTestCaseVo.

        版本URI

        :param version_uri: The version_uri of this BatchCreateUpdateApiTestCaseVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def origin_uri(self):
        r"""Gets the origin_uri of this BatchCreateUpdateApiTestCaseVo.

        源资源URI

        :return: The origin_uri of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        r"""Sets the origin_uri of this BatchCreateUpdateApiTestCaseVo.

        源资源URI

        :param origin_uri: The origin_uri of this BatchCreateUpdateApiTestCaseVo.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this BatchCreateUpdateApiTestCaseVo.

        父资源URI

        :return: The parent_uri of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this BatchCreateUpdateApiTestCaseVo.

        父资源URI

        :param parent_uri: The parent_uri of this BatchCreateUpdateApiTestCaseVo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_path(self):
        r"""Gets the parent_path of this BatchCreateUpdateApiTestCaseVo.

        父资源路径

        :return: The parent_path of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        r"""Sets the parent_path of this BatchCreateUpdateApiTestCaseVo.

        父资源路径

        :param parent_path: The parent_path of this BatchCreateUpdateApiTestCaseVo.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def creation_version_uri(self):
        r"""Gets the creation_version_uri of this BatchCreateUpdateApiTestCaseVo.

        创建版本URI

        :return: The creation_version_uri of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        r"""Sets the creation_version_uri of this BatchCreateUpdateApiTestCaseVo.

        创建版本URI

        :param creation_version_uri: The creation_version_uri of this BatchCreateUpdateApiTestCaseVo.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def creation_date(self):
        r"""Gets the creation_date of this BatchCreateUpdateApiTestCaseVo.

        创建时间

        :return: The creation_date of this BatchCreateUpdateApiTestCaseVo.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this BatchCreateUpdateApiTestCaseVo.

        创建时间

        :param creation_date: The creation_date of this BatchCreateUpdateApiTestCaseVo.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        r"""Gets the creation_date_timestamp of this BatchCreateUpdateApiTestCaseVo.

        创建时间时间戳

        :return: The creation_date_timestamp of this BatchCreateUpdateApiTestCaseVo.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        r"""Sets the creation_date_timestamp of this BatchCreateUpdateApiTestCaseVo.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this BatchCreateUpdateApiTestCaseVo.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def author_name(self):
        r"""Gets the author_name of this BatchCreateUpdateApiTestCaseVo.

        创建人名称

        :return: The author_name of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this BatchCreateUpdateApiTestCaseVo.

        创建人名称

        :param author_name: The author_name of this BatchCreateUpdateApiTestCaseVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def comment(self):
        r"""Gets the comment of this BatchCreateUpdateApiTestCaseVo.

        备注

        :return: The comment of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this BatchCreateUpdateApiTestCaseVo.

        备注

        :param comment: The comment of this BatchCreateUpdateApiTestCaseVo.
        :type comment: str
        """
        self._comment = comment

    @property
    def number(self):
        r"""Gets the number of this BatchCreateUpdateApiTestCaseVo.

        编号

        :return: The number of this BatchCreateUpdateApiTestCaseVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this BatchCreateUpdateApiTestCaseVo.

        编号

        :param number: The number of this BatchCreateUpdateApiTestCaseVo.
        :type number: str
        """
        self._number = number

    @property
    def success_list(self):
        r"""Gets the success_list of this BatchCreateUpdateApiTestCaseVo.

        创建成功的用例列表

        :return: The success_list of this BatchCreateUpdateApiTestCaseVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        """
        return self._success_list

    @success_list.setter
    def success_list(self, success_list):
        r"""Sets the success_list of this BatchCreateUpdateApiTestCaseVo.

        创建成功的用例列表

        :param success_list: The success_list of this BatchCreateUpdateApiTestCaseVo.
        :type success_list: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        """
        self._success_list = success_list

    @property
    def failed_list(self):
        r"""Gets the failed_list of this BatchCreateUpdateApiTestCaseVo.

        创建失败的用例列表

        :return: The failed_list of this BatchCreateUpdateApiTestCaseVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`]
        """
        return self._failed_list

    @failed_list.setter
    def failed_list(self, failed_list):
        r"""Sets the failed_list of this BatchCreateUpdateApiTestCaseVo.

        创建失败的用例列表

        :param failed_list: The failed_list of this BatchCreateUpdateApiTestCaseVo.
        :type failed_list: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseInfo`]
        """
        self._failed_list = failed_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCreateUpdateApiTestCaseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
