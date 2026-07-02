# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsRequest:

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
        'metric_name': 'str',
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'dim_3': 'str',
        'start': 'str',
        'limit': 'int',
        'order': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'dim_3': 'dim.3',
        'start': 'start',
        'limit': 'limit',
        'order': 'order'
    }

    def __init__(self, namespace=None, metric_name=None, dim_0=None, dim_1=None, dim_2=None, dim_3=None, start=None, limit=None, order=None):
        r"""ListMetricsRequest

        The model defined in huaweicloud sdk

        :param namespace: **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 
        :type namespace: str
        :param metric_name: **参数解释** 资源的监控指标名称，样例：弹性云服务器监控指标中的cpu_util。 各服务资源的指标名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符 （-），长度为[1,96]个字符 **默认取值** 不涉及 
        :type metric_name: str
        :param dim_0: **参数解释** 指标的第一个维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_0: str
        :param dim_1: **参数解释** 指标的第二个维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_1: str
        :param dim_2: **参数解释** 指标的第三个维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.2&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_2: str
        :param dim_3: **参数解释** 指标的第四个维度，目前最多支持4个维度，维度格式为dim.{i}&#x3D;key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.3&#x3D;key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 
        :type dim_3: str
        :param start: **参数解释** 分页起始值，格式为：namespace.metric_name.key:value 例如：start&#x3D;SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d **约束限制** 不涉及 **取值范围** 首次传空字符串，后续请求传递上一页返回值内的marker字段，作为下一页请求的分页起始值 **默认取值** 不涉及 
        :type start: str
        :param limit: **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** 条数限制为[1,1000] **默认取值** 1000 
        :type limit: int
        :param order: **参数解释** 用于标识结果的排序方法 **约束限制** 不涉及 **取值范围** 枚举值： - asc 升序 - desc 降序 **默认取值** asc 
        :type order: str
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._dim_3 = None
        self._start = None
        self._limit = None
        self._order = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dim_0 is not None:
            self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        if dim_3 is not None:
            self.dim_3 = dim_3
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order

    @property
    def namespace(self):
        r"""Gets the namespace of this ListMetricsRequest.

        **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 

        :return: The namespace of this ListMetricsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListMetricsRequest.

        **参数解释** 服务命名空间，样例：弹性云服务器的命名空间为SYS.ECS。 各服务命名空间请参阅[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)。 **约束限制** 不涉及 **取值范围** 格式为service.item，service和item以点号拼接组成。 service和item必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_），长度为[3,32]个字符 **默认取值** 不涉及 

        :param namespace: The namespace of this ListMetricsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ListMetricsRequest.

        **参数解释** 资源的监控指标名称，样例：弹性云服务器监控指标中的cpu_util。 各服务资源的指标名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符 （-），长度为[1,96]个字符 **默认取值** 不涉及 

        :return: The metric_name of this ListMetricsRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListMetricsRequest.

        **参数解释** 资源的监控指标名称，样例：弹性云服务器监控指标中的cpu_util。 各服务资源的指标名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** 必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符 （-），长度为[1,96]个字符 **默认取值** 不涉及 

        :param metric_name: The metric_name of this ListMetricsRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dim_0(self):
        r"""Gets the dim_0 of this ListMetricsRequest.

        **参数解释** 指标的第一个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_0 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        r"""Sets the dim_0 of this ListMetricsRequest.

        **参数解释** 指标的第一个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.0=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_0: The dim_0 of this ListMetricsRequest.
        :type dim_0: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        r"""Gets the dim_1 of this ListMetricsRequest.

        **参数解释** 指标的第二个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_1 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        r"""Sets the dim_1 of this ListMetricsRequest.

        **参数解释** 指标的第二个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.1=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_1: The dim_1 of this ListMetricsRequest.
        :type dim_1: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        r"""Gets the dim_2 of this ListMetricsRequest.

        **参数解释** 指标的第三个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.2=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_2 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        r"""Sets the dim_2 of this ListMetricsRequest.

        **参数解释** 指标的第三个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.2=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_2: The dim_2 of this ListMetricsRequest.
        :type dim_2: str
        """
        self._dim_2 = dim_2

    @property
    def dim_3(self):
        r"""Gets the dim_3 of this ListMetricsRequest.

        **参数解释** 指标的第四个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.3=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :return: The dim_3 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim_3

    @dim_3.setter
    def dim_3(self, dim_3):
        r"""Sets the dim_3 of this ListMetricsRequest.

        **参数解释** 指标的第四个维度，目前最多支持4个维度，维度格式为dim.{i}=key,value。样例：instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 各服务资源的维度名称，请参阅具体云服务的文档。您可以直接从[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/zh-cn/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)页面导航至相应文档。 **约束限制** 不涉及 **取值范围** dim.3=key,value，由key、value以逗号拼接组成。 key必须以字母（大写或小写）开头，后面可以跟零个或多个字母（大写或小写）、数字、下划线（_）、连字符（-），长度为[1,32]个字符 value由多个字母（大写或小写）、数字、下划线（_）、连字符（-）、点（.）、斜杠（/）、井号（#）、英文左括号（(）、英文右括号（)）组合而成，首个字符可以包含星号（*），但不能以连字符（-）开头，长度为[1,256]个字符 **默认取值** 不涉及 

        :param dim_3: The dim_3 of this ListMetricsRequest.
        :type dim_3: str
        """
        self._dim_3 = dim_3

    @property
    def start(self):
        r"""Gets the start of this ListMetricsRequest.

        **参数解释** 分页起始值，格式为：namespace.metric_name.key:value 例如：start=SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d **约束限制** 不涉及 **取值范围** 首次传空字符串，后续请求传递上一页返回值内的marker字段，作为下一页请求的分页起始值 **默认取值** 不涉及 

        :return: The start of this ListMetricsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListMetricsRequest.

        **参数解释** 分页起始值，格式为：namespace.metric_name.key:value 例如：start=SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d **约束限制** 不涉及 **取值范围** 首次传空字符串，后续请求传递上一页返回值内的marker字段，作为下一页请求的分页起始值 **默认取值** 不涉及 

        :param start: The start of this ListMetricsRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListMetricsRequest.

        **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** 条数限制为[1,1000] **默认取值** 1000 

        :return: The limit of this ListMetricsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMetricsRequest.

        **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** 条数限制为[1,1000] **默认取值** 1000 

        :param limit: The limit of this ListMetricsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListMetricsRequest.

        **参数解释** 用于标识结果的排序方法 **约束限制** 不涉及 **取值范围** 枚举值： - asc 升序 - desc 降序 **默认取值** asc 

        :return: The order of this ListMetricsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListMetricsRequest.

        **参数解释** 用于标识结果的排序方法 **约束限制** 不涉及 **取值范围** 枚举值： - asc 升序 - desc 降序 **默认取值** asc 

        :param order: The order of this ListMetricsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
