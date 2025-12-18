# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommitsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'offset': 'int',
        'limit': 'int',
        'ref_name': 'str',
        'since': 'str',
        'until': 'str',
        'path': 'str',
        'message': 'str',
        'author': 'str',
        'order_by_date': 'bool',
        'follow': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'ref_name': 'ref_name',
        'since': 'since',
        'until': 'until',
        'path': 'path',
        'message': 'message',
        'author': 'author',
        'order_by_date': 'order_by_date',
        'follow': 'follow'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, ref_name=None, since=None, until=None, path=None, message=None, author=None, order_by_date=None, follow=None):
        r"""ListCommitsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param ref_name: 分支/tag名
        :type ref_name: str
        :param since: 起始时间（不包含）
        :type since: str
        :param until: 结束时间（不包含）
        :type until: str
        :param path: The file path
        :type path: str
        :param message: 提交信息或者commit id
        :type message: str
        :param author: 代码作者名称
        :type author: str
        :param order_by_date: 是否按照时间降序排序
        :type order_by_date: bool
        :param follow: 为true时可以追踪文件移动、改名前后的提交记录
        :type follow: bool
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._ref_name = None
        self._since = None
        self._until = None
        self._path = None
        self._message = None
        self._author = None
        self._order_by_date = None
        self._follow = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if ref_name is not None:
            self.ref_name = ref_name
        if since is not None:
            self.since = since
        if until is not None:
            self.until = until
        if path is not None:
            self.path = path
        if message is not None:
            self.message = message
        if author is not None:
            self.author = author
        if order_by_date is not None:
            self.order_by_date = order_by_date
        if follow is not None:
            self.follow = follow

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListCommitsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListCommitsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListCommitsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListCommitsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCommitsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListCommitsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCommitsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListCommitsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCommitsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListCommitsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCommitsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListCommitsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ref_name(self):
        r"""Gets the ref_name of this ListCommitsRequest.

        分支/tag名

        :return: The ref_name of this ListCommitsRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        r"""Sets the ref_name of this ListCommitsRequest.

        分支/tag名

        :param ref_name: The ref_name of this ListCommitsRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def since(self):
        r"""Gets the since of this ListCommitsRequest.

        起始时间（不包含）

        :return: The since of this ListCommitsRequest.
        :rtype: str
        """
        return self._since

    @since.setter
    def since(self, since):
        r"""Sets the since of this ListCommitsRequest.

        起始时间（不包含）

        :param since: The since of this ListCommitsRequest.
        :type since: str
        """
        self._since = since

    @property
    def until(self):
        r"""Gets the until of this ListCommitsRequest.

        结束时间（不包含）

        :return: The until of this ListCommitsRequest.
        :rtype: str
        """
        return self._until

    @until.setter
    def until(self, until):
        r"""Sets the until of this ListCommitsRequest.

        结束时间（不包含）

        :param until: The until of this ListCommitsRequest.
        :type until: str
        """
        self._until = until

    @property
    def path(self):
        r"""Gets the path of this ListCommitsRequest.

        The file path

        :return: The path of this ListCommitsRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListCommitsRequest.

        The file path

        :param path: The path of this ListCommitsRequest.
        :type path: str
        """
        self._path = path

    @property
    def message(self):
        r"""Gets the message of this ListCommitsRequest.

        提交信息或者commit id

        :return: The message of this ListCommitsRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListCommitsRequest.

        提交信息或者commit id

        :param message: The message of this ListCommitsRequest.
        :type message: str
        """
        self._message = message

    @property
    def author(self):
        r"""Gets the author of this ListCommitsRequest.

        代码作者名称

        :return: The author of this ListCommitsRequest.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ListCommitsRequest.

        代码作者名称

        :param author: The author of this ListCommitsRequest.
        :type author: str
        """
        self._author = author

    @property
    def order_by_date(self):
        r"""Gets the order_by_date of this ListCommitsRequest.

        是否按照时间降序排序

        :return: The order_by_date of this ListCommitsRequest.
        :rtype: bool
        """
        return self._order_by_date

    @order_by_date.setter
    def order_by_date(self, order_by_date):
        r"""Sets the order_by_date of this ListCommitsRequest.

        是否按照时间降序排序

        :param order_by_date: The order_by_date of this ListCommitsRequest.
        :type order_by_date: bool
        """
        self._order_by_date = order_by_date

    @property
    def follow(self):
        r"""Gets the follow of this ListCommitsRequest.

        为true时可以追踪文件移动、改名前后的提交记录

        :return: The follow of this ListCommitsRequest.
        :rtype: bool
        """
        return self._follow

    @follow.setter
    def follow(self, follow):
        r"""Sets the follow of this ListCommitsRequest.

        为true时可以追踪文件移动、改名前后的提交记录

        :param follow: The follow of this ListCommitsRequest.
        :type follow: bool
        """
        self._follow = follow

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
        if not isinstance(other, ListCommitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
