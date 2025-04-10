# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'inst_type': 'str',
        'ip': 'str',
        'public_ip': 'str',
        'start_time': 'str',
        'status': 'str',
        'volume_size': 'int'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'inst_type': 'inst_type',
        'ip': 'ip',
        'public_ip': 'public_ip',
        'start_time': 'start_time',
        'status': 'status',
        'volume_size': 'volume_size'
    }

    def __init__(self, engine_type=None, inst_type=None, ip=None, public_ip=None, start_time=None, status=None, volume_size=None):
        r"""InstInfo

        The model defined in huaweicloud sdk

        :param engine_type: 引擎类型
        :type engine_type: str
        :param inst_type: 实例类型
        :type inst_type: str
        :param ip: 迁移实例所在的私有IP
        :type ip: str
        :param public_ip: 迁移实例所在的公网IP
        :type public_ip: str
        :param start_time: 迁移实例任务定时启动时间
        :type start_time: str
        :param status: 迁移实例的状态
        :type status: str
        :param volume_size: 迁移实例的磁盘大小
        :type volume_size: int
        """
        
        

        self._engine_type = None
        self._inst_type = None
        self._ip = None
        self._public_ip = None
        self._start_time = None
        self._status = None
        self._volume_size = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if inst_type is not None:
            self.inst_type = inst_type
        if ip is not None:
            self.ip = ip
        if public_ip is not None:
            self.public_ip = public_ip
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if volume_size is not None:
            self.volume_size = volume_size

    @property
    def engine_type(self):
        r"""Gets the engine_type of this InstInfo.

        引擎类型

        :return: The engine_type of this InstInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this InstInfo.

        引擎类型

        :param engine_type: The engine_type of this InstInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def inst_type(self):
        r"""Gets the inst_type of this InstInfo.

        实例类型

        :return: The inst_type of this InstInfo.
        :rtype: str
        """
        return self._inst_type

    @inst_type.setter
    def inst_type(self, inst_type):
        r"""Sets the inst_type of this InstInfo.

        实例类型

        :param inst_type: The inst_type of this InstInfo.
        :type inst_type: str
        """
        self._inst_type = inst_type

    @property
    def ip(self):
        r"""Gets the ip of this InstInfo.

        迁移实例所在的私有IP

        :return: The ip of this InstInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this InstInfo.

        迁移实例所在的私有IP

        :param ip: The ip of this InstInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this InstInfo.

        迁移实例所在的公网IP

        :return: The public_ip of this InstInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this InstInfo.

        迁移实例所在的公网IP

        :param public_ip: The public_ip of this InstInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def start_time(self):
        r"""Gets the start_time of this InstInfo.

        迁移实例任务定时启动时间

        :return: The start_time of this InstInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this InstInfo.

        迁移实例任务定时启动时间

        :param start_time: The start_time of this InstInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this InstInfo.

        迁移实例的状态

        :return: The status of this InstInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstInfo.

        迁移实例的状态

        :param status: The status of this InstInfo.
        :type status: str
        """
        self._status = status

    @property
    def volume_size(self):
        r"""Gets the volume_size of this InstInfo.

        迁移实例的磁盘大小

        :return: The volume_size of this InstInfo.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this InstInfo.

        迁移实例的磁盘大小

        :param volume_size: The volume_size of this InstInfo.
        :type volume_size: int
        """
        self._volume_size = volume_size

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
        if not isinstance(other, InstInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
