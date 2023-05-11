# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecommendWord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommend_word_id': 'str',
        'recommend_word_name': 'str',
        'level_value': 'int',
        'sort_value': 'int',
        'theme_id': 'str',
        'theme_name': 'str',
        'answer_info': 'AnswerInfo'
    }

    attribute_map = {
        'recommend_word_id': 'recommend_word_id',
        'recommend_word_name': 'recommend_word_name',
        'level_value': 'level_value',
        'sort_value': 'sort_value',
        'theme_id': 'theme_id',
        'theme_name': 'theme_name',
        'answer_info': 'answer_info'
    }

    def __init__(self, recommend_word_id=None, recommend_word_name=None, level_value=None, sort_value=None, theme_id=None, theme_name=None, answer_info=None):
        """RecommendWord

        The model defined in huaweicloud sdk

        :param recommend_word_id: 推荐词Id
        :type recommend_word_id: str
        :param recommend_word_name: 推荐词
        :type recommend_word_name: str
        :param level_value: 推荐词层级
        :type level_value: int
        :param sort_value: 推荐词排序，序号越小越靠前
        :type sort_value: int
        :param theme_id: 主题Id
        :type theme_id: str
        :param theme_name: 主题名称
        :type theme_name: str
        :param answer_info: 
        :type answer_info: :class:`huaweicloudsdkosm.v2.AnswerInfo`
        """
        
        

        self._recommend_word_id = None
        self._recommend_word_name = None
        self._level_value = None
        self._sort_value = None
        self._theme_id = None
        self._theme_name = None
        self._answer_info = None
        self.discriminator = None

        if recommend_word_id is not None:
            self.recommend_word_id = recommend_word_id
        if recommend_word_name is not None:
            self.recommend_word_name = recommend_word_name
        if level_value is not None:
            self.level_value = level_value
        if sort_value is not None:
            self.sort_value = sort_value
        if theme_id is not None:
            self.theme_id = theme_id
        if theme_name is not None:
            self.theme_name = theme_name
        if answer_info is not None:
            self.answer_info = answer_info

    @property
    def recommend_word_id(self):
        """Gets the recommend_word_id of this RecommendWord.

        推荐词Id

        :return: The recommend_word_id of this RecommendWord.
        :rtype: str
        """
        return self._recommend_word_id

    @recommend_word_id.setter
    def recommend_word_id(self, recommend_word_id):
        """Sets the recommend_word_id of this RecommendWord.

        推荐词Id

        :param recommend_word_id: The recommend_word_id of this RecommendWord.
        :type recommend_word_id: str
        """
        self._recommend_word_id = recommend_word_id

    @property
    def recommend_word_name(self):
        """Gets the recommend_word_name of this RecommendWord.

        推荐词

        :return: The recommend_word_name of this RecommendWord.
        :rtype: str
        """
        return self._recommend_word_name

    @recommend_word_name.setter
    def recommend_word_name(self, recommend_word_name):
        """Sets the recommend_word_name of this RecommendWord.

        推荐词

        :param recommend_word_name: The recommend_word_name of this RecommendWord.
        :type recommend_word_name: str
        """
        self._recommend_word_name = recommend_word_name

    @property
    def level_value(self):
        """Gets the level_value of this RecommendWord.

        推荐词层级

        :return: The level_value of this RecommendWord.
        :rtype: int
        """
        return self._level_value

    @level_value.setter
    def level_value(self, level_value):
        """Sets the level_value of this RecommendWord.

        推荐词层级

        :param level_value: The level_value of this RecommendWord.
        :type level_value: int
        """
        self._level_value = level_value

    @property
    def sort_value(self):
        """Gets the sort_value of this RecommendWord.

        推荐词排序，序号越小越靠前

        :return: The sort_value of this RecommendWord.
        :rtype: int
        """
        return self._sort_value

    @sort_value.setter
    def sort_value(self, sort_value):
        """Sets the sort_value of this RecommendWord.

        推荐词排序，序号越小越靠前

        :param sort_value: The sort_value of this RecommendWord.
        :type sort_value: int
        """
        self._sort_value = sort_value

    @property
    def theme_id(self):
        """Gets the theme_id of this RecommendWord.

        主题Id

        :return: The theme_id of this RecommendWord.
        :rtype: str
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this RecommendWord.

        主题Id

        :param theme_id: The theme_id of this RecommendWord.
        :type theme_id: str
        """
        self._theme_id = theme_id

    @property
    def theme_name(self):
        """Gets the theme_name of this RecommendWord.

        主题名称

        :return: The theme_name of this RecommendWord.
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this RecommendWord.

        主题名称

        :param theme_name: The theme_name of this RecommendWord.
        :type theme_name: str
        """
        self._theme_name = theme_name

    @property
    def answer_info(self):
        """Gets the answer_info of this RecommendWord.

        :return: The answer_info of this RecommendWord.
        :rtype: :class:`huaweicloudsdkosm.v2.AnswerInfo`
        """
        return self._answer_info

    @answer_info.setter
    def answer_info(self, answer_info):
        """Sets the answer_info of this RecommendWord.

        :param answer_info: The answer_info of this RecommendWord.
        :type answer_info: :class:`huaweicloudsdkosm.v2.AnswerInfo`
        """
        self._answer_info = answer_info

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
        if not isinstance(other, RecommendWord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
