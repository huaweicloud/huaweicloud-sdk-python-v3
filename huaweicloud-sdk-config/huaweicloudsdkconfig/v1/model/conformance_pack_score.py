# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConformancePackScore:

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
        'name': 'str',
        'score': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'score': 'score'
    }

    def __init__(self, id=None, name=None, score=None):
        r"""ConformancePackScore

        The model defined in huaweicloud sdk

        :param id: 合规规则包ID。
        :type id: str
        :param name: 合规规则包名称。
        :type name: str
        :param score: 合规规则包分数。
        :type score: str
        """
        
        

        self._id = None
        self._name = None
        self._score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if score is not None:
            self.score = score

    @property
    def id(self):
        r"""Gets the id of this ConformancePackScore.

        合规规则包ID。

        :return: The id of this ConformancePackScore.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConformancePackScore.

        合规规则包ID。

        :param id: The id of this ConformancePackScore.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ConformancePackScore.

        合规规则包名称。

        :return: The name of this ConformancePackScore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConformancePackScore.

        合规规则包名称。

        :param name: The name of this ConformancePackScore.
        :type name: str
        """
        self._name = name

    @property
    def score(self):
        r"""Gets the score of this ConformancePackScore.

        合规规则包分数。

        :return: The score of this ConformancePackScore.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this ConformancePackScore.

        合规规则包分数。

        :param score: The score of this ConformancePackScore.
        :type score: str
        """
        self._score = score

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
        if not isinstance(other, ConformancePackScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
