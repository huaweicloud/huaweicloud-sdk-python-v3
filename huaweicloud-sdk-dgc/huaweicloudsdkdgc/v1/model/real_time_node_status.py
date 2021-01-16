# coding: utf-8

import pprint
import re

import six





class RealTimeNodeStatus:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'log_path': 'str',
        'node_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'log_path': 'logPath',
        'node_type': 'nodeType'
    }

    def __init__(self, name=None, status=None, log_path=None, node_type=None):
        """RealTimeNodeStatus - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._status = None
        self._log_path = None
        self._node_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if log_path is not None:
            self.log_path = log_path
        if node_type is not None:
            self.node_type = node_type

    @property
    def name(self):
        """Gets the name of this RealTimeNodeStatus.


        :return: The name of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RealTimeNodeStatus.


        :param name: The name of this RealTimeNodeStatus.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this RealTimeNodeStatus.


        :return: The status of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RealTimeNodeStatus.


        :param status: The status of this RealTimeNodeStatus.
        :type: str
        """
        self._status = status

    @property
    def log_path(self):
        """Gets the log_path of this RealTimeNodeStatus.


        :return: The log_path of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this RealTimeNodeStatus.


        :param log_path: The log_path of this RealTimeNodeStatus.
        :type: str
        """
        self._log_path = log_path

    @property
    def node_type(self):
        """Gets the node_type of this RealTimeNodeStatus.


        :return: The node_type of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this RealTimeNodeStatus.


        :param node_type: The node_type of this RealTimeNodeStatus.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RealTimeNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
