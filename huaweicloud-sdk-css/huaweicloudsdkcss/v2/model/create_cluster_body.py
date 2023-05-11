# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterBody:

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
        'backup_strategy': 'CreateClusterBackupStrategyBody',
        'roles': 'list[CreateClusterRolesBody]',
        'nics': 'CreateClusterInstanceNicsBody',
        'enterprise_project_id': 'str',
        'tags': 'list[CreateClusterTagsBody]',
        'availability_zone': 'str',
        'datastore': 'CreateClusterDatastoreBody',
        'authority_enable': 'bool',
        'https_enable': 'bool',
        'admin_pwd': 'str',
        'public_ip_req': 'CreateClusterPublicIpReq',
        'load_balance': 'CreateClusterLoadBalance',
        'public_kibana_req': 'CreateClusterPublicKibanaReq',
        'pay_info': 'PayInfoBody'
    }

    attribute_map = {
        'name': 'name',
        'backup_strategy': 'backupStrategy',
        'roles': 'roles',
        'nics': 'nics',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'availability_zone': 'availability_zone',
        'datastore': 'datastore',
        'authority_enable': 'authorityEnable',
        'https_enable': 'httpsEnable',
        'admin_pwd': 'adminPwd',
        'public_ip_req': 'publicIPReq',
        'load_balance': 'loadBalance',
        'public_kibana_req': 'publicKibanaReq',
        'pay_info': 'payInfo'
    }

    def __init__(self, name=None, backup_strategy=None, roles=None, nics=None, enterprise_project_id=None, tags=None, availability_zone=None, datastore=None, authority_enable=None, https_enable=None, admin_pwd=None, public_ip_req=None, load_balance=None, public_kibana_req=None, pay_info=None):
        """CreateClusterBody

        The model defined in huaweicloud sdk

        :param name: 集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。
        :type name: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkcss.v2.CreateClusterBackupStrategyBody`
        :param roles: 
        :type roles: list[:class:`huaweicloudsdkcss.v2.CreateClusterRolesBody`]
        :param nics: 
        :type nics: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceNicsBody`
        :param enterprise_project_id: 企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\&quot;-\&quot;连字符的UUID格式，或者是字符串\&quot;0\&quot;。\&quot;0\&quot;表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: 集群标签。
        :type tags: list[:class:`huaweicloudsdkcss.v2.CreateClusterTagsBody`]
        :param availability_zone: 可用区。
        :type availability_zone: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcss.v2.CreateClusterDatastoreBody`
        :param authority_enable: 是否开启认证，取值范围为true或false。默认关闭认证功能。  - true：表示集群开启认证。 - false：表示集群不开启认证。  &gt;此参数只有6.5.4及之后版本支持。
        :type authority_enable: bool
        :param https_enable: 设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。 - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  &gt;此参数只有6.5.4及之后版本支持。
        :type https_enable: bool
        :param admin_pwd: 安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。  - 参数范围：8~32个字符。  - 参数要求：密码至少包含大写字母，小写字母，数字、特殊字符四类中的三类，其中可输入的特殊字符为：~!@#$%&amp;*()-_&#x3D;|[{}];:,&lt;.&gt;/?
        :type admin_pwd: str
        :param public_ip_req: 
        :type public_ip_req: :class:`huaweicloudsdkcss.v2.CreateClusterPublicIpReq`
        :param load_balance: 
        :type load_balance: :class:`huaweicloudsdkcss.v2.CreateClusterLoadBalance`
        :param public_kibana_req: 
        :type public_kibana_req: :class:`huaweicloudsdkcss.v2.CreateClusterPublicKibanaReq`
        :param pay_info: 
        :type pay_info: :class:`huaweicloudsdkcss.v2.PayInfoBody`
        """
        
        

        self._name = None
        self._backup_strategy = None
        self._roles = None
        self._nics = None
        self._enterprise_project_id = None
        self._tags = None
        self._availability_zone = None
        self._datastore = None
        self._authority_enable = None
        self._https_enable = None
        self._admin_pwd = None
        self._public_ip_req = None
        self._load_balance = None
        self._public_kibana_req = None
        self._pay_info = None
        self.discriminator = None

        self.name = name
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        self.roles = roles
        self.nics = nics
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.datastore = datastore
        if authority_enable is not None:
            self.authority_enable = authority_enable
        if https_enable is not None:
            self.https_enable = https_enable
        if admin_pwd is not None:
            self.admin_pwd = admin_pwd
        if public_ip_req is not None:
            self.public_ip_req = public_ip_req
        if load_balance is not None:
            self.load_balance = load_balance
        if public_kibana_req is not None:
            self.public_kibana_req = public_kibana_req
        if pay_info is not None:
            self.pay_info = pay_info

    @property
    def name(self):
        """Gets the name of this CreateClusterBody.

        集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :return: The name of this CreateClusterBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterBody.

        集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :param name: The name of this CreateClusterBody.
        :type name: str
        """
        self._name = name

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateClusterBody.

        :return: The backup_strategy of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterBackupStrategyBody`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateClusterBody.

        :param backup_strategy: The backup_strategy of this CreateClusterBody.
        :type backup_strategy: :class:`huaweicloudsdkcss.v2.CreateClusterBackupStrategyBody`
        """
        self._backup_strategy = backup_strategy

    @property
    def roles(self):
        """Gets the roles of this CreateClusterBody.

        :return: The roles of this CreateClusterBody.
        :rtype: list[:class:`huaweicloudsdkcss.v2.CreateClusterRolesBody`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateClusterBody.

        :param roles: The roles of this CreateClusterBody.
        :type roles: list[:class:`huaweicloudsdkcss.v2.CreateClusterRolesBody`]
        """
        self._roles = roles

    @property
    def nics(self):
        """Gets the nics of this CreateClusterBody.

        :return: The nics of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceNicsBody`
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateClusterBody.

        :param nics: The nics of this CreateClusterBody.
        :type nics: :class:`huaweicloudsdkcss.v2.CreateClusterInstanceNicsBody`
        """
        self._nics = nics

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。

        :return: The enterprise_project_id of this CreateClusterBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateClusterBody.

        集群标签。

        :return: The tags of this CreateClusterBody.
        :rtype: list[:class:`huaweicloudsdkcss.v2.CreateClusterTagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClusterBody.

        集群标签。

        :param tags: The tags of this CreateClusterBody.
        :type tags: list[:class:`huaweicloudsdkcss.v2.CreateClusterTagsBody`]
        """
        self._tags = tags

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClusterBody.

        可用区。

        :return: The availability_zone of this CreateClusterBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClusterBody.

        可用区。

        :param availability_zone: The availability_zone of this CreateClusterBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def datastore(self):
        """Gets the datastore of this CreateClusterBody.

        :return: The datastore of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterDatastoreBody`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateClusterBody.

        :param datastore: The datastore of this CreateClusterBody.
        :type datastore: :class:`huaweicloudsdkcss.v2.CreateClusterDatastoreBody`
        """
        self._datastore = datastore

    @property
    def authority_enable(self):
        """Gets the authority_enable of this CreateClusterBody.

        是否开启认证，取值范围为true或false。默认关闭认证功能。  - true：表示集群开启认证。 - false：表示集群不开启认证。  >此参数只有6.5.4及之后版本支持。

        :return: The authority_enable of this CreateClusterBody.
        :rtype: bool
        """
        return self._authority_enable

    @authority_enable.setter
    def authority_enable(self, authority_enable):
        """Sets the authority_enable of this CreateClusterBody.

        是否开启认证，取值范围为true或false。默认关闭认证功能。  - true：表示集群开启认证。 - false：表示集群不开启认证。  >此参数只有6.5.4及之后版本支持。

        :param authority_enable: The authority_enable of this CreateClusterBody.
        :type authority_enable: bool
        """
        self._authority_enable = authority_enable

    @property
    def https_enable(self):
        """Gets the https_enable of this CreateClusterBody.

        设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。 - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  >此参数只有6.5.4及之后版本支持。

        :return: The https_enable of this CreateClusterBody.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this CreateClusterBody.

        设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。 - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  >此参数只有6.5.4及之后版本支持。

        :param https_enable: The https_enable of this CreateClusterBody.
        :type https_enable: bool
        """
        self._https_enable = https_enable

    @property
    def admin_pwd(self):
        """Gets the admin_pwd of this CreateClusterBody.

        安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。  - 参数范围：8~32个字符。  - 参数要求：密码至少包含大写字母，小写字母，数字、特殊字符四类中的三类，其中可输入的特殊字符为：~!@#$%&*()-_=|[{}];:,<.>/?

        :return: The admin_pwd of this CreateClusterBody.
        :rtype: str
        """
        return self._admin_pwd

    @admin_pwd.setter
    def admin_pwd(self, admin_pwd):
        """Sets the admin_pwd of this CreateClusterBody.

        安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。  - 参数范围：8~32个字符。  - 参数要求：密码至少包含大写字母，小写字母，数字、特殊字符四类中的三类，其中可输入的特殊字符为：~!@#$%&*()-_=|[{}];:,<.>/?

        :param admin_pwd: The admin_pwd of this CreateClusterBody.
        :type admin_pwd: str
        """
        self._admin_pwd = admin_pwd

    @property
    def public_ip_req(self):
        """Gets the public_ip_req of this CreateClusterBody.

        :return: The public_ip_req of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterPublicIpReq`
        """
        return self._public_ip_req

    @public_ip_req.setter
    def public_ip_req(self, public_ip_req):
        """Sets the public_ip_req of this CreateClusterBody.

        :param public_ip_req: The public_ip_req of this CreateClusterBody.
        :type public_ip_req: :class:`huaweicloudsdkcss.v2.CreateClusterPublicIpReq`
        """
        self._public_ip_req = public_ip_req

    @property
    def load_balance(self):
        """Gets the load_balance of this CreateClusterBody.

        :return: The load_balance of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterLoadBalance`
        """
        return self._load_balance

    @load_balance.setter
    def load_balance(self, load_balance):
        """Sets the load_balance of this CreateClusterBody.

        :param load_balance: The load_balance of this CreateClusterBody.
        :type load_balance: :class:`huaweicloudsdkcss.v2.CreateClusterLoadBalance`
        """
        self._load_balance = load_balance

    @property
    def public_kibana_req(self):
        """Gets the public_kibana_req of this CreateClusterBody.

        :return: The public_kibana_req of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.CreateClusterPublicKibanaReq`
        """
        return self._public_kibana_req

    @public_kibana_req.setter
    def public_kibana_req(self, public_kibana_req):
        """Sets the public_kibana_req of this CreateClusterBody.

        :param public_kibana_req: The public_kibana_req of this CreateClusterBody.
        :type public_kibana_req: :class:`huaweicloudsdkcss.v2.CreateClusterPublicKibanaReq`
        """
        self._public_kibana_req = public_kibana_req

    @property
    def pay_info(self):
        """Gets the pay_info of this CreateClusterBody.

        :return: The pay_info of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v2.PayInfoBody`
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        """Sets the pay_info of this CreateClusterBody.

        :param pay_info: The pay_info of this CreateClusterBody.
        :type pay_info: :class:`huaweicloudsdkcss.v2.PayInfoBody`
        """
        self._pay_info = pay_info

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
        if not isinstance(other, CreateClusterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
