# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'int',
        'log_group_name': 'str',
        'log_group_id': 'str',
        'ttl_in_days': 'int',
        'tag': 'dict(str, str)'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_group_name': 'log_group_name',
        'log_group_id': 'log_group_id',
        'ttl_in_days': 'ttl_in_days',
        'tag': 'tag'
    }

    def __init__(self, creation_time=None, log_group_name=None, log_group_id=None, ttl_in_days=None, tag=None):
        """LogGroup

        The model defined in huaweicloud sdk

        :param creation_time: 创建时间 
        :type creation_time: int
        :param log_group_name: 日志组名称 
        :type log_group_name: str
        :param log_group_id: 日志组ID 
        :type log_group_id: str
        :param ttl_in_days: 日志存储时间 天 
        :type ttl_in_days: int
        :param tag: 日志流所属标签
        :type tag: dict(str, str)
        """
        
        

        self._creation_time = None
        self._log_group_name = None
        self._log_group_id = None
        self._ttl_in_days = None
        self._tag = None
        self.discriminator = None

        self.creation_time = creation_time
        self.log_group_name = log_group_name
        self.log_group_id = log_group_id
        self.ttl_in_days = ttl_in_days
        if tag is not None:
            self.tag = tag

    @property
    def creation_time(self):
        """Gets the creation_time of this LogGroup.

        创建时间 

        :return: The creation_time of this LogGroup.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this LogGroup.

        创建时间 

        :param creation_time: The creation_time of this LogGroup.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_group_name(self):
        """Gets the log_group_name of this LogGroup.

        日志组名称 

        :return: The log_group_name of this LogGroup.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this LogGroup.

        日志组名称 

        :param log_group_name: The log_group_name of this LogGroup.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_group_id(self):
        """Gets the log_group_id of this LogGroup.

        日志组ID 

        :return: The log_group_id of this LogGroup.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this LogGroup.

        日志组ID 

        :param log_group_id: The log_group_id of this LogGroup.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def ttl_in_days(self):
        """Gets the ttl_in_days of this LogGroup.

        日志存储时间 天 

        :return: The ttl_in_days of this LogGroup.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """Sets the ttl_in_days of this LogGroup.

        日志存储时间 天 

        :param ttl_in_days: The ttl_in_days of this LogGroup.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def tag(self):
        """Gets the tag of this LogGroup.

        日志流所属标签

        :return: The tag of this LogGroup.
        :rtype: dict(str, str)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this LogGroup.

        日志流所属标签

        :param tag: The tag of this LogGroup.
        :type tag: dict(str, str)
        """
        self._tag = tag

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
        if not isinstance(other, LogGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
