# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlinkSqlJobTemplateRequestBody:

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
        'desc': 'str',
        'sql_body': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'sql_body': 'sql_body'
    }

    def __init__(self, name=None, desc=None, sql_body=None):
        r"""UpdateFlinkSqlJobTemplateRequestBody

        The model defined in huaweicloud sdk

        :param name: 模板名称，长度限制：0-57个字符。
        :type name: str
        :param desc: 模板描述，长度限制：0-2048个字符。
        :type desc: str
        :param sql_body: Stream SQL语句，至少包含source，query，sink三个部分，长度限制：0-1024*1024个字符。
        :type sql_body: str
        """
        
        

        self._name = None
        self._desc = None
        self._sql_body = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if sql_body is not None:
            self.sql_body = sql_body

    @property
    def name(self):
        r"""Gets the name of this UpdateFlinkSqlJobTemplateRequestBody.

        模板名称，长度限制：0-57个字符。

        :return: The name of this UpdateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateFlinkSqlJobTemplateRequestBody.

        模板名称，长度限制：0-57个字符。

        :param name: The name of this UpdateFlinkSqlJobTemplateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this UpdateFlinkSqlJobTemplateRequestBody.

        模板描述，长度限制：0-2048个字符。

        :return: The desc of this UpdateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UpdateFlinkSqlJobTemplateRequestBody.

        模板描述，长度限制：0-2048个字符。

        :param desc: The desc of this UpdateFlinkSqlJobTemplateRequestBody.
        :type desc: str
        """
        self._desc = desc

    @property
    def sql_body(self):
        r"""Gets the sql_body of this UpdateFlinkSqlJobTemplateRequestBody.

        Stream SQL语句，至少包含source，query，sink三个部分，长度限制：0-1024*1024个字符。

        :return: The sql_body of this UpdateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        r"""Sets the sql_body of this UpdateFlinkSqlJobTemplateRequestBody.

        Stream SQL语句，至少包含source，query，sink三个部分，长度限制：0-1024*1024个字符。

        :param sql_body: The sql_body of this UpdateFlinkSqlJobTemplateRequestBody.
        :type sql_body: str
        """
        self._sql_body = sql_body

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
        if not isinstance(other, UpdateFlinkSqlJobTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
