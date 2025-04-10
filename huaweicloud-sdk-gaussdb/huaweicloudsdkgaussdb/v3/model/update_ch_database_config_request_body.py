# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChDatabaseConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_instance_id': 'str',
        'source_node_id': 'str',
        'database': 'str',
        'value': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'database': 'database',
        'value': 'value'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, database=None, value=None):
        r"""UpdateChDatabaseConfigRequestBody

        The model defined in huaweicloud sdk

        :param source_instance_id: 源实例ID，严格匹配UUID规则。
        :type source_instance_id: str
        :param source_node_id: 源实例节点ID。
        :type source_node_id: str
        :param database: 数据库名。
        :type database: str
        :param value: 配置值。仅支持修改同步范围，不支持修改白名单或黑名单类型。  例如：创建了白名单数据同步，调用本接口修改时， 支持 \&quot;value\&quot;：\&quot;{\\\&quot;white_list\\\&quot;:\\\&quot;test1,test2,test3\\\&quot;}\&quot; 不支持 \&quot;value\&quot;：\&quot;{\\\&quot;black_list\\\&quot;:\\\&quot;test1,test2,test3\\\&quot;}\&quot;
        :type value: str
        """
        
        

        self._source_instance_id = None
        self._source_node_id = None
        self._database = None
        self._value = None
        self.discriminator = None

        self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        self.database = database
        self.value = value

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this UpdateChDatabaseConfigRequestBody.

        源实例ID，严格匹配UUID规则。

        :return: The source_instance_id of this UpdateChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this UpdateChDatabaseConfigRequestBody.

        源实例ID，严格匹配UUID规则。

        :param source_instance_id: The source_instance_id of this UpdateChDatabaseConfigRequestBody.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        r"""Gets the source_node_id of this UpdateChDatabaseConfigRequestBody.

        源实例节点ID。

        :return: The source_node_id of this UpdateChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        r"""Sets the source_node_id of this UpdateChDatabaseConfigRequestBody.

        源实例节点ID。

        :param source_node_id: The source_node_id of this UpdateChDatabaseConfigRequestBody.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def database(self):
        r"""Gets the database of this UpdateChDatabaseConfigRequestBody.

        数据库名。

        :return: The database of this UpdateChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this UpdateChDatabaseConfigRequestBody.

        数据库名。

        :param database: The database of this UpdateChDatabaseConfigRequestBody.
        :type database: str
        """
        self._database = database

    @property
    def value(self):
        r"""Gets the value of this UpdateChDatabaseConfigRequestBody.

        配置值。仅支持修改同步范围，不支持修改白名单或黑名单类型。  例如：创建了白名单数据同步，调用本接口修改时， 支持 \"value\"：\"{\\\"white_list\\\":\\\"test1,test2,test3\\\"}\" 不支持 \"value\"：\"{\\\"black_list\\\":\\\"test1,test2,test3\\\"}\"

        :return: The value of this UpdateChDatabaseConfigRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this UpdateChDatabaseConfigRequestBody.

        配置值。仅支持修改同步范围，不支持修改白名单或黑名单类型。  例如：创建了白名单数据同步，调用本接口修改时， 支持 \"value\"：\"{\\\"white_list\\\":\\\"test1,test2,test3\\\"}\" 不支持 \"value\"：\"{\\\"black_list\\\":\\\"test1,test2,test3\\\"}\"

        :param value: The value of this UpdateChDatabaseConfigRequestBody.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, UpdateChDatabaseConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
