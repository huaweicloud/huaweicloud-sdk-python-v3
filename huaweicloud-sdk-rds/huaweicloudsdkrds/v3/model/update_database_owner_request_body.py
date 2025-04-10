# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseOwnerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'database': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'database': 'database'
    }

    def __init__(self, owner=None, database=None):
        r"""UpdateDatabaseOwnerRequestBody

        The model defined in huaweicloud sdk

        :param owner: 修改后数据库owner
        :type owner: str
        :param database: 数据库名称
        :type database: str
        """
        
        

        self._owner = None
        self._database = None
        self.discriminator = None

        self.owner = owner
        self.database = database

    @property
    def owner(self):
        r"""Gets the owner of this UpdateDatabaseOwnerRequestBody.

        修改后数据库owner

        :return: The owner of this UpdateDatabaseOwnerRequestBody.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this UpdateDatabaseOwnerRequestBody.

        修改后数据库owner

        :param owner: The owner of this UpdateDatabaseOwnerRequestBody.
        :type owner: str
        """
        self._owner = owner

    @property
    def database(self):
        r"""Gets the database of this UpdateDatabaseOwnerRequestBody.

        数据库名称

        :return: The database of this UpdateDatabaseOwnerRequestBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this UpdateDatabaseOwnerRequestBody.

        数据库名称

        :param database: The database of this UpdateDatabaseOwnerRequestBody.
        :type database: str
        """
        self._database = database

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
        if not isinstance(other, UpdateDatabaseOwnerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
