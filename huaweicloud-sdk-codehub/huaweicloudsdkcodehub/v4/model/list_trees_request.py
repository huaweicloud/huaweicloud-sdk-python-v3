# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTreesRequest:

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
        'ref': 'str',
        'path': 'str',
        'recursive': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'ref': 'ref',
        'path': 'path',
        'recursive': 'recursive',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, ref=None, path=None, recursive=None, offset=None, limit=None):
        r"""ListTreesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param ref: **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type ref: str
        :param path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type path: str
        :param recursive: **参数解释：** 是否递归查询
        :type recursive: bool
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._ref = None
        self._path = None
        self._recursive = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        if ref is not None:
            self.ref = ref
        if path is not None:
            self.path = path
        if recursive is not None:
            self.recursive = recursive
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListTreesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListTreesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListTreesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListTreesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def ref(self):
        r"""Gets the ref of this ListTreesRequest.

        **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The ref of this ListTreesRequest.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this ListTreesRequest.

        **参数解释：** 引用，可以是分支名称、标签名称或者commitid，如果不传则为默认分支。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param ref: The ref of this ListTreesRequest.
        :type ref: str
        """
        self._ref = ref

    @property
    def path(self):
        r"""Gets the path of this ListTreesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The path of this ListTreesRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListTreesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param path: The path of this ListTreesRequest.
        :type path: str
        """
        self._path = path

    @property
    def recursive(self):
        r"""Gets the recursive of this ListTreesRequest.

        **参数解释：** 是否递归查询

        :return: The recursive of this ListTreesRequest.
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        r"""Sets the recursive of this ListTreesRequest.

        **参数解释：** 是否递归查询

        :param recursive: The recursive of this ListTreesRequest.
        :type recursive: bool
        """
        self._recursive = recursive

    @property
    def offset(self):
        r"""Gets the offset of this ListTreesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListTreesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTreesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListTreesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTreesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListTreesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTreesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListTreesRequest.
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
        if not isinstance(other, ListTreesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
