# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpWelfareInfoResponseInfoHotInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'url_json': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url_json': 'url_json'
    }

    def __init__(self, title=None, url_json=None):
        r"""HttpWelfareInfoResponseInfoHotInfo

        The model defined in huaweicloud sdk

        :param title: **参数解释**: 热点事件标题 **取值范围**: 字符长度1-256 
        :type title: str
        :param url_json: **参数解释**: 热点事件链接，包括中国站，国际站欧洲站，由console根据不同的场景选择跳转 **取值范围**: 字符长度0-65535 
        :type url_json: str
        """
        
        

        self._title = None
        self._url_json = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if url_json is not None:
            self.url_json = url_json

    @property
    def title(self):
        r"""Gets the title of this HttpWelfareInfoResponseInfoHotInfo.

        **参数解释**: 热点事件标题 **取值范围**: 字符长度1-256 

        :return: The title of this HttpWelfareInfoResponseInfoHotInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this HttpWelfareInfoResponseInfoHotInfo.

        **参数解释**: 热点事件标题 **取值范围**: 字符长度1-256 

        :param title: The title of this HttpWelfareInfoResponseInfoHotInfo.
        :type title: str
        """
        self._title = title

    @property
    def url_json(self):
        r"""Gets the url_json of this HttpWelfareInfoResponseInfoHotInfo.

        **参数解释**: 热点事件链接，包括中国站，国际站欧洲站，由console根据不同的场景选择跳转 **取值范围**: 字符长度0-65535 

        :return: The url_json of this HttpWelfareInfoResponseInfoHotInfo.
        :rtype: str
        """
        return self._url_json

    @url_json.setter
    def url_json(self, url_json):
        r"""Sets the url_json of this HttpWelfareInfoResponseInfoHotInfo.

        **参数解释**: 热点事件链接，包括中国站，国际站欧洲站，由console根据不同的场景选择跳转 **取值范围**: 字符长度0-65535 

        :param url_json: The url_json of this HttpWelfareInfoResponseInfoHotInfo.
        :type url_json: str
        """
        self._url_json = url_json

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
        if not isinstance(other, HttpWelfareInfoResponseInfoHotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
