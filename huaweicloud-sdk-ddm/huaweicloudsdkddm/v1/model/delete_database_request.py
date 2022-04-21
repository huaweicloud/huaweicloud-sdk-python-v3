# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseRequest:

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
        'ddm_dbname': 'str',
        'delete_rds_data': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'ddm_dbname': 'ddm_dbname',
        'delete_rds_data': 'delete_rds_data'
    }

    def __init__(self, instance_id=None, ddm_dbname=None, delete_rds_data=None):
        """DeleteDatabaseRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param ddm_dbname: 需要查询的逻辑库名称，不区分大小写。
        :type ddm_dbname: str
        :param delete_rds_data: 是否同时删除关联后端数据库实例上存储的数据。 - 取值为“true”：删除。 - 取值为空或“false”：不删除。 默认值为空。
        :type delete_rds_data: str
        """
        
        

        self._instance_id = None
        self._ddm_dbname = None
        self._delete_rds_data = None
        self.discriminator = None

        self.instance_id = instance_id
        self.ddm_dbname = ddm_dbname
        if delete_rds_data is not None:
            self.delete_rds_data = delete_rds_data

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteDatabaseRequest.

        DDM实例ID。

        :return: The instance_id of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteDatabaseRequest.

        DDM实例ID。

        :param instance_id: The instance_id of this DeleteDatabaseRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ddm_dbname(self):
        """Gets the ddm_dbname of this DeleteDatabaseRequest.

        需要查询的逻辑库名称，不区分大小写。

        :return: The ddm_dbname of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._ddm_dbname

    @ddm_dbname.setter
    def ddm_dbname(self, ddm_dbname):
        """Sets the ddm_dbname of this DeleteDatabaseRequest.

        需要查询的逻辑库名称，不区分大小写。

        :param ddm_dbname: The ddm_dbname of this DeleteDatabaseRequest.
        :type ddm_dbname: str
        """
        self._ddm_dbname = ddm_dbname

    @property
    def delete_rds_data(self):
        """Gets the delete_rds_data of this DeleteDatabaseRequest.

        是否同时删除关联后端数据库实例上存储的数据。 - 取值为“true”：删除。 - 取值为空或“false”：不删除。 默认值为空。

        :return: The delete_rds_data of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._delete_rds_data

    @delete_rds_data.setter
    def delete_rds_data(self, delete_rds_data):
        """Sets the delete_rds_data of this DeleteDatabaseRequest.

        是否同时删除关联后端数据库实例上存储的数据。 - 取值为“true”：删除。 - 取值为空或“false”：不删除。 默认值为空。

        :param delete_rds_data: The delete_rds_data of this DeleteDatabaseRequest.
        :type delete_rds_data: str
        """
        self._delete_rds_data = delete_rds_data

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
        if not isinstance(other, DeleteDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
