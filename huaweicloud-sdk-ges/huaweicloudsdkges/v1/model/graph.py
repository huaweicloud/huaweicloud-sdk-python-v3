# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Graph:

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
        'graph_size_type_index': 'str',
        'arch': 'str',
        'data_source': 'DataSource',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'public_ip': 'PublicIp',
        'enable_multi_az': 'bool',
        'encryption': 'EncryptionReq',
        'lts_operation_trace': 'LtsOperationTraceReq',
        'sys_tags': 'list[SysTagsRes]',
        'enable_rbac': 'bool',
        'enable_full_text_index': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'graph_size_type_index': 'graphSizeTypeIndex',
        'arch': 'arch',
        'data_source': 'dataSource',
        'vpc_id': 'vpcId',
        'subnet_id': 'subnetId',
        'security_group_id': 'securityGroupId',
        'public_ip': 'publicIp',
        'enable_multi_az': 'enableMultiAz',
        'encryption': 'encryption',
        'lts_operation_trace': 'ltsOperationTrace',
        'sys_tags': 'sys_tags',
        'enable_rbac': 'enableRBAC',
        'enable_full_text_index': 'enableFullTextIndex'
    }

    def __init__(self, name=None, graph_size_type_index=None, arch=None, data_source=None, vpc_id=None, subnet_id=None, security_group_id=None, public_ip=None, enable_multi_az=None, encryption=None, lts_operation_trace=None, sys_tags=None, enable_rbac=None, enable_full_text_index=None):
        r"""Graph

        The model defined in huaweicloud sdk

        :param name: 图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。
        :type name: str
        :param graph_size_type_index: 图规模类型索引。 - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 401：十亿增强边
        :type graph_size_type_index: str
        :param arch: 图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。 - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。
        :type arch: str
        :param data_source: 
        :type data_source: :class:`huaweicloudsdkges.v1.DataSource`
        :param vpc_id:   虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 指定虚拟私有云下的子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkges.v1.PublicIp`
        :param enable_multi_az: 创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。
        :type enable_multi_az: bool
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkges.v1.EncryptionReq`
        :param lts_operation_trace: 
        :type lts_operation_trace: :class:`huaweicloudsdkges.v1.LtsOperationTraceReq`
        :param sys_tags: 企业项目信息，如果未指定则不开启，默认不开启。
        :type sys_tags: list[:class:`huaweicloudsdkges.v1.SysTagsRes`]
        :param enable_rbac: 创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。
        :type enable_rbac: bool
        :param enable_full_text_index: 创建的图是否开启全文索引控制，默认不启用，值为false。如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 &gt;开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。
        :type enable_full_text_index: bool
        """
        
        

        self._name = None
        self._graph_size_type_index = None
        self._arch = None
        self._data_source = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._public_ip = None
        self._enable_multi_az = None
        self._encryption = None
        self._lts_operation_trace = None
        self._sys_tags = None
        self._enable_rbac = None
        self._enable_full_text_index = None
        self.discriminator = None

        self.name = name
        self.graph_size_type_index = graph_size_type_index
        if arch is not None:
            self.arch = arch
        if data_source is not None:
            self.data_source = data_source
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        if public_ip is not None:
            self.public_ip = public_ip
        if enable_multi_az is not None:
            self.enable_multi_az = enable_multi_az
        if encryption is not None:
            self.encryption = encryption
        if lts_operation_trace is not None:
            self.lts_operation_trace = lts_operation_trace
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if enable_rbac is not None:
            self.enable_rbac = enable_rbac
        if enable_full_text_index is not None:
            self.enable_full_text_index = enable_full_text_index

    @property
    def name(self):
        r"""Gets the name of this Graph.

        图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。

        :return: The name of this Graph.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Graph.

        图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。

        :param name: The name of this Graph.
        :type name: str
        """
        self._name = name

    @property
    def graph_size_type_index(self):
        r"""Gets the graph_size_type_index of this Graph.

        图规模类型索引。 - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 401：十亿增强边

        :return: The graph_size_type_index of this Graph.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        r"""Sets the graph_size_type_index of this Graph.

        图规模类型索引。 - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 401：十亿增强边

        :param graph_size_type_index: The graph_size_type_index of this Graph.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def arch(self):
        r"""Gets the arch of this Graph.

        图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。 - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。

        :return: The arch of this Graph.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this Graph.

        图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。 - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。

        :param arch: The arch of this Graph.
        :type arch: str
        """
        self._arch = arch

    @property
    def data_source(self):
        r"""Gets the data_source of this Graph.

        :return: The data_source of this Graph.
        :rtype: :class:`huaweicloudsdkges.v1.DataSource`
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this Graph.

        :param data_source: The data_source of this Graph.
        :type data_source: :class:`huaweicloudsdkges.v1.DataSource`
        """
        self._data_source = data_source

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Graph.

          虚拟私有云ID。

        :return: The vpc_id of this Graph.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Graph.

          虚拟私有云ID。

        :param vpc_id: The vpc_id of this Graph.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this Graph.

        指定虚拟私有云下的子网ID。

        :return: The subnet_id of this Graph.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this Graph.

        指定虚拟私有云下的子网ID。

        :param subnet_id: The subnet_id of this Graph.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this Graph.

        安全组ID。

        :return: The security_group_id of this Graph.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this Graph.

        安全组ID。

        :param security_group_id: The security_group_id of this Graph.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this Graph.

        :return: The public_ip of this Graph.
        :rtype: :class:`huaweicloudsdkges.v1.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this Graph.

        :param public_ip: The public_ip of this Graph.
        :type public_ip: :class:`huaweicloudsdkges.v1.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def enable_multi_az(self):
        r"""Gets the enable_multi_az of this Graph.

        创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。

        :return: The enable_multi_az of this Graph.
        :rtype: bool
        """
        return self._enable_multi_az

    @enable_multi_az.setter
    def enable_multi_az(self, enable_multi_az):
        r"""Sets the enable_multi_az of this Graph.

        创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。

        :param enable_multi_az: The enable_multi_az of this Graph.
        :type enable_multi_az: bool
        """
        self._enable_multi_az = enable_multi_az

    @property
    def encryption(self):
        r"""Gets the encryption of this Graph.

        :return: The encryption of this Graph.
        :rtype: :class:`huaweicloudsdkges.v1.EncryptionReq`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this Graph.

        :param encryption: The encryption of this Graph.
        :type encryption: :class:`huaweicloudsdkges.v1.EncryptionReq`
        """
        self._encryption = encryption

    @property
    def lts_operation_trace(self):
        r"""Gets the lts_operation_trace of this Graph.

        :return: The lts_operation_trace of this Graph.
        :rtype: :class:`huaweicloudsdkges.v1.LtsOperationTraceReq`
        """
        return self._lts_operation_trace

    @lts_operation_trace.setter
    def lts_operation_trace(self, lts_operation_trace):
        r"""Sets the lts_operation_trace of this Graph.

        :param lts_operation_trace: The lts_operation_trace of this Graph.
        :type lts_operation_trace: :class:`huaweicloudsdkges.v1.LtsOperationTraceReq`
        """
        self._lts_operation_trace = lts_operation_trace

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this Graph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :return: The sys_tags of this Graph.
        :rtype: list[:class:`huaweicloudsdkges.v1.SysTagsRes`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this Graph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :param sys_tags: The sys_tags of this Graph.
        :type sys_tags: list[:class:`huaweicloudsdkges.v1.SysTagsRes`]
        """
        self._sys_tags = sys_tags

    @property
    def enable_rbac(self):
        r"""Gets the enable_rbac of this Graph.

        创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。

        :return: The enable_rbac of this Graph.
        :rtype: bool
        """
        return self._enable_rbac

    @enable_rbac.setter
    def enable_rbac(self, enable_rbac):
        r"""Sets the enable_rbac of this Graph.

        创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。

        :param enable_rbac: The enable_rbac of this Graph.
        :type enable_rbac: bool
        """
        self._enable_rbac = enable_rbac

    @property
    def enable_full_text_index(self):
        r"""Gets the enable_full_text_index of this Graph.

        创建的图是否开启全文索引控制，默认不启用，值为false。如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 >开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。

        :return: The enable_full_text_index of this Graph.
        :rtype: bool
        """
        return self._enable_full_text_index

    @enable_full_text_index.setter
    def enable_full_text_index(self, enable_full_text_index):
        r"""Sets the enable_full_text_index of this Graph.

        创建的图是否开启全文索引控制，默认不启用，值为false。如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 >开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。

        :param enable_full_text_index: The enable_full_text_index of this Graph.
        :type enable_full_text_index: bool
        """
        self._enable_full_text_index = enable_full_text_index

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
        if not isinstance(other, Graph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
