# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class StartFailoverResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'workflow_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'nodeId',
        'workflow_id': 'workflowId'
    }

    def __init__(self, instance_id=None, node_id=None, workflow_id=None):
        """StartFailoverResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._instance_id = None
        self._node_id = None
        self._workflow_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if workflow_id is not None:
            self.workflow_id = workflow_id

    @property
    def instance_id(self):
        """Gets the instance_id of this StartFailoverResponse.

        实例Id

        :return: The instance_id of this StartFailoverResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this StartFailoverResponse.

        实例Id

        :param instance_id: The instance_id of this StartFailoverResponse.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        """Gets the node_id of this StartFailoverResponse.

        节点Id

        :return: The node_id of this StartFailoverResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this StartFailoverResponse.

        节点Id

        :param node_id: The node_id of this StartFailoverResponse.
        :type: str
        """
        self._node_id = node_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this StartFailoverResponse.

        任务Id

        :return: The workflow_id of this StartFailoverResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this StartFailoverResponse.

        任务Id

        :param workflow_id: The workflow_id of this StartFailoverResponse.
        :type: str
        """
        self._workflow_id = workflow_id

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
        if not isinstance(other, StartFailoverResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
