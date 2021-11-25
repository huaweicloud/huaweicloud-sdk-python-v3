# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThrottleSpecialInfo:


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
        'app_id': 'str',
        'object_id': 'str',
        'object_type': 'str',
        'object_name': 'str',
        'throttle_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'call_limits': 'call_limits',
        'apply_time': 'apply_time',
        'app_name': 'app_name',
        'app_id': 'app_id',
        'object_id': 'object_id',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'throttle_id': 'throttle_id'
    }

    def __init__(self, id=None, call_limits=None, apply_time=None, app_name=None, app_id=None, object_id=None, object_type=None, object_name=None, throttle_id=None):
        """ThrottleSpecialInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._call_limits = None
        self._apply_time = None
        self._app_name = None
        self._app_id = None
        self._object_id = None
        self._object_type = None
        self._object_name = None
        self._throttle_id = None
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
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if object_name is not None:
            self.object_name = object_name
        if throttle_id is not None:
            self.throttle_id = throttle_id

    @property
    def id(self):
        """Gets the id of this ThrottleSpecialInfo.

        特殊配置的编号

        :return: The id of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleSpecialInfo.

        特殊配置的编号

        :param id: The id of this ThrottleSpecialInfo.
        :type: str
        """
        self._id = id

    @property
    def call_limits(self):
        """Gets the call_limits of this ThrottleSpecialInfo.

        特殊对象在流控时间内能够访问API的最大次数限制

        :return: The call_limits of this ThrottleSpecialInfo.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this ThrottleSpecialInfo.

        特殊对象在流控时间内能够访问API的最大次数限制

        :param call_limits: The call_limits of this ThrottleSpecialInfo.
        :type: int
        """
        self._call_limits = call_limits

    @property
    def apply_time(self):
        """Gets the apply_time of this ThrottleSpecialInfo.

        设置时间

        :return: The apply_time of this ThrottleSpecialInfo.
        :rtype: datetime
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ThrottleSpecialInfo.

        设置时间

        :param apply_time: The apply_time of this ThrottleSpecialInfo.
        :type: datetime
        """
        self._apply_time = apply_time

    @property
    def app_name(self):
        """Gets the app_name of this ThrottleSpecialInfo.

        作用的APP名称

        :return: The app_name of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ThrottleSpecialInfo.

        作用的APP名称

        :param app_name: The app_name of this ThrottleSpecialInfo.
        :type: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this ThrottleSpecialInfo.

        作用的APP编号

        :return: The app_id of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ThrottleSpecialInfo.

        作用的APP编号

        :param app_id: The app_id of this ThrottleSpecialInfo.
        :type: str
        """
        self._app_id = app_id

    @property
    def object_id(self):
        """Gets the object_id of this ThrottleSpecialInfo.

        特殊对象的身份标识

        :return: The object_id of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ThrottleSpecialInfo.

        特殊对象的身份标识

        :param object_id: The object_id of this ThrottleSpecialInfo.
        :type: str
        """
        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this ThrottleSpecialInfo.

        特殊对象类型：APP、USER

        :return: The object_type of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ThrottleSpecialInfo.

        特殊对象类型：APP、USER

        :param object_type: The object_type of this ThrottleSpecialInfo.
        :type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        """Gets the object_name of this ThrottleSpecialInfo.

        作用的APP或租户的名称

        :return: The object_name of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this ThrottleSpecialInfo.

        作用的APP或租户的名称

        :param object_name: The object_name of this ThrottleSpecialInfo.
        :type: str
        """
        self._object_name = object_name

    @property
    def throttle_id(self):
        """Gets the throttle_id of this ThrottleSpecialInfo.

        流控策略编号

        :return: The throttle_id of this ThrottleSpecialInfo.
        :rtype: str
        """
        return self._throttle_id

    @throttle_id.setter
    def throttle_id(self, throttle_id):
        """Sets the throttle_id of this ThrottleSpecialInfo.

        流控策略编号

        :param throttle_id: The throttle_id of this ThrottleSpecialInfo.
        :type: str
        """
        self._throttle_id = throttle_id

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
        if not isinstance(other, ThrottleSpecialInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other