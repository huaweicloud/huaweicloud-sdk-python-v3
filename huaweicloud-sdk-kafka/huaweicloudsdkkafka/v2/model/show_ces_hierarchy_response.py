# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCesHierarchyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[ShowCeshierarchyRespDimensions]',
        'instance_ids': 'list[ShowCeshierarchyRespInstanceIds]',
        'nodes': 'list[ShowCeshierarchyRespNodes]',
        'queues': 'list[ShowCeshierarchyRespQueues]',
        'groups': 'list[str]'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'instance_ids': 'instance_ids',
        'nodes': 'nodes',
        'queues': 'queues',
        'groups': 'groups'
    }

    def __init__(self, dimensions=None, instance_ids=None, nodes=None, queues=None, groups=None):
        """ShowCesHierarchyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._dimensions = None
        self._instance_ids = None
        self._nodes = None
        self._queues = None
        self._groups = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if nodes is not None:
            self.nodes = nodes
        if queues is not None:
            self.queues = queues
        if groups is not None:
            self.groups = groups

    @property
    def dimensions(self):
        """Gets the dimensions of this ShowCesHierarchyResponse.

        监控维度。

        :return: The dimensions of this ShowCesHierarchyResponse.
        :rtype: list[ShowCeshierarchyRespDimensions]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ShowCesHierarchyResponse.

        监控维度。

        :param dimensions: The dimensions of this ShowCesHierarchyResponse.
        :type: list[ShowCeshierarchyRespDimensions]
        """
        self._dimensions = dimensions

    @property
    def instance_ids(self):
        """Gets the instance_ids of this ShowCesHierarchyResponse.

        实例信息。

        :return: The instance_ids of this ShowCesHierarchyResponse.
        :rtype: list[ShowCeshierarchyRespInstanceIds]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this ShowCesHierarchyResponse.

        实例信息。

        :param instance_ids: The instance_ids of this ShowCesHierarchyResponse.
        :type: list[ShowCeshierarchyRespInstanceIds]
        """
        self._instance_ids = instance_ids

    @property
    def nodes(self):
        """Gets the nodes of this ShowCesHierarchyResponse.

        节点信息。

        :return: The nodes of this ShowCesHierarchyResponse.
        :rtype: list[ShowCeshierarchyRespNodes]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowCesHierarchyResponse.

        节点信息。

        :param nodes: The nodes of this ShowCesHierarchyResponse.
        :type: list[ShowCeshierarchyRespNodes]
        """
        self._nodes = nodes

    @property
    def queues(self):
        """Gets the queues of this ShowCesHierarchyResponse.

        队列信息。

        :return: The queues of this ShowCesHierarchyResponse.
        :rtype: list[ShowCeshierarchyRespQueues]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this ShowCesHierarchyResponse.

        队列信息。

        :param queues: The queues of this ShowCesHierarchyResponse.
        :type: list[ShowCeshierarchyRespQueues]
        """
        self._queues = queues

    @property
    def groups(self):
        """Gets the groups of this ShowCesHierarchyResponse.

        消费组信息。

        :return: The groups of this ShowCesHierarchyResponse.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ShowCesHierarchyResponse.

        消费组信息。

        :param groups: The groups of this ShowCesHierarchyResponse.
        :type: list[str]
        """
        self._groups = groups

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
        if not isinstance(other, ShowCesHierarchyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
