# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlserverDatabaseForDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'character_set': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'character_set': 'character_set',
        'state': 'state'
    }

    def __init__(self, name=None, character_set=None, state=None):
        r"""SqlserverDatabaseForDetail

        The model defined in huaweicloud sdk

        :param name: 数据库名称。
        :type name: str
        :param character_set: 数据库使用的字符集，例如Chinese_PRC_CI_AS等。
        :type character_set: str
        :param state: 数据库状态。取值如下:  Creating:表示创建中。 Running:表示使用中。 Deleting:表示删除中。 NotExists:表示不存在。
        :type state: str
        """
        
        

        self._name = None
        self._character_set = None
        self._state = None
        self.discriminator = None

        self.name = name
        self.character_set = character_set
        self.state = state

    @property
    def name(self):
        r"""Gets the name of this SqlserverDatabaseForDetail.

        数据库名称。

        :return: The name of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SqlserverDatabaseForDetail.

        数据库名称。

        :param name: The name of this SqlserverDatabaseForDetail.
        :type name: str
        """
        self._name = name

    @property
    def character_set(self):
        r"""Gets the character_set of this SqlserverDatabaseForDetail.

        数据库使用的字符集，例如Chinese_PRC_CI_AS等。

        :return: The character_set of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        r"""Sets the character_set of this SqlserverDatabaseForDetail.

        数据库使用的字符集，例如Chinese_PRC_CI_AS等。

        :param character_set: The character_set of this SqlserverDatabaseForDetail.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def state(self):
        r"""Gets the state of this SqlserverDatabaseForDetail.

        数据库状态。取值如下:  Creating:表示创建中。 Running:表示使用中。 Deleting:表示删除中。 NotExists:表示不存在。

        :return: The state of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SqlserverDatabaseForDetail.

        数据库状态。取值如下:  Creating:表示创建中。 Running:表示使用中。 Deleting:表示删除中。 NotExists:表示不存在。

        :param state: The state of this SqlserverDatabaseForDetail.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, SqlserverDatabaseForDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
