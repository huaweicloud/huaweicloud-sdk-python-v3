# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MuteRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'desc': 'str',
        'match': 'list[list[Match]]',
        'mute_config': 'MuteConfig',
        'name': 'str',
        'timezone': 'str',
        'update_time': 'int',
        'user_id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'desc': 'desc',
        'match': 'match',
        'mute_config': 'mute_config',
        'name': 'name',
        'timezone': 'timezone',
        'update_time': 'update_time',
        'user_id': 'user_id'
    }

    def __init__(self, create_time=None, desc=None, match=None, mute_config=None, name=None, timezone=None, update_time=None, user_id=None):
        """MuteRule

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: int
        :param desc: 规则描述
        :type desc: str
        :param match: 规则的匹配条件。串行条件和并行条件的最大数量限制为10。
        :type match: list[list[Match]]
        :param mute_config: 
        :type mute_config: :class:`huaweicloudsdkaom.v2.MuteConfig`
        :param name: 规则名称。名称包含大小写字母、数字、特殊字符（_）、不能以下划线开头或结尾，最大长度为100。
        :type name: str
        :param timezone: 时区
        :type timezone: str
        :param update_time: 修改时间
        :type update_time: int
        :param user_id: 用户ID
        :type user_id: str
        """
        
        

        self._create_time = None
        self._desc = None
        self._match = None
        self._mute_config = None
        self._name = None
        self._timezone = None
        self._update_time = None
        self._user_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if desc is not None:
            self.desc = desc
        self.match = match
        self.mute_config = mute_config
        self.name = name
        self.timezone = timezone
        if update_time is not None:
            self.update_time = update_time
        if user_id is not None:
            self.user_id = user_id

    @property
    def create_time(self):
        """Gets the create_time of this MuteRule.

        创建时间

        :return: The create_time of this MuteRule.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this MuteRule.

        创建时间

        :param create_time: The create_time of this MuteRule.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def desc(self):
        """Gets the desc of this MuteRule.

        规则描述

        :return: The desc of this MuteRule.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this MuteRule.

        规则描述

        :param desc: The desc of this MuteRule.
        :type desc: str
        """
        self._desc = desc

    @property
    def match(self):
        """Gets the match of this MuteRule.

        规则的匹配条件。串行条件和并行条件的最大数量限制为10。

        :return: The match of this MuteRule.
        :rtype: list[list[Match]]
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this MuteRule.

        规则的匹配条件。串行条件和并行条件的最大数量限制为10。

        :param match: The match of this MuteRule.
        :type match: list[list[Match]]
        """
        self._match = match

    @property
    def mute_config(self):
        """Gets the mute_config of this MuteRule.

        :return: The mute_config of this MuteRule.
        :rtype: :class:`huaweicloudsdkaom.v2.MuteConfig`
        """
        return self._mute_config

    @mute_config.setter
    def mute_config(self, mute_config):
        """Sets the mute_config of this MuteRule.

        :param mute_config: The mute_config of this MuteRule.
        :type mute_config: :class:`huaweicloudsdkaom.v2.MuteConfig`
        """
        self._mute_config = mute_config

    @property
    def name(self):
        """Gets the name of this MuteRule.

        规则名称。名称包含大小写字母、数字、特殊字符（_）、不能以下划线开头或结尾，最大长度为100。

        :return: The name of this MuteRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MuteRule.

        规则名称。名称包含大小写字母、数字、特殊字符（_）、不能以下划线开头或结尾，最大长度为100。

        :param name: The name of this MuteRule.
        :type name: str
        """
        self._name = name

    @property
    def timezone(self):
        """Gets the timezone of this MuteRule.

        时区

        :return: The timezone of this MuteRule.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this MuteRule.

        时区

        :param timezone: The timezone of this MuteRule.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def update_time(self):
        """Gets the update_time of this MuteRule.

        修改时间

        :return: The update_time of this MuteRule.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this MuteRule.

        修改时间

        :param update_time: The update_time of this MuteRule.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def user_id(self):
        """Gets the user_id of this MuteRule.

        用户ID

        :return: The user_id of this MuteRule.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MuteRule.

        用户ID

        :param user_id: The user_id of this MuteRule.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, MuteRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
