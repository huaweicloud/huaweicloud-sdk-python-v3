# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_mode': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'category_id': 'str'
    }

    attribute_map = {
        'build_mode': 'build_mode',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'category_id': 'category_id'
    }

    def __init__(self, build_mode=None, start_time=None, end_time=None, category_id=None):
        """BuildTaskInfo

        The model defined in huaweicloud sdk

        :param build_mode: 任务模式
        :type build_mode: str
        :param start_time: 任务开始时间
        :type start_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param category_id: 策略ID
        :type category_id: str
        """
        
        

        self._build_mode = None
        self._start_time = None
        self._end_time = None
        self._category_id = None
        self.discriminator = None

        self.build_mode = build_mode
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if category_id is not None:
            self.category_id = category_id

    @property
    def build_mode(self):
        """Gets the build_mode of this BuildTaskInfo.

        任务模式

        :return: The build_mode of this BuildTaskInfo.
        :rtype: str
        """
        return self._build_mode

    @build_mode.setter
    def build_mode(self, build_mode):
        """Sets the build_mode of this BuildTaskInfo.

        任务模式

        :param build_mode: The build_mode of this BuildTaskInfo.
        :type build_mode: str
        """
        self._build_mode = build_mode

    @property
    def start_time(self):
        """Gets the start_time of this BuildTaskInfo.

        任务开始时间

        :return: The start_time of this BuildTaskInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BuildTaskInfo.

        任务开始时间

        :param start_time: The start_time of this BuildTaskInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this BuildTaskInfo.

        任务结束时间

        :return: The end_time of this BuildTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BuildTaskInfo.

        任务结束时间

        :param end_time: The end_time of this BuildTaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def category_id(self):
        """Gets the category_id of this BuildTaskInfo.

        策略ID

        :return: The category_id of this BuildTaskInfo.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this BuildTaskInfo.

        策略ID

        :param category_id: The category_id of this BuildTaskInfo.
        :type category_id: str
        """
        self._category_id = category_id

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
        if not isinstance(other, BuildTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
