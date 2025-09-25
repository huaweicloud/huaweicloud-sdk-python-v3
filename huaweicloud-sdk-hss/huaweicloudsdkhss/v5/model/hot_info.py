# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotInfo:

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
        'update_time': 'int',
        'severity_level': 'str'
    }

    attribute_map = {
        'title': 'title',
        'update_time': 'update_time',
        'severity_level': 'severity_level'
    }

    def __init__(self, title=None, update_time=None, severity_level=None):
        r"""HotInfo

        The model defined in huaweicloud sdk

        :param title: **参数解释**: 标题 **取值范围**: 字符长度0-256位 
        :type title: str
        :param update_time: **参数解释**: 更新时间 **取值范围**: 最小值0，最大值4071095999000 
        :type update_time: int
        :param severity_level: **参数解释**: 级别 **取值范围**: 字符长度0-32位 
        :type severity_level: str
        """
        
        

        self._title = None
        self._update_time = None
        self._severity_level = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if update_time is not None:
            self.update_time = update_time
        if severity_level is not None:
            self.severity_level = severity_level

    @property
    def title(self):
        r"""Gets the title of this HotInfo.

        **参数解释**: 标题 **取值范围**: 字符长度0-256位 

        :return: The title of this HotInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this HotInfo.

        **参数解释**: 标题 **取值范围**: 字符长度0-256位 

        :param title: The title of this HotInfo.
        :type title: str
        """
        self._title = title

    @property
    def update_time(self):
        r"""Gets the update_time of this HotInfo.

        **参数解释**: 更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :return: The update_time of this HotInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this HotInfo.

        **参数解释**: 更新时间 **取值范围**: 最小值0，最大值4071095999000 

        :param update_time: The update_time of this HotInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def severity_level(self):
        r"""Gets the severity_level of this HotInfo.

        **参数解释**: 级别 **取值范围**: 字符长度0-32位 

        :return: The severity_level of this HotInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this HotInfo.

        **参数解释**: 级别 **取值范围**: 字符长度0-32位 

        :param severity_level: The severity_level of this HotInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

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
        if not isinstance(other, HotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
