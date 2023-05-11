# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecommendWordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_service_key': 'str',
        'x_site': 'str',
        'x_language': 'str',
        'recommend_word_id': 'str',
        'level_value': 'int',
        'theme_name': 'str'
    }

    attribute_map = {
        'x_service_key': 'x-service-key',
        'x_site': 'x-site',
        'x_language': 'x-language',
        'recommend_word_id': 'recommend_word_id',
        'level_value': 'level_value',
        'theme_name': 'theme_name'
    }

    def __init__(self, x_service_key=None, x_site=None, x_language=None, recommend_word_id=None, level_value=None, theme_name=None):
        """ListRecommendWordsRequest

        The model defined in huaweicloud sdk

        :param x_service_key: 调用智能客服服务标志。
        :type x_service_key: str
        :param x_site: 站点标记，0-中国站  1-国际站
        :type x_site: str
        :param x_language: 区域语言简写，en-us  zh-cn
        :type x_language: str
        :param recommend_word_id: 推荐词Id
        :type recommend_word_id: str
        :param level_value: 推荐词层级
        :type level_value: int
        :param theme_name: 主题名称
        :type theme_name: str
        """
        
        

        self._x_service_key = None
        self._x_site = None
        self._x_language = None
        self._recommend_word_id = None
        self._level_value = None
        self._theme_name = None
        self.discriminator = None

        if x_service_key is not None:
            self.x_service_key = x_service_key
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if recommend_word_id is not None:
            self.recommend_word_id = recommend_word_id
        if level_value is not None:
            self.level_value = level_value
        if theme_name is not None:
            self.theme_name = theme_name

    @property
    def x_service_key(self):
        """Gets the x_service_key of this ListRecommendWordsRequest.

        调用智能客服服务标志。

        :return: The x_service_key of this ListRecommendWordsRequest.
        :rtype: str
        """
        return self._x_service_key

    @x_service_key.setter
    def x_service_key(self, x_service_key):
        """Sets the x_service_key of this ListRecommendWordsRequest.

        调用智能客服服务标志。

        :param x_service_key: The x_service_key of this ListRecommendWordsRequest.
        :type x_service_key: str
        """
        self._x_service_key = x_service_key

    @property
    def x_site(self):
        """Gets the x_site of this ListRecommendWordsRequest.

        站点标记，0-中国站  1-国际站

        :return: The x_site of this ListRecommendWordsRequest.
        :rtype: str
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListRecommendWordsRequest.

        站点标记，0-中国站  1-国际站

        :param x_site: The x_site of this ListRecommendWordsRequest.
        :type x_site: str
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListRecommendWordsRequest.

        区域语言简写，en-us  zh-cn

        :return: The x_language of this ListRecommendWordsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListRecommendWordsRequest.

        区域语言简写，en-us  zh-cn

        :param x_language: The x_language of this ListRecommendWordsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def recommend_word_id(self):
        """Gets the recommend_word_id of this ListRecommendWordsRequest.

        推荐词Id

        :return: The recommend_word_id of this ListRecommendWordsRequest.
        :rtype: str
        """
        return self._recommend_word_id

    @recommend_word_id.setter
    def recommend_word_id(self, recommend_word_id):
        """Sets the recommend_word_id of this ListRecommendWordsRequest.

        推荐词Id

        :param recommend_word_id: The recommend_word_id of this ListRecommendWordsRequest.
        :type recommend_word_id: str
        """
        self._recommend_word_id = recommend_word_id

    @property
    def level_value(self):
        """Gets the level_value of this ListRecommendWordsRequest.

        推荐词层级

        :return: The level_value of this ListRecommendWordsRequest.
        :rtype: int
        """
        return self._level_value

    @level_value.setter
    def level_value(self, level_value):
        """Sets the level_value of this ListRecommendWordsRequest.

        推荐词层级

        :param level_value: The level_value of this ListRecommendWordsRequest.
        :type level_value: int
        """
        self._level_value = level_value

    @property
    def theme_name(self):
        """Gets the theme_name of this ListRecommendWordsRequest.

        主题名称

        :return: The theme_name of this ListRecommendWordsRequest.
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this ListRecommendWordsRequest.

        主题名称

        :param theme_name: The theme_name of this ListRecommendWordsRequest.
        :type theme_name: str
        """
        self._theme_name = theme_name

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
        if not isinstance(other, ListRecommendWordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
