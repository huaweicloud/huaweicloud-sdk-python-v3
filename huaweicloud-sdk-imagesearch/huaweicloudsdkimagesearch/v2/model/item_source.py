# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desc': 'str',
        'custom_tags': 'dict(str, str)',
        'custom_num_tags': 'dict(str, float)',
        'keywords': 'list[str]'
    }

    attribute_map = {
        'desc': 'desc',
        'custom_tags': 'custom_tags',
        'custom_num_tags': 'custom_num_tags',
        'keywords': 'keywords'
    }

    def __init__(self, desc=None, custom_tags=None, custom_num_tags=None, keywords=None):
        r"""ItemSource

        The model defined in huaweicloud sdk

        :param desc: 数据描述信息。
        :type desc: str
        :param custom_tags: 数据自定义字符标签。
        :type custom_tags: dict(str, str)
        :param custom_num_tags: 数据自定义数值标签。
        :type custom_num_tags: dict(str, float)
        :param keywords: 数据关键词列表。
        :type keywords: list[str]
        """
        
        

        self._desc = None
        self._custom_tags = None
        self._custom_num_tags = None
        self._keywords = None
        self.discriminator = None

        if desc is not None:
            self.desc = desc
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_num_tags is not None:
            self.custom_num_tags = custom_num_tags
        if keywords is not None:
            self.keywords = keywords

    @property
    def desc(self):
        r"""Gets the desc of this ItemSource.

        数据描述信息。

        :return: The desc of this ItemSource.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ItemSource.

        数据描述信息。

        :param desc: The desc of this ItemSource.
        :type desc: str
        """
        self._desc = desc

    @property
    def custom_tags(self):
        r"""Gets the custom_tags of this ItemSource.

        数据自定义字符标签。

        :return: The custom_tags of this ItemSource.
        :rtype: dict(str, str)
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        r"""Sets the custom_tags of this ItemSource.

        数据自定义字符标签。

        :param custom_tags: The custom_tags of this ItemSource.
        :type custom_tags: dict(str, str)
        """
        self._custom_tags = custom_tags

    @property
    def custom_num_tags(self):
        r"""Gets the custom_num_tags of this ItemSource.

        数据自定义数值标签。

        :return: The custom_num_tags of this ItemSource.
        :rtype: dict(str, float)
        """
        return self._custom_num_tags

    @custom_num_tags.setter
    def custom_num_tags(self, custom_num_tags):
        r"""Sets the custom_num_tags of this ItemSource.

        数据自定义数值标签。

        :param custom_num_tags: The custom_num_tags of this ItemSource.
        :type custom_num_tags: dict(str, float)
        """
        self._custom_num_tags = custom_num_tags

    @property
    def keywords(self):
        r"""Gets the keywords of this ItemSource.

        数据关键词列表。

        :return: The keywords of this ItemSource.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ItemSource.

        数据关键词列表。

        :param keywords: The keywords of this ItemSource.
        :type keywords: list[str]
        """
        self._keywords = keywords

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
        if not isinstance(other, ItemSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
