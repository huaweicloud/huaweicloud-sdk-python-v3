# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_source': 'object',
        'timestamp': 'int'
    }

    attribute_map = {
        'data_source': 'data_source',
        'timestamp': 'timestamp'
    }

    def __init__(self, data_source=None, timestamp=None):
        r"""SearchResult

        The model defined in huaweicloud sdk

        :param data_source: 原始日志内容
        :type data_source: object
        :param timestamp: 数据接收时间
        :type timestamp: int
        """
        
        

        self._data_source = None
        self._timestamp = None
        self.discriminator = None

        self.data_source = data_source
        self.timestamp = timestamp

    @property
    def data_source(self):
        r"""Gets the data_source of this SearchResult.

        原始日志内容

        :return: The data_source of this SearchResult.
        :rtype: object
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this SearchResult.

        原始日志内容

        :param data_source: The data_source of this SearchResult.
        :type data_source: object
        """
        self._data_source = data_source

    @property
    def timestamp(self):
        r"""Gets the timestamp of this SearchResult.

        数据接收时间

        :return: The timestamp of this SearchResult.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this SearchResult.

        数据接收时间

        :param timestamp: The timestamp of this SearchResult.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
