# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LanguageCheckInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_language': 'str',
        'shoot_script': 'list[LiveShootScriptItem]'
    }

    attribute_map = {
        'target_language': 'target_language',
        'shoot_script': 'shoot_script'
    }

    def __init__(self, target_language=None, shoot_script=None):
        """LanguageCheckInfoReq

        The model defined in huaweicloud sdk

        :param target_language: 目标语言
        :type target_language: str
        :param shoot_script: 用户传来的剧本文本信息
        :type shoot_script: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        
        

        self._target_language = None
        self._shoot_script = None
        self.discriminator = None

        self.target_language = target_language
        self.shoot_script = shoot_script

    @property
    def target_language(self):
        """Gets the target_language of this LanguageCheckInfoReq.

        目标语言

        :return: The target_language of this LanguageCheckInfoReq.
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this LanguageCheckInfoReq.

        目标语言

        :param target_language: The target_language of this LanguageCheckInfoReq.
        :type target_language: str
        """
        self._target_language = target_language

    @property
    def shoot_script(self):
        """Gets the shoot_script of this LanguageCheckInfoReq.

        用户传来的剧本文本信息

        :return: The shoot_script of this LanguageCheckInfoReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        return self._shoot_script

    @shoot_script.setter
    def shoot_script(self, shoot_script):
        """Sets the shoot_script of this LanguageCheckInfoReq.

        用户传来的剧本文本信息

        :param shoot_script: The shoot_script of this LanguageCheckInfoReq.
        :type shoot_script: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        self._shoot_script = shoot_script

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
        if not isinstance(other, LanguageCheckInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
