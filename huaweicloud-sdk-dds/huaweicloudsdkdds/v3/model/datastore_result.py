# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatastoreResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'node_type': 'node_type',
        'version': 'version'
    }

    def __init__(self, node_type=None, version=None):
        r"""DatastoreResult

        The model defined in huaweicloud sdk

        :param node_type: node_type参数模板节点类型。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。
        :type node_type: str
        :param version: version数据库版本。
        :type version: str
        """
        
        

        self._node_type = None
        self._version = None
        self.discriminator = None

        self.node_type = node_type
        self.version = version

    @property
    def node_type(self):
        r"""Gets the node_type of this DatastoreResult.

        node_type参数模板节点类型。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。

        :return: The node_type of this DatastoreResult.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this DatastoreResult.

        node_type参数模板节点类型。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。

        :param node_type: The node_type of this DatastoreResult.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def version(self):
        r"""Gets the version of this DatastoreResult.

        version数据库版本。

        :return: The version of this DatastoreResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DatastoreResult.

        version数据库版本。

        :param version: The version of this DatastoreResult.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, DatastoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
