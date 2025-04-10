# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelayRestoreSchema:

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
        'tables': 'list[DelayRestoreTable]'
    }

    attribute_map = {
        'name': 'name',
        'total_tables': 'total_tables',
        'tables': 'tables'
    }

    def __init__(self, name=None, total_tables=None, tables=None):
        r"""DelayRestoreSchema

        The model defined in huaweicloud sdk

        :param name: schema名称
        :type name: str
        :param total_tables: 返回该schema下的总表数量
        :type total_tables: int
        :param tables: 该schema下的表列表
        :type tables: list[:class:`huaweicloudsdkrds.v3.DelayRestoreTable`]
        """
        
        

        self._name = None
        self._total_tables = None
        self._tables = None
        self.discriminator = None

        self.name = name
        if total_tables is not None:
            self.total_tables = total_tables
        if tables is not None:
            self.tables = tables

    @property
    def name(self):
        r"""Gets the name of this DelayRestoreSchema.

        schema名称

        :return: The name of this DelayRestoreSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DelayRestoreSchema.

        schema名称

        :param name: The name of this DelayRestoreSchema.
        :type name: str
        """
        self._name = name

    @property
    def total_tables(self):
        r"""Gets the total_tables of this DelayRestoreSchema.

        返回该schema下的总表数量

        :return: The total_tables of this DelayRestoreSchema.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        r"""Sets the total_tables of this DelayRestoreSchema.

        返回该schema下的总表数量

        :param total_tables: The total_tables of this DelayRestoreSchema.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def tables(self):
        r"""Gets the tables of this DelayRestoreSchema.

        该schema下的表列表

        :return: The tables of this DelayRestoreSchema.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DelayRestoreTable`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this DelayRestoreSchema.

        该schema下的表列表

        :param tables: The tables of this DelayRestoreSchema.
        :type tables: list[:class:`huaweicloudsdkrds.v3.DelayRestoreTable`]
        """
        self._tables = tables

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
        if not isinstance(other, DelayRestoreSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
