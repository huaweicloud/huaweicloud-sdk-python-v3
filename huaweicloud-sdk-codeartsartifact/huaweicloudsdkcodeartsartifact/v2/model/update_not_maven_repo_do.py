# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotMavenRepoDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_name': 'str',
        'format': 'str',
        'description': 'str',
        'repository_ids': 'list[str]',
        'includes_pattern': 'str',
        'deployment_policy': 'str',
        'auto_clean_snapshot': 'bool',
        'snapshot_alive_days': 'str',
        'max_unique_snapshots': 'str',
        'allow_anonymous': 'bool'
    }

    attribute_map = {
        'repo_name': 'repo_name',
        'format': 'format',
        'description': 'description',
        'repository_ids': 'repository_ids',
        'includes_pattern': 'includes_pattern',
        'deployment_policy': 'deployment_policy',
        'auto_clean_snapshot': 'auto_clean_snapshot',
        'snapshot_alive_days': 'snapshot_alive_days',
        'max_unique_snapshots': 'max_unique_snapshots',
        'allow_anonymous': 'allow_anonymous'
    }

    def __init__(self, repo_name=None, format=None, description=None, repository_ids=None, includes_pattern=None, deployment_policy=None, auto_clean_snapshot=None, snapshot_alive_days=None, max_unique_snapshots=None, allow_anonymous=None):
        r"""UpdateNotMavenRepoDO

        The model defined in huaweicloud sdk

        :param repo_name: 仓库名称
        :type repo_name: str
        :param format: 仓库格式
        :type format: str
        :param description: 仓库描述
        :type description: str
        :param repository_ids: 仓库id列表
        :type repository_ids: list[str]
        :param includes_pattern: 路径白名单
        :type includes_pattern: str
        :param deployment_policy: 仓库属性-覆盖策略
        :type deployment_policy: str
        :param auto_clean_snapshot: 自动清理快照
        :type auto_clean_snapshot: bool
        :param snapshot_alive_days: 快照保存时间长度
        :type snapshot_alive_days: str
        :param max_unique_snapshots: 最大不同快照个数
        :type max_unique_snapshots: str
        :param allow_anonymous: 是否允许匿名
        :type allow_anonymous: bool
        """
        
        

        self._repo_name = None
        self._format = None
        self._description = None
        self._repository_ids = None
        self._includes_pattern = None
        self._deployment_policy = None
        self._auto_clean_snapshot = None
        self._snapshot_alive_days = None
        self._max_unique_snapshots = None
        self._allow_anonymous = None
        self.discriminator = None

        self.repo_name = repo_name
        self.format = format
        if description is not None:
            self.description = description
        self.repository_ids = repository_ids
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if deployment_policy is not None:
            self.deployment_policy = deployment_policy
        if auto_clean_snapshot is not None:
            self.auto_clean_snapshot = auto_clean_snapshot
        if snapshot_alive_days is not None:
            self.snapshot_alive_days = snapshot_alive_days
        if max_unique_snapshots is not None:
            self.max_unique_snapshots = max_unique_snapshots
        if allow_anonymous is not None:
            self.allow_anonymous = allow_anonymous

    @property
    def repo_name(self):
        r"""Gets the repo_name of this UpdateNotMavenRepoDO.

        仓库名称

        :return: The repo_name of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this UpdateNotMavenRepoDO.

        仓库名称

        :param repo_name: The repo_name of this UpdateNotMavenRepoDO.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def format(self):
        r"""Gets the format of this UpdateNotMavenRepoDO.

        仓库格式

        :return: The format of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this UpdateNotMavenRepoDO.

        仓库格式

        :param format: The format of this UpdateNotMavenRepoDO.
        :type format: str
        """
        self._format = format

    @property
    def description(self):
        r"""Gets the description of this UpdateNotMavenRepoDO.

        仓库描述

        :return: The description of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateNotMavenRepoDO.

        仓库描述

        :param description: The description of this UpdateNotMavenRepoDO.
        :type description: str
        """
        self._description = description

    @property
    def repository_ids(self):
        r"""Gets the repository_ids of this UpdateNotMavenRepoDO.

        仓库id列表

        :return: The repository_ids of this UpdateNotMavenRepoDO.
        :rtype: list[str]
        """
        return self._repository_ids

    @repository_ids.setter
    def repository_ids(self, repository_ids):
        r"""Sets the repository_ids of this UpdateNotMavenRepoDO.

        仓库id列表

        :param repository_ids: The repository_ids of this UpdateNotMavenRepoDO.
        :type repository_ids: list[str]
        """
        self._repository_ids = repository_ids

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this UpdateNotMavenRepoDO.

        路径白名单

        :return: The includes_pattern of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this UpdateNotMavenRepoDO.

        路径白名单

        :param includes_pattern: The includes_pattern of this UpdateNotMavenRepoDO.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def deployment_policy(self):
        r"""Gets the deployment_policy of this UpdateNotMavenRepoDO.

        仓库属性-覆盖策略

        :return: The deployment_policy of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._deployment_policy

    @deployment_policy.setter
    def deployment_policy(self, deployment_policy):
        r"""Sets the deployment_policy of this UpdateNotMavenRepoDO.

        仓库属性-覆盖策略

        :param deployment_policy: The deployment_policy of this UpdateNotMavenRepoDO.
        :type deployment_policy: str
        """
        self._deployment_policy = deployment_policy

    @property
    def auto_clean_snapshot(self):
        r"""Gets the auto_clean_snapshot of this UpdateNotMavenRepoDO.

        自动清理快照

        :return: The auto_clean_snapshot of this UpdateNotMavenRepoDO.
        :rtype: bool
        """
        return self._auto_clean_snapshot

    @auto_clean_snapshot.setter
    def auto_clean_snapshot(self, auto_clean_snapshot):
        r"""Sets the auto_clean_snapshot of this UpdateNotMavenRepoDO.

        自动清理快照

        :param auto_clean_snapshot: The auto_clean_snapshot of this UpdateNotMavenRepoDO.
        :type auto_clean_snapshot: bool
        """
        self._auto_clean_snapshot = auto_clean_snapshot

    @property
    def snapshot_alive_days(self):
        r"""Gets the snapshot_alive_days of this UpdateNotMavenRepoDO.

        快照保存时间长度

        :return: The snapshot_alive_days of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._snapshot_alive_days

    @snapshot_alive_days.setter
    def snapshot_alive_days(self, snapshot_alive_days):
        r"""Sets the snapshot_alive_days of this UpdateNotMavenRepoDO.

        快照保存时间长度

        :param snapshot_alive_days: The snapshot_alive_days of this UpdateNotMavenRepoDO.
        :type snapshot_alive_days: str
        """
        self._snapshot_alive_days = snapshot_alive_days

    @property
    def max_unique_snapshots(self):
        r"""Gets the max_unique_snapshots of this UpdateNotMavenRepoDO.

        最大不同快照个数

        :return: The max_unique_snapshots of this UpdateNotMavenRepoDO.
        :rtype: str
        """
        return self._max_unique_snapshots

    @max_unique_snapshots.setter
    def max_unique_snapshots(self, max_unique_snapshots):
        r"""Sets the max_unique_snapshots of this UpdateNotMavenRepoDO.

        最大不同快照个数

        :param max_unique_snapshots: The max_unique_snapshots of this UpdateNotMavenRepoDO.
        :type max_unique_snapshots: str
        """
        self._max_unique_snapshots = max_unique_snapshots

    @property
    def allow_anonymous(self):
        r"""Gets the allow_anonymous of this UpdateNotMavenRepoDO.

        是否允许匿名

        :return: The allow_anonymous of this UpdateNotMavenRepoDO.
        :rtype: bool
        """
        return self._allow_anonymous

    @allow_anonymous.setter
    def allow_anonymous(self, allow_anonymous):
        r"""Sets the allow_anonymous of this UpdateNotMavenRepoDO.

        是否允许匿名

        :param allow_anonymous: The allow_anonymous of this UpdateNotMavenRepoDO.
        :type allow_anonymous: bool
        """
        self._allow_anonymous = allow_anonymous

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
        if not isinstance(other, UpdateNotMavenRepoDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
