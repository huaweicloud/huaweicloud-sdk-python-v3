# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'name': 'str',
        'status': 'str',
        'node_type': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'status': 'status',
        'node_type': 'nodeType'
    }

    def __init__(self, uid=None, name=None, status=None, node_type=None):
        r"""NodeInfo

        The model defined in huaweicloud sdk

        :param uid: 节点UID
        :type uid: str
        :param name: 节点名称
        :type name: str
        :param status: 状态
        :type status: str
        :param node_type: 节点类型
        :type node_type: str
        """
        
        

        self._uid = None
        self._name = None
        self._status = None
        self._node_type = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if node_type is not None:
            self.node_type = node_type

    @property
    def uid(self):
        r"""Gets the uid of this NodeInfo.

        节点UID

        :return: The uid of this NodeInfo.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this NodeInfo.

        节点UID

        :param uid: The uid of this NodeInfo.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this NodeInfo.

        节点名称

        :return: The name of this NodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeInfo.

        节点名称

        :param name: The name of this NodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this NodeInfo.

        状态

        :return: The status of this NodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeInfo.

        状态

        :param status: The status of this NodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def node_type(self):
        r"""Gets the node_type of this NodeInfo.

        节点类型

        :return: The node_type of this NodeInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this NodeInfo.

        节点类型

        :param node_type: The node_type of this NodeInfo.
        :type node_type: str
        """
        self._node_type = node_type

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
        if not isinstance(other, NodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
