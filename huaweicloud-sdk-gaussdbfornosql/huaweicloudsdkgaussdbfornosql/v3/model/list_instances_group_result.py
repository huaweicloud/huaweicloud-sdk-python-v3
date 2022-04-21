# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'id': 'str',
        'status': 'str',
        'volume': 'Volume',
        'nodes': 'list[ListInstancesNodeResult]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'volume': 'volume',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, status=None, volume=None, nodes=None):
        """ListInstancesGroupResult

        The model defined in huaweicloud sdk

        :param id: 组ID。
        :type id: str
        :param status: 组状态。
        :type status: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbfornosql.v3.Volume`
        :param nodes: 节点信息。
        :type nodes: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesNodeResult`]
        """
        
        

        self._id = None
        self._status = None
        self._volume = None
        self._nodes = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.volume = volume
        self.nodes = nodes

    @property
    def id(self):
        """Gets the id of this ListInstancesGroupResult.

        组ID。

        :return: The id of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesGroupResult.

        组ID。

        :param id: The id of this ListInstancesGroupResult.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ListInstancesGroupResult.

        组状态。

        :return: The status of this ListInstancesGroupResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesGroupResult.

        组状态。

        :param status: The status of this ListInstancesGroupResult.
        :type status: str
        """
        self._status = status

    @property
    def volume(self):
        """Gets the volume of this ListInstancesGroupResult.


        :return: The volume of this ListInstancesGroupResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ListInstancesGroupResult.


        :param volume: The volume of this ListInstancesGroupResult.
        :type volume: :class:`huaweicloudsdkgaussdbfornosql.v3.Volume`
        """
        self._volume = volume

    @property
    def nodes(self):
        """Gets the nodes of this ListInstancesGroupResult.

        节点信息。

        :return: The nodes of this ListInstancesGroupResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesNodeResult`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ListInstancesGroupResult.

        节点信息。

        :param nodes: The nodes of this ListInstancesGroupResult.
        :type nodes: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesNodeResult`]
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
        if not isinstance(other, ListInstancesGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
