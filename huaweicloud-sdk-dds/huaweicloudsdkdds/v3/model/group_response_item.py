# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupResponseItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'volume': 'Volume',
        'nodes': 'list[NodeItem]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'volume': 'volume',
        'nodes': 'nodes'
    }

    def __init__(self, type=None, id=None, name=None, status=None, volume=None, nodes=None):
        """GroupResponseItem

        The model defined in huaweicloud sdk

        :param type: 节点类型。 取值： - shard - config - mongos - replica - single
        :type type: str
        :param id: 组ID。节点类型为shard和config时，该参数有效。
        :type id: str
        :param name: 组名称。节点类型为shard和config时，该参数有效。
        :type name: str
        :param status: 组状态。节点类型为shard和config时，该参数有效。
        :type status: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkdds.v3.Volume`
        :param nodes: 节点信息。
        :type nodes: list[:class:`huaweicloudsdkdds.v3.NodeItem`]
        """
        
        

        self._type = None
        self._id = None
        self._name = None
        self._status = None
        self._volume = None
        self._nodes = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.name = name
        self.status = status
        self.volume = volume
        self.nodes = nodes

    @property
    def type(self):
        """Gets the type of this GroupResponseItem.

        节点类型。 取值： - shard - config - mongos - replica - single

        :return: The type of this GroupResponseItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupResponseItem.

        节点类型。 取值： - shard - config - mongos - replica - single

        :param type: The type of this GroupResponseItem.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this GroupResponseItem.

        组ID。节点类型为shard和config时，该参数有效。

        :return: The id of this GroupResponseItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupResponseItem.

        组ID。节点类型为shard和config时，该参数有效。

        :param id: The id of this GroupResponseItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupResponseItem.

        组名称。节点类型为shard和config时，该参数有效。

        :return: The name of this GroupResponseItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupResponseItem.

        组名称。节点类型为shard和config时，该参数有效。

        :param name: The name of this GroupResponseItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this GroupResponseItem.

        组状态。节点类型为shard和config时，该参数有效。

        :return: The status of this GroupResponseItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GroupResponseItem.

        组状态。节点类型为shard和config时，该参数有效。

        :param status: The status of this GroupResponseItem.
        :type status: str
        """
        self._status = status

    @property
    def volume(self):
        """Gets the volume of this GroupResponseItem.

        :return: The volume of this GroupResponseItem.
        :rtype: :class:`huaweicloudsdkdds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GroupResponseItem.

        :param volume: The volume of this GroupResponseItem.
        :type volume: :class:`huaweicloudsdkdds.v3.Volume`
        """
        self._volume = volume

    @property
    def nodes(self):
        """Gets the nodes of this GroupResponseItem.

        节点信息。

        :return: The nodes of this GroupResponseItem.
        :rtype: list[:class:`huaweicloudsdkdds.v3.NodeItem`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this GroupResponseItem.

        节点信息。

        :param nodes: The nodes of this GroupResponseItem.
        :type nodes: list[:class:`huaweicloudsdkdds.v3.NodeItem`]
        """
        self._nodes = nodes

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
        if not isinstance(other, GroupResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
