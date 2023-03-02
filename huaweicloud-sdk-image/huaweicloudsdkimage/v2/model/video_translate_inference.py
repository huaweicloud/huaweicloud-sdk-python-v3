# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoTranslateInference:

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
        'rewrite': 'str',
        'rewrite_config': 'VideoTranslateInferenceRewriteConfig'
    }

    attribute_map = {
        'target_language': 'target_language',
        'rewrite': 'rewrite',
        'rewrite_config': 'rewrite_config'
    }

    def __init__(self, target_language=None, rewrite=None, rewrite_config=None):
        """VideoTranslateInference

        The model defined in huaweicloud sdk

        :param target_language: 字幕翻译目标语言
        :type target_language: str
        :param rewrite: 是否回写
        :type rewrite: str
        :param rewrite_config: 
        :type rewrite_config: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfig`
        """
        
        

        self._target_language = None
        self._rewrite = None
        self._rewrite_config = None
        self.discriminator = None

        self.target_language = target_language
        if rewrite is not None:
            self.rewrite = rewrite
        if rewrite_config is not None:
            self.rewrite_config = rewrite_config

    @property
    def target_language(self):
        """Gets the target_language of this VideoTranslateInference.

        字幕翻译目标语言

        :return: The target_language of this VideoTranslateInference.
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this VideoTranslateInference.

        字幕翻译目标语言

        :param target_language: The target_language of this VideoTranslateInference.
        :type target_language: str
        """
        self._target_language = target_language

    @property
    def rewrite(self):
        """Gets the rewrite of this VideoTranslateInference.

        是否回写

        :return: The rewrite of this VideoTranslateInference.
        :rtype: str
        """
        return self._rewrite

    @rewrite.setter
    def rewrite(self, rewrite):
        """Sets the rewrite of this VideoTranslateInference.

        是否回写

        :param rewrite: The rewrite of this VideoTranslateInference.
        :type rewrite: str
        """
        self._rewrite = rewrite

    @property
    def rewrite_config(self):
        """Gets the rewrite_config of this VideoTranslateInference.

        :return: The rewrite_config of this VideoTranslateInference.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfig`
        """
        return self._rewrite_config

    @rewrite_config.setter
    def rewrite_config(self, rewrite_config):
        """Sets the rewrite_config of this VideoTranslateInference.

        :param rewrite_config: The rewrite_config of this VideoTranslateInference.
        :type rewrite_config: :class:`huaweicloudsdkimage.v2.VideoTranslateInferenceRewriteConfig`
        """
        self._rewrite_config = rewrite_config

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
        if not isinstance(other, VideoTranslateInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
