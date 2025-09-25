# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoKillTransactionConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'usernames': 'list[str]',
        'threshold': 'int',
        'auto_stop': 'bool',
        'database_names': 'list[str]',
        'database_names_select': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'usernames': 'usernames',
        'threshold': 'threshold',
        'auto_stop': 'auto_stop',
        'database_names': 'database_names',
        'database_names_select': 'database_names_select'
    }

    def __init__(self, type=None, usernames=None, threshold=None, auto_stop=None, database_names=None, database_names_select=None):
        r"""ShowAutoKillTransactionConfigResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**: 配置类型。 **取值范围**: 不涉及。
        :type type: str
        :param usernames: **参数解释**: 筛选用户名。
        :type usernames: list[str]
        :param threshold: **参数解释**: 阈值。 **取值范围**: 不涉及。
        :type threshold: int
        :param auto_stop: **参数解释**: 配置是否开启。 **取值范围**: 不涉及。
        :type auto_stop: bool
        :param database_names: **参数解释**: 当前实例包含的所有数据库。
        :type database_names: list[str]
        :param database_names_select: **参数解释**: 筛选数据库名。
        :type database_names_select: list[str]
        """
        
        super(ShowAutoKillTransactionConfigResponse, self).__init__()

        self._type = None
        self._usernames = None
        self._threshold = None
        self._auto_stop = None
        self._database_names = None
        self._database_names_select = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if usernames is not None:
            self.usernames = usernames
        if threshold is not None:
            self.threshold = threshold
        if auto_stop is not None:
            self.auto_stop = auto_stop
        if database_names is not None:
            self.database_names = database_names
        if database_names_select is not None:
            self.database_names_select = database_names_select

    @property
    def type(self):
        r"""Gets the type of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 配置类型。 **取值范围**: 不涉及。

        :return: The type of this ShowAutoKillTransactionConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 配置类型。 **取值范围**: 不涉及。

        :param type: The type of this ShowAutoKillTransactionConfigResponse.
        :type type: str
        """
        self._type = type

    @property
    def usernames(self):
        r"""Gets the usernames of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 筛选用户名。

        :return: The usernames of this ShowAutoKillTransactionConfigResponse.
        :rtype: list[str]
        """
        return self._usernames

    @usernames.setter
    def usernames(self, usernames):
        r"""Sets the usernames of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 筛选用户名。

        :param usernames: The usernames of this ShowAutoKillTransactionConfigResponse.
        :type usernames: list[str]
        """
        self._usernames = usernames

    @property
    def threshold(self):
        r"""Gets the threshold of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 阈值。 **取值范围**: 不涉及。

        :return: The threshold of this ShowAutoKillTransactionConfigResponse.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 阈值。 **取值范围**: 不涉及。

        :param threshold: The threshold of this ShowAutoKillTransactionConfigResponse.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def auto_stop(self):
        r"""Gets the auto_stop of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 配置是否开启。 **取值范围**: 不涉及。

        :return: The auto_stop of this ShowAutoKillTransactionConfigResponse.
        :rtype: bool
        """
        return self._auto_stop

    @auto_stop.setter
    def auto_stop(self, auto_stop):
        r"""Sets the auto_stop of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 配置是否开启。 **取值范围**: 不涉及。

        :param auto_stop: The auto_stop of this ShowAutoKillTransactionConfigResponse.
        :type auto_stop: bool
        """
        self._auto_stop = auto_stop

    @property
    def database_names(self):
        r"""Gets the database_names of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 当前实例包含的所有数据库。

        :return: The database_names of this ShowAutoKillTransactionConfigResponse.
        :rtype: list[str]
        """
        return self._database_names

    @database_names.setter
    def database_names(self, database_names):
        r"""Sets the database_names of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 当前实例包含的所有数据库。

        :param database_names: The database_names of this ShowAutoKillTransactionConfigResponse.
        :type database_names: list[str]
        """
        self._database_names = database_names

    @property
    def database_names_select(self):
        r"""Gets the database_names_select of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 筛选数据库名。

        :return: The database_names_select of this ShowAutoKillTransactionConfigResponse.
        :rtype: list[str]
        """
        return self._database_names_select

    @database_names_select.setter
    def database_names_select(self, database_names_select):
        r"""Sets the database_names_select of this ShowAutoKillTransactionConfigResponse.

        **参数解释**: 筛选数据库名。

        :param database_names_select: The database_names_select of this ShowAutoKillTransactionConfigResponse.
        :type database_names_select: list[str]
        """
        self._database_names_select = database_names_select

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
        if not isinstance(other, ShowAutoKillTransactionConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
