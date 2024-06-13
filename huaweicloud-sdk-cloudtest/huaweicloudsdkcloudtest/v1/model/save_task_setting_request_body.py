# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveTaskSettingRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_running_time': 'int',
        'is_long_run': 'str'
    }

    attribute_map = {
        'max_running_time': 'max_running_time',
        'is_long_run': 'is_long_run'
    }

    def __init__(self, max_running_time=None, is_long_run=None):
        """SaveTaskSettingRequestBody

        The model defined in huaweicloud sdk

        :param max_running_time: 自定义时长
        :type max_running_time: int
        :param is_long_run: 是否长期运行
        :type is_long_run: str
        """
        
        

        self._max_running_time = None
        self._is_long_run = None
        self.discriminator = None

        if max_running_time is not None:
            self.max_running_time = max_running_time
        if is_long_run is not None:
            self.is_long_run = is_long_run

    @property
    def max_running_time(self):
        """Gets the max_running_time of this SaveTaskSettingRequestBody.

        自定义时长

        :return: The max_running_time of this SaveTaskSettingRequestBody.
        :rtype: int
        """
        return self._max_running_time

    @max_running_time.setter
    def max_running_time(self, max_running_time):
        """Sets the max_running_time of this SaveTaskSettingRequestBody.

        自定义时长

        :param max_running_time: The max_running_time of this SaveTaskSettingRequestBody.
        :type max_running_time: int
        """
        self._max_running_time = max_running_time

    @property
    def is_long_run(self):
        """Gets the is_long_run of this SaveTaskSettingRequestBody.

        是否长期运行

        :return: The is_long_run of this SaveTaskSettingRequestBody.
        :rtype: str
        """
        return self._is_long_run

    @is_long_run.setter
    def is_long_run(self, is_long_run):
        """Sets the is_long_run of this SaveTaskSettingRequestBody.

        是否长期运行

        :param is_long_run: The is_long_run of this SaveTaskSettingRequestBody.
        :type is_long_run: str
        """
        self._is_long_run = is_long_run

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
        if not isinstance(other, SaveTaskSettingRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
