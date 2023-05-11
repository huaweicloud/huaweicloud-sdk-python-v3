# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookInstanceRunStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'playbook_instance_id': 'str',
        'playbook_instance_name': 'str',
        'playbook_instance_run_time': 'float'
    }

    attribute_map = {
        'playbook_instance_id': 'playbook_instance_id',
        'playbook_instance_name': 'playbook_instance_name',
        'playbook_instance_run_time': 'playbook_instance_run_time'
    }

    def __init__(self, playbook_instance_id=None, playbook_instance_name=None, playbook_instance_run_time=None):
        """PlaybookInstanceRunStatistics

        The model defined in huaweicloud sdk

        :param playbook_instance_id: 剧本实例ID
        :type playbook_instance_id: str
        :param playbook_instance_name: 剧本实例名称
        :type playbook_instance_name: str
        :param playbook_instance_run_time: 剧本实例运行时间
        :type playbook_instance_run_time: float
        """
        
        

        self._playbook_instance_id = None
        self._playbook_instance_name = None
        self._playbook_instance_run_time = None
        self.discriminator = None

        if playbook_instance_id is not None:
            self.playbook_instance_id = playbook_instance_id
        if playbook_instance_name is not None:
            self.playbook_instance_name = playbook_instance_name
        if playbook_instance_run_time is not None:
            self.playbook_instance_run_time = playbook_instance_run_time

    @property
    def playbook_instance_id(self):
        """Gets the playbook_instance_id of this PlaybookInstanceRunStatistics.

        剧本实例ID

        :return: The playbook_instance_id of this PlaybookInstanceRunStatistics.
        :rtype: str
        """
        return self._playbook_instance_id

    @playbook_instance_id.setter
    def playbook_instance_id(self, playbook_instance_id):
        """Sets the playbook_instance_id of this PlaybookInstanceRunStatistics.

        剧本实例ID

        :param playbook_instance_id: The playbook_instance_id of this PlaybookInstanceRunStatistics.
        :type playbook_instance_id: str
        """
        self._playbook_instance_id = playbook_instance_id

    @property
    def playbook_instance_name(self):
        """Gets the playbook_instance_name of this PlaybookInstanceRunStatistics.

        剧本实例名称

        :return: The playbook_instance_name of this PlaybookInstanceRunStatistics.
        :rtype: str
        """
        return self._playbook_instance_name

    @playbook_instance_name.setter
    def playbook_instance_name(self, playbook_instance_name):
        """Sets the playbook_instance_name of this PlaybookInstanceRunStatistics.

        剧本实例名称

        :param playbook_instance_name: The playbook_instance_name of this PlaybookInstanceRunStatistics.
        :type playbook_instance_name: str
        """
        self._playbook_instance_name = playbook_instance_name

    @property
    def playbook_instance_run_time(self):
        """Gets the playbook_instance_run_time of this PlaybookInstanceRunStatistics.

        剧本实例运行时间

        :return: The playbook_instance_run_time of this PlaybookInstanceRunStatistics.
        :rtype: float
        """
        return self._playbook_instance_run_time

    @playbook_instance_run_time.setter
    def playbook_instance_run_time(self, playbook_instance_run_time):
        """Sets the playbook_instance_run_time of this PlaybookInstanceRunStatistics.

        剧本实例运行时间

        :param playbook_instance_run_time: The playbook_instance_run_time of this PlaybookInstanceRunStatistics.
        :type playbook_instance_run_time: float
        """
        self._playbook_instance_run_time = playbook_instance_run_time

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
        if not isinstance(other, PlaybookInstanceRunStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
