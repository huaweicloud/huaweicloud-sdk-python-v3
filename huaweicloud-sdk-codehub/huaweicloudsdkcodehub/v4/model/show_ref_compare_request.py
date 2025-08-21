# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRefCompareRequest:

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
        '_from': 'str',
        'to': 'str',
        'compare_type': 'str',
        'target_id': 'int',
        'straight': 'bool',
        'ignore_whitespace_change': 'bool',
        'view': 'str',
        'only_count': 'bool',
        'file_path': 'str',
        'additional_fields': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        '_from': 'from',
        'to': 'to',
        'compare_type': 'compare_type',
        'target_id': 'target_id',
        'straight': 'straight',
        'ignore_whitespace_change': 'ignore_whitespace_change',
        'view': 'view',
        'only_count': 'only_count',
        'file_path': 'file_path',
        'additional_fields': 'additional_fields',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, _from=None, to=None, compare_type=None, target_id=None, straight=None, ignore_whitespace_change=None, view=None, only_count=None, file_path=None, additional_fields=None, offset=None, limit=None):
        r"""ShowRefCompareRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param _from: **参数解释：** 要开始比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type _from: str
        :param to: **参数解释：** 要停止比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type to: str
        :param compare_type: **参数解释：** 对比类型。 **取值范围：** - branch，分支。 - commit，提交。 - tag，标签。
        :type compare_type: str
        :param target_id: **参数解释：** 合并请求的目标仓库，默认为仓库ID。
        :type target_id: int
        :param straight: **参数解释：** 比较方法。 **取值范围：** - true，用于&#x60;from&#x60;和&#x60;to&#x60;之间的直接比较(&#x60;from&#x60;..&#x60;to&#x60;)。 - false，使用merge base进行比较(&#x60;from&#x60;...&#x60;to&#x60;)。
        :type straight: bool
        :param ignore_whitespace_change: **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。
        :type ignore_whitespace_change: bool
        :param view: **参数解释：** 是否忽略空白数量更改。 **取值范围：** - count，数量。 - commits，提交信息。 - diffs，差异信息。 - files，文件信息。 - commits,diffs，提交信息和差异信息。
        :type view: str
        :param only_count: **参数解释：** 是否仅返回带有提交计数和diffs计数的结果。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。
        :type only_count: bool
        :param file_path: **参数解释：** 根据给定的文件路径返回不同的结果。如果文件已重命名，则file_path应包括old_path和new_path，如“file_path&#x3D;old_path,new_path”。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type file_path: str
        :param additional_fields: **参数解释：** 根据给定的参数返回不同的结果。 **取值范围：** - change_lines，变更行数。
        :type additional_fields: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self.__from = None
        self._to = None
        self._compare_type = None
        self._target_id = None
        self._straight = None
        self._ignore_whitespace_change = None
        self._view = None
        self._only_count = None
        self._file_path = None
        self._additional_fields = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        self._from = _from
        self.to = to
        if compare_type is not None:
            self.compare_type = compare_type
        if target_id is not None:
            self.target_id = target_id
        if straight is not None:
            self.straight = straight
        if ignore_whitespace_change is not None:
            self.ignore_whitespace_change = ignore_whitespace_change
        if view is not None:
            self.view = view
        if only_count is not None:
            self.only_count = only_count
        if file_path is not None:
            self.file_path = file_path
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRefCompareRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowRefCompareRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRefCompareRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowRefCompareRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def _from(self):
        r"""Gets the _from of this ShowRefCompareRequest.

        **参数解释：** 要开始比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The _from of this ShowRefCompareRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowRefCompareRequest.

        **参数解释：** 要开始比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param _from: The _from of this ShowRefCompareRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowRefCompareRequest.

        **参数解释：** 要停止比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The to of this ShowRefCompareRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowRefCompareRequest.

        **参数解释：** 要停止比较的分支名称、标签名称或者commitid。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param to: The to of this ShowRefCompareRequest.
        :type to: str
        """
        self._to = to

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ShowRefCompareRequest.

        **参数解释：** 对比类型。 **取值范围：** - branch，分支。 - commit，提交。 - tag，标签。

        :return: The compare_type of this ShowRefCompareRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ShowRefCompareRequest.

        **参数解释：** 对比类型。 **取值范围：** - branch，分支。 - commit，提交。 - tag，标签。

        :param compare_type: The compare_type of this ShowRefCompareRequest.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def target_id(self):
        r"""Gets the target_id of this ShowRefCompareRequest.

        **参数解释：** 合并请求的目标仓库，默认为仓库ID。

        :return: The target_id of this ShowRefCompareRequest.
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this ShowRefCompareRequest.

        **参数解释：** 合并请求的目标仓库，默认为仓库ID。

        :param target_id: The target_id of this ShowRefCompareRequest.
        :type target_id: int
        """
        self._target_id = target_id

    @property
    def straight(self):
        r"""Gets the straight of this ShowRefCompareRequest.

        **参数解释：** 比较方法。 **取值范围：** - true，用于`from`和`to`之间的直接比较(`from`..`to`)。 - false，使用merge base进行比较(`from`...`to`)。

        :return: The straight of this ShowRefCompareRequest.
        :rtype: bool
        """
        return self._straight

    @straight.setter
    def straight(self, straight):
        r"""Sets the straight of this ShowRefCompareRequest.

        **参数解释：** 比较方法。 **取值范围：** - true，用于`from`和`to`之间的直接比较(`from`..`to`)。 - false，使用merge base进行比较(`from`...`to`)。

        :param straight: The straight of this ShowRefCompareRequest.
        :type straight: bool
        """
        self._straight = straight

    @property
    def ignore_whitespace_change(self):
        r"""Gets the ignore_whitespace_change of this ShowRefCompareRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。

        :return: The ignore_whitespace_change of this ShowRefCompareRequest.
        :rtype: bool
        """
        return self._ignore_whitespace_change

    @ignore_whitespace_change.setter
    def ignore_whitespace_change(self, ignore_whitespace_change):
        r"""Sets the ignore_whitespace_change of this ShowRefCompareRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。

        :param ignore_whitespace_change: The ignore_whitespace_change of this ShowRefCompareRequest.
        :type ignore_whitespace_change: bool
        """
        self._ignore_whitespace_change = ignore_whitespace_change

    @property
    def view(self):
        r"""Gets the view of this ShowRefCompareRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - count，数量。 - commits，提交信息。 - diffs，差异信息。 - files，文件信息。 - commits,diffs，提交信息和差异信息。

        :return: The view of this ShowRefCompareRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ShowRefCompareRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - count，数量。 - commits，提交信息。 - diffs，差异信息。 - files，文件信息。 - commits,diffs，提交信息和差异信息。

        :param view: The view of this ShowRefCompareRequest.
        :type view: str
        """
        self._view = view

    @property
    def only_count(self):
        r"""Gets the only_count of this ShowRefCompareRequest.

        **参数解释：** 是否仅返回带有提交计数和diffs计数的结果。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。

        :return: The only_count of this ShowRefCompareRequest.
        :rtype: bool
        """
        return self._only_count

    @only_count.setter
    def only_count(self, only_count):
        r"""Sets the only_count of this ShowRefCompareRequest.

        **参数解释：** 是否仅返回带有提交计数和diffs计数的结果。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。

        :param only_count: The only_count of this ShowRefCompareRequest.
        :type only_count: bool
        """
        self._only_count = only_count

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowRefCompareRequest.

        **参数解释：** 根据给定的文件路径返回不同的结果。如果文件已重命名，则file_path应包括old_path和new_path，如“file_path=old_path,new_path”。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The file_path of this ShowRefCompareRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowRefCompareRequest.

        **参数解释：** 根据给定的文件路径返回不同的结果。如果文件已重命名，则file_path应包括old_path和new_path，如“file_path=old_path,new_path”。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param file_path: The file_path of this ShowRefCompareRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def additional_fields(self):
        r"""Gets the additional_fields of this ShowRefCompareRequest.

        **参数解释：** 根据给定的参数返回不同的结果。 **取值范围：** - change_lines，变更行数。

        :return: The additional_fields of this ShowRefCompareRequest.
        :rtype: str
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        r"""Sets the additional_fields of this ShowRefCompareRequest.

        **参数解释：** 根据给定的参数返回不同的结果。 **取值范围：** - change_lines，变更行数。

        :param additional_fields: The additional_fields of this ShowRefCompareRequest.
        :type additional_fields: str
        """
        self._additional_fields = additional_fields

    @property
    def offset(self):
        r"""Gets the offset of this ShowRefCompareRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ShowRefCompareRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowRefCompareRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ShowRefCompareRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowRefCompareRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ShowRefCompareRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowRefCompareRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ShowRefCompareRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowRefCompareRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
