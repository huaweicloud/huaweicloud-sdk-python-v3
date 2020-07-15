# coding: utf-8

import pprint
import re

import six





class ListInstancesGroupResult:


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
        'volume': 'ListInstancesVolumeResult',
        'nodes': 'list[ListInstancesNodeResult]'
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
        """ListInstancesGroupResult - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the type of this ListInstancesGroupResult.

        节点类型。 取值： - shard - config - mongos - replica - single

        :return: The type of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstancesGroupResult.

        节点类型。 取值： - shard - config - mongos - replica - single

        :param type: The type of this ListInstancesGroupResult.
        :type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this ListInstancesGroupResult.

        组ID。节点类型为shard和config时，该参数有效。

        :return: The id of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesGroupResult.

        组ID。节点类型为shard和config时，该参数有效。

        :param id: The id of this ListInstancesGroupResult.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInstancesGroupResult.

        组名组名称。节点类型为shard和config时，该参数有效。

        :return: The name of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesGroupResult.

        组名组名称。节点类型为shard和config时，该参数有效。

        :param name: The name of this ListInstancesGroupResult.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListInstancesGroupResult.

        组状态。节点类型为shard和config时，该参数有效。

        :return: The status of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesGroupResult.

        组状态。节点类型为shard和config时，该参数有效。

        :param status: The status of this ListInstancesGroupResult.
        :type: str
        """
        self._status = status

    @property
    def volume(self):
        """Gets the volume of this ListInstancesGroupResult.


        :return: The volume of this ListInstancesGroupResult.
        :rtype: ListInstancesVolumeResult
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ListInstancesGroupResult.


        :param volume: The volume of this ListInstancesGroupResult.
        :type: ListInstancesVolumeResult
        """
        self._volume = volume

    @property
    def nodes(self):
        """Gets the nodes of this ListInstancesGroupResult.

        节点信息。

        :return: The nodes of this ListInstancesGroupResult.
        :rtype: list[ListInstancesNodeResult]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ListInstancesGroupResult.

        节点信息。

        :param nodes: The nodes of this ListInstancesGroupResult.
        :type: list[ListInstancesNodeResult]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstancesGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
