# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeyTrendRequest:

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
        'stat_type': 'str',
        'key': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'stat_type': 'stat_type',
        'key': 'key',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, stat_type=None, key=None, start_at=None, end_at=None, x_language=None):
        r"""ShowKeyTrendRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param stat_type: 统计维度。size/storage/qps/traffic，默认size
        :type stat_type: str
        :param key: key名称（需URL编码）
        :type key: str
        :param start_at: 开始时间（毫秒时间戳）
        :type start_at: int
        :param end_at: 结束时间（毫秒时间戳）
        :type end_at: int
        :param x_language: 请求语言类型。en-us：英文。zh-cn：中文。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._stat_type = None
        self._key = None
        self._start_at = None
        self._end_at = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if stat_type is not None:
            self.stat_type = stat_type
        self.key = key
        self.start_at = start_at
        self.end_at = end_at
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKeyTrendRequest.

        实例ID

        :return: The instance_id of this ShowKeyTrendRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKeyTrendRequest.

        实例ID

        :param instance_id: The instance_id of this ShowKeyTrendRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowKeyTrendRequest.

        统计维度。size/storage/qps/traffic，默认size

        :return: The stat_type of this ShowKeyTrendRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowKeyTrendRequest.

        统计维度。size/storage/qps/traffic，默认size

        :param stat_type: The stat_type of this ShowKeyTrendRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def key(self):
        r"""Gets the key of this ShowKeyTrendRequest.

        key名称（需URL编码）

        :return: The key of this ShowKeyTrendRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowKeyTrendRequest.

        key名称（需URL编码）

        :param key: The key of this ShowKeyTrendRequest.
        :type key: str
        """
        self._key = key

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowKeyTrendRequest.

        开始时间（毫秒时间戳）

        :return: The start_at of this ShowKeyTrendRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowKeyTrendRequest.

        开始时间（毫秒时间戳）

        :param start_at: The start_at of this ShowKeyTrendRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowKeyTrendRequest.

        结束时间（毫秒时间戳）

        :return: The end_at of this ShowKeyTrendRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowKeyTrendRequest.

        结束时间（毫秒时间戳）

        :param end_at: The end_at of this ShowKeyTrendRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowKeyTrendRequest.

        请求语言类型。en-us：英文。zh-cn：中文。

        :return: The x_language of this ShowKeyTrendRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowKeyTrendRequest.

        请求语言类型。en-us：英文。zh-cn：中文。

        :param x_language: The x_language of this ShowKeyTrendRequest.
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
        if not isinstance(other, ShowKeyTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
