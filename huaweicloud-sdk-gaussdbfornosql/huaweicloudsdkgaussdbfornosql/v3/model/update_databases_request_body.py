# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabasesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'db_id': 'int'
    }

    attribute_map = {
        'action': 'action',
        'db_id': 'db_id'
    }

    def __init__(self, action=None, db_id=None):
        r"""UpdateDatabasesRequestBody

        The model defined in huaweicloud sdk

        :param action: 对实例的操作:  flush:清理数据
        :type action: str
        :param db_id: 指定需要清理的DB_ID,当action为flush时,才会生效。
        :type db_id: int
        """
        
        

        self._action = None
        self._db_id = None
        self.discriminator = None

        self.action = action
        if db_id is not None:
            self.db_id = db_id

    @property
    def action(self):
        r"""Gets the action of this UpdateDatabasesRequestBody.

        对实例的操作:  flush:清理数据

        :return: The action of this UpdateDatabasesRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateDatabasesRequestBody.

        对实例的操作:  flush:清理数据

        :param action: The action of this UpdateDatabasesRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def db_id(self):
        r"""Gets the db_id of this UpdateDatabasesRequestBody.

        指定需要清理的DB_ID,当action为flush时,才会生效。

        :return: The db_id of this UpdateDatabasesRequestBody.
        :rtype: int
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this UpdateDatabasesRequestBody.

        指定需要清理的DB_ID,当action为flush时,才会生效。

        :param db_id: The db_id of this UpdateDatabasesRequestBody.
        :type db_id: int
        """
        self._db_id = db_id

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
        if not isinstance(other, UpdateDatabasesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
