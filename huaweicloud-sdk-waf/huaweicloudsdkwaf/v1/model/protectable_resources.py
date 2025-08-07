# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectableResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_name': 'str',
        'loadbalancer_id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'listeners': 'list[Listener]',
        'eips': 'list[EipInfo]'
    }

    attribute_map = {
        'loadbalancer_name': 'loadbalancer_name',
        'loadbalancer_id': 'loadbalancer_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'listeners': 'listeners',
        'eips': 'eips'
    }

    def __init__(self, loadbalancer_name=None, loadbalancer_id=None, domain_id=None, project_id=None, listeners=None, eips=None):
        r"""ProtectableResources

        The model defined in huaweicloud sdk

        :param loadbalancer_name: **参数解释：** 负载均衡器名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type loadbalancer_name: str
        :param loadbalancer_id: **参数解释：** 负载均衡器ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type loadbalancer_id: str
        :param domain_id: **参数解释：** 负载均衡器所属的账号ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_id: str
        :param project_id: **参数解释：** 负载均衡器所在的项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param listeners: **参数解释：** 当前ELB所关联的监听器列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type listeners: list[:class:`huaweicloudsdkwaf.v1.Listener`]
        :param eips: **参数解释：** 负载均衡器绑定的EIP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type eips: list[:class:`huaweicloudsdkwaf.v1.EipInfo`]
        """
        
        

        self._loadbalancer_name = None
        self._loadbalancer_id = None
        self._domain_id = None
        self._project_id = None
        self._listeners = None
        self._eips = None
        self.discriminator = None

        if loadbalancer_name is not None:
            self.loadbalancer_name = loadbalancer_name
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if listeners is not None:
            self.listeners = listeners
        if eips is not None:
            self.eips = eips

    @property
    def loadbalancer_name(self):
        r"""Gets the loadbalancer_name of this ProtectableResources.

        **参数解释：** 负载均衡器名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The loadbalancer_name of this ProtectableResources.
        :rtype: str
        """
        return self._loadbalancer_name

    @loadbalancer_name.setter
    def loadbalancer_name(self, loadbalancer_name):
        r"""Sets the loadbalancer_name of this ProtectableResources.

        **参数解释：** 负载均衡器名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param loadbalancer_name: The loadbalancer_name of this ProtectableResources.
        :type loadbalancer_name: str
        """
        self._loadbalancer_name = loadbalancer_name

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ProtectableResources.

        **参数解释：** 负载均衡器ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The loadbalancer_id of this ProtectableResources.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ProtectableResources.

        **参数解释：** 负载均衡器ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param loadbalancer_id: The loadbalancer_id of this ProtectableResources.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProtectableResources.

        **参数解释：** 负载均衡器所属的账号ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_id of this ProtectableResources.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProtectableResources.

        **参数解释：** 负载均衡器所属的账号ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_id: The domain_id of this ProtectableResources.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ProtectableResources.

        **参数解释：** 负载均衡器所在的项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ProtectableResources.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProtectableResources.

        **参数解释：** 负载均衡器所在的项目ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ProtectableResources.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def listeners(self):
        r"""Gets the listeners of this ProtectableResources.

        **参数解释：** 当前ELB所关联的监听器列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The listeners of this ProtectableResources.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.Listener`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this ProtectableResources.

        **参数解释：** 当前ELB所关联的监听器列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param listeners: The listeners of this ProtectableResources.
        :type listeners: list[:class:`huaweicloudsdkwaf.v1.Listener`]
        """
        self._listeners = listeners

    @property
    def eips(self):
        r"""Gets the eips of this ProtectableResources.

        **参数解释：** 负载均衡器绑定的EIP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The eips of this ProtectableResources.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.EipInfo`]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        r"""Sets the eips of this ProtectableResources.

        **参数解释：** 负载均衡器绑定的EIP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param eips: The eips of this ProtectableResources.
        :type eips: list[:class:`huaweicloudsdkwaf.v1.EipInfo`]
        """
        self._eips = eips

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
        if not isinstance(other, ProtectableResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
