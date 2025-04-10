# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDdmDatabaseRequest:

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
        'delete_dn_data': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'database_name': 'database_name',
        'delete_dn_data': 'delete_dn_data'
    }

    def __init__(self, instance_id=None, database_name=None, delete_dn_data=None):
        r"""DeleteDdmDatabaseRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param database_name: 逻辑库名称。
        :type database_name: str
        :param delete_dn_data: 是否同时删除关联后端数据库实例上存储的数据。 - 取值为true：删除。 - 取值为false：不删除。
        :type delete_dn_data: bool
        """
        
        

        self._instance_id = None
        self._database_name = None
        self._delete_dn_data = None
        self.discriminator = None

        self.instance_id = instance_id
        self.database_name = database_name
        self.delete_dn_data = delete_dn_data

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteDdmDatabaseRequest.

        DDM实例ID。

        :return: The instance_id of this DeleteDdmDatabaseRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteDdmDatabaseRequest.

        DDM实例ID。

        :param instance_id: The instance_id of this DeleteDdmDatabaseRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def database_name(self):
        r"""Gets the database_name of this DeleteDdmDatabaseRequest.

        逻辑库名称。

        :return: The database_name of this DeleteDdmDatabaseRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DeleteDdmDatabaseRequest.

        逻辑库名称。

        :param database_name: The database_name of this DeleteDdmDatabaseRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def delete_dn_data(self):
        r"""Gets the delete_dn_data of this DeleteDdmDatabaseRequest.

        是否同时删除关联后端数据库实例上存储的数据。 - 取值为true：删除。 - 取值为false：不删除。

        :return: The delete_dn_data of this DeleteDdmDatabaseRequest.
        :rtype: bool
        """
        return self._delete_dn_data

    @delete_dn_data.setter
    def delete_dn_data(self, delete_dn_data):
        r"""Sets the delete_dn_data of this DeleteDdmDatabaseRequest.

        是否同时删除关联后端数据库实例上存储的数据。 - 取值为true：删除。 - 取值为false：不删除。

        :param delete_dn_data: The delete_dn_data of this DeleteDdmDatabaseRequest.
        :type delete_dn_data: bool
        """
        self._delete_dn_data = delete_dn_data

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
        if not isinstance(other, DeleteDdmDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
