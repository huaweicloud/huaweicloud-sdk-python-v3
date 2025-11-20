# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallK8sOptionsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'labels': 'dict(str, str)',
        'taints': 'list[Taint]',
        'max_pods': 'int'
    }

    attribute_map = {
        'labels': 'labels',
        'taints': 'taints',
        'max_pods': 'maxPods'
    }

    def __init__(self, labels=None, taints=None, max_pods=None):
        r"""ReinstallK8sOptionsConfig

        The model defined in huaweicloud sdk

        :param labels: **参数解释**： 格式为key/value键值对。 **约束限制**： 键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60; **取值范围**： 不涉及 **默认取值**： 不涉及
        :type labels: dict(str, str)
        :param taints: 支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  &#x60;&#x60;&#x60; \&quot;taints\&quot;: [{   \&quot;key\&quot;: \&quot;status\&quot;,   \&quot;value\&quot;: \&quot;unavailable\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }, {   \&quot;key\&quot;: \&quot;looks\&quot;,   \&quot;value\&quot;: \&quot;bad\&quot;,   \&quot;effect\&quot;: \&quot;NoSchedule\&quot; }] &#x60;&#x60;&#x60; 
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        :param max_pods: **参数解释**： 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 节点可以创建多少个Pod，受多个参数影响，具体请参见[节点可创建的最大Pod数量说明](maxPods.xml)。 **约束限制**： 不涉及 **取值范围**： 取值范围为16~256。 **默认取值**： 不涉及
        :type max_pods: int
        """
        
        

        self._labels = None
        self._taints = None
        self._max_pods = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        if taints is not None:
            self.taints = taints
        if max_pods is not None:
            self.max_pods = max_pods

    @property
    def labels(self):
        r"""Gets the labels of this ReinstallK8sOptionsConfig.

        **参数解释**： 格式为key/value键值对。 **约束限制**： 键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The labels of this ReinstallK8sOptionsConfig.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ReinstallK8sOptionsConfig.

        **参数解释**： 格式为key/value键值对。 **约束限制**： 键值对个数不超过20条。 - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀，例如example.com/my-key，DNS子域最长253个字符。 - Value：可以为空或者非空字符串，非空字符串必须以字符或数字开头和结尾，可以包含字母、数字、连字符、下划线和点，最长63个字符。  示例： ``` \"k8sTags\": {   \"key\": \"value\" } ``` **取值范围**： 不涉及 **默认取值**： 不涉及

        :param labels: The labels of this ReinstallK8sOptionsConfig.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def taints(self):
        r"""Gets the taints of this ReinstallK8sOptionsConfig.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :return: The taints of this ReinstallK8sOptionsConfig.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this ReinstallK8sOptionsConfig.

        支持给创建出来的节点加Taints来设置反亲和性，taints配置不超过20条。每条Taints包含以下3个参数：  - Key：必须以字母或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符；另外可以使用DNS子域作为前缀。 - Value：必须以字符或数字开头，可以包含字母、数字、连字符、下划线和点，最长63个字符。 - Effect：只可选NoSchedule，PreferNoSchedule或NoExecute。  示例：  ``` \"taints\": [{   \"key\": \"status\",   \"value\": \"unavailable\",   \"effect\": \"NoSchedule\" }, {   \"key\": \"looks\",   \"value\": \"bad\",   \"effect\": \"NoSchedule\" }] ``` 

        :param taints: The taints of this ReinstallK8sOptionsConfig.
        :type taints: list[:class:`huaweicloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def max_pods(self):
        r"""Gets the max_pods of this ReinstallK8sOptionsConfig.

        **参数解释**： 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 节点可以创建多少个Pod，受多个参数影响，具体请参见[节点可创建的最大Pod数量说明](maxPods.xml)。 **约束限制**： 不涉及 **取值范围**： 取值范围为16~256。 **默认取值**： 不涉及

        :return: The max_pods of this ReinstallK8sOptionsConfig.
        :rtype: int
        """
        return self._max_pods

    @max_pods.setter
    def max_pods(self, max_pods):
        r"""Sets the max_pods of this ReinstallK8sOptionsConfig.

        **参数解释**： 节点最大允许创建的实例数(Pod)，该数量包含系统默认实例。 该设置的目的为防止节点因管理过多实例而负载过重，请根据您的业务需要进行设置。 节点可以创建多少个Pod，受多个参数影响，具体请参见[节点可创建的最大Pod数量说明](maxPods.xml)。 **约束限制**： 不涉及 **取值范围**： 取值范围为16~256。 **默认取值**： 不涉及

        :param max_pods: The max_pods of this ReinstallK8sOptionsConfig.
        :type max_pods: int
        """
        self._max_pods = max_pods

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
        if not isinstance(other, ReinstallK8sOptionsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
