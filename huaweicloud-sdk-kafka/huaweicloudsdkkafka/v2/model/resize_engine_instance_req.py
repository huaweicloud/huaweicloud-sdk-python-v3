# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeEngineInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oper_type': 'str',
        'new_storage_space': 'int',
        'new_broker_num': 'int',
        'new_product_id': 'str',
        'publicip_id': 'str',
        'tenant_ips': 'list[str]',
        'second_tenant_subnet_id': 'str'
    }

    attribute_map = {
        'oper_type': 'oper_type',
        'new_storage_space': 'new_storage_space',
        'new_broker_num': 'new_broker_num',
        'new_product_id': 'new_product_id',
        'publicip_id': 'publicip_id',
        'tenant_ips': 'tenant_ips',
        'second_tenant_subnet_id': 'second_tenant_subnet_id'
    }

    def __init__(self, oper_type=None, new_storage_space=None, new_broker_num=None, new_product_id=None, publicip_id=None, tenant_ips=None, second_tenant_subnet_id=None):
        """ResizeEngineInstanceReq

        The model defined in huaweicloud sdk

        :param oper_type: 变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。
        :type oper_type: str
        :param new_storage_space: 扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 &#x3D; 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。
        :type new_storage_space: int
        :param new_broker_num: 当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。
        :type new_broker_num: int
        :param new_product_id: 垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。
        :type new_product_id: str
        :param publicip_id: 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  当oper_type类型是horizontal时，该参数必填。
        :type publicip_id: str
        :param tenant_ips: 指定的内网IP地址，仅支持指定IPv4。  指定的IP数量只能小于等于新增节点数量。  当指定IP小于节点数量时，未指定的节点随机分配内网IP地址。
        :type tenant_ips: list[str]
        :param second_tenant_subnet_id: 实例扩容时新节点使用备用子网的id  当实例扩容使用备用子网，则传入此值  需要联系客服添加白名单才能传入此值
        :type second_tenant_subnet_id: str
        """
        
        

        self._oper_type = None
        self._new_storage_space = None
        self._new_broker_num = None
        self._new_product_id = None
        self._publicip_id = None
        self._tenant_ips = None
        self._second_tenant_subnet_id = None
        self.discriminator = None

        self.oper_type = oper_type
        if new_storage_space is not None:
            self.new_storage_space = new_storage_space
        if new_broker_num is not None:
            self.new_broker_num = new_broker_num
        if new_product_id is not None:
            self.new_product_id = new_product_id
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if tenant_ips is not None:
            self.tenant_ips = tenant_ips
        if second_tenant_subnet_id is not None:
            self.second_tenant_subnet_id = second_tenant_subnet_id

    @property
    def oper_type(self):
        """Gets the oper_type of this ResizeEngineInstanceReq.

        变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。

        :return: The oper_type of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._oper_type

    @oper_type.setter
    def oper_type(self, oper_type):
        """Sets the oper_type of this ResizeEngineInstanceReq.

        变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。

        :param oper_type: The oper_type of this ResizeEngineInstanceReq.
        :type oper_type: str
        """
        self._oper_type = oper_type

    @property
    def new_storage_space(self):
        """Gets the new_storage_space of this ResizeEngineInstanceReq.

        扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 = 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。

        :return: The new_storage_space of this ResizeEngineInstanceReq.
        :rtype: int
        """
        return self._new_storage_space

    @new_storage_space.setter
    def new_storage_space(self, new_storage_space):
        """Sets the new_storage_space of this ResizeEngineInstanceReq.

        扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 = 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。

        :param new_storage_space: The new_storage_space of this ResizeEngineInstanceReq.
        :type new_storage_space: int
        """
        self._new_storage_space = new_storage_space

    @property
    def new_broker_num(self):
        """Gets the new_broker_num of this ResizeEngineInstanceReq.

        当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。

        :return: The new_broker_num of this ResizeEngineInstanceReq.
        :rtype: int
        """
        return self._new_broker_num

    @new_broker_num.setter
    def new_broker_num(self, new_broker_num):
        """Sets the new_broker_num of this ResizeEngineInstanceReq.

        当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。

        :param new_broker_num: The new_broker_num of this ResizeEngineInstanceReq.
        :type new_broker_num: int
        """
        self._new_broker_num = new_broker_num

    @property
    def new_product_id(self):
        """Gets the new_product_id of this ResizeEngineInstanceReq.

        垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。

        :return: The new_product_id of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._new_product_id

    @new_product_id.setter
    def new_product_id(self, new_product_id):
        """Sets the new_product_id of this ResizeEngineInstanceReq.

        垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。  产品ID可以从[查询产品规格列表](ListEngineProducts.xml)获取。

        :param new_product_id: The new_product_id of this ResizeEngineInstanceReq.
        :type new_product_id: str
        """
        self._new_product_id = new_product_id

    @property
    def publicip_id(self):
        """Gets the publicip_id of this ResizeEngineInstanceReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  当oper_type类型是horizontal时，该参数必填。

        :return: The publicip_id of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this ResizeEngineInstanceReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  当oper_type类型是horizontal时，该参数必填。

        :param publicip_id: The publicip_id of this ResizeEngineInstanceReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def tenant_ips(self):
        """Gets the tenant_ips of this ResizeEngineInstanceReq.

        指定的内网IP地址，仅支持指定IPv4。  指定的IP数量只能小于等于新增节点数量。  当指定IP小于节点数量时，未指定的节点随机分配内网IP地址。

        :return: The tenant_ips of this ResizeEngineInstanceReq.
        :rtype: list[str]
        """
        return self._tenant_ips

    @tenant_ips.setter
    def tenant_ips(self, tenant_ips):
        """Sets the tenant_ips of this ResizeEngineInstanceReq.

        指定的内网IP地址，仅支持指定IPv4。  指定的IP数量只能小于等于新增节点数量。  当指定IP小于节点数量时，未指定的节点随机分配内网IP地址。

        :param tenant_ips: The tenant_ips of this ResizeEngineInstanceReq.
        :type tenant_ips: list[str]
        """
        self._tenant_ips = tenant_ips

    @property
    def second_tenant_subnet_id(self):
        """Gets the second_tenant_subnet_id of this ResizeEngineInstanceReq.

        实例扩容时新节点使用备用子网的id  当实例扩容使用备用子网，则传入此值  需要联系客服添加白名单才能传入此值

        :return: The second_tenant_subnet_id of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._second_tenant_subnet_id

    @second_tenant_subnet_id.setter
    def second_tenant_subnet_id(self, second_tenant_subnet_id):
        """Sets the second_tenant_subnet_id of this ResizeEngineInstanceReq.

        实例扩容时新节点使用备用子网的id  当实例扩容使用备用子网，则传入此值  需要联系客服添加白名单才能传入此值

        :param second_tenant_subnet_id: The second_tenant_subnet_id of this ResizeEngineInstanceReq.
        :type second_tenant_subnet_id: str
        """
        self._second_tenant_subnet_id = second_tenant_subnet_id

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
        if not isinstance(other, ResizeEngineInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
