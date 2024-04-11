# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayErrorSqlTemplateResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'target_name': 'str',
        'schema_name': 'str',
        'query_type': 'str',
        'target_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'target_name': 'target_name',
        'schema_name': 'schema_name',
        'query_type': 'query_type',
        'target_type': 'target_type',
        'count': 'count'
    }

    def __init__(self, sql_template=None, target_name=None, schema_name=None, query_type=None, target_type=None, count=None):
        """ReplayErrorSqlTemplateResp

        The model defined in huaweicloud sdk

        :param sql_template: SQL模板
        :type sql_template: str
        :param target_name: 目标库昵称
        :type target_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param query_type: SQL类型
        :type query_type: str
        :param target_type: 目标库类型
        :type target_type: str
        :param count: 归类的SQL数量
        :type count: int
        """
        
        

        self._sql_template = None
        self._target_name = None
        self._schema_name = None
        self._query_type = None
        self._target_type = None
        self._count = None
        self.discriminator = None

        if sql_template is not None:
            self.sql_template = sql_template
        if target_name is not None:
            self.target_name = target_name
        if schema_name is not None:
            self.schema_name = schema_name
        if query_type is not None:
            self.query_type = query_type
        if target_type is not None:
            self.target_type = target_type
        if count is not None:
            self.count = count

    @property
    def sql_template(self):
        """Gets the sql_template of this ReplayErrorSqlTemplateResp.

        SQL模板

        :return: The sql_template of this ReplayErrorSqlTemplateResp.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        """Sets the sql_template of this ReplayErrorSqlTemplateResp.

        SQL模板

        :param sql_template: The sql_template of this ReplayErrorSqlTemplateResp.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def target_name(self):
        """Gets the target_name of this ReplayErrorSqlTemplateResp.

        目标库昵称

        :return: The target_name of this ReplayErrorSqlTemplateResp.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this ReplayErrorSqlTemplateResp.

        目标库昵称

        :param target_name: The target_name of this ReplayErrorSqlTemplateResp.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def schema_name(self):
        """Gets the schema_name of this ReplayErrorSqlTemplateResp.

        schema名称

        :return: The schema_name of this ReplayErrorSqlTemplateResp.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this ReplayErrorSqlTemplateResp.

        schema名称

        :param schema_name: The schema_name of this ReplayErrorSqlTemplateResp.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def query_type(self):
        """Gets the query_type of this ReplayErrorSqlTemplateResp.

        SQL类型

        :return: The query_type of this ReplayErrorSqlTemplateResp.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ReplayErrorSqlTemplateResp.

        SQL类型

        :param query_type: The query_type of this ReplayErrorSqlTemplateResp.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def target_type(self):
        """Gets the target_type of this ReplayErrorSqlTemplateResp.

        目标库类型

        :return: The target_type of this ReplayErrorSqlTemplateResp.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ReplayErrorSqlTemplateResp.

        目标库类型

        :param target_type: The target_type of this ReplayErrorSqlTemplateResp.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def count(self):
        """Gets the count of this ReplayErrorSqlTemplateResp.

        归类的SQL数量

        :return: The count of this ReplayErrorSqlTemplateResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ReplayErrorSqlTemplateResp.

        归类的SQL数量

        :param count: The count of this ReplayErrorSqlTemplateResp.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ReplayErrorSqlTemplateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
