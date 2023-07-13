# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Logtank:

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
        'project_id': 'str',
        'loadbalancer_id': 'str',
        'log_group_id': 'str',
        'log_topic_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'loadbalancer_id': 'loadbalancer_id',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id'
    }

    def __init__(self, id=None, project_id=None, loadbalancer_id=None, log_group_id=None, log_topic_id=None):
        """Logtank

        The model defined in huaweicloud sdk

        :param id: 云日志ID。
        :type id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param loadbalancer_id: 负载均衡器ID。
        :type loadbalancer_id: str
        :param log_group_id: 云日志分组ID。
        :type log_group_id: str
        :param log_topic_id: 云日志主题ID。
        :type log_topic_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._loadbalancer_id = None
        self._log_group_id = None
        self._log_topic_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.loadbalancer_id = loadbalancer_id
        self.log_group_id = log_group_id
        self.log_topic_id = log_topic_id

    @property
    def id(self):
        """Gets the id of this Logtank.

        云日志ID。

        :return: The id of this Logtank.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Logtank.

        云日志ID。

        :param id: The id of this Logtank.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Logtank.

        项目ID。

        :return: The project_id of this Logtank.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Logtank.

        项目ID。

        :param project_id: The project_id of this Logtank.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this Logtank.

        负载均衡器ID。

        :return: The loadbalancer_id of this Logtank.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this Logtank.

        负载均衡器ID。

        :param loadbalancer_id: The loadbalancer_id of this Logtank.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this Logtank.

        云日志分组ID。

        :return: The log_group_id of this Logtank.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this Logtank.

        云日志分组ID。

        :param log_group_id: The log_group_id of this Logtank.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this Logtank.

        云日志主题ID。

        :return: The log_topic_id of this Logtank.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this Logtank.

        云日志主题ID。

        :param log_topic_id: The log_topic_id of this Logtank.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

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
        if not isinstance(other, Logtank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
