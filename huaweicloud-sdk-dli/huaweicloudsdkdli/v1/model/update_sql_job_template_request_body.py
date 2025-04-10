# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlJobTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'sql_name': 'str',
        'description': 'str',
        'group': 'str'
    }

    attribute_map = {
        'sql': 'sql',
        'sql_name': 'sql_name',
        'description': 'description',
        'group': 'group'
    }

    def __init__(self, sql=None, sql_name=None, description=None, group=None):
        r"""UpdateSqlJobTemplateRequestBody

        The model defined in huaweicloud sdk

        :param sql: 更新后SQL模板文本。
        :type sql: str
        :param sql_name: 更新后SQL模板名称，该名称在当前工程下必须唯一。
        :type sql_name: str
        :param description: SQL模板的描述信息，可以为空。
        :type description: str
        :param group: 分组名称。
        :type group: str
        """
        
        

        self._sql = None
        self._sql_name = None
        self._description = None
        self._group = None
        self.discriminator = None

        if sql is not None:
            self.sql = sql
        if sql_name is not None:
            self.sql_name = sql_name
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group

    @property
    def sql(self):
        r"""Gets the sql of this UpdateSqlJobTemplateRequestBody.

        更新后SQL模板文本。

        :return: The sql of this UpdateSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this UpdateSqlJobTemplateRequestBody.

        更新后SQL模板文本。

        :param sql: The sql of this UpdateSqlJobTemplateRequestBody.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_name(self):
        r"""Gets the sql_name of this UpdateSqlJobTemplateRequestBody.

        更新后SQL模板名称，该名称在当前工程下必须唯一。

        :return: The sql_name of this UpdateSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._sql_name

    @sql_name.setter
    def sql_name(self, sql_name):
        r"""Sets the sql_name of this UpdateSqlJobTemplateRequestBody.

        更新后SQL模板名称，该名称在当前工程下必须唯一。

        :param sql_name: The sql_name of this UpdateSqlJobTemplateRequestBody.
        :type sql_name: str
        """
        self._sql_name = sql_name

    @property
    def description(self):
        r"""Gets the description of this UpdateSqlJobTemplateRequestBody.

        SQL模板的描述信息，可以为空。

        :return: The description of this UpdateSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSqlJobTemplateRequestBody.

        SQL模板的描述信息，可以为空。

        :param description: The description of this UpdateSqlJobTemplateRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def group(self):
        r"""Gets the group of this UpdateSqlJobTemplateRequestBody.

        分组名称。

        :return: The group of this UpdateSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this UpdateSqlJobTemplateRequestBody.

        分组名称。

        :param group: The group of this UpdateSqlJobTemplateRequestBody.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, UpdateSqlJobTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
