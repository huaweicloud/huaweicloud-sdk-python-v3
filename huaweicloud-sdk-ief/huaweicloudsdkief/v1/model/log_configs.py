# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfigs:

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
        'size': 'int',
        'level': 'str',
        'rotate_num': 'int',
        'rotate_period': 'str',
        'type': 'str',
        'component': 'str'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'level': 'level',
        'rotate_num': 'rotate_num',
        'rotate_period': 'rotate_period',
        'type': 'type',
        'component': 'component'
    }

    def __init__(self, id=None, size=None, level=None, rotate_num=None, rotate_period=None, type=None, component=None):
        """LogConfigs

        The model defined in huaweicloud sdk

        :param id: 数据库保存的主键，不需要关注此字段。
        :type id: str
        :param size: 应用日志文件大小限制，单位MB，默认50，取值范围10-1000。
        :type size: int
        :param level: - 当type为LTS时，应用级日志可配置为On或Off；系统级日志可配置为Off/Error/Warning/Info/Debug； - 当type为local时，无需配置level。
        :type level: str
        :param rotate_num: 应用日志rotate个数，默认5，取值范围1-10。
        :type rotate_num: int
        :param rotate_period: 应用日志rotate周期，可选项： - daily - monthly - weekly - yearly
        :type rotate_period: str
        :param type: - LTS：将日志发送到AOM - local：本地日志
        :type type: str
        :param component: - app：部署到边缘节点上的应用的日志 - system：边缘节点上系统的日志
        :type component: str
        """
        
        

        self._id = None
        self._size = None
        self._level = None
        self._rotate_num = None
        self._rotate_period = None
        self._type = None
        self._component = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if level is not None:
            self.level = level
        if rotate_num is not None:
            self.rotate_num = rotate_num
        if rotate_period is not None:
            self.rotate_period = rotate_period
        self.type = type
        self.component = component

    @property
    def id(self):
        """Gets the id of this LogConfigs.

        数据库保存的主键，不需要关注此字段。

        :return: The id of this LogConfigs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogConfigs.

        数据库保存的主键，不需要关注此字段。

        :param id: The id of this LogConfigs.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this LogConfigs.

        应用日志文件大小限制，单位MB，默认50，取值范围10-1000。

        :return: The size of this LogConfigs.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogConfigs.

        应用日志文件大小限制，单位MB，默认50，取值范围10-1000。

        :param size: The size of this LogConfigs.
        :type size: int
        """
        self._size = size

    @property
    def level(self):
        """Gets the level of this LogConfigs.

        - 当type为LTS时，应用级日志可配置为On或Off；系统级日志可配置为Off/Error/Warning/Info/Debug； - 当type为local时，无需配置level。

        :return: The level of this LogConfigs.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LogConfigs.

        - 当type为LTS时，应用级日志可配置为On或Off；系统级日志可配置为Off/Error/Warning/Info/Debug； - 当type为local时，无需配置level。

        :param level: The level of this LogConfigs.
        :type level: str
        """
        self._level = level

    @property
    def rotate_num(self):
        """Gets the rotate_num of this LogConfigs.

        应用日志rotate个数，默认5，取值范围1-10。

        :return: The rotate_num of this LogConfigs.
        :rtype: int
        """
        return self._rotate_num

    @rotate_num.setter
    def rotate_num(self, rotate_num):
        """Sets the rotate_num of this LogConfigs.

        应用日志rotate个数，默认5，取值范围1-10。

        :param rotate_num: The rotate_num of this LogConfigs.
        :type rotate_num: int
        """
        self._rotate_num = rotate_num

    @property
    def rotate_period(self):
        """Gets the rotate_period of this LogConfigs.

        应用日志rotate周期，可选项： - daily - monthly - weekly - yearly

        :return: The rotate_period of this LogConfigs.
        :rtype: str
        """
        return self._rotate_period

    @rotate_period.setter
    def rotate_period(self, rotate_period):
        """Sets the rotate_period of this LogConfigs.

        应用日志rotate周期，可选项： - daily - monthly - weekly - yearly

        :param rotate_period: The rotate_period of this LogConfigs.
        :type rotate_period: str
        """
        self._rotate_period = rotate_period

    @property
    def type(self):
        """Gets the type of this LogConfigs.

        - LTS：将日志发送到AOM - local：本地日志

        :return: The type of this LogConfigs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogConfigs.

        - LTS：将日志发送到AOM - local：本地日志

        :param type: The type of this LogConfigs.
        :type type: str
        """
        self._type = type

    @property
    def component(self):
        """Gets the component of this LogConfigs.

        - app：部署到边缘节点上的应用的日志 - system：边缘节点上系统的日志

        :return: The component of this LogConfigs.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this LogConfigs.

        - app：部署到边缘节点上的应用的日志 - system：边缘节点上系统的日志

        :param component: The component of this LogConfigs.
        :type component: str
        """
        self._component = component

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
        if not isinstance(other, LogConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
