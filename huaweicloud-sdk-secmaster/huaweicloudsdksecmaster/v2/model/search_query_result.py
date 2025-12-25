# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQueryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'str',
        'data_source': 'object'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'data_source': 'data_source'
    }

    def __init__(self, timestamp=None, data_source=None):
        r"""SearchQueryResult

        The model defined in huaweicloud sdk

        :param timestamp: 时间戳
        :type timestamp: str
        :param data_source: 数据源
        :type data_source: object
        """
        
        

        self._timestamp = None
        self._data_source = None
        self.discriminator = None

        self.timestamp = timestamp
        self.data_source = data_source

    @property
    def timestamp(self):
        r"""Gets the timestamp of this SearchQueryResult.

        时间戳

        :return: The timestamp of this SearchQueryResult.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this SearchQueryResult.

        时间戳

        :param timestamp: The timestamp of this SearchQueryResult.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def data_source(self):
        r"""Gets the data_source of this SearchQueryResult.

        数据源

        :return: The data_source of this SearchQueryResult.
        :rtype: object
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this SearchQueryResult.

        数据源

        :param data_source: The data_source of this SearchQueryResult.
        :type data_source: object
        """
        self._data_source = data_source

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
        if not isinstance(other, SearchQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
