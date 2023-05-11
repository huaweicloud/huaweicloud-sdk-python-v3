# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRspProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_name': 'str',
        'process_path': 'str',
        'process_pid': 'str',
        'process_uid': 'str',
        'process_cmdline': 'str'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_pid': 'process_pid',
        'process_uid': 'process_uid',
        'process_cmdline': 'process_cmdline'
    }

    def __init__(self, process_name=None, process_path=None, process_pid=None, process_uid=None, process_cmdline=None):
        """ShowAlertRspProcess

        The model defined in huaweicloud sdk

        :param process_name: The name, display only
        :type process_name: str
        :param process_path: The name, display only
        :type process_path: str
        :param process_pid: Id value
        :type process_pid: str
        :param process_uid: Id value
        :type process_uid: str
        :param process_cmdline: The name, display only
        :type process_cmdline: str
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_pid = None
        self._process_uid = None
        self._process_cmdline = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_pid is not None:
            self.process_pid = process_pid
        if process_uid is not None:
            self.process_uid = process_uid
        if process_cmdline is not None:
            self.process_cmdline = process_cmdline

    @property
    def process_name(self):
        """Gets the process_name of this ShowAlertRspProcess.

        The name, display only

        :return: The process_name of this ShowAlertRspProcess.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """Sets the process_name of this ShowAlertRspProcess.

        The name, display only

        :param process_name: The process_name of this ShowAlertRspProcess.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        """Gets the process_path of this ShowAlertRspProcess.

        The name, display only

        :return: The process_path of this ShowAlertRspProcess.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        """Sets the process_path of this ShowAlertRspProcess.

        The name, display only

        :param process_path: The process_path of this ShowAlertRspProcess.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        """Gets the process_pid of this ShowAlertRspProcess.

        Id value

        :return: The process_pid of this ShowAlertRspProcess.
        :rtype: str
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        """Sets the process_pid of this ShowAlertRspProcess.

        Id value

        :param process_pid: The process_pid of this ShowAlertRspProcess.
        :type process_pid: str
        """
        self._process_pid = process_pid

    @property
    def process_uid(self):
        """Gets the process_uid of this ShowAlertRspProcess.

        Id value

        :return: The process_uid of this ShowAlertRspProcess.
        :rtype: str
        """
        return self._process_uid

    @process_uid.setter
    def process_uid(self, process_uid):
        """Sets the process_uid of this ShowAlertRspProcess.

        Id value

        :param process_uid: The process_uid of this ShowAlertRspProcess.
        :type process_uid: str
        """
        self._process_uid = process_uid

    @property
    def process_cmdline(self):
        """Gets the process_cmdline of this ShowAlertRspProcess.

        The name, display only

        :return: The process_cmdline of this ShowAlertRspProcess.
        :rtype: str
        """
        return self._process_cmdline

    @process_cmdline.setter
    def process_cmdline(self, process_cmdline):
        """Sets the process_cmdline of this ShowAlertRspProcess.

        The name, display only

        :param process_cmdline: The process_cmdline of this ShowAlertRspProcess.
        :type process_cmdline: str
        """
        self._process_cmdline = process_cmdline

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
        if not isinstance(other, ShowAlertRspProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
