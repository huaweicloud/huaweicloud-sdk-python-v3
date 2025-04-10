# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePacifyWordsSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'language': 'LanguageEnum',
        'enable_pacify_words': 'bool'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'language': 'language',
        'enable_pacify_words': 'enable_pacify_words'
    }

    def __init__(self, robot_id=None, language=None, enable_pacify_words=None):
        r"""UpdatePacifyWordsSwitchReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param enable_pacify_words: 安抚话术功能开关。
        :type enable_pacify_words: bool
        """
        
        

        self._robot_id = None
        self._language = None
        self._enable_pacify_words = None
        self.discriminator = None

        self.robot_id = robot_id
        self.language = language
        self.enable_pacify_words = enable_pacify_words

    @property
    def robot_id(self):
        r"""Gets the robot_id of this UpdatePacifyWordsSwitchReq.

        应用ID。

        :return: The robot_id of this UpdatePacifyWordsSwitchReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this UpdatePacifyWordsSwitchReq.

        应用ID。

        :param robot_id: The robot_id of this UpdatePacifyWordsSwitchReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def language(self):
        r"""Gets the language of this UpdatePacifyWordsSwitchReq.

        :return: The language of this UpdatePacifyWordsSwitchReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdatePacifyWordsSwitchReq.

        :param language: The language of this UpdatePacifyWordsSwitchReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def enable_pacify_words(self):
        r"""Gets the enable_pacify_words of this UpdatePacifyWordsSwitchReq.

        安抚话术功能开关。

        :return: The enable_pacify_words of this UpdatePacifyWordsSwitchReq.
        :rtype: bool
        """
        return self._enable_pacify_words

    @enable_pacify_words.setter
    def enable_pacify_words(self, enable_pacify_words):
        r"""Sets the enable_pacify_words of this UpdatePacifyWordsSwitchReq.

        安抚话术功能开关。

        :param enable_pacify_words: The enable_pacify_words of this UpdatePacifyWordsSwitchReq.
        :type enable_pacify_words: bool
        """
        self._enable_pacify_words = enable_pacify_words

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
        if not isinstance(other, UpdatePacifyWordsSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
