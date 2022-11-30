# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'int',
        'content': 'str',
        'ttl': 'int',
        'ttl_type': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'content': 'content',
        'ttl': 'ttl',
        'ttl_type': 'ttl_type',
        'priority': 'priority'
    }

    def __init__(self, rule_type=None, content=None, ttl=None, ttl_type=None, priority=None):
        """Rules

        The model defined in huaweicloud sdk

        :param rule_type: 0：全部类型，表示匹配所有文件，默认值。  1：文件类型，表示按文件后缀匹配。  2：文件夹类型，表示按目录匹配。  3：文件全路径类型，表示按文件全路径匹配。
        :type rule_type: int
        :param content: 缓存匹配设置。  当rule_type为0时，为空。  当rule_type为1时，为文件后缀，输入首字符为“.”，以“;”进行分隔，如.jpg;.zip;.exe，并且输入的文件名后缀总数不超过20个。 当rule_type为2时，为目录，输入要求以“/”作为首字符，以“;”进行分隔，如/test/folder01;/test/folder02，并且输入的目录路径总数不超过20个。 当rule_type为3时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，如/test/index.html或/test/\\*.jpg。
        :type content: str
        :param ttl: 缓存时间。最大支持365天。
        :type ttl: int
        :param ttl_type: 缓存时间单位。1：秒；2：分；3：小时；4：天。
        :type ttl_type: int
        :param priority: 此条配置的权重值, 默认值1，数值越大，优先级越高。取值范围为1-100，权重值不能相同。
        :type priority: int
        """
        
        

        self._rule_type = None
        self._content = None
        self._ttl = None
        self._ttl_type = None
        self._priority = None
        self.discriminator = None

        self.rule_type = rule_type
        if content is not None:
            self.content = content
        self.ttl = ttl
        self.ttl_type = ttl_type
        self.priority = priority

    @property
    def rule_type(self):
        """Gets the rule_type of this Rules.

        0：全部类型，表示匹配所有文件，默认值。  1：文件类型，表示按文件后缀匹配。  2：文件夹类型，表示按目录匹配。  3：文件全路径类型，表示按文件全路径匹配。

        :return: The rule_type of this Rules.
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this Rules.

        0：全部类型，表示匹配所有文件，默认值。  1：文件类型，表示按文件后缀匹配。  2：文件夹类型，表示按目录匹配。  3：文件全路径类型，表示按文件全路径匹配。

        :param rule_type: The rule_type of this Rules.
        :type rule_type: int
        """
        self._rule_type = rule_type

    @property
    def content(self):
        """Gets the content of this Rules.

        缓存匹配设置。  当rule_type为0时，为空。  当rule_type为1时，为文件后缀，输入首字符为“.”，以“;”进行分隔，如.jpg;.zip;.exe，并且输入的文件名后缀总数不超过20个。 当rule_type为2时，为目录，输入要求以“/”作为首字符，以“;”进行分隔，如/test/folder01;/test/folder02，并且输入的目录路径总数不超过20个。 当rule_type为3时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，如/test/index.html或/test/\\*.jpg。

        :return: The content of this Rules.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Rules.

        缓存匹配设置。  当rule_type为0时，为空。  当rule_type为1时，为文件后缀，输入首字符为“.”，以“;”进行分隔，如.jpg;.zip;.exe，并且输入的文件名后缀总数不超过20个。 当rule_type为2时，为目录，输入要求以“/”作为首字符，以“;”进行分隔，如/test/folder01;/test/folder02，并且输入的目录路径总数不超过20个。 当rule_type为3时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件，如/test/index.html或/test/\\*.jpg。

        :param content: The content of this Rules.
        :type content: str
        """
        self._content = content

    @property
    def ttl(self):
        """Gets the ttl of this Rules.

        缓存时间。最大支持365天。

        :return: The ttl of this Rules.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Rules.

        缓存时间。最大支持365天。

        :param ttl: The ttl of this Rules.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_type(self):
        """Gets the ttl_type of this Rules.

        缓存时间单位。1：秒；2：分；3：小时；4：天。

        :return: The ttl_type of this Rules.
        :rtype: int
        """
        return self._ttl_type

    @ttl_type.setter
    def ttl_type(self, ttl_type):
        """Sets the ttl_type of this Rules.

        缓存时间单位。1：秒；2：分；3：小时；4：天。

        :param ttl_type: The ttl_type of this Rules.
        :type ttl_type: int
        """
        self._ttl_type = ttl_type

    @property
    def priority(self):
        """Gets the priority of this Rules.

        此条配置的权重值, 默认值1，数值越大，优先级越高。取值范围为1-100，权重值不能相同。

        :return: The priority of this Rules.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Rules.

        此条配置的权重值, 默认值1，数值越大，优先级越高。取值范围为1-100，权重值不能相同。

        :param priority: The priority of this Rules.
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
        if not isinstance(other, Rules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
