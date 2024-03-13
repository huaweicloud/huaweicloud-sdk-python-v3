# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDERepositoryPair:

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
        'includes_pattern': 'str',
        'project_id': 'str',
        'description': 'str',
        'snapshot': 'str',
        'release': 'str'
    }

    attribute_map = {
        'repo_name': 'repo_name',
        'includes_pattern': 'includes_pattern',
        'project_id': 'project_id',
        'description': 'description',
        'snapshot': 'snapshot',
        'release': 'release'
    }

    def __init__(self, repo_name=None, includes_pattern=None, project_id=None, description=None, snapshot=None, release=None):
        """IDERepositoryPair

        The model defined in huaweicloud sdk

        :param repo_name: 仓库名称
        :type repo_name: str
        :param includes_pattern: 路径
        :type includes_pattern: str
        :param project_id: 项目id
        :type project_id: str
        :param description: 描述
        :type description: str
        :param snapshot: snapshot仓库名称
        :type snapshot: str
        :param release: release仓库名称
        :type release: str
        """
        
        

        self._repo_name = None
        self._includes_pattern = None
        self._project_id = None
        self._description = None
        self._snapshot = None
        self._release = None
        self.discriminator = None

        if repo_name is not None:
            self.repo_name = repo_name
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if snapshot is not None:
            self.snapshot = snapshot
        if release is not None:
            self.release = release

    @property
    def repo_name(self):
        """Gets the repo_name of this IDERepositoryPair.

        仓库名称

        :return: The repo_name of this IDERepositoryPair.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this IDERepositoryPair.

        仓库名称

        :param repo_name: The repo_name of this IDERepositoryPair.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def includes_pattern(self):
        """Gets the includes_pattern of this IDERepositoryPair.

        路径

        :return: The includes_pattern of this IDERepositoryPair.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        """Sets the includes_pattern of this IDERepositoryPair.

        路径

        :param includes_pattern: The includes_pattern of this IDERepositoryPair.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def project_id(self):
        """Gets the project_id of this IDERepositoryPair.

        项目id

        :return: The project_id of this IDERepositoryPair.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IDERepositoryPair.

        项目id

        :param project_id: The project_id of this IDERepositoryPair.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this IDERepositoryPair.

        描述

        :return: The description of this IDERepositoryPair.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IDERepositoryPair.

        描述

        :param description: The description of this IDERepositoryPair.
        :type description: str
        """
        self._description = description

    @property
    def snapshot(self):
        """Gets the snapshot of this IDERepositoryPair.

        snapshot仓库名称

        :return: The snapshot of this IDERepositoryPair.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this IDERepositoryPair.

        snapshot仓库名称

        :param snapshot: The snapshot of this IDERepositoryPair.
        :type snapshot: str
        """
        self._snapshot = snapshot

    @property
    def release(self):
        """Gets the release of this IDERepositoryPair.

        release仓库名称

        :return: The release of this IDERepositoryPair.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this IDERepositoryPair.

        release仓库名称

        :param release: The release of this IDERepositoryPair.
        :type release: str
        """
        self._release = release

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
        if not isinstance(other, IDERepositoryPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
