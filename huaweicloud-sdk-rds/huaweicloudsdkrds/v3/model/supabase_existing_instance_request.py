# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseExistingInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'database_name': 'str',
        'database_pwd': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'database_name': 'database_name',
        'database_pwd': 'database_pwd'
    }

    def __init__(self, instance_id=None, database_name=None, database_pwd=None):
        r"""SupabaseExistingInstanceRequest

        The model defined in huaweicloud sdk

        :param instance_id: 数据库实例ID（必须为PostgreSQL实例）。
        :type instance_id: str
        :param database_name: 对接的数据库用户名。
        :type database_name: str
        :param database_pwd: 对接的数据库密码。
        :type database_pwd: str
        """
        
        

        self._instance_id = None
        self._database_name = None
        self._database_pwd = None
        self.discriminator = None

        self.instance_id = instance_id
        self.database_name = database_name
        self.database_pwd = database_pwd

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SupabaseExistingInstanceRequest.

        数据库实例ID（必须为PostgreSQL实例）。

        :return: The instance_id of this SupabaseExistingInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SupabaseExistingInstanceRequest.

        数据库实例ID（必须为PostgreSQL实例）。

        :param instance_id: The instance_id of this SupabaseExistingInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def database_name(self):
        r"""Gets the database_name of this SupabaseExistingInstanceRequest.

        对接的数据库用户名。

        :return: The database_name of this SupabaseExistingInstanceRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SupabaseExistingInstanceRequest.

        对接的数据库用户名。

        :param database_name: The database_name of this SupabaseExistingInstanceRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def database_pwd(self):
        r"""Gets the database_pwd of this SupabaseExistingInstanceRequest.

        对接的数据库密码。

        :return: The database_pwd of this SupabaseExistingInstanceRequest.
        :rtype: str
        """
        return self._database_pwd

    @database_pwd.setter
    def database_pwd(self, database_pwd):
        r"""Sets the database_pwd of this SupabaseExistingInstanceRequest.

        对接的数据库密码。

        :param database_pwd: The database_pwd of this SupabaseExistingInstanceRequest.
        :type database_pwd: str
        """
        self._database_pwd = database_pwd

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupabaseExistingInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
