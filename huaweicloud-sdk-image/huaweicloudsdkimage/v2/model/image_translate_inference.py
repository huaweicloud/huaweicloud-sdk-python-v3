# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageTranslateInference:

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
        'rewrite': 'str'
    }

    attribute_map = {
        'target_language': 'target_language',
        'rewrite': 'rewrite'
    }

    def __init__(self, target_language=None, rewrite=None):
        """ImageTranslateInference

        The model defined in huaweicloud sdk

        :param target_language: 文本翻译目标语言，支持中文（“zh”）、翻译中文（“zh-tw”）、英语（“en”）、日语（“ja”）、泰语（“th”）、阿拉伯语（“ar”）、韩语（“ko”）
        :type target_language: str
        :param rewrite: 是否回写，默认为是
        :type rewrite: str
        """
        
        

        self._target_language = None
        self._rewrite = None
        self.discriminator = None

        self.target_language = target_language
        if rewrite is not None:
            self.rewrite = rewrite

    @property
    def target_language(self):
        """Gets the target_language of this ImageTranslateInference.

        文本翻译目标语言，支持中文（“zh”）、翻译中文（“zh-tw”）、英语（“en”）、日语（“ja”）、泰语（“th”）、阿拉伯语（“ar”）、韩语（“ko”）

        :return: The target_language of this ImageTranslateInference.
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this ImageTranslateInference.

        文本翻译目标语言，支持中文（“zh”）、翻译中文（“zh-tw”）、英语（“en”）、日语（“ja”）、泰语（“th”）、阿拉伯语（“ar”）、韩语（“ko”）

        :param target_language: The target_language of this ImageTranslateInference.
        :type target_language: str
        """
        self._target_language = target_language

    @property
    def rewrite(self):
        """Gets the rewrite of this ImageTranslateInference.

        是否回写，默认为是

        :return: The rewrite of this ImageTranslateInference.
        :rtype: str
        """
        return self._rewrite

    @rewrite.setter
    def rewrite(self, rewrite):
        """Sets the rewrite of this ImageTranslateInference.

        是否回写，默认为是

        :param rewrite: The rewrite of this ImageTranslateInference.
        :type rewrite: str
        """
        self._rewrite = rewrite

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
        if not isinstance(other, ImageTranslateInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
