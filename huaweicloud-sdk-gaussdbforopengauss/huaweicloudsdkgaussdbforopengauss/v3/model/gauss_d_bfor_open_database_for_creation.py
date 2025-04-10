# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenDatabaseForCreation:

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
        'character_set': 'str',
        'owner': 'str',
        'template': 'str',
        'lc_collate': 'str',
        'lc_ctype': 'str'
    }

    attribute_map = {
        'name': 'name',
        'character_set': 'character_set',
        'owner': 'owner',
        'template': 'template',
        'lc_collate': 'lc_collate',
        'lc_ctype': 'lc_ctype'
    }

    def __init__(self, name=None, character_set=None, owner=None, template=None, lc_collate=None, lc_ctype=None):
        r"""GaussDBforOpenDatabaseForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。 GaussDB 模板库包括postgres， template0 ，template1。
        :type name: str
        :param character_set: 数据库字符集。默认C。
        :type character_set: str
        :param owner: 数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。
        :type owner: str
        :param template: 数据库模板名称，仅为template0。
        :type template: str
        :param lc_collate: 数据库排序集。默认默认C。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select &#39;a&#39;&gt;&#39;A&#39;;执行结果为false，但在&#39;C&#39;下，select &#39;a&#39;&gt;&#39;A&#39;;结果为true。如果数据库从“O”迁移到GaussDB ，数据库排序集需使用&#39;C&#39;才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。
        :type lc_collate: str
        :param lc_ctype: 数据库分类集。默认C。
        :type lc_ctype: str
        """
        
        

        self._name = None
        self._character_set = None
        self._owner = None
        self._template = None
        self._lc_collate = None
        self._lc_ctype = None
        self.discriminator = None

        self.name = name
        if character_set is not None:
            self.character_set = character_set
        if owner is not None:
            self.owner = owner
        if template is not None:
            self.template = template
        if lc_collate is not None:
            self.lc_collate = lc_collate
        if lc_ctype is not None:
            self.lc_ctype = lc_ctype

    @property
    def name(self):
        r"""Gets the name of this GaussDBforOpenDatabaseForCreation.

        数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。 GaussDB 模板库包括postgres， template0 ，template1。

        :return: The name of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GaussDBforOpenDatabaseForCreation.

        数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。 GaussDB 模板库包括postgres， template0 ，template1。

        :param name: The name of this GaussDBforOpenDatabaseForCreation.
        :type name: str
        """
        self._name = name

    @property
    def character_set(self):
        r"""Gets the character_set of this GaussDBforOpenDatabaseForCreation.

        数据库字符集。默认C。

        :return: The character_set of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        r"""Sets the character_set of this GaussDBforOpenDatabaseForCreation.

        数据库字符集。默认C。

        :param character_set: The character_set of this GaussDBforOpenDatabaseForCreation.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def owner(self):
        r"""Gets the owner of this GaussDBforOpenDatabaseForCreation.

        数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :return: The owner of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this GaussDBforOpenDatabaseForCreation.

        数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :param owner: The owner of this GaussDBforOpenDatabaseForCreation.
        :type owner: str
        """
        self._owner = owner

    @property
    def template(self):
        r"""Gets the template of this GaussDBforOpenDatabaseForCreation.

        数据库模板名称，仅为template0。

        :return: The template of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this GaussDBforOpenDatabaseForCreation.

        数据库模板名称，仅为template0。

        :param template: The template of this GaussDBforOpenDatabaseForCreation.
        :type template: str
        """
        self._template = template

    @property
    def lc_collate(self):
        r"""Gets the lc_collate of this GaussDBforOpenDatabaseForCreation.

        数据库排序集。默认默认C。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select 'a'>'A';执行结果为false，但在'C'下，select 'a'>'A';结果为true。如果数据库从“O”迁移到GaussDB ，数据库排序集需使用'C'才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。

        :return: The lc_collate of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._lc_collate

    @lc_collate.setter
    def lc_collate(self, lc_collate):
        r"""Sets the lc_collate of this GaussDBforOpenDatabaseForCreation.

        数据库排序集。默认默认C。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select 'a'>'A';执行结果为false，但在'C'下，select 'a'>'A';结果为true。如果数据库从“O”迁移到GaussDB ，数据库排序集需使用'C'才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。

        :param lc_collate: The lc_collate of this GaussDBforOpenDatabaseForCreation.
        :type lc_collate: str
        """
        self._lc_collate = lc_collate

    @property
    def lc_ctype(self):
        r"""Gets the lc_ctype of this GaussDBforOpenDatabaseForCreation.

        数据库分类集。默认C。

        :return: The lc_ctype of this GaussDBforOpenDatabaseForCreation.
        :rtype: str
        """
        return self._lc_ctype

    @lc_ctype.setter
    def lc_ctype(self, lc_ctype):
        r"""Sets the lc_ctype of this GaussDBforOpenDatabaseForCreation.

        数据库分类集。默认C。

        :param lc_ctype: The lc_ctype of this GaussDBforOpenDatabaseForCreation.
        :type lc_ctype: str
        """
        self._lc_ctype = lc_ctype

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
        if not isinstance(other, GaussDBforOpenDatabaseForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
