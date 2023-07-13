# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmConfigResponse:

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
        'alarm_id': 'str',
        'alarm_name': 'str',
        'name_space': 'str',
        'alarm_level': 'str',
        'is_user_visible': 'str',
        'is_converge': 'str',
        'converge_time': 'int',
        'is_maintain_visible': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'name_space': 'name_space',
        'alarm_level': 'alarm_level',
        'is_user_visible': 'is_user_visible',
        'is_converge': 'is_converge',
        'converge_time': 'converge_time',
        'is_maintain_visible': 'is_maintain_visible'
    }

    def __init__(self, id=None, alarm_id=None, alarm_name=None, name_space=None, alarm_level=None, is_user_visible=None, is_converge=None, converge_time=None, is_maintain_visible=None):
        """AlarmConfigResponse

        The model defined in huaweicloud sdk

        :param id: 告警配置ID
        :type id: str
        :param alarm_id: 告警ID
        :type alarm_id: str
        :param alarm_name: 告警名称
        :type alarm_name: str
        :param name_space: 所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS
        :type name_space: str
        :param alarm_level: 告警级别
        :type alarm_level: str
        :param is_user_visible: 用户是否可见
        :type is_user_visible: str
        :param is_converge: 是否覆盖
        :type is_converge: str
        :param converge_time: 覆盖时间
        :type converge_time: int
        :param is_maintain_visible: 运维是否可见
        :type is_maintain_visible: str
        """
        
        

        self._id = None
        self._alarm_id = None
        self._alarm_name = None
        self._name_space = None
        self._alarm_level = None
        self._is_user_visible = None
        self._is_converge = None
        self._converge_time = None
        self._is_maintain_visible = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if name_space is not None:
            self.name_space = name_space
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if is_user_visible is not None:
            self.is_user_visible = is_user_visible
        if is_converge is not None:
            self.is_converge = is_converge
        if converge_time is not None:
            self.converge_time = converge_time
        if is_maintain_visible is not None:
            self.is_maintain_visible = is_maintain_visible

    @property
    def id(self):
        """Gets the id of this AlarmConfigResponse.

        告警配置ID

        :return: The id of this AlarmConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmConfigResponse.

        告警配置ID

        :param id: The id of this AlarmConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmConfigResponse.

        告警ID

        :return: The alarm_id of this AlarmConfigResponse.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmConfigResponse.

        告警ID

        :param alarm_id: The alarm_id of this AlarmConfigResponse.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this AlarmConfigResponse.

        告警名称

        :return: The alarm_name of this AlarmConfigResponse.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this AlarmConfigResponse.

        告警名称

        :param alarm_name: The alarm_name of this AlarmConfigResponse.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def name_space(self):
        """Gets the name_space of this AlarmConfigResponse.

        所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS

        :return: The name_space of this AlarmConfigResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this AlarmConfigResponse.

        所属服务，支持DWS,DLI,DGC,CloudTable,CDM,GES,CSS

        :param name_space: The name_space of this AlarmConfigResponse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmConfigResponse.

        告警级别

        :return: The alarm_level of this AlarmConfigResponse.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmConfigResponse.

        告警级别

        :param alarm_level: The alarm_level of this AlarmConfigResponse.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def is_user_visible(self):
        """Gets the is_user_visible of this AlarmConfigResponse.

        用户是否可见

        :return: The is_user_visible of this AlarmConfigResponse.
        :rtype: str
        """
        return self._is_user_visible

    @is_user_visible.setter
    def is_user_visible(self, is_user_visible):
        """Sets the is_user_visible of this AlarmConfigResponse.

        用户是否可见

        :param is_user_visible: The is_user_visible of this AlarmConfigResponse.
        :type is_user_visible: str
        """
        self._is_user_visible = is_user_visible

    @property
    def is_converge(self):
        """Gets the is_converge of this AlarmConfigResponse.

        是否覆盖

        :return: The is_converge of this AlarmConfigResponse.
        :rtype: str
        """
        return self._is_converge

    @is_converge.setter
    def is_converge(self, is_converge):
        """Sets the is_converge of this AlarmConfigResponse.

        是否覆盖

        :param is_converge: The is_converge of this AlarmConfigResponse.
        :type is_converge: str
        """
        self._is_converge = is_converge

    @property
    def converge_time(self):
        """Gets the converge_time of this AlarmConfigResponse.

        覆盖时间

        :return: The converge_time of this AlarmConfigResponse.
        :rtype: int
        """
        return self._converge_time

    @converge_time.setter
    def converge_time(self, converge_time):
        """Sets the converge_time of this AlarmConfigResponse.

        覆盖时间

        :param converge_time: The converge_time of this AlarmConfigResponse.
        :type converge_time: int
        """
        self._converge_time = converge_time

    @property
    def is_maintain_visible(self):
        """Gets the is_maintain_visible of this AlarmConfigResponse.

        运维是否可见

        :return: The is_maintain_visible of this AlarmConfigResponse.
        :rtype: str
        """
        return self._is_maintain_visible

    @is_maintain_visible.setter
    def is_maintain_visible(self, is_maintain_visible):
        """Sets the is_maintain_visible of this AlarmConfigResponse.

        运维是否可见

        :param is_maintain_visible: The is_maintain_visible of this AlarmConfigResponse.
        :type is_maintain_visible: str
        """
        self._is_maintain_visible = is_maintain_visible

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
        if not isinstance(other, AlarmConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
