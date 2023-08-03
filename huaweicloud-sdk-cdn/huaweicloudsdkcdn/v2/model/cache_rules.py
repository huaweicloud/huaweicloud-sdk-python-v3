# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheRules:

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
        'ttl': 'int',
        'ttl_unit': 'str',
        'priority': 'int',
        'follow_origin': 'str',
        'url_parameter_type': 'str',
        'url_parameter_value': 'str'
    }

    attribute_map = {
        'match_type': 'match_type',
        'match_value': 'match_value',
        'ttl': 'ttl',
        'ttl_unit': 'ttl_unit',
        'priority': 'priority',
        'follow_origin': 'follow_origin',
        'url_parameter_type': 'url_parameter_type',
        'url_parameter_value': 'url_parameter_value'
    }

    def __init__(self, match_type=None, match_value=None, ttl=None, ttl_unit=None, priority=None, follow_origin=None, url_parameter_type=None, url_parameter_value=None):
        """CacheRules

        The model defined in huaweicloud sdk

        :param match_type: 匹配类型: - all：匹配所有文件， - file_extension：按文件后缀匹配， - catalog：按目录匹配， - full_path：全路径匹配， - home_page：按首页匹配。   &gt; 配置单条缓存规则时，可不传，默认为all。   &gt; 配置多条缓存规则时，此参数必传。
        :type match_type: str
        :param match_value: 缓存匹配设置， 当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件， 如/test/index.html,/test/\\*.jpg。 当match_type为home_page时，为空。
        :type match_value: str
        :param ttl: 缓存过期时间，最大支持365天。  &gt; 默认值为0。
        :type ttl: int
        :param ttl_unit: 缓存过期时间单位，s：秒；m：分；h：小时；d：天。
        :type ttl_unit: str
        :param priority: 此条缓存规则的优先级, 默认值1，数值越大，优先级越高，取值范围为1-100，优先级不能相同。
        :type priority: int
        :param follow_origin: 缓存遵循源站开关，on：打开，off：关闭。  &gt; 默认值为off。
        :type follow_origin: str
        :param url_parameter_type: URL参数： - del_params：忽略指定URL参数， - reserve_params：保留指定URL参数， - ignore_url_params：忽略全部URL参数， - full_url：使用完整URL参数。   &gt; 不传此参数时，默认为full_url。
        :type url_parameter_type: str
        :param url_parameter_value: URL参数值，最多设置10条，以\&quot;,\&quot;分隔。  &gt; 当url_parameter_type为del_params或reserve_params时必填。
        :type url_parameter_value: str
        """
        
        

        self._match_type = None
        self._match_value = None
        self._ttl = None
        self._ttl_unit = None
        self._priority = None
        self._follow_origin = None
        self._url_parameter_type = None
        self._url_parameter_value = None
        self.discriminator = None

        if match_type is not None:
            self.match_type = match_type
        if match_value is not None:
            self.match_value = match_value
        if ttl is not None:
            self.ttl = ttl
        self.ttl_unit = ttl_unit
        self.priority = priority
        if follow_origin is not None:
            self.follow_origin = follow_origin
        if url_parameter_type is not None:
            self.url_parameter_type = url_parameter_type
        if url_parameter_value is not None:
            self.url_parameter_value = url_parameter_value

    @property
    def match_type(self):
        """Gets the match_type of this CacheRules.

        匹配类型: - all：匹配所有文件， - file_extension：按文件后缀匹配， - catalog：按目录匹配， - full_path：全路径匹配， - home_page：按首页匹配。   > 配置单条缓存规则时，可不传，默认为all。   > 配置多条缓存规则时，此参数必传。

        :return: The match_type of this CacheRules.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this CacheRules.

        匹配类型: - all：匹配所有文件， - file_extension：按文件后缀匹配， - catalog：按目录匹配， - full_path：全路径匹配， - home_page：按首页匹配。   > 配置单条缓存规则时，可不传，默认为all。   > 配置多条缓存规则时，此参数必传。

        :param match_type: The match_type of this CacheRules.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_value(self):
        """Gets the match_value of this CacheRules.

        缓存匹配设置， 当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件， 如/test/index.html,/test/\\*.jpg。 当match_type为home_page时，为空。

        :return: The match_value of this CacheRules.
        :rtype: str
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        """Sets the match_value of this CacheRules.

        缓存匹配设置， 当match_type为all时，为空。当match_type为file_extension时，为文件后缀，输入首字符为“.”，以“,”进行分隔， 如.jpg,.zip,.exe，并且输入的文 件名后缀总数不超过20个。 当match_type为catalog时，为目录，输入要求以“/”作为首字符， 以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过20个。  当match_type为full_path时，为全路径，输入要求以“/”作为首字符，支持匹配指定目录下的具体文件，或者带通配符“\\*”的文件， 如/test/index.html,/test/\\*.jpg。 当match_type为home_page时，为空。

        :param match_value: The match_value of this CacheRules.
        :type match_value: str
        """
        self._match_value = match_value

    @property
    def ttl(self):
        """Gets the ttl of this CacheRules.

        缓存过期时间，最大支持365天。  > 默认值为0。

        :return: The ttl of this CacheRules.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CacheRules.

        缓存过期时间，最大支持365天。  > 默认值为0。

        :param ttl: The ttl of this CacheRules.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_unit(self):
        """Gets the ttl_unit of this CacheRules.

        缓存过期时间单位，s：秒；m：分；h：小时；d：天。

        :return: The ttl_unit of this CacheRules.
        :rtype: str
        """
        return self._ttl_unit

    @ttl_unit.setter
    def ttl_unit(self, ttl_unit):
        """Sets the ttl_unit of this CacheRules.

        缓存过期时间单位，s：秒；m：分；h：小时；d：天。

        :param ttl_unit: The ttl_unit of this CacheRules.
        :type ttl_unit: str
        """
        self._ttl_unit = ttl_unit

    @property
    def priority(self):
        """Gets the priority of this CacheRules.

        此条缓存规则的优先级, 默认值1，数值越大，优先级越高，取值范围为1-100，优先级不能相同。

        :return: The priority of this CacheRules.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CacheRules.

        此条缓存规则的优先级, 默认值1，数值越大，优先级越高，取值范围为1-100，优先级不能相同。

        :param priority: The priority of this CacheRules.
        :type priority: int
        """
        self._priority = priority

    @property
    def follow_origin(self):
        """Gets the follow_origin of this CacheRules.

        缓存遵循源站开关，on：打开，off：关闭。  > 默认值为off。

        :return: The follow_origin of this CacheRules.
        :rtype: str
        """
        return self._follow_origin

    @follow_origin.setter
    def follow_origin(self, follow_origin):
        """Sets the follow_origin of this CacheRules.

        缓存遵循源站开关，on：打开，off：关闭。  > 默认值为off。

        :param follow_origin: The follow_origin of this CacheRules.
        :type follow_origin: str
        """
        self._follow_origin = follow_origin

    @property
    def url_parameter_type(self):
        """Gets the url_parameter_type of this CacheRules.

        URL参数： - del_params：忽略指定URL参数， - reserve_params：保留指定URL参数， - ignore_url_params：忽略全部URL参数， - full_url：使用完整URL参数。   > 不传此参数时，默认为full_url。

        :return: The url_parameter_type of this CacheRules.
        :rtype: str
        """
        return self._url_parameter_type

    @url_parameter_type.setter
    def url_parameter_type(self, url_parameter_type):
        """Sets the url_parameter_type of this CacheRules.

        URL参数： - del_params：忽略指定URL参数， - reserve_params：保留指定URL参数， - ignore_url_params：忽略全部URL参数， - full_url：使用完整URL参数。   > 不传此参数时，默认为full_url。

        :param url_parameter_type: The url_parameter_type of this CacheRules.
        :type url_parameter_type: str
        """
        self._url_parameter_type = url_parameter_type

    @property
    def url_parameter_value(self):
        """Gets the url_parameter_value of this CacheRules.

        URL参数值，最多设置10条，以\",\"分隔。  > 当url_parameter_type为del_params或reserve_params时必填。

        :return: The url_parameter_value of this CacheRules.
        :rtype: str
        """
        return self._url_parameter_value

    @url_parameter_value.setter
    def url_parameter_value(self, url_parameter_value):
        """Sets the url_parameter_value of this CacheRules.

        URL参数值，最多设置10条，以\",\"分隔。  > 当url_parameter_type为del_params或reserve_params时必填。

        :param url_parameter_value: The url_parameter_value of this CacheRules.
        :type url_parameter_value: str
        """
        self._url_parameter_value = url_parameter_value

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
        if not isinstance(other, CacheRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
