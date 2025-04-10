# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAfterParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'id': 'str'
    }

    attribute_map = {
        'score': 'score',
        'id': 'id'
    }

    def __init__(self, score=None, id=None):
        r"""SearchAfterParam

        The model defined in huaweicloud sdk

        :param score: 结果的得分。
        :type score: float
        :param id: 结果的唯一ID。
        :type id: str
        """
        
        

        self._score = None
        self._id = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if id is not None:
            self.id = id

    @property
    def score(self):
        r"""Gets the score of this SearchAfterParam.

        结果的得分。

        :return: The score of this SearchAfterParam.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this SearchAfterParam.

        结果的得分。

        :param score: The score of this SearchAfterParam.
        :type score: float
        """
        self._score = score

    @property
    def id(self):
        r"""Gets the id of this SearchAfterParam.

        结果的唯一ID。

        :return: The id of this SearchAfterParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SearchAfterParam.

        结果的唯一ID。

        :param id: The id of this SearchAfterParam.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, SearchAfterParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
