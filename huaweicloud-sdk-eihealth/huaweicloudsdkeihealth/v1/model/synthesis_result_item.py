# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route': 'list[str]',
        'score': 'float'
    }

    attribute_map = {
        'route': 'route',
        'score': 'score'
    }

    def __init__(self, route=None, score=None):
        """SynthesisResultItem

        The model defined in huaweicloud sdk

        :param route: 分子合成规划，列表内是reactions id
        :type route: list[str]
        :param score: 当前分子合成路径的得分
        :type score: float
        """
        
        

        self._route = None
        self._score = None
        self.discriminator = None

        self.route = route
        self.score = score

    @property
    def route(self):
        """Gets the route of this SynthesisResultItem.

        分子合成规划，列表内是reactions id

        :return: The route of this SynthesisResultItem.
        :rtype: list[str]
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this SynthesisResultItem.

        分子合成规划，列表内是reactions id

        :param route: The route of this SynthesisResultItem.
        :type route: list[str]
        """
        self._route = route

    @property
    def score(self):
        """Gets the score of this SynthesisResultItem.

        当前分子合成路径的得分

        :return: The score of this SynthesisResultItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SynthesisResultItem.

        当前分子合成路径的得分

        :param score: The score of this SynthesisResultItem.
        :type score: float
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
        if not isinstance(other, SynthesisResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
