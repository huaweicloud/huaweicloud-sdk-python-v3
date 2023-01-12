# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGraphReqGraph:

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'public_ip': 'CreateGraphReqGraphPublicIp',
        'enable_multi_az': 'bool',
        'encryption': 'CreateGraphReqGraphEncryption',
        'lts_operation_trace': 'CreateGraphReqGraphLtsOperationTrace',
        'sys_tags': 'list[CreateGraphReqGraphSysTags]',
        'tags': 'list[ListGraphsRespTags]',
        'enable_rbac': 'bool',
        'enable_full_text_index': 'bool',
        'enable_hyg': 'bool',
        'crypt_algorithm': 'str',
        'enable_https': 'bool',
        'product_type': 'str',
        'vertex_id_type': 'CreateGraphReqGraphVertexIdType'
    }

    attribute_map = {
        'name': 'name',
        'graph_size_type_index': 'graph_size_type_index',
        'arch': 'arch',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'public_ip': 'public_ip',
        'enable_multi_az': 'enable_multi_az',
        'encryption': 'encryption',
        'lts_operation_trace': 'lts_operation_trace',
        'sys_tags': 'sys_tags',
        'tags': 'tags',
        'enable_rbac': 'enable_rbac',
        'enable_full_text_index': 'enable_full_text_index',
        'enable_hyg': 'enable_hyg',
        'crypt_algorithm': 'crypt_algorithm',
        'enable_https': 'enable_https',
        'product_type': 'product_type',
        'vertex_id_type': 'vertex_id_type'
    }

    def __init__(self, name=None, graph_size_type_index=None, arch=None, vpc_id=None, subnet_id=None, security_group_id=None, public_ip=None, enable_multi_az=None, encryption=None, lts_operation_trace=None, sys_tags=None, tags=None, enable_rbac=None, enable_full_text_index=None, enable_hyg=None, crypt_algorithm=None, enable_https=None, product_type=None, vertex_id_type=None):
        """CreateGraphReqGraph

        The model defined in huaweicloud sdk

        :param name: 图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。
        :type name: str
        :param graph_size_type_index: 图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边
        :type graph_size_type_index: str
        :param arch: 图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。  - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。
        :type arch: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 指定虚拟私有云下的子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphPublicIp`
        :param enable_multi_az: 创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。
        :type enable_multi_az: bool
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphEncryption`
        :param lts_operation_trace: 
        :type lts_operation_trace: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphLtsOperationTrace`
        :param sys_tags: 企业项目信息，如果未指定则不开启，默认不开启。
        :type sys_tags: list[:class:`huaweicloudsdkges.v2.CreateGraphReqGraphSysTags`]
        :param tags: 支持标签TMS，做费用归集，默认不开启。
        :type tags: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        :param enable_rbac: 创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。
        :type enable_rbac: bool
        :param enable_full_text_index: 创建的图是否开启全文索引控制，默认不启用，值为false。 如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 &gt; 开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。
        :type enable_full_text_index: bool
        :param enable_hyg: 该参数只对千亿规格图生效。
        :type enable_hyg: bool
        :param crypt_algorithm: 图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）
        :type crypt_algorithm: str
        :param enable_https: 是否开启安全模式，开启安全模式会对性能有较大影响
        :type enable_https: bool
        :param product_type: 图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\&quot;6\&quot;时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版
        :type product_type: str
        :param vertex_id_type: 
        :type vertex_id_type: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphVertexIdType`
        """
        
        

        self._name = None
        self._graph_size_type_index = None
        self._arch = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._public_ip = None
        self._enable_multi_az = None
        self._encryption = None
        self._lts_operation_trace = None
        self._sys_tags = None
        self._tags = None
        self._enable_rbac = None
        self._enable_full_text_index = None
        self._enable_hyg = None
        self._crypt_algorithm = None
        self._enable_https = None
        self._product_type = None
        self._vertex_id_type = None
        self.discriminator = None

        self.name = name
        self.graph_size_type_index = graph_size_type_index
        if arch is not None:
            self.arch = arch
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
        if tags is not None:
            self.tags = tags
        if enable_rbac is not None:
            self.enable_rbac = enable_rbac
        if enable_full_text_index is not None:
            self.enable_full_text_index = enable_full_text_index
        if enable_hyg is not None:
            self.enable_hyg = enable_hyg
        self.crypt_algorithm = crypt_algorithm
        self.enable_https = enable_https
        if product_type is not None:
            self.product_type = product_type
        if vertex_id_type is not None:
            self.vertex_id_type = vertex_id_type

    @property
    def name(self):
        """Gets the name of this CreateGraphReqGraph.

        图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。

        :return: The name of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGraphReqGraph.

        图名称（输入长度在4位到50位之间，必须以字母开头，可以包含字母、数字或者下划线，不能包含其他的特殊字符）。

        :param name: The name of this CreateGraphReqGraph.
        :type name: str
        """
        self._name = name

    @property
    def graph_size_type_index(self):
        """Gets the graph_size_type_index of this CreateGraphReqGraph.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :return: The graph_size_type_index of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        """Sets the graph_size_type_index of this CreateGraphReqGraph.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :param graph_size_type_index: The graph_size_type_index of this CreateGraphReqGraph.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def arch(self):
        """Gets the arch of this CreateGraphReqGraph.

        图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。  - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。

        :return: The arch of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateGraphReqGraph.

        图实例CPU架构类型，取值为x86_64和aarch64。默认取x86_64。  - x86_64：X64 64位架构。 - aarch64：ARM 64位架构。

        :param arch: The arch of this CreateGraphReqGraph.
        :type arch: str
        """
        self._arch = arch

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateGraphReqGraph.

        虚拟私有云ID。

        :return: The vpc_id of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateGraphReqGraph.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this CreateGraphReqGraph.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateGraphReqGraph.

        指定虚拟私有云下的子网ID。

        :return: The subnet_id of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateGraphReqGraph.

        指定虚拟私有云下的子网ID。

        :param subnet_id: The subnet_id of this CreateGraphReqGraph.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateGraphReqGraph.

        安全组ID。

        :return: The security_group_id of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateGraphReqGraph.

        安全组ID。

        :param security_group_id: The security_group_id of this CreateGraphReqGraph.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def public_ip(self):
        """Gets the public_ip of this CreateGraphReqGraph.

        :return: The public_ip of this CreateGraphReqGraph.
        :rtype: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphPublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CreateGraphReqGraph.

        :param public_ip: The public_ip of this CreateGraphReqGraph.
        :type public_ip: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphPublicIp`
        """
        self._public_ip = public_ip

    @property
    def enable_multi_az(self):
        """Gets the enable_multi_az of this CreateGraphReqGraph.

        创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。

        :return: The enable_multi_az of this CreateGraphReqGraph.
        :rtype: bool
        """
        return self._enable_multi_az

    @enable_multi_az.setter
    def enable_multi_az(self, enable_multi_az):
        """Sets the enable_multi_az of this CreateGraphReqGraph.

        创建的图是否支持跨可用区（AZ），默认值是false，如果设置为true，系统将会把图中的ECS建在两个可用区中。  如果创建图时，不加该参数，则会将图中的ECS都建在一个可用区中。

        :param enable_multi_az: The enable_multi_az of this CreateGraphReqGraph.
        :type enable_multi_az: bool
        """
        self._enable_multi_az = enable_multi_az

    @property
    def encryption(self):
        """Gets the encryption of this CreateGraphReqGraph.

        :return: The encryption of this CreateGraphReqGraph.
        :rtype: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphEncryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this CreateGraphReqGraph.

        :param encryption: The encryption of this CreateGraphReqGraph.
        :type encryption: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphEncryption`
        """
        self._encryption = encryption

    @property
    def lts_operation_trace(self):
        """Gets the lts_operation_trace of this CreateGraphReqGraph.

        :return: The lts_operation_trace of this CreateGraphReqGraph.
        :rtype: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphLtsOperationTrace`
        """
        return self._lts_operation_trace

    @lts_operation_trace.setter
    def lts_operation_trace(self, lts_operation_trace):
        """Sets the lts_operation_trace of this CreateGraphReqGraph.

        :param lts_operation_trace: The lts_operation_trace of this CreateGraphReqGraph.
        :type lts_operation_trace: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphLtsOperationTrace`
        """
        self._lts_operation_trace = lts_operation_trace

    @property
    def sys_tags(self):
        """Gets the sys_tags of this CreateGraphReqGraph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :return: The sys_tags of this CreateGraphReqGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.CreateGraphReqGraphSysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this CreateGraphReqGraph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :param sys_tags: The sys_tags of this CreateGraphReqGraph.
        :type sys_tags: list[:class:`huaweicloudsdkges.v2.CreateGraphReqGraphSysTags`]
        """
        self._sys_tags = sys_tags

    @property
    def tags(self):
        """Gets the tags of this CreateGraphReqGraph.

        支持标签TMS，做费用归集，默认不开启。

        :return: The tags of this CreateGraphReqGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateGraphReqGraph.

        支持标签TMS，做费用归集，默认不开启。

        :param tags: The tags of this CreateGraphReqGraph.
        :type tags: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        self._tags = tags

    @property
    def enable_rbac(self):
        """Gets the enable_rbac of this CreateGraphReqGraph.

        创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。

        :return: The enable_rbac of this CreateGraphReqGraph.
        :rtype: bool
        """
        return self._enable_rbac

    @enable_rbac.setter
    def enable_rbac(self, enable_rbac):
        """Sets the enable_rbac of this CreateGraphReqGraph.

        创建的图是否启用细粒度权限控制，默认不启用，值为false。如果设置为true，创建的图所有用户都没有权限，需要调用业务面细粒度权限控制API进行授权操作才可以访问图。

        :param enable_rbac: The enable_rbac of this CreateGraphReqGraph.
        :type enable_rbac: bool
        """
        self._enable_rbac = enable_rbac

    @property
    def enable_full_text_index(self):
        """Gets the enable_full_text_index of this CreateGraphReqGraph.

        创建的图是否开启全文索引控制，默认不启用，值为false。 如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 > 开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。

        :return: The enable_full_text_index of this CreateGraphReqGraph.
        :rtype: bool
        """
        return self._enable_full_text_index

    @enable_full_text_index.setter
    def enable_full_text_index(self, enable_full_text_index):
        """Sets the enable_full_text_index of this CreateGraphReqGraph.

        创建的图是否开启全文索引控制，默认不启用，值为false。 如果设置为true，十亿增强版-规格版图支持全文索引，创建图时会创建云搜索服务集群。 > 开启全文索引功能。如果CSS服务已经部署，图实例会自动创建CSS集群，图创建时间较长。如果CSS服务没有部署则图创建失败。

        :param enable_full_text_index: The enable_full_text_index of this CreateGraphReqGraph.
        :type enable_full_text_index: bool
        """
        self._enable_full_text_index = enable_full_text_index

    @property
    def enable_hyg(self):
        """Gets the enable_hyg of this CreateGraphReqGraph.

        该参数只对千亿规格图生效。

        :return: The enable_hyg of this CreateGraphReqGraph.
        :rtype: bool
        """
        return self._enable_hyg

    @enable_hyg.setter
    def enable_hyg(self, enable_hyg):
        """Sets the enable_hyg of this CreateGraphReqGraph.

        该参数只对千亿规格图生效。

        :param enable_hyg: The enable_hyg of this CreateGraphReqGraph.
        :type enable_hyg: bool
        """
        self._enable_hyg = enable_hyg

    @property
    def crypt_algorithm(self):
        """Gets the crypt_algorithm of this CreateGraphReqGraph.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :return: The crypt_algorithm of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        """Sets the crypt_algorithm of this CreateGraphReqGraph.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :param crypt_algorithm: The crypt_algorithm of this CreateGraphReqGraph.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

    @property
    def enable_https(self):
        """Gets the enable_https of this CreateGraphReqGraph.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :return: The enable_https of this CreateGraphReqGraph.
        :rtype: bool
        """
        return self._enable_https

    @enable_https.setter
    def enable_https(self, enable_https):
        """Sets the enable_https of this CreateGraphReqGraph.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :param enable_https: The enable_https of this CreateGraphReqGraph.
        :type enable_https: bool
        """
        self._enable_https = enable_https

    @property
    def product_type(self):
        """Gets the product_type of this CreateGraphReqGraph.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :return: The product_type of this CreateGraphReqGraph.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this CreateGraphReqGraph.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :param product_type: The product_type of this CreateGraphReqGraph.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def vertex_id_type(self):
        """Gets the vertex_id_type of this CreateGraphReqGraph.

        :return: The vertex_id_type of this CreateGraphReqGraph.
        :rtype: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphVertexIdType`
        """
        return self._vertex_id_type

    @vertex_id_type.setter
    def vertex_id_type(self, vertex_id_type):
        """Sets the vertex_id_type of this CreateGraphReqGraph.

        :param vertex_id_type: The vertex_id_type of this CreateGraphReqGraph.
        :type vertex_id_type: :class:`huaweicloudsdkges.v2.CreateGraphReqGraphVertexIdType`
        """
        self._vertex_id_type = vertex_id_type

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
        if not isinstance(other, CreateGraphReqGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
