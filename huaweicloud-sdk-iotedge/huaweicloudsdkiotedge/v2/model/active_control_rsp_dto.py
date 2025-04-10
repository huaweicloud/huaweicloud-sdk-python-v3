# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActiveControlRspDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_type': 'str',
        'control_id': 'str',
        'priority': 'int',
        'value': 'object',
        'end_time': 'int',
        'create_time': 'int'
    }

    attribute_map = {
        'control_type': 'control_type',
        'control_id': 'control_id',
        'priority': 'priority',
        'value': 'value',
        'end_time': 'end_time',
        'create_time': 'create_time'
    }

    def __init__(self, control_type=None, control_id=None, priority=None, value=None, end_time=None, create_time=None):
        r"""ActiveControlRspDTO

        The model defined in huaweicloud sdk

        :param control_type: 控制类型，包括control、schedule、local_control
        :type control_type: str
        :param control_id: 控制id
        :type control_id: str
        :param priority: 控制的优先级
        :type priority: int
        :param value: 此次控制的值
        :type value: object
        :param end_time: 控制的结束时间
        :type end_time: int
        :param create_time: 记录创建的时间
        :type create_time: int
        """
        
        

        self._control_type = None
        self._control_id = None
        self._priority = None
        self._value = None
        self._end_time = None
        self._create_time = None
        self.discriminator = None

        if control_type is not None:
            self.control_type = control_type
        if control_id is not None:
            self.control_id = control_id
        if priority is not None:
            self.priority = priority
        if value is not None:
            self.value = value
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def control_type(self):
        r"""Gets the control_type of this ActiveControlRspDTO.

        控制类型，包括control、schedule、local_control

        :return: The control_type of this ActiveControlRspDTO.
        :rtype: str
        """
        return self._control_type

    @control_type.setter
    def control_type(self, control_type):
        r"""Sets the control_type of this ActiveControlRspDTO.

        控制类型，包括control、schedule、local_control

        :param control_type: The control_type of this ActiveControlRspDTO.
        :type control_type: str
        """
        self._control_type = control_type

    @property
    def control_id(self):
        r"""Gets the control_id of this ActiveControlRspDTO.

        控制id

        :return: The control_id of this ActiveControlRspDTO.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        r"""Sets the control_id of this ActiveControlRspDTO.

        控制id

        :param control_id: The control_id of this ActiveControlRspDTO.
        :type control_id: str
        """
        self._control_id = control_id

    @property
    def priority(self):
        r"""Gets the priority of this ActiveControlRspDTO.

        控制的优先级

        :return: The priority of this ActiveControlRspDTO.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ActiveControlRspDTO.

        控制的优先级

        :param priority: The priority of this ActiveControlRspDTO.
        :type priority: int
        """
        self._priority = priority

    @property
    def value(self):
        r"""Gets the value of this ActiveControlRspDTO.

        此次控制的值

        :return: The value of this ActiveControlRspDTO.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ActiveControlRspDTO.

        此次控制的值

        :param value: The value of this ActiveControlRspDTO.
        :type value: object
        """
        self._value = value

    @property
    def end_time(self):
        r"""Gets the end_time of this ActiveControlRspDTO.

        控制的结束时间

        :return: The end_time of this ActiveControlRspDTO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ActiveControlRspDTO.

        控制的结束时间

        :param end_time: The end_time of this ActiveControlRspDTO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ActiveControlRspDTO.

        记录创建的时间

        :return: The create_time of this ActiveControlRspDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ActiveControlRspDTO.

        记录创建的时间

        :param create_time: The create_time of this ActiveControlRspDTO.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ActiveControlRspDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
