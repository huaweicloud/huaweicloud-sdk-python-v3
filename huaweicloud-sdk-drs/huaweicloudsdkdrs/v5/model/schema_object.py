# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_type': 'str',
        'name': 'str',
        'all': 'bool',
        'tables': 'dict(str, TableObject)'
    }

    attribute_map = {
        'sync_type': 'sync_type',
        'name': 'name',
        'all': 'all',
        'tables': 'tables'
    }

    def __init__(self, sync_type=None, name=None, all=None, tables=None):
        """SchemaObject

        The model defined in huaweicloud sdk

        :param sync_type: 该模式在实时同步场景下的类型。取值： - config：仅当该模式作为数据过滤高级设置的关联模式时，需要填写，此时该模式以及该模式下的tables“不会”被同步到目标库，name、all属性不生效，tables需要填写被关联的相关对象。（注意：如果需要同步该模式对象，则在下级对象中填写sync_type值为config。）
        :type sync_type: str
        :param name: 该模式在目标库的名称（模式名映射）。
        :type name: str
        :param all: 是否整模式迁移或同步。注意： 1.当该模式下的表、列需要做数据过滤、列过滤、列映射时，填false，否则填true； 2.当该模式下的表需要做附加列时，需要填true，并且在表级对象的columns里填写附加列信息； 3.当该模式下的表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；
        :type all: bool
        :param tables: 需要迁移或同步的表，当整模式迁移或同步为false时需要填写。
        :type tables: dict(str, TableObject)
        """
        
        

        self._sync_type = None
        self._name = None
        self._all = None
        self._tables = None
        self.discriminator = None

        if sync_type is not None:
            self.sync_type = sync_type
        if name is not None:
            self.name = name
        if all is not None:
            self.all = all
        if tables is not None:
            self.tables = tables

    @property
    def sync_type(self):
        """Gets the sync_type of this SchemaObject.

        该模式在实时同步场景下的类型。取值： - config：仅当该模式作为数据过滤高级设置的关联模式时，需要填写，此时该模式以及该模式下的tables“不会”被同步到目标库，name、all属性不生效，tables需要填写被关联的相关对象。（注意：如果需要同步该模式对象，则在下级对象中填写sync_type值为config。）

        :return: The sync_type of this SchemaObject.
        :rtype: str
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        """Sets the sync_type of this SchemaObject.

        该模式在实时同步场景下的类型。取值： - config：仅当该模式作为数据过滤高级设置的关联模式时，需要填写，此时该模式以及该模式下的tables“不会”被同步到目标库，name、all属性不生效，tables需要填写被关联的相关对象。（注意：如果需要同步该模式对象，则在下级对象中填写sync_type值为config。）

        :param sync_type: The sync_type of this SchemaObject.
        :type sync_type: str
        """
        self._sync_type = sync_type

    @property
    def name(self):
        """Gets the name of this SchemaObject.

        该模式在目标库的名称（模式名映射）。

        :return: The name of this SchemaObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SchemaObject.

        该模式在目标库的名称（模式名映射）。

        :param name: The name of this SchemaObject.
        :type name: str
        """
        self._name = name

    @property
    def all(self):
        """Gets the all of this SchemaObject.

        是否整模式迁移或同步。注意： 1.当该模式下的表、列需要做数据过滤、列过滤、列映射时，填false，否则填true； 2.当该模式下的表需要做附加列时，需要填true，并且在表级对象的columns里填写附加列信息； 3.当该模式下的表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；

        :return: The all of this SchemaObject.
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this SchemaObject.

        是否整模式迁移或同步。注意： 1.当该模式下的表、列需要做数据过滤、列过滤、列映射时，填false，否则填true； 2.当该模式下的表需要做附加列时，需要填true，并且在表级对象的columns里填写附加列信息； 3.当该模式下的表所包含的列作为数据过滤高级设置的关联列时，需要填true，并且在columns里填写关联列信息、config_conditions填写数据过滤高级设置的配置条件；

        :param all: The all of this SchemaObject.
        :type all: bool
        """
        self._all = all

    @property
    def tables(self):
        """Gets the tables of this SchemaObject.

        需要迁移或同步的表，当整模式迁移或同步为false时需要填写。

        :return: The tables of this SchemaObject.
        :rtype: dict(str, TableObject)
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this SchemaObject.

        需要迁移或同步的表，当整模式迁移或同步为false时需要填写。

        :param tables: The tables of this SchemaObject.
        :type tables: dict(str, TableObject)
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
        if not isinstance(other, SchemaObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
