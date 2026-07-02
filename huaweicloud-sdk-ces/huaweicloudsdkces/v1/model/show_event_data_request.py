# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'dim_3': 'str',
        'type': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'dim_3': 'dim.3',
        'type': 'type',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, namespace=None, dim_0=None, dim_1=None, dim_2=None, dim_3=None, type=None, _from=None, to=None):
        r"""ShowEventDataRequest

        The model defined in huaweicloud sdk

        :param namespace: **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 
        :type namespace: str
        :param dim_0: **参数解释** 指标的第一层维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_0: str
        :param dim_1: **参数解释** 指标的第二层维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_1: str
        :param dim_2: **参数解释** 指标的第三层维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.2&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_2: str
        :param dim_3: **参数解释** 指标的第四层维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.3&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_3: str
        :param type: **参数解释** 事件类型 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,64]个字符 **默认取值** 不涉及 
        :type type: str
        :param _from: **参数解释** 查询数据起始时间，UNIX时间戳，单位毫秒 **约束限制** 不涉及 **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 
        :type _from: int
        :param to: **参数解释** 查询数据截止时间,UNIX时间戳，单位毫秒 **约束限制** from必须小于to **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 
        :type to: int
        """
        
        

        self._namespace = None
        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._dim_3 = None
        self._type = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.namespace = namespace
        self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        if dim_3 is not None:
            self.dim_3 = dim_3
        self.type = type
        self._from = _from
        self.to = to

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowEventDataRequest.

        **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 

        :return: The namespace of this ShowEventDataRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowEventDataRequest.

        **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 

        :param namespace: The namespace of this ShowEventDataRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dim_0(self):
        r"""Gets the dim_0 of this ShowEventDataRequest.

        **参数解释** 指标的第一层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_0 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        r"""Sets the dim_0 of this ShowEventDataRequest.

        **参数解释** 指标的第一层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_0: The dim_0 of this ShowEventDataRequest.
        :type dim_0: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        r"""Gets the dim_1 of this ShowEventDataRequest.

        **参数解释** 指标的第二层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_1 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        r"""Sets the dim_1 of this ShowEventDataRequest.

        **参数解释** 指标的第二层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_1: The dim_1 of this ShowEventDataRequest.
        :type dim_1: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        r"""Gets the dim_2 of this ShowEventDataRequest.

        **参数解释** 指标的第三层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.2=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_2 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        r"""Sets the dim_2 of this ShowEventDataRequest.

        **参数解释** 指标的第三层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.2=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_2: The dim_2 of this ShowEventDataRequest.
        :type dim_2: str
        """
        self._dim_2 = dim_2

    @property
    def dim_3(self):
        r"""Gets the dim_3 of this ShowEventDataRequest.

        **参数解释** 指标的第四层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.3=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_3 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_3

    @dim_3.setter
    def dim_3(self, dim_3):
        r"""Sets the dim_3 of this ShowEventDataRequest.

        **参数解释** 指标的第四层维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档 **约束限制** 不涉及 **取值范围** dim.3=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_3: The dim_3 of this ShowEventDataRequest.
        :type dim_3: str
        """
        self._dim_3 = dim_3

    @property
    def type(self):
        r"""Gets the type of this ShowEventDataRequest.

        **参数解释** 事件类型 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,64]个字符 **默认取值** 不涉及 

        :return: The type of this ShowEventDataRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowEventDataRequest.

        **参数解释** 事件类型 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,64]个字符 **默认取值** 不涉及 

        :param type: The type of this ShowEventDataRequest.
        :type type: str
        """
        self._type = type

    @property
    def _from(self):
        r"""Gets the _from of this ShowEventDataRequest.

        **参数解释** 查询数据起始时间，UNIX时间戳，单位毫秒 **约束限制** 不涉及 **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 

        :return: The _from of this ShowEventDataRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ShowEventDataRequest.

        **参数解释** 查询数据起始时间，UNIX时间戳，单位毫秒 **约束限制** 不涉及 **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 

        :param _from: The _from of this ShowEventDataRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ShowEventDataRequest.

        **参数解释** 查询数据截止时间,UNIX时间戳，单位毫秒 **约束限制** from必须小于to **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 

        :return: The to of this ShowEventDataRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ShowEventDataRequest.

        **参数解释** 查询数据截止时间,UNIX时间戳，单位毫秒 **约束限制** from必须小于to **取值范围** 毫秒级时间戳，范围为[0,9999999999999] **默认取值** 不涉及 

        :param to: The to of this ShowEventDataRequest.
        :type to: int
        """
        self._to = to

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowEventDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
