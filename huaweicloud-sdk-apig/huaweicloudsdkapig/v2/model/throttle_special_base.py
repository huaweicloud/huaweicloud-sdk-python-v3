# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThrottleSpecialBase:

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
        'call_limits': 'int',
        'apply_time': 'datetime',
        'app_name': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'call_limits': 'call_limits',
        'apply_time': 'apply_time',
        'app_name': 'app_name',
        'app_id': 'app_id'
    }

    def __init__(self, id=None, call_limits=None, apply_time=None, app_name=None, app_id=None):
        """ThrottleSpecialBase

        The model defined in huaweicloud sdk

        :param id: 特殊配置的编号
        :type id: str
        :param call_limits: 特殊对象在流控时间内能够访问API的最大次数限制
        :type call_limits: int
        :param apply_time: 设置时间
        :type apply_time: datetime
        :param app_name: 作用的APP名称
        :type app_name: str
        :param app_id: 作用的APP编号
        :type app_id: str
        """
        
        

        self._id = None
        self._call_limits = None
        self._apply_time = None
        self._app_name = None
        self._app_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if call_limits is not None:
            self.call_limits = call_limits
        if apply_time is not None:
            self.apply_time = apply_time
        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id

    @property
    def id(self):
        """Gets the id of this ThrottleSpecialBase.

        特殊配置的编号

        :return: The id of this ThrottleSpecialBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleSpecialBase.

        特殊配置的编号

        :param id: The id of this ThrottleSpecialBase.
        :type id: str
        """
        self._id = id

    @property
    def call_limits(self):
        """Gets the call_limits of this ThrottleSpecialBase.

        特殊对象在流控时间内能够访问API的最大次数限制

        :return: The call_limits of this ThrottleSpecialBase.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this ThrottleSpecialBase.

        特殊对象在流控时间内能够访问API的最大次数限制

        :param call_limits: The call_limits of this ThrottleSpecialBase.
        :type call_limits: int
        """
        self._call_limits = call_limits

    @property
    def apply_time(self):
        """Gets the apply_time of this ThrottleSpecialBase.

        设置时间

        :return: The apply_time of this ThrottleSpecialBase.
        :rtype: datetime
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ThrottleSpecialBase.

        设置时间

        :param apply_time: The apply_time of this ThrottleSpecialBase.
        :type apply_time: datetime
        """
        self._apply_time = apply_time

    @property
    def app_name(self):
        """Gets the app_name of this ThrottleSpecialBase.

        作用的APP名称

        :return: The app_name of this ThrottleSpecialBase.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ThrottleSpecialBase.

        作用的APP名称

        :param app_name: The app_name of this ThrottleSpecialBase.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this ThrottleSpecialBase.

        作用的APP编号

        :return: The app_id of this ThrottleSpecialBase.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ThrottleSpecialBase.

        作用的APP编号

        :param app_id: The app_id of this ThrottleSpecialBase.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ThrottleSpecialBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
