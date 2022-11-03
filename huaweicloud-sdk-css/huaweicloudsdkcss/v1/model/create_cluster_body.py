# coding: utf-8

import re
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
        'instance': 'CreateClusterInstanceBody',
        'datastore': 'CreateClusterDatastoreBody',
        'name': 'str',
        'instance_num': 'int',
        'backup_strategy': 'CreateClusterBackupStrategyBody',
        'https_enable': 'bool',
        'authority_enable': 'bool',
        'admin_pwd': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[CreateClusterTagsBody]',
        'pay_info': 'PayInfoBody'
    }

    attribute_map = {
        'instance': 'instance',
        'datastore': 'datastore',
        'name': 'name',
        'instance_num': 'instanceNum',
        'backup_strategy': 'backupStrategy',
        'https_enable': 'httpsEnable',
        'authority_enable': 'authorityEnable',
        'admin_pwd': 'adminPwd',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'pay_info': 'payInfo'
    }

    def __init__(self, instance=None, datastore=None, name=None, instance_num=None, backup_strategy=None, https_enable=None, authority_enable=None, admin_pwd=None, enterprise_project_id=None, tags=None, pay_info=None):
        """CreateClusterBody

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceBody`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcss.v1.CreateClusterDatastoreBody`
        :param name: 集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。
        :type name: str
        :param instance_num: 集群实例个数，取值范围为1~32。
        :type instance_num: int
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkcss.v1.CreateClusterBackupStrategyBody`
        :param https_enable: 设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。  - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  &gt;此参数只有6.5.4及之后版本支持。
        :type https_enable: bool
        :param authority_enable: 是否开启认证，取值范围为true或false。默认关闭认证功能。  - true：表示集群开启认证。 - false：表示集群不开启认证。  &gt;此参数只有6.5.4及之后版本支持。
        :type authority_enable: bool
        :param admin_pwd: 安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。   - 管理员密码需要满足规则：    - 可输入的字符串长度为8-32个字符。    - 密码至少包含大写字母，小写字母，数字和特殊字符中的三类，其中可输入的特殊字符为：~!@#$%^&amp;*()-_&#x3D;+\\\\|[{}];:,&lt;.&gt;/?。   - 安全集群的密码会进行弱口令校验，建议设置安全性高的密码。
        :type admin_pwd: str
        :param enterprise_project_id: 企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\&quot;-\&quot;连字符的UUID格式，或者是字符串\&quot;0\&quot;。\&quot;0\&quot;表示默认企业项目。  关于企业项目ID的获取及企业项目特性的详细信息，请参见[[《企业管理服务用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hc,hws)[[《企业管理服务用户指南》](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hk,hws_hk)。
        :type enterprise_project_id: str
        :param tags: 集群标签。 关于标签特性的详细信息，请参见[[《标签管理服务介绍》](https://support.huaweicloud.com/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hc,hws)[[《标签管理服务介绍》](https://support.huaweicloud.com/intl/zh-cn/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hk,hws_hk)。
        :type tags: list[:class:`huaweicloudsdkcss.v1.CreateClusterTagsBody`]
        :param pay_info: 
        :type pay_info: :class:`huaweicloudsdkcss.v1.PayInfoBody`
        """
        
        

        self._instance = None
        self._datastore = None
        self._name = None
        self._instance_num = None
        self._backup_strategy = None
        self._https_enable = None
        self._authority_enable = None
        self._admin_pwd = None
        self._enterprise_project_id = None
        self._tags = None
        self._pay_info = None
        self.discriminator = None

        self.instance = instance
        self.datastore = datastore
        self.name = name
        self.instance_num = instance_num
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if https_enable is not None:
            self.https_enable = https_enable
        if authority_enable is not None:
            self.authority_enable = authority_enable
        if admin_pwd is not None:
            self.admin_pwd = admin_pwd
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if pay_info is not None:
            self.pay_info = pay_info

    @property
    def instance(self):
        """Gets the instance of this CreateClusterBody.


        :return: The instance of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceBody`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CreateClusterBody.


        :param instance: The instance of this CreateClusterBody.
        :type instance: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceBody`
        """
        self._instance = instance

    @property
    def datastore(self):
        """Gets the datastore of this CreateClusterBody.


        :return: The datastore of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterDatastoreBody`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateClusterBody.


        :param datastore: The datastore of this CreateClusterBody.
        :type datastore: :class:`huaweicloudsdkcss.v1.CreateClusterDatastoreBody`
        """
        self._datastore = datastore

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
    def instance_num(self):
        """Gets the instance_num of this CreateClusterBody.

        集群实例个数，取值范围为1~32。

        :return: The instance_num of this CreateClusterBody.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this CreateClusterBody.

        集群实例个数，取值范围为1~32。

        :param instance_num: The instance_num of this CreateClusterBody.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateClusterBody.


        :return: The backup_strategy of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterBackupStrategyBody`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateClusterBody.


        :param backup_strategy: The backup_strategy of this CreateClusterBody.
        :type backup_strategy: :class:`huaweicloudsdkcss.v1.CreateClusterBackupStrategyBody`
        """
        self._backup_strategy = backup_strategy

    @property
    def https_enable(self):
        """Gets the https_enable of this CreateClusterBody.

        设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。  - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  >此参数只有6.5.4及之后版本支持。

        :return: The https_enable of this CreateClusterBody.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this CreateClusterBody.

        设置是否进行通信加密。取值范围为true或false。默认关闭通信加密功能。当httpsEnable设置为true时，authorityEnable字段需要设置为true。  - true：表示集群进行通信加密。 - false：表示集群不进行通信加密。  >此参数只有6.5.4及之后版本支持。

        :param https_enable: The https_enable of this CreateClusterBody.
        :type https_enable: bool
        """
        self._https_enable = https_enable

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
    def admin_pwd(self):
        """Gets the admin_pwd of this CreateClusterBody.

        安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。   - 管理员密码需要满足规则：    - 可输入的字符串长度为8-32个字符。    - 密码至少包含大写字母，小写字母，数字和特殊字符中的三类，其中可输入的特殊字符为：~!@#$%^&*()-_=+\\\\|[{}];:,<.>/?。   - 安全集群的密码会进行弱口令校验，建议设置安全性高的密码。

        :return: The admin_pwd of this CreateClusterBody.
        :rtype: str
        """
        return self._admin_pwd

    @admin_pwd.setter
    def admin_pwd(self, admin_pwd):
        """Sets the admin_pwd of this CreateClusterBody.

        安全模式下集群管理员admin的密码，只有在创建集群时authorityEnable设置为true时需要设置此参数。   - 管理员密码需要满足规则：    - 可输入的字符串长度为8-32个字符。    - 密码至少包含大写字母，小写字母，数字和特殊字符中的三类，其中可输入的特殊字符为：~!@#$%^&*()-_=+\\\\|[{}];:,<.>/?。   - 安全集群的密码会进行弱口令校验，建议设置安全性高的密码。

        :param admin_pwd: The admin_pwd of this CreateClusterBody.
        :type admin_pwd: str
        """
        self._admin_pwd = admin_pwd

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。  关于企业项目ID的获取及企业项目特性的详细信息，请参见[[《企业管理服务用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hc,hws)[[《企业管理服务用户指南》](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hk,hws_hk)。

        :return: The enterprise_project_id of this CreateClusterBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。  关于企业项目ID的获取及企业项目特性的详细信息，请参见[[《企业管理服务用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hc,hws)[[《企业管理服务用户指南》](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hk,hws_hk)。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateClusterBody.

        集群标签。 关于标签特性的详细信息，请参见[[《标签管理服务介绍》](https://support.huaweicloud.com/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hc,hws)[[《标签管理服务介绍》](https://support.huaweicloud.com/intl/zh-cn/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hk,hws_hk)。

        :return: The tags of this CreateClusterBody.
        :rtype: list[:class:`huaweicloudsdkcss.v1.CreateClusterTagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClusterBody.

        集群标签。 关于标签特性的详细信息，请参见[[《标签管理服务介绍》](https://support.huaweicloud.com/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hc,hws)[[《标签管理服务介绍》](https://support.huaweicloud.com/intl/zh-cn/productdesc-tms/zh-cn_topic_0071335169.html)](tag:hk,hws_hk)。

        :param tags: The tags of this CreateClusterBody.
        :type tags: list[:class:`huaweicloudsdkcss.v1.CreateClusterTagsBody`]
        """
        self._tags = tags

    @property
    def pay_info(self):
        """Gets the pay_info of this CreateClusterBody.


        :return: The pay_info of this CreateClusterBody.
        :rtype: :class:`huaweicloudsdkcss.v1.PayInfoBody`
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        """Sets the pay_info of this CreateClusterBody.


        :param pay_info: The pay_info of this CreateClusterBody.
        :type pay_info: :class:`huaweicloudsdkcss.v1.PayInfoBody`
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
