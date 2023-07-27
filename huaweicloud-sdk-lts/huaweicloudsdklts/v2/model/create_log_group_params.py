# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogGroupParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_name': 'str',
        'ttl_in_days': 'int',
        'tags': 'list[TagsBody]'
    }

    attribute_map = {
        'log_group_name': 'log_group_name',
        'ttl_in_days': 'ttl_in_days',
        'tags': 'tags'
    }

    def __init__(self, log_group_name=None, ttl_in_days=None, tags=None):
        """CreateLogGroupParams

        The model defined in huaweicloud sdk

        :param log_group_name: 需要创建的日志组名称。
        :type log_group_name: str
        :param ttl_in_days: 日志存储时间（天），取值范围：1-30。
        :type ttl_in_days: int
        :param tags: 标签字段信息
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        
        

        self._log_group_name = None
        self._ttl_in_days = None
        self._tags = None
        self.discriminator = None

        self.log_group_name = log_group_name
        self.ttl_in_days = ttl_in_days
        if tags is not None:
            self.tags = tags

    @property
    def log_group_name(self):
        """Gets the log_group_name of this CreateLogGroupParams.

        需要创建的日志组名称。

        :return: The log_group_name of this CreateLogGroupParams.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this CreateLogGroupParams.

        需要创建的日志组名称。

        :param log_group_name: The log_group_name of this CreateLogGroupParams.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def ttl_in_days(self):
        """Gets the ttl_in_days of this CreateLogGroupParams.

        日志存储时间（天），取值范围：1-30。

        :return: The ttl_in_days of this CreateLogGroupParams.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """Sets the ttl_in_days of this CreateLogGroupParams.

        日志存储时间（天），取值范围：1-30。

        :param ttl_in_days: The ttl_in_days of this CreateLogGroupParams.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def tags(self):
        """Gets the tags of this CreateLogGroupParams.

        标签字段信息

        :return: The tags of this CreateLogGroupParams.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateLogGroupParams.

        标签字段信息

        :param tags: The tags of this CreateLogGroupParams.
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
        if not isinstance(other, CreateLogGroupParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
