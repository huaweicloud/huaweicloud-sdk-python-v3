# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_name': 'str',
        'member_number': 'int',
        'status': 'int',
        'owner': 'str',
        'created_after': 'datetime',
        'created_before': 'datetime',
        'sort': 'str',
        'sort_field': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_name': 'repository_name',
        'member_number': 'member_number',
        'status': 'status',
        'owner': 'owner',
        'created_after': 'created_after',
        'created_before': 'created_before',
        'sort': 'sort',
        'sort_field': 'sort_field',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_name=None, member_number=None, status=None, owner=None, created_after=None, created_before=None, sort=None, sort_field=None, offset=None, limit=None):
        r"""ListTenantRepositoriesRequest

        The model defined in huaweicloud sdk

        :param repository_name: **参数解释：** 仓库名称。 **取值范围：** 字符串长度不少于1，不超过128。
        :type repository_name: str
        :param member_number: **参数解释：** 成员数量。
        :type member_number: int
        :param status: **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。
        :type status: int
        :param owner: **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。
        :type owner: str
        :param created_after: **参数解释：** 筛选在该时间之后创建的仓库。
        :type created_after: datetime
        :param created_before: **参数解释：** 筛选在该时间之前创建的仓库。
        :type created_before: datetime
        :param sort: **参数解释：** 结果集排序方式。 **约束限制：** 与sort_field搭配使用。  **取值范围：** - asc，正序返回。 - desc，倒序返回。
        :type sort: str
        :param sort_field: **参数解释：** 用作排序的字段。 - owner，仓库所有者。 - capacity，使用空间。 - status，状态。 - create_time，创建时间。 - member_number，成员数量。 - repository_name，仓库名称。
        :type sort_field: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_name = None
        self._member_number = None
        self._status = None
        self._owner = None
        self._created_after = None
        self._created_before = None
        self._sort = None
        self._sort_field = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if repository_name is not None:
            self.repository_name = repository_name
        if member_number is not None:
            self.member_number = member_number
        if status is not None:
            self.status = status
        if owner is not None:
            self.owner = owner
        if created_after is not None:
            self.created_after = created_after
        if created_before is not None:
            self.created_before = created_before
        if sort is not None:
            self.sort = sort
        if sort_field is not None:
            self.sort_field = sort_field
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库名称。 **取值范围：** 字符串长度不少于1，不超过128。

        :return: The repository_name of this ListTenantRepositoriesRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库名称。 **取值范围：** 字符串长度不少于1，不超过128。

        :param repository_name: The repository_name of this ListTenantRepositoriesRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def member_number(self):
        r"""Gets the member_number of this ListTenantRepositoriesRequest.

        **参数解释：** 成员数量。

        :return: The member_number of this ListTenantRepositoriesRequest.
        :rtype: int
        """
        return self._member_number

    @member_number.setter
    def member_number(self, member_number):
        r"""Sets the member_number of this ListTenantRepositoriesRequest.

        **参数解释：** 成员数量。

        :param member_number: The member_number of this ListTenantRepositoriesRequest.
        :type member_number: int
        """
        self._member_number = member_number

    @property
    def status(self):
        r"""Gets the status of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。

        :return: The status of this ListTenantRepositoriesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。

        :param status: The status of this ListTenantRepositoriesRequest.
        :type status: int
        """
        self._status = status

    @property
    def owner(self):
        r"""Gets the owner of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。

        :return: The owner of this ListTenantRepositoriesRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListTenantRepositoriesRequest.

        **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。

        :param owner: The owner of this ListTenantRepositoriesRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def created_after(self):
        r"""Gets the created_after of this ListTenantRepositoriesRequest.

        **参数解释：** 筛选在该时间之后创建的仓库。

        :return: The created_after of this ListTenantRepositoriesRequest.
        :rtype: datetime
        """
        return self._created_after

    @created_after.setter
    def created_after(self, created_after):
        r"""Sets the created_after of this ListTenantRepositoriesRequest.

        **参数解释：** 筛选在该时间之后创建的仓库。

        :param created_after: The created_after of this ListTenantRepositoriesRequest.
        :type created_after: datetime
        """
        self._created_after = created_after

    @property
    def created_before(self):
        r"""Gets the created_before of this ListTenantRepositoriesRequest.

        **参数解释：** 筛选在该时间之前创建的仓库。

        :return: The created_before of this ListTenantRepositoriesRequest.
        :rtype: datetime
        """
        return self._created_before

    @created_before.setter
    def created_before(self, created_before):
        r"""Sets the created_before of this ListTenantRepositoriesRequest.

        **参数解释：** 筛选在该时间之前创建的仓库。

        :param created_before: The created_before of this ListTenantRepositoriesRequest.
        :type created_before: datetime
        """
        self._created_before = created_before

    @property
    def sort(self):
        r"""Gets the sort of this ListTenantRepositoriesRequest.

        **参数解释：** 结果集排序方式。 **约束限制：** 与sort_field搭配使用。  **取值范围：** - asc，正序返回。 - desc，倒序返回。

        :return: The sort of this ListTenantRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListTenantRepositoriesRequest.

        **参数解释：** 结果集排序方式。 **约束限制：** 与sort_field搭配使用。  **取值范围：** - asc，正序返回。 - desc，倒序返回。

        :param sort: The sort of this ListTenantRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListTenantRepositoriesRequest.

        **参数解释：** 用作排序的字段。 - owner，仓库所有者。 - capacity，使用空间。 - status，状态。 - create_time，创建时间。 - member_number，成员数量。 - repository_name，仓库名称。

        :return: The sort_field of this ListTenantRepositoriesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListTenantRepositoriesRequest.

        **参数解释：** 用作排序的字段。 - owner，仓库所有者。 - capacity，使用空间。 - status，状态。 - create_time，创建时间。 - member_number，成员数量。 - repository_name，仓库名称。

        :param sort_field: The sort_field of this ListTenantRepositoriesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListTenantRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListTenantRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListTenantRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListTenantRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTenantRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
