# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component': 'str',
        'level': 'str',
        'rotate_num': 'int',
        'rotate_period': 'str',
        'size': 'int',
        'type': 'str',
        'log_group_id': 'str'
    }

    attribute_map = {
        'component': 'component',
        'level': 'level',
        'rotate_num': 'rotate_num',
        'rotate_period': 'rotate_period',
        'size': 'size',
        'type': 'type',
        'log_group_id': 'log_group_id'
    }

    def __init__(self, component=None, level=None, rotate_num=None, rotate_period=None, size=None, type=None, log_group_id=None):
        """LogConfig

        The model defined in huaweicloud sdk

        :param component: app：应用日志。 system：系统的日志
        :type component: str
        :param level: 系统级日志可配置为/error/warning/info/debug ; 不传会默认为info。
        :type level: str
        :param rotate_num: 日志rotate个数，默认5，hilens取值范围1-30，ief取值范围1-10
        :type rotate_num: int
        :param rotate_period: 日志rotate周期，可选项，只支持ief：daily monthly weekly yearly.
        :type rotate_period: str
        :param size: 应用日志文件大小限制，单位MB，默认50，取值范围10-1000。
        :type size: int
        :param type: - LTS 将日志发送到云日志服务（Log Tank Service，简称LTS） - local 本地日志
        :type type: str
        :param log_group_id: 
        :type log_group_id: str
        """
        
        

        self._component = None
        self._level = None
        self._rotate_num = None
        self._rotate_period = None
        self._size = None
        self._type = None
        self._log_group_id = None
        self.discriminator = None

        if component is not None:
            self.component = component
        if level is not None:
            self.level = level
        if rotate_num is not None:
            self.rotate_num = rotate_num
        if rotate_period is not None:
            self.rotate_period = rotate_period
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if log_group_id is not None:
            self.log_group_id = log_group_id

    @property
    def component(self):
        """Gets the component of this LogConfig.

        app：应用日志。 system：系统的日志

        :return: The component of this LogConfig.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this LogConfig.

        app：应用日志。 system：系统的日志

        :param component: The component of this LogConfig.
        :type component: str
        """
        self._component = component

    @property
    def level(self):
        """Gets the level of this LogConfig.

        系统级日志可配置为/error/warning/info/debug ; 不传会默认为info。

        :return: The level of this LogConfig.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LogConfig.

        系统级日志可配置为/error/warning/info/debug ; 不传会默认为info。

        :param level: The level of this LogConfig.
        :type level: str
        """
        self._level = level

    @property
    def rotate_num(self):
        """Gets the rotate_num of this LogConfig.

        日志rotate个数，默认5，hilens取值范围1-30，ief取值范围1-10

        :return: The rotate_num of this LogConfig.
        :rtype: int
        """
        return self._rotate_num

    @rotate_num.setter
    def rotate_num(self, rotate_num):
        """Sets the rotate_num of this LogConfig.

        日志rotate个数，默认5，hilens取值范围1-30，ief取值范围1-10

        :param rotate_num: The rotate_num of this LogConfig.
        :type rotate_num: int
        """
        self._rotate_num = rotate_num

    @property
    def rotate_period(self):
        """Gets the rotate_period of this LogConfig.

        日志rotate周期，可选项，只支持ief：daily monthly weekly yearly.

        :return: The rotate_period of this LogConfig.
        :rtype: str
        """
        return self._rotate_period

    @rotate_period.setter
    def rotate_period(self, rotate_period):
        """Sets the rotate_period of this LogConfig.

        日志rotate周期，可选项，只支持ief：daily monthly weekly yearly.

        :param rotate_period: The rotate_period of this LogConfig.
        :type rotate_period: str
        """
        self._rotate_period = rotate_period

    @property
    def size(self):
        """Gets the size of this LogConfig.

        应用日志文件大小限制，单位MB，默认50，取值范围10-1000。

        :return: The size of this LogConfig.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogConfig.

        应用日志文件大小限制，单位MB，默认50，取值范围10-1000。

        :param size: The size of this LogConfig.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this LogConfig.

        - LTS 将日志发送到云日志服务（Log Tank Service，简称LTS） - local 本地日志

        :return: The type of this LogConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogConfig.

        - LTS 将日志发送到云日志服务（Log Tank Service，简称LTS） - local 本地日志

        :param type: The type of this LogConfig.
        :type type: str
        """
        self._type = type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this LogConfig.

        :return: The log_group_id of this LogConfig.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this LogConfig.

        :param log_group_id: The log_group_id of this LogConfig.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

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
        if not isinstance(other, LogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
