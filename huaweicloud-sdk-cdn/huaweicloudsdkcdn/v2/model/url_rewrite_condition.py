# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlRewriteCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_type': 'str',
        'match_value': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'match_type': 'match_type',
        'match_value': 'match_value',
        'priority': 'priority'
    }

    def __init__(self, match_type=None, match_value=None, priority=None):
        r"""UrlRewriteCondition

        The model defined in huaweicloud sdk

        :param match_type: 匹配类型。   - catalog：指定目录下的文件需执行访问URL重写规则，   - full_path：某个完整路径下的文件需执行访问URL重写规则。
        :type match_type: str
        :param match_value: 匹配内容。当match_type为catalog时，为目录路径，输入要求以“/”作为首字符，以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。
        :type match_value: str
        :param priority: 访问URL重写规则的优先级。取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。
        :type priority: int
        """
        
        

        self._match_type = None
        self._match_value = None
        self._priority = None
        self.discriminator = None

        self.match_type = match_type
        self.match_value = match_value
        self.priority = priority

    @property
    def match_type(self):
        r"""Gets the match_type of this UrlRewriteCondition.

        匹配类型。   - catalog：指定目录下的文件需执行访问URL重写规则，   - full_path：某个完整路径下的文件需执行访问URL重写规则。

        :return: The match_type of this UrlRewriteCondition.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this UrlRewriteCondition.

        匹配类型。   - catalog：指定目录下的文件需执行访问URL重写规则，   - full_path：某个完整路径下的文件需执行访问URL重写规则。

        :param match_type: The match_type of this UrlRewriteCondition.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        r"""Gets the match_value of this UrlRewriteCondition.

        匹配内容。当match_type为catalog时，为目录路径，输入要求以“/”作为首字符，以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。

        :return: The match_value of this UrlRewriteCondition.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        r"""Sets the match_value of this UrlRewriteCondition.

        匹配内容。当match_type为catalog时，为目录路径，输入要求以“/”作为首字符，以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。 当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。

        :param match_value: The match_value of this UrlRewriteCondition.
        :type match_value: str
        """
        self._match_value = match_value

    @property
    def priority(self):
        r"""Gets the priority of this UrlRewriteCondition.

        访问URL重写规则的优先级。取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。

        :return: The priority of this UrlRewriteCondition.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UrlRewriteCondition.

        访问URL重写规则的优先级。取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。

        :param priority: The priority of this UrlRewriteCondition.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, UrlRewriteCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
