# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussUserWithPrivilege:

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
        'readonly': 'bool',
        'schema_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'readonly': 'readonly',
        'schema_name': 'schema_name'
    }

    def __init__(self, name=None, readonly=None, schema_name=None):
        """GaussDBforOpenGaussUserWithPrivilege

        The model defined in huaweicloud sdk

        :param name: 数据库帐号名称。  数据库帐号名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同且帐号名称必须存在。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。
        :type name: str
        :param readonly: 数据库帐号权限。 - true：只读。 - false：可读可写。
        :type readonly: bool
        :param schema_name: schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和GaussDB 模板库重名，且schema名称必须存在。  GaussDB 模板库包括postgres， template0 ，template1, public，information_schema。
        :type schema_name: str
        """
        
        

        self._name = None
        self._readonly = None
        self._schema_name = None
        self.discriminator = None

        self.name = name
        self.readonly = readonly
        self.schema_name = schema_name

    @property
    def name(self):
        """Gets the name of this GaussDBforOpenGaussUserWithPrivilege.

        数据库帐号名称。  数据库帐号名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同且帐号名称必须存在。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :return: The name of this GaussDBforOpenGaussUserWithPrivilege.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GaussDBforOpenGaussUserWithPrivilege.

        数据库帐号名称。  数据库帐号名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同且帐号名称必须存在。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :param name: The name of this GaussDBforOpenGaussUserWithPrivilege.
        :type name: str
        """
        self._name = name

    @property
    def readonly(self):
        """Gets the readonly of this GaussDBforOpenGaussUserWithPrivilege.

        数据库帐号权限。 - true：只读。 - false：可读可写。

        :return: The readonly of this GaussDBforOpenGaussUserWithPrivilege.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this GaussDBforOpenGaussUserWithPrivilege.

        数据库帐号权限。 - true：只读。 - false：可读可写。

        :param readonly: The readonly of this GaussDBforOpenGaussUserWithPrivilege.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def schema_name(self):
        """Gets the schema_name of this GaussDBforOpenGaussUserWithPrivilege.

        schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和GaussDB 模板库重名，且schema名称必须存在。  GaussDB 模板库包括postgres， template0 ，template1, public，information_schema。

        :return: The schema_name of this GaussDBforOpenGaussUserWithPrivilege.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this GaussDBforOpenGaussUserWithPrivilege.

        schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和GaussDB 模板库重名，且schema名称必须存在。  GaussDB 模板库包括postgres， template0 ，template1, public，information_schema。

        :param schema_name: The schema_name of this GaussDBforOpenGaussUserWithPrivilege.
        :type schema_name: str
        """
        self._schema_name = schema_name

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
        if not isinstance(other, GaussDBforOpenGaussUserWithPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
