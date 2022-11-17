# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationSaveRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'timezone': 'str',
        'user_name': 'str',
        'topics': 'list[Topics]'
    }

    attribute_map = {
        'language': 'language',
        'timezone': 'timezone',
        'user_name': 'user_name',
        'topics': 'topics'
    }

    def __init__(self, language=None, timezone=None, user_name=None, topics=None):
        """NotificationSaveRule

        The model defined in huaweicloud sdk

        :param language: 首选项对应的语言
        :type language: str
        :param timezone: 首选项对应的时区信息
        :type timezone: str
        :param user_name: 用户名
        :type user_name: str
        :param topics: 主题信息
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        
        

        self._language = None
        self._timezone = None
        self._user_name = None
        self._topics = None
        self.discriminator = None

        self.language = language
        if timezone is not None:
            self.timezone = timezone
        self.user_name = user_name
        self.topics = topics

    @property
    def language(self):
        """Gets the language of this NotificationSaveRule.

        首选项对应的语言

        :return: The language of this NotificationSaveRule.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this NotificationSaveRule.

        首选项对应的语言

        :param language: The language of this NotificationSaveRule.
        :type language: str
        """
        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this NotificationSaveRule.

        首选项对应的时区信息

        :return: The timezone of this NotificationSaveRule.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this NotificationSaveRule.

        首选项对应的时区信息

        :param timezone: The timezone of this NotificationSaveRule.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def user_name(self):
        """Gets the user_name of this NotificationSaveRule.

        用户名

        :return: The user_name of this NotificationSaveRule.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NotificationSaveRule.

        用户名

        :param user_name: The user_name of this NotificationSaveRule.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def topics(self):
        """Gets the topics of this NotificationSaveRule.

        主题信息

        :return: The topics of this NotificationSaveRule.
        :rtype: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this NotificationSaveRule.

        主题信息

        :param topics: The topics of this NotificationSaveRule.
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        self._topics = topics

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
        if not isinstance(other, NotificationSaveRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
