# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMissingIndexScriptRequest:

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
        'table_name': 'str',
        'equality_columns': 'str',
        'inequality_columns': 'str',
        'included_columns': 'str',
        'object_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'table_name': 'table_name',
        'equality_columns': 'equality_columns',
        'inequality_columns': 'inequality_columns',
        'included_columns': 'included_columns',
        'object_id': 'object_id'
    }

    def __init__(self, instance_id=None, table_name=None, equality_columns=None, inequality_columns=None, included_columns=None, object_id=None):
        r"""ShowMissingIndexScriptRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param table_name: 表名
        :type table_name: str
        :param equality_columns: 相等列
        :type equality_columns: str
        :param inequality_columns: 不等列
        :type inequality_columns: str
        :param included_columns: 包含列
        :type included_columns: str
        :param object_id: 对象ID
        :type object_id: str
        """
        
        

        self._instance_id = None
        self._table_name = None
        self._equality_columns = None
        self._inequality_columns = None
        self._included_columns = None
        self._object_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.table_name = table_name
        self.equality_columns = equality_columns
        self.inequality_columns = inequality_columns
        self.included_columns = included_columns
        self.object_id = object_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowMissingIndexScriptRequest.

        实例ID

        :return: The instance_id of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowMissingIndexScriptRequest.

        实例ID

        :param instance_id: The instance_id of this ShowMissingIndexScriptRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowMissingIndexScriptRequest.

        表名

        :return: The table_name of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowMissingIndexScriptRequest.

        表名

        :param table_name: The table_name of this ShowMissingIndexScriptRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def equality_columns(self):
        r"""Gets the equality_columns of this ShowMissingIndexScriptRequest.

        相等列

        :return: The equality_columns of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._equality_columns

    @equality_columns.setter
    def equality_columns(self, equality_columns):
        r"""Sets the equality_columns of this ShowMissingIndexScriptRequest.

        相等列

        :param equality_columns: The equality_columns of this ShowMissingIndexScriptRequest.
        :type equality_columns: str
        """
        self._equality_columns = equality_columns

    @property
    def inequality_columns(self):
        r"""Gets the inequality_columns of this ShowMissingIndexScriptRequest.

        不等列

        :return: The inequality_columns of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._inequality_columns

    @inequality_columns.setter
    def inequality_columns(self, inequality_columns):
        r"""Sets the inequality_columns of this ShowMissingIndexScriptRequest.

        不等列

        :param inequality_columns: The inequality_columns of this ShowMissingIndexScriptRequest.
        :type inequality_columns: str
        """
        self._inequality_columns = inequality_columns

    @property
    def included_columns(self):
        r"""Gets the included_columns of this ShowMissingIndexScriptRequest.

        包含列

        :return: The included_columns of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._included_columns

    @included_columns.setter
    def included_columns(self, included_columns):
        r"""Sets the included_columns of this ShowMissingIndexScriptRequest.

        包含列

        :param included_columns: The included_columns of this ShowMissingIndexScriptRequest.
        :type included_columns: str
        """
        self._included_columns = included_columns

    @property
    def object_id(self):
        r"""Gets the object_id of this ShowMissingIndexScriptRequest.

        对象ID

        :return: The object_id of this ShowMissingIndexScriptRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ShowMissingIndexScriptRequest.

        对象ID

        :param object_id: The object_id of this ShowMissingIndexScriptRequest.
        :type object_id: str
        """
        self._object_id = object_id

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
        if not isinstance(other, ShowMissingIndexScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
