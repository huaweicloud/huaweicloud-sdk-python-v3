# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBatchSyncReqImageTextConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'black_glossary_names': 'list[str]',
        'white_glossary_names': 'list[str]'
    }

    attribute_map = {
        'black_glossary_names': 'black_glossary_names',
        'white_glossary_names': 'white_glossary_names'
    }

    def __init__(self, black_glossary_names=None, white_glossary_names=None):
        r"""ImageBatchSyncReqImageTextConfig

        The model defined in huaweicloud sdk

        :param black_glossary_names: 检测时使用的自定义黑名单词库列表。
        :type black_glossary_names: list[str]
        :param white_glossary_names: 检测时使用的自定义白名单词库列表。
        :type white_glossary_names: list[str]
        """
        
        

        self._black_glossary_names = None
        self._white_glossary_names = None
        self.discriminator = None

        if black_glossary_names is not None:
            self.black_glossary_names = black_glossary_names
        if white_glossary_names is not None:
            self.white_glossary_names = white_glossary_names

    @property
    def black_glossary_names(self):
        r"""Gets the black_glossary_names of this ImageBatchSyncReqImageTextConfig.

        检测时使用的自定义黑名单词库列表。

        :return: The black_glossary_names of this ImageBatchSyncReqImageTextConfig.
        :rtype: list[str]
        """
        return self._black_glossary_names

    @black_glossary_names.setter
    def black_glossary_names(self, black_glossary_names):
        r"""Sets the black_glossary_names of this ImageBatchSyncReqImageTextConfig.

        检测时使用的自定义黑名单词库列表。

        :param black_glossary_names: The black_glossary_names of this ImageBatchSyncReqImageTextConfig.
        :type black_glossary_names: list[str]
        """
        self._black_glossary_names = black_glossary_names

    @property
    def white_glossary_names(self):
        r"""Gets the white_glossary_names of this ImageBatchSyncReqImageTextConfig.

        检测时使用的自定义白名单词库列表。

        :return: The white_glossary_names of this ImageBatchSyncReqImageTextConfig.
        :rtype: list[str]
        """
        return self._white_glossary_names

    @white_glossary_names.setter
    def white_glossary_names(self, white_glossary_names):
        r"""Sets the white_glossary_names of this ImageBatchSyncReqImageTextConfig.

        检测时使用的自定义白名单词库列表。

        :param white_glossary_names: The white_glossary_names of this ImageBatchSyncReqImageTextConfig.
        :type white_glossary_names: list[str]
        """
        self._white_glossary_names = white_glossary_names

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
        if not isinstance(other, ImageBatchSyncReqImageTextConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
