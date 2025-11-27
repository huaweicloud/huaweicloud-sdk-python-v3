# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kubernetes_version': 'str',
        'conditions': 'list[ConditionStatus]',
        'node_summary': 'NodeSummary',
        'resource_summary': 'ResourceSummary',
        'endpoints': 'object',
        'phase': 'str',
        'reason': 'str',
        'message': 'str',
        'arrear_freeze': 'str',
        'police_freeze': 'str',
        'api_enablements': 'list[APIEnablement]'
    }

    attribute_map = {
        'kubernetes_version': 'kubernetesVersion',
        'conditions': 'conditions',
        'node_summary': 'nodeSummary',
        'resource_summary': 'resourceSummary',
        'endpoints': 'endpoints',
        'phase': 'phase',
        'reason': 'reason',
        'message': 'message',
        'arrear_freeze': 'arrearFreeze',
        'police_freeze': 'policeFreeze',
        'api_enablements': 'apiEnablements'
    }

    def __init__(self, kubernetes_version=None, conditions=None, node_summary=None, resource_summary=None, endpoints=None, phase=None, reason=None, message=None, arrear_freeze=None, police_freeze=None, api_enablements=None):
        r"""ClusterStatus

        The model defined in huaweicloud sdk

        :param kubernetes_version: kubernetes版本
        :type kubernetes_version: str
        :param conditions: conditions信息
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        :param node_summary: 
        :type node_summary: :class:`huaweicloudsdkucs.v1.NodeSummary`
        :param resource_summary: 
        :type resource_summary: :class:`huaweicloudsdkucs.v1.ResourceSummary`
        :param endpoints: 端点
        :type endpoints: object
        :param phase: 阶段状态信息
        :type phase: str
        :param reason: 表述上次状况变化的原因
        :type reason: str
        :param message: 上次状态转换的详细信息
        :type message: str
        :param arrear_freeze: 欠费冻结
        :type arrear_freeze: str
        :param police_freeze: 公安冻结
        :type police_freeze: str
        :param api_enablements: 开启的资源列表
        :type api_enablements: list[:class:`huaweicloudsdkucs.v1.APIEnablement`]
        """
        
        

        self._kubernetes_version = None
        self._conditions = None
        self._node_summary = None
        self._resource_summary = None
        self._endpoints = None
        self._phase = None
        self._reason = None
        self._message = None
        self._arrear_freeze = None
        self._police_freeze = None
        self._api_enablements = None
        self.discriminator = None

        if kubernetes_version is not None:
            self.kubernetes_version = kubernetes_version
        if conditions is not None:
            self.conditions = conditions
        if node_summary is not None:
            self.node_summary = node_summary
        if resource_summary is not None:
            self.resource_summary = resource_summary
        if endpoints is not None:
            self.endpoints = endpoints
        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if arrear_freeze is not None:
            self.arrear_freeze = arrear_freeze
        if police_freeze is not None:
            self.police_freeze = police_freeze
        if api_enablements is not None:
            self.api_enablements = api_enablements

    @property
    def kubernetes_version(self):
        r"""Gets the kubernetes_version of this ClusterStatus.

        kubernetes版本

        :return: The kubernetes_version of this ClusterStatus.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        r"""Sets the kubernetes_version of this ClusterStatus.

        kubernetes版本

        :param kubernetes_version: The kubernetes_version of this ClusterStatus.
        :type kubernetes_version: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def conditions(self):
        r"""Gets the conditions of this ClusterStatus.

        conditions信息

        :return: The conditions of this ClusterStatus.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ClusterStatus.

        conditions信息

        :param conditions: The conditions of this ClusterStatus.
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        """
        self._conditions = conditions

    @property
    def node_summary(self):
        r"""Gets the node_summary of this ClusterStatus.

        :return: The node_summary of this ClusterStatus.
        :rtype: :class:`huaweicloudsdkucs.v1.NodeSummary`
        """
        return self._node_summary

    @node_summary.setter
    def node_summary(self, node_summary):
        r"""Sets the node_summary of this ClusterStatus.

        :param node_summary: The node_summary of this ClusterStatus.
        :type node_summary: :class:`huaweicloudsdkucs.v1.NodeSummary`
        """
        self._node_summary = node_summary

    @property
    def resource_summary(self):
        r"""Gets the resource_summary of this ClusterStatus.

        :return: The resource_summary of this ClusterStatus.
        :rtype: :class:`huaweicloudsdkucs.v1.ResourceSummary`
        """
        return self._resource_summary

    @resource_summary.setter
    def resource_summary(self, resource_summary):
        r"""Sets the resource_summary of this ClusterStatus.

        :param resource_summary: The resource_summary of this ClusterStatus.
        :type resource_summary: :class:`huaweicloudsdkucs.v1.ResourceSummary`
        """
        self._resource_summary = resource_summary

    @property
    def endpoints(self):
        r"""Gets the endpoints of this ClusterStatus.

        端点

        :return: The endpoints of this ClusterStatus.
        :rtype: object
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this ClusterStatus.

        端点

        :param endpoints: The endpoints of this ClusterStatus.
        :type endpoints: object
        """
        self._endpoints = endpoints

    @property
    def phase(self):
        r"""Gets the phase of this ClusterStatus.

        阶段状态信息

        :return: The phase of this ClusterStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this ClusterStatus.

        阶段状态信息

        :param phase: The phase of this ClusterStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def reason(self):
        r"""Gets the reason of this ClusterStatus.

        表述上次状况变化的原因

        :return: The reason of this ClusterStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ClusterStatus.

        表述上次状况变化的原因

        :param reason: The reason of this ClusterStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        r"""Gets the message of this ClusterStatus.

        上次状态转换的详细信息

        :return: The message of this ClusterStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ClusterStatus.

        上次状态转换的详细信息

        :param message: The message of this ClusterStatus.
        :type message: str
        """
        self._message = message

    @property
    def arrear_freeze(self):
        r"""Gets the arrear_freeze of this ClusterStatus.

        欠费冻结

        :return: The arrear_freeze of this ClusterStatus.
        :rtype: str
        """
        return self._arrear_freeze

    @arrear_freeze.setter
    def arrear_freeze(self, arrear_freeze):
        r"""Sets the arrear_freeze of this ClusterStatus.

        欠费冻结

        :param arrear_freeze: The arrear_freeze of this ClusterStatus.
        :type arrear_freeze: str
        """
        self._arrear_freeze = arrear_freeze

    @property
    def police_freeze(self):
        r"""Gets the police_freeze of this ClusterStatus.

        公安冻结

        :return: The police_freeze of this ClusterStatus.
        :rtype: str
        """
        return self._police_freeze

    @police_freeze.setter
    def police_freeze(self, police_freeze):
        r"""Sets the police_freeze of this ClusterStatus.

        公安冻结

        :param police_freeze: The police_freeze of this ClusterStatus.
        :type police_freeze: str
        """
        self._police_freeze = police_freeze

    @property
    def api_enablements(self):
        r"""Gets the api_enablements of this ClusterStatus.

        开启的资源列表

        :return: The api_enablements of this ClusterStatus.
        :rtype: list[:class:`huaweicloudsdkucs.v1.APIEnablement`]
        """
        return self._api_enablements

    @api_enablements.setter
    def api_enablements(self, api_enablements):
        r"""Sets the api_enablements of this ClusterStatus.

        开启的资源列表

        :param api_enablements: The api_enablements of this ClusterStatus.
        :type api_enablements: list[:class:`huaweicloudsdkucs.v1.APIEnablement`]
        """
        self._api_enablements = api_enablements

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
        if not isinstance(other, ClusterStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
