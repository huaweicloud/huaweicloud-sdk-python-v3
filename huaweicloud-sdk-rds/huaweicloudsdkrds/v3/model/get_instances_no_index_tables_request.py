# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetInstancesNoIndexTablesRequest:

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
        'newest': 'bool',
        'table_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'newest': 'newest',
        'table_type': 'table_type'
    }

    def __init__(self, instance_id=None, newest=None, table_type=None):
        r"""GetInstancesNoIndexTablesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param newest: 指定查询是否应侧重于检索最新或最新的特殊表。
        :type newest: bool
        :param table_type: 表格类型。
        :type table_type: str
        """
        
        

        self._instance_id = None
        self._newest = None
        self._table_type = None
        self.discriminator = None

        self.instance_id = instance_id
        self.newest = newest
        self.table_type = table_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this GetInstancesNoIndexTablesRequest.

        实例ID

        :return: The instance_id of this GetInstancesNoIndexTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this GetInstancesNoIndexTablesRequest.

        实例ID

        :param instance_id: The instance_id of this GetInstancesNoIndexTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def newest(self):
        r"""Gets the newest of this GetInstancesNoIndexTablesRequest.

        指定查询是否应侧重于检索最新或最新的特殊表。

        :return: The newest of this GetInstancesNoIndexTablesRequest.
        :rtype: bool
        """
        return self._newest

    @newest.setter
    def newest(self, newest):
        r"""Sets the newest of this GetInstancesNoIndexTablesRequest.

        指定查询是否应侧重于检索最新或最新的特殊表。

        :param newest: The newest of this GetInstancesNoIndexTablesRequest.
        :type newest: bool
        """
        self._newest = newest

    @property
    def table_type(self):
        r"""Gets the table_type of this GetInstancesNoIndexTablesRequest.

        表格类型。

        :return: The table_type of this GetInstancesNoIndexTablesRequest.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this GetInstancesNoIndexTablesRequest.

        表格类型。

        :param table_type: The table_type of this GetInstancesNoIndexTablesRequest.
        :type table_type: str
        """
        self._table_type = table_type

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
        if not isinstance(other, GetInstancesNoIndexTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
