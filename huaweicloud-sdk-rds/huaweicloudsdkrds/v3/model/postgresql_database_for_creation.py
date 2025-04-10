# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlDatabaseForCreation:

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
        'lc_ctype': 'str',
        'is_revoke_public_privilege': 'bool',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'character_set': 'character_set',
        'owner': 'owner',
        'template': 'template',
        'lc_collate': 'lc_collate',
        'lc_ctype': 'lc_ctype',
        'is_revoke_public_privilege': 'is_revoke_public_privilege',
        'comment': 'comment'
    }

    def __init__(self, name=None, character_set=None, owner=None, template=None, lc_collate=None, lc_ctype=None, is_revoke_public_privilege=None, comment=None):
        r"""PostgresqlDatabaseForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和RDS for PostgreSQL模板库重名。  RDS for PostgreSQL模板库包括postgres， template0 ，template1。
        :type name: str
        :param character_set: 数据库字符集。默认UTF8。
        :type character_set: str
        :param owner: 数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。
        :type owner: str
        :param template: 数据库模板名称，可选值template0，template1。默认template1。
        :type template: str
        :param lc_collate: 数据库排序集。默认en_US.UTF-8。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select &#39;a&#39;&gt;&#39;A&#39;;执行结果为false，但在&#39;C&#39;下，select &#39;a&#39;&gt;&#39;A&#39;;结果为true。如果数据库从“O”迁移到PostgreSQL，数据库排序集需使用&#39;C&#39;才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。
        :type lc_collate: str
        :param lc_ctype: 数据库分类集。默认en_US.UTF-8。
        :type lc_ctype: str
        :param is_revoke_public_privilege: 是否回收public schema的PUBLIC CREATE权限。 true，表示回收该权限。 false，表示不回收该权限。 缺省时默认是false。
        :type is_revoke_public_privilege: bool
        :param comment: 数据库备注。 取值范围：长度1~512个字符。
        :type comment: str
        """
        
        

        self._name = None
        self._character_set = None
        self._owner = None
        self._template = None
        self._lc_collate = None
        self._lc_ctype = None
        self._is_revoke_public_privilege = None
        self._comment = None
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
        if is_revoke_public_privilege is not None:
            self.is_revoke_public_privilege = is_revoke_public_privilege
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        r"""Gets the name of this PostgresqlDatabaseForCreation.

        数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和RDS for PostgreSQL模板库重名。  RDS for PostgreSQL模板库包括postgres， template0 ，template1。

        :return: The name of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PostgresqlDatabaseForCreation.

        数据库名称。  数据库名称长度可在1～63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和RDS for PostgreSQL模板库重名。  RDS for PostgreSQL模板库包括postgres， template0 ，template1。

        :param name: The name of this PostgresqlDatabaseForCreation.
        :type name: str
        """
        self._name = name

    @property
    def character_set(self):
        r"""Gets the character_set of this PostgresqlDatabaseForCreation.

        数据库字符集。默认UTF8。

        :return: The character_set of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        r"""Sets the character_set of this PostgresqlDatabaseForCreation.

        数据库字符集。默认UTF8。

        :param character_set: The character_set of this PostgresqlDatabaseForCreation.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def owner(self):
        r"""Gets the owner of this PostgresqlDatabaseForCreation.

        数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。

        :return: The owner of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this PostgresqlDatabaseForCreation.

        数据库所属用户，缺省时默认是root，不能和系统用户重名，且必须是已存在的用户。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。

        :param owner: The owner of this PostgresqlDatabaseForCreation.
        :type owner: str
        """
        self._owner = owner

    @property
    def template(self):
        r"""Gets the template of this PostgresqlDatabaseForCreation.

        数据库模板名称，可选值template0，template1。默认template1。

        :return: The template of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this PostgresqlDatabaseForCreation.

        数据库模板名称，可选值template0，template1。默认template1。

        :param template: The template of this PostgresqlDatabaseForCreation.
        :type template: str
        """
        self._template = template

    @property
    def lc_collate(self):
        r"""Gets the lc_collate of this PostgresqlDatabaseForCreation.

        数据库排序集。默认en_US.UTF-8。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select 'a'>'A';执行结果为false，但在'C'下，select 'a'>'A';结果为true。如果数据库从“O”迁移到PostgreSQL，数据库排序集需使用'C'才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。

        :return: The lc_collate of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._lc_collate

    @lc_collate.setter
    def lc_collate(self, lc_collate):
        r"""Sets the lc_collate of this PostgresqlDatabaseForCreation.

        数据库排序集。默认en_US.UTF-8。  - 须知： 不同的排序规则下，相同字符串的比较其结果可能是不同的。 例如，在en_US.utf8下， select 'a'>'A';执行结果为false，但在'C'下，select 'a'>'A';结果为true。如果数据库从“O”迁移到PostgreSQL，数据库排序集需使用'C'才能得到一致的预期。支持的排序规则可以查询系统表 pg_collation。

        :param lc_collate: The lc_collate of this PostgresqlDatabaseForCreation.
        :type lc_collate: str
        """
        self._lc_collate = lc_collate

    @property
    def lc_ctype(self):
        r"""Gets the lc_ctype of this PostgresqlDatabaseForCreation.

        数据库分类集。默认en_US.UTF-8。

        :return: The lc_ctype of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._lc_ctype

    @lc_ctype.setter
    def lc_ctype(self, lc_ctype):
        r"""Sets the lc_ctype of this PostgresqlDatabaseForCreation.

        数据库分类集。默认en_US.UTF-8。

        :param lc_ctype: The lc_ctype of this PostgresqlDatabaseForCreation.
        :type lc_ctype: str
        """
        self._lc_ctype = lc_ctype

    @property
    def is_revoke_public_privilege(self):
        r"""Gets the is_revoke_public_privilege of this PostgresqlDatabaseForCreation.

        是否回收public schema的PUBLIC CREATE权限。 true，表示回收该权限。 false，表示不回收该权限。 缺省时默认是false。

        :return: The is_revoke_public_privilege of this PostgresqlDatabaseForCreation.
        :rtype: bool
        """
        return self._is_revoke_public_privilege

    @is_revoke_public_privilege.setter
    def is_revoke_public_privilege(self, is_revoke_public_privilege):
        r"""Sets the is_revoke_public_privilege of this PostgresqlDatabaseForCreation.

        是否回收public schema的PUBLIC CREATE权限。 true，表示回收该权限。 false，表示不回收该权限。 缺省时默认是false。

        :param is_revoke_public_privilege: The is_revoke_public_privilege of this PostgresqlDatabaseForCreation.
        :type is_revoke_public_privilege: bool
        """
        self._is_revoke_public_privilege = is_revoke_public_privilege

    @property
    def comment(self):
        r"""Gets the comment of this PostgresqlDatabaseForCreation.

        数据库备注。 取值范围：长度1~512个字符。

        :return: The comment of this PostgresqlDatabaseForCreation.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this PostgresqlDatabaseForCreation.

        数据库备注。 取值范围：长度1~512个字符。

        :param comment: The comment of this PostgresqlDatabaseForCreation.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, PostgresqlDatabaseForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
