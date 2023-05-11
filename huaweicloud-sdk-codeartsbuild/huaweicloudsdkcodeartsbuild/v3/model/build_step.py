# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildStep:

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
        'build_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'build_time': 'build_time'
    }

    def __init__(self, name=None, status=None, build_time=None):
        """BuildStep

        The model defined in huaweicloud sdk

        :param name: 步骤名称
        :type name: str
        :param status: 步骤状态,可选值（running运行中，success成功，error失败，未运行为空字符串）
        :type status: str
        :param build_time: 步骤执行时长，单位ms
        :type build_time: int
        """
        
        

        self._name = None
        self._status = None
        self._build_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if build_time is not None:
            self.build_time = build_time

    @property
    def name(self):
        """Gets the name of this BuildStep.

        步骤名称

        :return: The name of this BuildStep.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildStep.

        步骤名称

        :param name: The name of this BuildStep.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this BuildStep.

        步骤状态,可选值（running运行中，success成功，error失败，未运行为空字符串）

        :return: The status of this BuildStep.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BuildStep.

        步骤状态,可选值（running运行中，success成功，error失败，未运行为空字符串）

        :param status: The status of this BuildStep.
        :type status: str
        """
        self._status = status

    @property
    def build_time(self):
        """Gets the build_time of this BuildStep.

        步骤执行时长，单位ms

        :return: The build_time of this BuildStep.
        :rtype: int
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        """Sets the build_time of this BuildStep.

        步骤执行时长，单位ms

        :param build_time: The build_time of this BuildStep.
        :type build_time: int
        """
        self._build_time = build_time

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
        if not isinstance(other, BuildStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
