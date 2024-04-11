# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BrowserCacheRulesCondition:

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
        """BrowserCacheRulesCondition

        The model defined in huaweicloud sdk

        :param match_type: 匹配类型:   - all：匹配所有文件，   - file_extension：按文件后缀匹配，   - catalog：按目录匹配，   - full_path：全路径匹配，   - home_page：按首页匹配。
        :type match_type: str
        :param match_value: 缓存匹配设置，当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。  当match_type为home_page时，为空。
        :type match_value: str
        :param priority: 浏览器缓存的优先级，取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。
        :type priority: int
        """
        
        

        self._match_type = None
        self._match_value = None
        self._priority = None
        self.discriminator = None

        self.match_type = match_type
        if match_value is not None:
            self.match_value = match_value
        self.priority = priority

    @property
    def match_type(self):
        """Gets the match_type of this BrowserCacheRulesCondition.

        匹配类型:   - all：匹配所有文件，   - file_extension：按文件后缀匹配，   - catalog：按目录匹配，   - full_path：全路径匹配，   - home_page：按首页匹配。

        :return: The match_type of this BrowserCacheRulesCondition.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this BrowserCacheRulesCondition.

        匹配类型:   - all：匹配所有文件，   - file_extension：按文件后缀匹配，   - catalog：按目录匹配，   - full_path：全路径匹配，   - home_page：按首页匹配。

        :param match_type: The match_type of this BrowserCacheRulesCondition.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        """Gets the match_value of this BrowserCacheRulesCondition.

        缓存匹配设置，当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。  当match_type为home_page时，为空。

        :return: The match_value of this BrowserCacheRulesCondition.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        """Sets the match_value of this BrowserCacheRulesCondition.

        缓存匹配设置，当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，单条全路径缓存规则里仅支持配置一个全路径，如/test/index.html或/test/\\*.jpg。  当match_type为home_page时，为空。

        :param match_value: The match_value of this BrowserCacheRulesCondition.
        :type match_value: str
        """
        self._match_value = match_value

    @property
    def priority(self):
        """Gets the priority of this BrowserCacheRulesCondition.

        浏览器缓存的优先级，取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。

        :return: The priority of this BrowserCacheRulesCondition.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BrowserCacheRulesCondition.

        浏览器缓存的优先级，取值为1-100之间的整数，数值越大优先级越高。优先级设置具有唯一性，不支持多条规则设置同一优先级，且优先级不能为空。

        :param priority: The priority of this BrowserCacheRulesCondition.
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
        if not isinstance(other, BrowserCacheRulesCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
