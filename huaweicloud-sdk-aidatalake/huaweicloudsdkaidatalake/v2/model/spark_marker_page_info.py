# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkMarkerPageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'previous_marker': 'str',
        'current_count': 'int'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'previous_marker': 'previous_marker',
        'current_count': 'current_count'
    }

    def __init__(self, next_marker=None, previous_marker=None, current_count=None):
        r"""SparkMarkerPageInfo

        The model defined in huaweicloud sdk

        :param next_marker: **参数解释**：下一页游标，用于标识下一页数据的起始位置。为空表示没有更多数据。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。 
        :type next_marker: str
        :param previous_marker: **参数解释**：上一页游标，用于标识上一页数据的起始位置。为空表示当前页是第一页。 **取值范围**：采用UUID格式，长度为36个字符。 
        :type previous_marker: str
        :param current_count: **参数解释**：当前页数据条数，用于标识当前返回的数据数量。 **取值范围**：大于等于0的整数，最大不超过100。 
        :type current_count: int
        """
        
        

        self._next_marker = None
        self._previous_marker = None
        self._current_count = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker
        if previous_marker is not None:
            self.previous_marker = previous_marker
        if current_count is not None:
            self.current_count = current_count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this SparkMarkerPageInfo.

        **参数解释**：下一页游标，用于标识下一页数据的起始位置。为空表示没有更多数据。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。 

        :return: The next_marker of this SparkMarkerPageInfo.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this SparkMarkerPageInfo.

        **参数解释**：下一页游标，用于标识下一页数据的起始位置。为空表示没有更多数据。 **取值范围**：采用UUID格式，长度为36个字符，例如：6c98db52-cac2-4ff1-9a91-b7793e95557d。 

        :param next_marker: The next_marker of this SparkMarkerPageInfo.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def previous_marker(self):
        r"""Gets the previous_marker of this SparkMarkerPageInfo.

        **参数解释**：上一页游标，用于标识上一页数据的起始位置。为空表示当前页是第一页。 **取值范围**：采用UUID格式，长度为36个字符。 

        :return: The previous_marker of this SparkMarkerPageInfo.
        :rtype: str
        """
        return self._previous_marker

    @previous_marker.setter
    def previous_marker(self, previous_marker):
        r"""Sets the previous_marker of this SparkMarkerPageInfo.

        **参数解释**：上一页游标，用于标识上一页数据的起始位置。为空表示当前页是第一页。 **取值范围**：采用UUID格式，长度为36个字符。 

        :param previous_marker: The previous_marker of this SparkMarkerPageInfo.
        :type previous_marker: str
        """
        self._previous_marker = previous_marker

    @property
    def current_count(self):
        r"""Gets the current_count of this SparkMarkerPageInfo.

        **参数解释**：当前页数据条数，用于标识当前返回的数据数量。 **取值范围**：大于等于0的整数，最大不超过100。 

        :return: The current_count of this SparkMarkerPageInfo.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        r"""Sets the current_count of this SparkMarkerPageInfo.

        **参数解释**：当前页数据条数，用于标识当前返回的数据数量。 **取值范围**：大于等于0的整数，最大不超过100。 

        :param current_count: The current_count of this SparkMarkerPageInfo.
        :type current_count: int
        """
        self._current_count = current_count

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
        if not isinstance(other, SparkMarkerPageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
