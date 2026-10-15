# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChapterConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'sub_chapters': 'dict(str, bool)'
    }

    attribute_map = {
        'enabled': 'enabled',
        'sub_chapters': 'sub_chapters'
    }

    def __init__(self, enabled=None, sub_chapters=None):
        r"""ChapterConfigReq

        The model defined in huaweicloud sdk

        :param enabled: 是否启用该章节。BASIC_INFO章节始终为true。
        :type enabled: bool
        :param sub_chapters: 子章节配置，key为子章节编码，value为是否启用。无子章节的章节可不传此字段。
        :type sub_chapters: dict(str, bool)
        """
        
        

        self._enabled = None
        self._sub_chapters = None
        self.discriminator = None

        self.enabled = enabled
        if sub_chapters is not None:
            self.sub_chapters = sub_chapters

    @property
    def enabled(self):
        r"""Gets the enabled of this ChapterConfigReq.

        是否启用该章节。BASIC_INFO章节始终为true。

        :return: The enabled of this ChapterConfigReq.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ChapterConfigReq.

        是否启用该章节。BASIC_INFO章节始终为true。

        :param enabled: The enabled of this ChapterConfigReq.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def sub_chapters(self):
        r"""Gets the sub_chapters of this ChapterConfigReq.

        子章节配置，key为子章节编码，value为是否启用。无子章节的章节可不传此字段。

        :return: The sub_chapters of this ChapterConfigReq.
        :rtype: dict(str, bool)
        """
        return self._sub_chapters

    @sub_chapters.setter
    def sub_chapters(self, sub_chapters):
        r"""Sets the sub_chapters of this ChapterConfigReq.

        子章节配置，key为子章节编码，value为是否启用。无子章节的章节可不传此字段。

        :param sub_chapters: The sub_chapters of this ChapterConfigReq.
        :type sub_chapters: dict(str, bool)
        """
        self._sub_chapters = sub_chapters

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChapterConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
