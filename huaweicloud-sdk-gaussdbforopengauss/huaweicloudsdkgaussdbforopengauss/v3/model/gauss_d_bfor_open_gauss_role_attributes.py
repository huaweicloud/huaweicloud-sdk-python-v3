# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussRoleAttributes:

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
        'schema': 'str',
        'readonly': 'bool',
        'default_privilege_grantee': 'str'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema',
        'readonly': 'readonly',
        'default_privilege_grantee': 'default_privilege_grantee'
    }

    def __init__(self, name=None, schema=None, readonly=None, default_privilege_grantee=None):
        r"""GaussDBforOpenGaussRoleAttributes

        The model defined in huaweicloud sdk

        :param name: 数据库角色名称。 不能使用系统用户或角色，且名称必须存在。 系统用户/角色包括“rdsAdmin”,“rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。
        :type name: str
        :param schema: SCHEMA名称。 不能和模板库以及系统内schema重名，且schema名称必须存在。 模板库包括postgres， template0 ，template1, 系统内schema包括public，information_schema。
        :type schema: str
        :param readonly: 数据库角色权限。 - true：只读。 - false：可读可写。
        :type readonly: bool
        :param default_privilege_grantee: 数据库用户/角色名称。 该字段的含义是将此用户/角色的权限授予给name字段指定的角色，通过readonly字段判断是否授予只读权限。 不能和系统用户/角色名称相同，且用户/角色名称必须存在，系统用户/角色包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。
        :type default_privilege_grantee: str
        """
        
        

        self._name = None
        self._schema = None
        self._readonly = None
        self._default_privilege_grantee = None
        self.discriminator = None

        self.name = name
        self.schema = schema
        self.readonly = readonly
        if default_privilege_grantee is not None:
            self.default_privilege_grantee = default_privilege_grantee

    @property
    def name(self):
        r"""Gets the name of this GaussDBforOpenGaussRoleAttributes.

        数据库角色名称。 不能使用系统用户或角色，且名称必须存在。 系统用户/角色包括“rdsAdmin”,“rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。

        :return: The name of this GaussDBforOpenGaussRoleAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GaussDBforOpenGaussRoleAttributes.

        数据库角色名称。 不能使用系统用户或角色，且名称必须存在。 系统用户/角色包括“rdsAdmin”,“rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。

        :param name: The name of this GaussDBforOpenGaussRoleAttributes.
        :type name: str
        """
        self._name = name

    @property
    def schema(self):
        r"""Gets the schema of this GaussDBforOpenGaussRoleAttributes.

        SCHEMA名称。 不能和模板库以及系统内schema重名，且schema名称必须存在。 模板库包括postgres， template0 ，template1, 系统内schema包括public，information_schema。

        :return: The schema of this GaussDBforOpenGaussRoleAttributes.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this GaussDBforOpenGaussRoleAttributes.

        SCHEMA名称。 不能和模板库以及系统内schema重名，且schema名称必须存在。 模板库包括postgres， template0 ，template1, 系统内schema包括public，information_schema。

        :param schema: The schema of this GaussDBforOpenGaussRoleAttributes.
        :type schema: str
        """
        self._schema = schema

    @property
    def readonly(self):
        r"""Gets the readonly of this GaussDBforOpenGaussRoleAttributes.

        数据库角色权限。 - true：只读。 - false：可读可写。

        :return: The readonly of this GaussDBforOpenGaussRoleAttributes.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this GaussDBforOpenGaussRoleAttributes.

        数据库角色权限。 - true：只读。 - false：可读可写。

        :param readonly: The readonly of this GaussDBforOpenGaussRoleAttributes.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def default_privilege_grantee(self):
        r"""Gets the default_privilege_grantee of this GaussDBforOpenGaussRoleAttributes.

        数据库用户/角色名称。 该字段的含义是将此用户/角色的权限授予给name字段指定的角色，通过readonly字段判断是否授予只读权限。 不能和系统用户/角色名称相同，且用户/角色名称必须存在，系统用户/角色包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。

        :return: The default_privilege_grantee of this GaussDBforOpenGaussRoleAttributes.
        :rtype: str
        """
        return self._default_privilege_grantee

    @default_privilege_grantee.setter
    def default_privilege_grantee(self, default_privilege_grantee):
        r"""Sets the default_privilege_grantee of this GaussDBforOpenGaussRoleAttributes.

        数据库用户/角色名称。 该字段的含义是将此用户/角色的权限授予给name字段指定的角色，通过readonly字段判断是否授予只读权限。 不能和系统用户/角色名称相同，且用户/角色名称必须存在，系统用户/角色包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”, “root”。

        :param default_privilege_grantee: The default_privilege_grantee of this GaussDBforOpenGaussRoleAttributes.
        :type default_privilege_grantee: str
        """
        self._default_privilege_grantee = default_privilege_grantee

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
        if not isinstance(other, GaussDBforOpenGaussRoleAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
