# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockBlockingDbRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None, x_language=None):
        r"""ListLockBlockingDbRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_time: 开始时间戳（Unix timestamp），单位：毫秒。
        :type start_time: int
        :param end_time: 结束时间戳（Unix timestamp），单位：毫秒。
        :type end_time: int
        :param x_language: 请求语言类型。en-us：英文。 zh-cn：中文。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListLockBlockingDbRequest.

        实例ID。

        :return: The instance_id of this ListLockBlockingDbRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListLockBlockingDbRequest.

        实例ID。

        :param instance_id: The instance_id of this ListLockBlockingDbRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLockBlockingDbRequest.

        开始时间戳（Unix timestamp），单位：毫秒。

        :return: The start_time of this ListLockBlockingDbRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLockBlockingDbRequest.

        开始时间戳（Unix timestamp），单位：毫秒。

        :param start_time: The start_time of this ListLockBlockingDbRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLockBlockingDbRequest.

        结束时间戳（Unix timestamp），单位：毫秒。

        :return: The end_time of this ListLockBlockingDbRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLockBlockingDbRequest.

        结束时间戳（Unix timestamp），单位：毫秒。

        :param end_time: The end_time of this ListLockBlockingDbRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListLockBlockingDbRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :return: The x_language of this ListLockBlockingDbRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListLockBlockingDbRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :param x_language: The x_language of this ListLockBlockingDbRequest.
        :type x_language: str
        """
        self._x_language = x_language

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListLockBlockingDbRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
