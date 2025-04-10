# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""RealTimeNodeStatus

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param status: 
        :type status: str
        :param log_path: 
        :type log_path: str
        :param node_type: 
        :type node_type: str
        """
        
        

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
        r"""Gets the name of this RealTimeNodeStatus.

        :return: The name of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RealTimeNodeStatus.

        :param name: The name of this RealTimeNodeStatus.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RealTimeNodeStatus.

        :return: The status of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RealTimeNodeStatus.

        :param status: The status of this RealTimeNodeStatus.
        :type status: str
        """
        self._status = status

    @property
    def log_path(self):
        r"""Gets the log_path of this RealTimeNodeStatus.

        :return: The log_path of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this RealTimeNodeStatus.

        :param log_path: The log_path of this RealTimeNodeStatus.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def node_type(self):
        r"""Gets the node_type of this RealTimeNodeStatus.

        :return: The node_type of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this RealTimeNodeStatus.

        :param node_type: The node_type of this RealTimeNodeStatus.
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
        if not isinstance(other, RealTimeNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
