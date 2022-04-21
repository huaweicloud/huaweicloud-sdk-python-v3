# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetentionLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'id': 'int',
        'namespace': 'str',
        'repo': 'str',
        'retention_id': 'int',
        'rule_type': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'namespace': 'namespace',
        'repo': 'repo',
        'retention_id': 'retention_id',
        'rule_type': 'rule_type',
        'tag': 'tag'
    }

    def __init__(self, created_at=None, id=None, namespace=None, repo=None, retention_id=None, rule_type=None, tag=None):
        """RetentionLog

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param id: ID
        :type id: int
        :param namespace: 组织名
        :type namespace: str
        :param repo: 镜像仓库名
        :type repo: str
        :param retention_id: 老化规则ID
        :type retention_id: int
        :param rule_type: 规则
        :type rule_type: str
        :param tag: 镜像版本
        :type tag: str
        """
        
        

        self._created_at = None
        self._id = None
        self._namespace = None
        self._repo = None
        self._retention_id = None
        self._rule_type = None
        self._tag = None
        self.discriminator = None

        self.created_at = created_at
        self.id = id
        self.namespace = namespace
        self.repo = repo
        self.retention_id = retention_id
        self.rule_type = rule_type
        self.tag = tag

    @property
    def created_at(self):
        """Gets the created_at of this RetentionLog.

        创建时间

        :return: The created_at of this RetentionLog.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RetentionLog.

        创建时间

        :param created_at: The created_at of this RetentionLog.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this RetentionLog.

        ID

        :return: The id of this RetentionLog.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RetentionLog.

        ID

        :param id: The id of this RetentionLog.
        :type id: int
        """
        self._id = id

    @property
    def namespace(self):
        """Gets the namespace of this RetentionLog.

        组织名

        :return: The namespace of this RetentionLog.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this RetentionLog.

        组织名

        :param namespace: The namespace of this RetentionLog.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repo(self):
        """Gets the repo of this RetentionLog.

        镜像仓库名

        :return: The repo of this RetentionLog.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this RetentionLog.

        镜像仓库名

        :param repo: The repo of this RetentionLog.
        :type repo: str
        """
        self._repo = repo

    @property
    def retention_id(self):
        """Gets the retention_id of this RetentionLog.

        老化规则ID

        :return: The retention_id of this RetentionLog.
        :rtype: int
        """
        return self._retention_id

    @retention_id.setter
    def retention_id(self, retention_id):
        """Sets the retention_id of this RetentionLog.

        老化规则ID

        :param retention_id: The retention_id of this RetentionLog.
        :type retention_id: int
        """
        self._retention_id = retention_id

    @property
    def rule_type(self):
        """Gets the rule_type of this RetentionLog.

        规则

        :return: The rule_type of this RetentionLog.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this RetentionLog.

        规则

        :param rule_type: The rule_type of this RetentionLog.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def tag(self):
        """Gets the tag of this RetentionLog.

        镜像版本

        :return: The tag of this RetentionLog.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this RetentionLog.

        镜像版本

        :param tag: The tag of this RetentionLog.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, RetentionLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
