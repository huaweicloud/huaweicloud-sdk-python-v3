# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'object_id': 'str',
        'key_word': 'str',
        'domain_set_type': 'int',
        'config_status': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'object_id': 'object_id',
        'key_word': 'key_word',
        'domain_set_type': 'domain_set_type',
        'config_status': 'config_status'
    }

    def __init__(self, enterprise_project_id=None, fw_instance_id=None, limit=None, offset=None, object_id=None, key_word=None, domain_set_type=None, config_status=None):
        r"""ListDomainSetsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param key_word: 关键字，可使用域名组名称或描述
        :type key_word: str
        :param domain_set_type: 域名组类型，0表示应用域名组，1表示网络域名组
        :type domain_set_type: int
        :param config_status: 配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常
        :type config_status: int
        """
        
        

        self._enterprise_project_id = None
        self._fw_instance_id = None
        self._limit = None
        self._offset = None
        self._object_id = None
        self._key_word = None
        self._domain_set_type = None
        self._config_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.fw_instance_id = fw_instance_id
        self.limit = limit
        self.offset = offset
        self.object_id = object_id
        if key_word is not None:
            self.key_word = key_word
        if domain_set_type is not None:
            self.domain_set_type = domain_set_type
        if config_status is not None:
            self.config_status = config_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDomainSetsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListDomainSetsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDomainSetsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListDomainSetsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListDomainSetsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListDomainSetsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListDomainSetsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListDomainSetsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListDomainSetsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListDomainSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDomainSetsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListDomainSetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDomainSetsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListDomainSetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDomainSetsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListDomainSetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def object_id(self):
        r"""Gets the object_id of this ListDomainSetsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this ListDomainSetsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListDomainSetsRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this ListDomainSetsRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def key_word(self):
        r"""Gets the key_word of this ListDomainSetsRequest.

        关键字，可使用域名组名称或描述

        :return: The key_word of this ListDomainSetsRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListDomainSetsRequest.

        关键字，可使用域名组名称或描述

        :param key_word: The key_word of this ListDomainSetsRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def domain_set_type(self):
        r"""Gets the domain_set_type of this ListDomainSetsRequest.

        域名组类型，0表示应用域名组，1表示网络域名组

        :return: The domain_set_type of this ListDomainSetsRequest.
        :rtype: int
        """
        return self._domain_set_type

    @domain_set_type.setter
    def domain_set_type(self, domain_set_type):
        r"""Sets the domain_set_type of this ListDomainSetsRequest.

        域名组类型，0表示应用域名组，1表示网络域名组

        :param domain_set_type: The domain_set_type of this ListDomainSetsRequest.
        :type domain_set_type: int
        """
        self._domain_set_type = domain_set_type

    @property
    def config_status(self):
        r"""Gets the config_status of this ListDomainSetsRequest.

        配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常

        :return: The config_status of this ListDomainSetsRequest.
        :rtype: int
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ListDomainSetsRequest.

        配置状态，-1表示未配置态，0表示配置失败，1表示配置成功，2表示配置中，3表示正常，4表示配置异常

        :param config_status: The config_status of this ListDomainSetsRequest.
        :type config_status: int
        """
        self._config_status = config_status

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
        if not isinstance(other, ListDomainSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
