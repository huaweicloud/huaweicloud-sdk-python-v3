# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeNodeToPeriodReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'node_list': 'list[str]',
        'period_order_param': 'PeriodOrderParam',
        'include_resources': 'list[str]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'node_list': 'nodeList',
        'period_order_param': 'periodOrderParam',
        'include_resources': 'includeResources'
    }

    def __init__(self, kind=None, api_version=None, node_list=None, period_order_param=None, include_resources=None):
        r"""BatchChangeNodeToPeriodReqBody

        The model defined in huaweicloud sdk

        :param kind: **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Node 
        :type kind: str
        :param api_version: **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v3 
        :type api_version: str
        :param node_list: **参数解释**： 要进行按需转包的CCE节点ID列表，示例如下： &#x60;&#x60;&#x60; \&quot;nodeList\&quot;: [\&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;, \&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;] &#x60;&#x60;&#x60; **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type node_list: list[str]
        :param period_order_param: 
        :type period_order_param: :class:`huaweicloudsdkcce.v3.PeriodOrderParam`
        :param include_resources: **参数解释**： 需要一起转包周期的资源类型列表，示例如下： &#x60;&#x60;&#x60; \&quot;includeResources\&quot;: [\&quot;eip\&quot;] &#x60;&#x60;&#x60; **约束限制**： 当前仅支持eip（弹性公网IP）资源 **取值范围**： - \&quot;eip\&quot;：弹性公网IP **默认取值**： 不涉及
        :type include_resources: list[str]
        """
        
        

        self._kind = None
        self._api_version = None
        self._node_list = None
        self._period_order_param = None
        self._include_resources = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        self.node_list = node_list
        self.period_order_param = period_order_param
        if include_resources is not None:
            self.include_resources = include_resources

    @property
    def kind(self):
        r"""Gets the kind of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Node 

        :return: The kind of this BatchChangeNodeToPeriodReqBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： API类型 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： Node 

        :param kind: The kind of this BatchChangeNodeToPeriodReqBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v3 

        :return: The api_version of this BatchChangeNodeToPeriodReqBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： API版本 **约束限制**： 该值不可修改 **取值范围**： 不涉及 **默认取值**： v3 

        :param api_version: The api_version of this BatchChangeNodeToPeriodReqBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def node_list(self):
        r"""Gets the node_list of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： 要进行按需转包的CCE节点ID列表，示例如下： ``` \"nodeList\": [\"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\", \"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\"] ``` **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The node_list of this BatchChangeNodeToPeriodReqBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： 要进行按需转包的CCE节点ID列表，示例如下： ``` \"nodeList\": [\"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\", \"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\"] ``` **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param node_list: The node_list of this BatchChangeNodeToPeriodReqBody.
        :type node_list: list[str]
        """
        self._node_list = node_list

    @property
    def period_order_param(self):
        r"""Gets the period_order_param of this BatchChangeNodeToPeriodReqBody.

        :return: The period_order_param of this BatchChangeNodeToPeriodReqBody.
        :rtype: :class:`huaweicloudsdkcce.v3.PeriodOrderParam`
        """
        return self._period_order_param

    @period_order_param.setter
    def period_order_param(self, period_order_param):
        r"""Sets the period_order_param of this BatchChangeNodeToPeriodReqBody.

        :param period_order_param: The period_order_param of this BatchChangeNodeToPeriodReqBody.
        :type period_order_param: :class:`huaweicloudsdkcce.v3.PeriodOrderParam`
        """
        self._period_order_param = period_order_param

    @property
    def include_resources(self):
        r"""Gets the include_resources of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： 需要一起转包周期的资源类型列表，示例如下： ``` \"includeResources\": [\"eip\"] ``` **约束限制**： 当前仅支持eip（弹性公网IP）资源 **取值范围**： - \"eip\"：弹性公网IP **默认取值**： 不涉及

        :return: The include_resources of this BatchChangeNodeToPeriodReqBody.
        :rtype: list[str]
        """
        return self._include_resources

    @include_resources.setter
    def include_resources(self, include_resources):
        r"""Sets the include_resources of this BatchChangeNodeToPeriodReqBody.

        **参数解释**： 需要一起转包周期的资源类型列表，示例如下： ``` \"includeResources\": [\"eip\"] ``` **约束限制**： 当前仅支持eip（弹性公网IP）资源 **取值范围**： - \"eip\"：弹性公网IP **默认取值**： 不涉及

        :param include_resources: The include_resources of this BatchChangeNodeToPeriodReqBody.
        :type include_resources: list[str]
        """
        self._include_resources = include_resources

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
        if not isinstance(other, BatchChangeNodeToPeriodReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
