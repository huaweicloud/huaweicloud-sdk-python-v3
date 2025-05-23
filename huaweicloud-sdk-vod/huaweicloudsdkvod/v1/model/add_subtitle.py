# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubtitle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'language': 'str',
        'obs_info': 'ObsInfo'
    }

    attribute_map = {
        'type': 'type',
        'language': 'language',
        'obs_info': 'obs_info'
    }

    def __init__(self, type=None, language=None, obs_info=None):
        r"""AddSubtitle

        The model defined in huaweicloud sdk

        :param type: 字幕类型，字幕封装当前仅支持VTT和SRT
        :type type: str
        :param language: 字幕语言
        :type language: str
        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        
        

        self._type = None
        self._language = None
        self._obs_info = None
        self.discriminator = None

        self.type = type
        self.language = language
        self.obs_info = obs_info

    @property
    def type(self):
        r"""Gets the type of this AddSubtitle.

        字幕类型，字幕封装当前仅支持VTT和SRT

        :return: The type of this AddSubtitle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddSubtitle.

        字幕类型，字幕封装当前仅支持VTT和SRT

        :param type: The type of this AddSubtitle.
        :type type: str
        """
        self._type = type

    @property
    def language(self):
        r"""Gets the language of this AddSubtitle.

        字幕语言

        :return: The language of this AddSubtitle.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this AddSubtitle.

        字幕语言

        :param language: The language of this AddSubtitle.
        :type language: str
        """
        self._language = language

    @property
    def obs_info(self):
        r"""Gets the obs_info of this AddSubtitle.

        :return: The obs_info of this AddSubtitle.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this AddSubtitle.

        :param obs_info: The obs_info of this AddSubtitle.
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._obs_info = obs_info

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
        if not isinstance(other, AddSubtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
