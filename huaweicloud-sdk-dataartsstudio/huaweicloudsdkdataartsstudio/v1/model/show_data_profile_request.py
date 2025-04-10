# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataProfileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dw_id': 'str',
        'db_type': 'str',
        'database_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dw_id': 'dw_id',
        'db_type': 'db_type',
        'database_name': 'database_name',
        'table_name': 'table_name'
    }

    def __init__(self, workspace=None, dw_id=None, db_type=None, database_name=None, table_name=None):
        r"""ShowDataProfileRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param dw_id: 数据连接ID
        :type dw_id: str
        :param db_type: 数据库类型
        :type db_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名
        :type table_name: str
        """
        
        

        self._workspace = None
        self._dw_id = None
        self._db_type = None
        self._database_name = None
        self._table_name = None
        self.discriminator = None

        self.workspace = workspace
        self.dw_id = dw_id
        self.db_type = db_type
        self.database_name = database_name
        self.table_name = table_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowDataProfileRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowDataProfileRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowDataProfileRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowDataProfileRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dw_id(self):
        r"""Gets the dw_id of this ShowDataProfileRequest.

        数据连接ID

        :return: The dw_id of this ShowDataProfileRequest.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this ShowDataProfileRequest.

        数据连接ID

        :param dw_id: The dw_id of this ShowDataProfileRequest.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def db_type(self):
        r"""Gets the db_type of this ShowDataProfileRequest.

        数据库类型

        :return: The db_type of this ShowDataProfileRequest.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ShowDataProfileRequest.

        数据库类型

        :param db_type: The db_type of this ShowDataProfileRequest.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowDataProfileRequest.

        数据库名称

        :return: The database_name of this ShowDataProfileRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowDataProfileRequest.

        数据库名称

        :param database_name: The database_name of this ShowDataProfileRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowDataProfileRequest.

        表名

        :return: The table_name of this ShowDataProfileRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowDataProfileRequest.

        表名

        :param table_name: The table_name of this ShowDataProfileRequest.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, ShowDataProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
