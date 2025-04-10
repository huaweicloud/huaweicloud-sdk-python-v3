# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'score': 'float',
        'source': 'ItemSource'
    }

    attribute_map = {
        'id': 'id',
        'score': 'score',
        'source': 'source'
    }

    def __init__(self, id=None, score=None, source=None):
        r"""SearchItem

        The model defined in huaweicloud sdk

        :param id: 数据唯一ID。
        :type id: str
        :param score: 数据匹配分数。
        :type score: float
        :param source: 
        :type source: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        """
        
        

        self._id = None
        self._score = None
        self._source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if score is not None:
            self.score = score
        if source is not None:
            self.source = source

    @property
    def id(self):
        r"""Gets the id of this SearchItem.

        数据唯一ID。

        :return: The id of this SearchItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SearchItem.

        数据唯一ID。

        :param id: The id of this SearchItem.
        :type id: str
        """
        self._id = id

    @property
    def score(self):
        r"""Gets the score of this SearchItem.

        数据匹配分数。

        :return: The score of this SearchItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this SearchItem.

        数据匹配分数。

        :param score: The score of this SearchItem.
        :type score: float
        """
        self._score = score

    @property
    def source(self):
        r"""Gets the source of this SearchItem.

        :return: The source of this SearchItem.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this SearchItem.

        :param source: The source of this SearchItem.
        :type source: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        """
        self._source = source

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
        if not isinstance(other, SearchItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
