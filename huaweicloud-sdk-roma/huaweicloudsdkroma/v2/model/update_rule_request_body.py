# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleRequestBody:

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
        'description': 'str',
        'status': 'int',
        'data_parsing_status': 'int',
        'sql_field': 'str',
        'sql_where': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'data_parsing_status': 'data_parsing_status',
        'sql_field': 'sql_field',
        'sql_where': 'sql_where'
    }

    def __init__(self, name=None, description=None, status=None, data_parsing_status=None, sql_field=None, sql_where=None):
        """UpdateRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称，支持英文大小写，数字，下划线和中划线,长度1-64
        :type name: str
        :param description: 描述，长度0-200
        :type description: str
        :param status: 规则状态 0-启用 1-停用，不填写时默认为0-启用
        :type status: int
        :param data_parsing_status: 数据解析状态，0-启用 1-停用，不填写时默认为1-禁用
        :type data_parsing_status: int
        :param sql_field: SQL查询字段
        :type sql_field: str
        :param sql_where: SQL查询条件
        :type sql_where: str
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._data_parsing_status = None
        self._sql_field = None
        self._sql_where = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if data_parsing_status is not None:
            self.data_parsing_status = data_parsing_status
        if sql_field is not None:
            self.sql_field = sql_field
        if sql_where is not None:
            self.sql_where = sql_where

    @property
    def name(self):
        """Gets the name of this UpdateRuleRequestBody.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :return: The name of this UpdateRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRuleRequestBody.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :param name: The name of this UpdateRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateRuleRequestBody.

        描述，长度0-200

        :return: The description of this UpdateRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRuleRequestBody.

        描述，长度0-200

        :param description: The description of this UpdateRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateRuleRequestBody.

        规则状态 0-启用 1-停用，不填写时默认为0-启用

        :return: The status of this UpdateRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateRuleRequestBody.

        规则状态 0-启用 1-停用，不填写时默认为0-启用

        :param status: The status of this UpdateRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def data_parsing_status(self):
        """Gets the data_parsing_status of this UpdateRuleRequestBody.

        数据解析状态，0-启用 1-停用，不填写时默认为1-禁用

        :return: The data_parsing_status of this UpdateRuleRequestBody.
        :rtype: int
        """
        return self._data_parsing_status

    @data_parsing_status.setter
    def data_parsing_status(self, data_parsing_status):
        """Sets the data_parsing_status of this UpdateRuleRequestBody.

        数据解析状态，0-启用 1-停用，不填写时默认为1-禁用

        :param data_parsing_status: The data_parsing_status of this UpdateRuleRequestBody.
        :type data_parsing_status: int
        """
        self._data_parsing_status = data_parsing_status

    @property
    def sql_field(self):
        """Gets the sql_field of this UpdateRuleRequestBody.

        SQL查询字段

        :return: The sql_field of this UpdateRuleRequestBody.
        :rtype: str
        """
        return self._sql_field

    @sql_field.setter
    def sql_field(self, sql_field):
        """Sets the sql_field of this UpdateRuleRequestBody.

        SQL查询字段

        :param sql_field: The sql_field of this UpdateRuleRequestBody.
        :type sql_field: str
        """
        self._sql_field = sql_field

    @property
    def sql_where(self):
        """Gets the sql_where of this UpdateRuleRequestBody.

        SQL查询条件

        :return: The sql_where of this UpdateRuleRequestBody.
        :rtype: str
        """
        return self._sql_where

    @sql_where.setter
    def sql_where(self, sql_where):
        """Sets the sql_where of this UpdateRuleRequestBody.

        SQL查询条件

        :param sql_where: The sql_where of this UpdateRuleRequestBody.
        :type sql_where: str
        """
        self._sql_where = sql_where

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
        if not isinstance(other, UpdateRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
