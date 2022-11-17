# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextDetectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'glossary_names': 'list[str]',
        'data': 'TextDetectionDataReq'
    }

    attribute_map = {
        'event_type': 'event_type',
        'glossary_names': 'glossary_names',
        'data': 'data'
    }

    def __init__(self, event_type=None, glossary_names=None, data=None):
        """TextDetectionReq

        The model defined in huaweicloud sdk

        :param event_type: 事件类型。  可选值如下：  nickname: 昵称  title: 标题  article: 帖⼦  comment: 评论  barrage: 弹幕  search: 搜索栏  profile: 个⼈简介
        :type event_type: str
        :param glossary_names: 检测时使用的自定义黑名单词库列表。
        :type glossary_names: list[str]
        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.TextDetectionDataReq`
        """
        
        

        self._event_type = None
        self._glossary_names = None
        self._data = None
        self.discriminator = None

        self.event_type = event_type
        if glossary_names is not None:
            self.glossary_names = glossary_names
        self.data = data

    @property
    def event_type(self):
        """Gets the event_type of this TextDetectionReq.

        事件类型。  可选值如下：  nickname: 昵称  title: 标题  article: 帖⼦  comment: 评论  barrage: 弹幕  search: 搜索栏  profile: 个⼈简介

        :return: The event_type of this TextDetectionReq.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this TextDetectionReq.

        事件类型。  可选值如下：  nickname: 昵称  title: 标题  article: 帖⼦  comment: 评论  barrage: 弹幕  search: 搜索栏  profile: 个⼈简介

        :param event_type: The event_type of this TextDetectionReq.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def glossary_names(self):
        """Gets the glossary_names of this TextDetectionReq.

        检测时使用的自定义黑名单词库列表。

        :return: The glossary_names of this TextDetectionReq.
        :rtype: list[str]
        """
        return self._glossary_names

    @glossary_names.setter
    def glossary_names(self, glossary_names):
        """Sets the glossary_names of this TextDetectionReq.

        检测时使用的自定义黑名单词库列表。

        :param glossary_names: The glossary_names of this TextDetectionReq.
        :type glossary_names: list[str]
        """
        self._glossary_names = glossary_names

    @property
    def data(self):
        """Gets the data of this TextDetectionReq.

        :return: The data of this TextDetectionReq.
        :rtype: :class:`huaweicloudsdkmoderation.v3.TextDetectionDataReq`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TextDetectionReq.

        :param data: The data of this TextDetectionReq.
        :type data: :class:`huaweicloudsdkmoderation.v3.TextDetectionDataReq`
        """
        self._data = data

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
        if not isinstance(other, TextDetectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
