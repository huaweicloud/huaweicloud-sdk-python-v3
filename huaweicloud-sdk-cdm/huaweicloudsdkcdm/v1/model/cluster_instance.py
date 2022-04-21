# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'shard_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'shard_id': 'shard_id'
    }

    def __init__(self, id=None, name=None, type=None, shard_id=None):
        """ClusterInstance

        The model defined in huaweicloud sdk

        :param id: 节点的虚拟机ID。
        :type id: str
        :param name: 节点的虚拟机名称。
        :type name: str
        :param type: 节点类型，只支持一种类型“cdm”。
        :type type: str
        :param shard_id: 分片ID
        :type shard_id: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._shard_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if shard_id is not None:
            self.shard_id = shard_id

    @property
    def id(self):
        """Gets the id of this ClusterInstance.

        节点的虚拟机ID。

        :return: The id of this ClusterInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterInstance.

        节点的虚拟机ID。

        :param id: The id of this ClusterInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterInstance.

        节点的虚拟机名称。

        :return: The name of this ClusterInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterInstance.

        节点的虚拟机名称。

        :param name: The name of this ClusterInstance.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ClusterInstance.

        节点类型，只支持一种类型“cdm”。

        :return: The type of this ClusterInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterInstance.

        节点类型，只支持一种类型“cdm”。

        :param type: The type of this ClusterInstance.
        :type type: str
        """
        self._type = type

    @property
    def shard_id(self):
        """Gets the shard_id of this ClusterInstance.

        分片ID

        :return: The shard_id of this ClusterInstance.
        :rtype: str
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        """Sets the shard_id of this ClusterInstance.

        分片ID

        :param shard_id: The shard_id of this ClusterInstance.
        :type shard_id: str
        """
        self._shard_id = shard_id

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
        if not isinstance(other, ClusterInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
