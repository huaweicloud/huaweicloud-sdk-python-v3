# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelayRestoreDatabase:

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
        'total_tables': 'int',
        'schemas': 'list[DelayRestoreSchema]'
    }

    attribute_map = {
        'name': 'name',
        'total_tables': 'total_tables',
        'schemas': 'schemas'
    }

    def __init__(self, name=None, total_tables=None, schemas=None):
        r"""DelayRestoreDatabase

        The model defined in huaweicloud sdk

        :param name: 数据库名称
        :type name: str
        :param total_tables: 返回该库下的总表数量
        :type total_tables: int
        :param schemas: 该库下的schema列表
        :type schemas: list[:class:`huaweicloudsdkrds.v3.DelayRestoreSchema`]
        """
        
        

        self._name = None
        self._total_tables = None
        self._schemas = None
        self.discriminator = None

        self.name = name
        if total_tables is not None:
            self.total_tables = total_tables
        if schemas is not None:
            self.schemas = schemas

    @property
    def name(self):
        r"""Gets the name of this DelayRestoreDatabase.

        数据库名称

        :return: The name of this DelayRestoreDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DelayRestoreDatabase.

        数据库名称

        :param name: The name of this DelayRestoreDatabase.
        :type name: str
        """
        self._name = name

    @property
    def total_tables(self):
        r"""Gets the total_tables of this DelayRestoreDatabase.

        返回该库下的总表数量

        :return: The total_tables of this DelayRestoreDatabase.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        r"""Sets the total_tables of this DelayRestoreDatabase.

        返回该库下的总表数量

        :param total_tables: The total_tables of this DelayRestoreDatabase.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def schemas(self):
        r"""Gets the schemas of this DelayRestoreDatabase.

        该库下的schema列表

        :return: The schemas of this DelayRestoreDatabase.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DelayRestoreSchema`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this DelayRestoreDatabase.

        该库下的schema列表

        :param schemas: The schemas of this DelayRestoreDatabase.
        :type schemas: list[:class:`huaweicloudsdkrds.v3.DelayRestoreSchema`]
        """
        self._schemas = schemas

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
        if not isinstance(other, DelayRestoreDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
