# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogStreamParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ttl_in_days': 'int',
        'tags': 'list[TagsBody]'
    }

    attribute_map = {
        'ttl_in_days': 'ttl_in_days',
        'tags': 'tags'
    }

    def __init__(self, ttl_in_days=None, tags=None):
        """UpdateLogStreamParams

        The model defined in huaweicloud sdk

        :param ttl_in_days: 日志存储时间（天）。   该参数仅对华东-上海一、华北-北京四、华南-广州用户开放。
        :type ttl_in_days: int
        :param tags: 标签字段信息
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        
        

        self._ttl_in_days = None
        self._tags = None
        self.discriminator = None

        self.ttl_in_days = ttl_in_days
        if tags is not None:
            self.tags = tags

    @property
    def ttl_in_days(self):
        """Gets the ttl_in_days of this UpdateLogStreamParams.

        日志存储时间（天）。   该参数仅对华东-上海一、华北-北京四、华南-广州用户开放。

        :return: The ttl_in_days of this UpdateLogStreamParams.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """Sets the ttl_in_days of this UpdateLogStreamParams.

        日志存储时间（天）。   该参数仅对华东-上海一、华北-北京四、华南-广州用户开放。

        :param ttl_in_days: The ttl_in_days of this UpdateLogStreamParams.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def tags(self):
        """Gets the tags of this UpdateLogStreamParams.

        标签字段信息

        :return: The tags of this UpdateLogStreamParams.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateLogStreamParams.

        标签字段信息

        :param tags: The tags of this UpdateLogStreamParams.
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateLogStreamParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
