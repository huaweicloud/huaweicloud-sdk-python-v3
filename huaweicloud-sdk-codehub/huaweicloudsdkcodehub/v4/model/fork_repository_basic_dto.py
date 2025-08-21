# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForkRepositoryBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'path': 'str',
        'develop_mode': 'str',
        'visibility': 'str',
        'security': 'str',
        'star_count': 'int',
        'forks_count': 'int',
        'open_merge_requests_count': 'int',
        'starred': 'bool',
        'name_with_namespace': 'str',
        'last_activity_at': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'path': 'path',
        'develop_mode': 'develop_mode',
        'visibility': 'visibility',
        'security': 'security',
        'star_count': 'star_count',
        'forks_count': 'forks_count',
        'open_merge_requests_count': 'open_merge_requests_count',
        'starred': 'starred',
        'name_with_namespace': 'name_with_namespace',
        'last_activity_at': 'last_activity_at',
        'created_at': 'created_at'
    }

    def __init__(self, namespace=None, path=None, develop_mode=None, visibility=None, security=None, star_count=None, forks_count=None, open_merge_requests_count=None, starred=None, name_with_namespace=None, last_activity_at=None, created_at=None):
        r"""ForkRepositoryBasicDto

        The model defined in huaweicloud sdk

        :param namespace: **参数解释：** 命名空间。 **约束限制：** view&#x3D;basic时返回
        :type namespace: str
        :param path: **参数解释：** 仓库路径。 **约束限制：** view&#x3D;basic时返回
        :type path: str
        :param develop_mode: **参数解释：** 开发模式。 **约束限制：** view&#x3D;basic时返回
        :type develop_mode: str
        :param visibility: **参数解释：** 可见性。 **约束限制：** view&#x3D;basic时返回
        :type visibility: str
        :param security: **参数解释：** 安全级别。 **约束限制：**  view&#x3D;basic时返回
        :type security: str
        :param star_count: **参数解释：** 关注数。 **约束限制：** view&#x3D;basic时返回
        :type star_count: int
        :param forks_count: **参数解释：** Fork数。 **约束限制：** view&#x3D;basic时返回
        :type forks_count: int
        :param open_merge_requests_count: **参数解释：** 开启的合并请求数。 **约束限制：** view&#x3D;basic时返回
        :type open_merge_requests_count: int
        :param starred: **参数解释：** 是否已关注。 **约束限制：** view&#x3D;basic时返回
        :type starred: bool
        :param name_with_namespace: **参数解释：** 带命名空间的仓库名称。 **约束限制：** view&#x3D;basic时返回
        :type name_with_namespace: str
        :param last_activity_at: **参数解释：** 最后活动时间。 **约束限制：** view&#x3D;basic时返回
        :type last_activity_at: str
        :param created_at: **参数解释：** 创建时间。 **约束限制：** view&#x3D;basic时返回
        :type created_at: str
        """
        
        

        self._namespace = None
        self._path = None
        self._develop_mode = None
        self._visibility = None
        self._security = None
        self._star_count = None
        self._forks_count = None
        self._open_merge_requests_count = None
        self._starred = None
        self._name_with_namespace = None
        self._last_activity_at = None
        self._created_at = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if path is not None:
            self.path = path
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if visibility is not None:
            self.visibility = visibility
        if security is not None:
            self.security = security
        if star_count is not None:
            self.star_count = star_count
        if forks_count is not None:
            self.forks_count = forks_count
        if open_merge_requests_count is not None:
            self.open_merge_requests_count = open_merge_requests_count
        if starred is not None:
            self.starred = starred
        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if last_activity_at is not None:
            self.last_activity_at = last_activity_at
        if created_at is not None:
            self.created_at = created_at

    @property
    def namespace(self):
        r"""Gets the namespace of this ForkRepositoryBasicDto.

        **参数解释：** 命名空间。 **约束限制：** view=basic时返回

        :return: The namespace of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ForkRepositoryBasicDto.

        **参数解释：** 命名空间。 **约束限制：** view=basic时返回

        :param namespace: The namespace of this ForkRepositoryBasicDto.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def path(self):
        r"""Gets the path of this ForkRepositoryBasicDto.

        **参数解释：** 仓库路径。 **约束限制：** view=basic时返回

        :return: The path of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ForkRepositoryBasicDto.

        **参数解释：** 仓库路径。 **约束限制：** view=basic时返回

        :param path: The path of this ForkRepositoryBasicDto.
        :type path: str
        """
        self._path = path

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this ForkRepositoryBasicDto.

        **参数解释：** 开发模式。 **约束限制：** view=basic时返回

        :return: The develop_mode of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this ForkRepositoryBasicDto.

        **参数解释：** 开发模式。 **约束限制：** view=basic时返回

        :param develop_mode: The develop_mode of this ForkRepositoryBasicDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def visibility(self):
        r"""Gets the visibility of this ForkRepositoryBasicDto.

        **参数解释：** 可见性。 **约束限制：** view=basic时返回

        :return: The visibility of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ForkRepositoryBasicDto.

        **参数解释：** 可见性。 **约束限制：** view=basic时返回

        :param visibility: The visibility of this ForkRepositoryBasicDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def security(self):
        r"""Gets the security of this ForkRepositoryBasicDto.

        **参数解释：** 安全级别。 **约束限制：**  view=basic时返回

        :return: The security of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        r"""Sets the security of this ForkRepositoryBasicDto.

        **参数解释：** 安全级别。 **约束限制：**  view=basic时返回

        :param security: The security of this ForkRepositoryBasicDto.
        :type security: str
        """
        self._security = security

    @property
    def star_count(self):
        r"""Gets the star_count of this ForkRepositoryBasicDto.

        **参数解释：** 关注数。 **约束限制：** view=basic时返回

        :return: The star_count of this ForkRepositoryBasicDto.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        r"""Sets the star_count of this ForkRepositoryBasicDto.

        **参数解释：** 关注数。 **约束限制：** view=basic时返回

        :param star_count: The star_count of this ForkRepositoryBasicDto.
        :type star_count: int
        """
        self._star_count = star_count

    @property
    def forks_count(self):
        r"""Gets the forks_count of this ForkRepositoryBasicDto.

        **参数解释：** Fork数。 **约束限制：** view=basic时返回

        :return: The forks_count of this ForkRepositoryBasicDto.
        :rtype: int
        """
        return self._forks_count

    @forks_count.setter
    def forks_count(self, forks_count):
        r"""Sets the forks_count of this ForkRepositoryBasicDto.

        **参数解释：** Fork数。 **约束限制：** view=basic时返回

        :param forks_count: The forks_count of this ForkRepositoryBasicDto.
        :type forks_count: int
        """
        self._forks_count = forks_count

    @property
    def open_merge_requests_count(self):
        r"""Gets the open_merge_requests_count of this ForkRepositoryBasicDto.

        **参数解释：** 开启的合并请求数。 **约束限制：** view=basic时返回

        :return: The open_merge_requests_count of this ForkRepositoryBasicDto.
        :rtype: int
        """
        return self._open_merge_requests_count

    @open_merge_requests_count.setter
    def open_merge_requests_count(self, open_merge_requests_count):
        r"""Sets the open_merge_requests_count of this ForkRepositoryBasicDto.

        **参数解释：** 开启的合并请求数。 **约束限制：** view=basic时返回

        :param open_merge_requests_count: The open_merge_requests_count of this ForkRepositoryBasicDto.
        :type open_merge_requests_count: int
        """
        self._open_merge_requests_count = open_merge_requests_count

    @property
    def starred(self):
        r"""Gets the starred of this ForkRepositoryBasicDto.

        **参数解释：** 是否已关注。 **约束限制：** view=basic时返回

        :return: The starred of this ForkRepositoryBasicDto.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this ForkRepositoryBasicDto.

        **参数解释：** 是否已关注。 **约束限制：** view=basic时返回

        :param starred: The starred of this ForkRepositoryBasicDto.
        :type starred: bool
        """
        self._starred = starred

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this ForkRepositoryBasicDto.

        **参数解释：** 带命名空间的仓库名称。 **约束限制：** view=basic时返回

        :return: The name_with_namespace of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this ForkRepositoryBasicDto.

        **参数解释：** 带命名空间的仓库名称。 **约束限制：** view=basic时返回

        :param name_with_namespace: The name_with_namespace of this ForkRepositoryBasicDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def last_activity_at(self):
        r"""Gets the last_activity_at of this ForkRepositoryBasicDto.

        **参数解释：** 最后活动时间。 **约束限制：** view=basic时返回

        :return: The last_activity_at of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        r"""Sets the last_activity_at of this ForkRepositoryBasicDto.

        **参数解释：** 最后活动时间。 **约束限制：** view=basic时返回

        :param last_activity_at: The last_activity_at of this ForkRepositoryBasicDto.
        :type last_activity_at: str
        """
        self._last_activity_at = last_activity_at

    @property
    def created_at(self):
        r"""Gets the created_at of this ForkRepositoryBasicDto.

        **参数解释：** 创建时间。 **约束限制：** view=basic时返回

        :return: The created_at of this ForkRepositoryBasicDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ForkRepositoryBasicDto.

        **参数解释：** 创建时间。 **约束限制：** view=basic时返回

        :param created_at: The created_at of this ForkRepositoryBasicDto.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, ForkRepositoryBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
