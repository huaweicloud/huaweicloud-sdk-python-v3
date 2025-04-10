# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimelineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'operation_time': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'operation_time': 'operation_time',
        'user_name': 'user_name'
    }

    def __init__(self, name=None, status=None, operation_time=None, user_name=None):
        r"""TimelineInfo

        The model defined in huaweicloud sdk

        :param name: 时间轴名称。
        :type name: str
        :param status: 状态。
        :type status: str
        :param operation_time: 操作时间。
        :type operation_time: str
        :param user_name: 用户名称。
        :type user_name: str
        """
        
        

        self._name = None
        self._status = None
        self._operation_time = None
        self._user_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if operation_time is not None:
            self.operation_time = operation_time
        if user_name is not None:
            self.user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this TimelineInfo.

        时间轴名称。

        :return: The name of this TimelineInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TimelineInfo.

        时间轴名称。

        :param name: The name of this TimelineInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this TimelineInfo.

        状态。

        :return: The status of this TimelineInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TimelineInfo.

        状态。

        :param status: The status of this TimelineInfo.
        :type status: str
        """
        self._status = status

    @property
    def operation_time(self):
        r"""Gets the operation_time of this TimelineInfo.

        操作时间。

        :return: The operation_time of this TimelineInfo.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this TimelineInfo.

        操作时间。

        :param operation_time: The operation_time of this TimelineInfo.
        :type operation_time: str
        """
        self._operation_time = operation_time

    @property
    def user_name(self):
        r"""Gets the user_name of this TimelineInfo.

        用户名称。

        :return: The user_name of this TimelineInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TimelineInfo.

        用户名称。

        :param user_name: The user_name of this TimelineInfo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, TimelineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
