# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpsRules1Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affected_application_like': 'int',
        'create_time': 'int',
        'fw_instance_id': 'str',
        'ips_cve_like': 'int',
        'ips_group': 'int',
        'ips_id': 'str',
        'ips_level': 'int',
        'ips_name_like': 'str',
        'ips_rules_type_like': 'int',
        'ips_status': 'str',
        'is_updated_ips_rule_queried': 'bool',
        'limit': 'int',
        'object_id': 'str',
        'offset': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'affected_application_like': 'affected_application_like',
        'create_time': 'create_time',
        'fw_instance_id': 'fw_instance_id',
        'ips_cve_like': 'ips_cve_like',
        'ips_group': 'ips_group',
        'ips_id': 'ips_id',
        'ips_level': 'ips_level',
        'ips_name_like': 'ips_name_like',
        'ips_rules_type_like': 'ips_rules_type_like',
        'ips_status': 'ips_status',
        'is_updated_ips_rule_queried': 'is_updated_ips_rule_queried',
        'limit': 'limit',
        'object_id': 'object_id',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, affected_application_like=None, create_time=None, fw_instance_id=None, ips_cve_like=None, ips_group=None, ips_id=None, ips_level=None, ips_name_like=None, ips_rules_type_like=None, ips_status=None, is_updated_ips_rule_queried=None, limit=None, object_id=None, offset=None, enterprise_project_id=None):
        r"""ListIpsRules1Request

        The model defined in huaweicloud sdk

        :param affected_application_like: 攻击对象
        :type affected_application_like: int
        :param create_time: 创建时间
        :type create_time: int
        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param ips_cve_like: cve
        :type ips_cve_like: int
        :param ips_group: ips组
        :type ips_group: int
        :param ips_id: ips规则id
        :type ips_id: str
        :param ips_level: ips等级
        :type ips_level: int
        :param ips_name_like: ips规则名称
        :type ips_name_like: str
        :param ips_rules_type_like: ips规则类型
        :type ips_rules_type_like: int
        :param ips_status: ips规则状态
        :type ips_status: str
        :param is_updated_ips_rule_queried: 是否查新更新规则
        :type is_updated_ips_rule_queried: bool
        :param limit: 分页查询数据量限制
        :type limit: int
        :param object_id: 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param offset: 查询偏移量
        :type offset: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._affected_application_like = None
        self._create_time = None
        self._fw_instance_id = None
        self._ips_cve_like = None
        self._ips_group = None
        self._ips_id = None
        self._ips_level = None
        self._ips_name_like = None
        self._ips_rules_type_like = None
        self._ips_status = None
        self._is_updated_ips_rule_queried = None
        self._limit = None
        self._object_id = None
        self._offset = None
        self._enterprise_project_id = None
        self.discriminator = None

        if affected_application_like is not None:
            self.affected_application_like = affected_application_like
        if create_time is not None:
            self.create_time = create_time
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if ips_cve_like is not None:
            self.ips_cve_like = ips_cve_like
        if ips_group is not None:
            self.ips_group = ips_group
        if ips_id is not None:
            self.ips_id = ips_id
        if ips_level is not None:
            self.ips_level = ips_level
        if ips_name_like is not None:
            self.ips_name_like = ips_name_like
        if ips_rules_type_like is not None:
            self.ips_rules_type_like = ips_rules_type_like
        if ips_status is not None:
            self.ips_status = ips_status
        if is_updated_ips_rule_queried is not None:
            self.is_updated_ips_rule_queried = is_updated_ips_rule_queried
        self.limit = limit
        self.object_id = object_id
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def affected_application_like(self):
        r"""Gets the affected_application_like of this ListIpsRules1Request.

        攻击对象

        :return: The affected_application_like of this ListIpsRules1Request.
        :rtype: int
        """
        return self._affected_application_like

    @affected_application_like.setter
    def affected_application_like(self, affected_application_like):
        r"""Sets the affected_application_like of this ListIpsRules1Request.

        攻击对象

        :param affected_application_like: The affected_application_like of this ListIpsRules1Request.
        :type affected_application_like: int
        """
        self._affected_application_like = affected_application_like

    @property
    def create_time(self):
        r"""Gets the create_time of this ListIpsRules1Request.

        创建时间

        :return: The create_time of this ListIpsRules1Request.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListIpsRules1Request.

        创建时间

        :param create_time: The create_time of this ListIpsRules1Request.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListIpsRules1Request.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListIpsRules1Request.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListIpsRules1Request.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListIpsRules1Request.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def ips_cve_like(self):
        r"""Gets the ips_cve_like of this ListIpsRules1Request.

        cve

        :return: The ips_cve_like of this ListIpsRules1Request.
        :rtype: int
        """
        return self._ips_cve_like

    @ips_cve_like.setter
    def ips_cve_like(self, ips_cve_like):
        r"""Sets the ips_cve_like of this ListIpsRules1Request.

        cve

        :param ips_cve_like: The ips_cve_like of this ListIpsRules1Request.
        :type ips_cve_like: int
        """
        self._ips_cve_like = ips_cve_like

    @property
    def ips_group(self):
        r"""Gets the ips_group of this ListIpsRules1Request.

        ips组

        :return: The ips_group of this ListIpsRules1Request.
        :rtype: int
        """
        return self._ips_group

    @ips_group.setter
    def ips_group(self, ips_group):
        r"""Sets the ips_group of this ListIpsRules1Request.

        ips组

        :param ips_group: The ips_group of this ListIpsRules1Request.
        :type ips_group: int
        """
        self._ips_group = ips_group

    @property
    def ips_id(self):
        r"""Gets the ips_id of this ListIpsRules1Request.

        ips规则id

        :return: The ips_id of this ListIpsRules1Request.
        :rtype: str
        """
        return self._ips_id

    @ips_id.setter
    def ips_id(self, ips_id):
        r"""Sets the ips_id of this ListIpsRules1Request.

        ips规则id

        :param ips_id: The ips_id of this ListIpsRules1Request.
        :type ips_id: str
        """
        self._ips_id = ips_id

    @property
    def ips_level(self):
        r"""Gets the ips_level of this ListIpsRules1Request.

        ips等级

        :return: The ips_level of this ListIpsRules1Request.
        :rtype: int
        """
        return self._ips_level

    @ips_level.setter
    def ips_level(self, ips_level):
        r"""Sets the ips_level of this ListIpsRules1Request.

        ips等级

        :param ips_level: The ips_level of this ListIpsRules1Request.
        :type ips_level: int
        """
        self._ips_level = ips_level

    @property
    def ips_name_like(self):
        r"""Gets the ips_name_like of this ListIpsRules1Request.

        ips规则名称

        :return: The ips_name_like of this ListIpsRules1Request.
        :rtype: str
        """
        return self._ips_name_like

    @ips_name_like.setter
    def ips_name_like(self, ips_name_like):
        r"""Sets the ips_name_like of this ListIpsRules1Request.

        ips规则名称

        :param ips_name_like: The ips_name_like of this ListIpsRules1Request.
        :type ips_name_like: str
        """
        self._ips_name_like = ips_name_like

    @property
    def ips_rules_type_like(self):
        r"""Gets the ips_rules_type_like of this ListIpsRules1Request.

        ips规则类型

        :return: The ips_rules_type_like of this ListIpsRules1Request.
        :rtype: int
        """
        return self._ips_rules_type_like

    @ips_rules_type_like.setter
    def ips_rules_type_like(self, ips_rules_type_like):
        r"""Sets the ips_rules_type_like of this ListIpsRules1Request.

        ips规则类型

        :param ips_rules_type_like: The ips_rules_type_like of this ListIpsRules1Request.
        :type ips_rules_type_like: int
        """
        self._ips_rules_type_like = ips_rules_type_like

    @property
    def ips_status(self):
        r"""Gets the ips_status of this ListIpsRules1Request.

        ips规则状态

        :return: The ips_status of this ListIpsRules1Request.
        :rtype: str
        """
        return self._ips_status

    @ips_status.setter
    def ips_status(self, ips_status):
        r"""Sets the ips_status of this ListIpsRules1Request.

        ips规则状态

        :param ips_status: The ips_status of this ListIpsRules1Request.
        :type ips_status: str
        """
        self._ips_status = ips_status

    @property
    def is_updated_ips_rule_queried(self):
        r"""Gets the is_updated_ips_rule_queried of this ListIpsRules1Request.

        是否查新更新规则

        :return: The is_updated_ips_rule_queried of this ListIpsRules1Request.
        :rtype: bool
        """
        return self._is_updated_ips_rule_queried

    @is_updated_ips_rule_queried.setter
    def is_updated_ips_rule_queried(self, is_updated_ips_rule_queried):
        r"""Sets the is_updated_ips_rule_queried of this ListIpsRules1Request.

        是否查新更新规则

        :param is_updated_ips_rule_queried: The is_updated_ips_rule_queried of this ListIpsRules1Request.
        :type is_updated_ips_rule_queried: bool
        """
        self._is_updated_ips_rule_queried = is_updated_ips_rule_queried

    @property
    def limit(self):
        r"""Gets the limit of this ListIpsRules1Request.

        分页查询数据量限制

        :return: The limit of this ListIpsRules1Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpsRules1Request.

        分页查询数据量限制

        :param limit: The limit of this ListIpsRules1Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def object_id(self):
        r"""Gets the object_id of this ListIpsRules1Request.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this ListIpsRules1Request.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListIpsRules1Request.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this ListIpsRules1Request.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def offset(self):
        r"""Gets the offset of this ListIpsRules1Request.

        查询偏移量

        :return: The offset of this ListIpsRules1Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIpsRules1Request.

        查询偏移量

        :param offset: The offset of this ListIpsRules1Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIpsRules1Request.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListIpsRules1Request.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIpsRules1Request.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListIpsRules1Request.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListIpsRules1Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
