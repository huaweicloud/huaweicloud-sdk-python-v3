# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewaySearchConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_type': 'str',
        'top_n': 'int',
        'score_threshold': 'str'
    }

    attribute_map = {
        'search_type': 'search_type',
        'top_n': 'top_n',
        'score_threshold': 'score_threshold'
    }

    def __init__(self, search_type=None, top_n=None, score_threshold=None):
        r"""CoreGatewaySearchConfiguration

        The model defined in huaweicloud sdk

        :param search_type: 搜索类型。
        :type search_type: str
        :param top_n: 语义检索返回的工具数量。
        :type top_n: int
        :param score_threshold: 语义检索相似得分阈值。
        :type score_threshold: str
        """
        
        

        self._search_type = None
        self._top_n = None
        self._score_threshold = None
        self.discriminator = None

        if search_type is not None:
            self.search_type = search_type
        if top_n is not None:
            self.top_n = top_n
        if score_threshold is not None:
            self.score_threshold = score_threshold

    @property
    def search_type(self):
        r"""Gets the search_type of this CoreGatewaySearchConfiguration.

        搜索类型。

        :return: The search_type of this CoreGatewaySearchConfiguration.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this CoreGatewaySearchConfiguration.

        搜索类型。

        :param search_type: The search_type of this CoreGatewaySearchConfiguration.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def top_n(self):
        r"""Gets the top_n of this CoreGatewaySearchConfiguration.

        语义检索返回的工具数量。

        :return: The top_n of this CoreGatewaySearchConfiguration.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        r"""Sets the top_n of this CoreGatewaySearchConfiguration.

        语义检索返回的工具数量。

        :param top_n: The top_n of this CoreGatewaySearchConfiguration.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def score_threshold(self):
        r"""Gets the score_threshold of this CoreGatewaySearchConfiguration.

        语义检索相似得分阈值。

        :return: The score_threshold of this CoreGatewaySearchConfiguration.
        :rtype: str
        """
        return self._score_threshold

    @score_threshold.setter
    def score_threshold(self, score_threshold):
        r"""Sets the score_threshold of this CoreGatewaySearchConfiguration.

        语义检索相似得分阈值。

        :param score_threshold: The score_threshold of this CoreGatewaySearchConfiguration.
        :type score_threshold: str
        """
        self._score_threshold = score_threshold

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
        if not isinstance(other, CoreGatewaySearchConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
