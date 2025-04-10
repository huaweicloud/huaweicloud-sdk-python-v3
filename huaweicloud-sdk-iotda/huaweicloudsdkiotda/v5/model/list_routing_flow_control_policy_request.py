# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRoutingFlowControlPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'scope': 'str',
        'scope_value': 'str',
        'policy_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'scope': 'scope',
        'scope_value': 'scope_value',
        'policy_name': 'policy_name',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, scope=None, scope_value=None, policy_name=None, limit=None, marker=None, offset=None):
        r"""ListRoutingFlowControlPolicyRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。
        :type instance_id: str
        :param scope: **参数说明**：流控策略作用域。不携带该参数时，查询所有作用域流控策略；取值USER时，查询租户级流控策略；取值为CHANNEL时，查询转发通道级流控策略；取值为RULE时，查询转发规则级流控策略；取值为ACTION时，查询转发动作级流控策略。
        :type scope: str
        :param scope_value: **参数说明**：流控策略作用域附加值。 不携带scope参数或scope参数取值为USER时，可不携带该字段，查询租户级流控策略。 scope参数取值为CHANNEL时，不携带该字段表示查询所有转发通道级流控策略，携带该字段表示查询该字段取值对应转发通道的流控策略。**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope参数为RULE时，不携带该字段表示查询所有转发规则级流控策略，携带该字段表示查询该字段取值对应转发规则的流控策略。 scope参数为ACTION时，不携带该字段表示查询所有转发动作级流控策略，携带该字段表示查询该字段取值对应转发动作的流控策略。
        :type scope_value: str
        :param policy_name: **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type policy_name: str
        :param limit: **参数说明**：分页查询时每页显示的记录数。默认每页10条记录，最大设定每页50条记录。 **取值范围**：1-50的整数，默认值为10。
        :type limit: int
        :param marker: **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。
        :type marker: str
        :param offset: **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。 - 限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._scope = None
        self._scope_value = None
        self._policy_name = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if scope is not None:
            self.scope = scope
        if scope_value is not None:
            self.scope_value = scope_value
        if policy_name is not None:
            self.policy_name = policy_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :return: The instance_id of this ListRoutingFlowControlPolicyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :param instance_id: The instance_id of this ListRoutingFlowControlPolicyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def scope(self):
        r"""Gets the scope of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：流控策略作用域。不携带该参数时，查询所有作用域流控策略；取值USER时，查询租户级流控策略；取值为CHANNEL时，查询转发通道级流控策略；取值为RULE时，查询转发规则级流控策略；取值为ACTION时，查询转发动作级流控策略。

        :return: The scope of this ListRoutingFlowControlPolicyRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：流控策略作用域。不携带该参数时，查询所有作用域流控策略；取值USER时，查询租户级流控策略；取值为CHANNEL时，查询转发通道级流控策略；取值为RULE时，查询转发规则级流控策略；取值为ACTION时，查询转发动作级流控策略。

        :param scope: The scope of this ListRoutingFlowControlPolicyRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def scope_value(self):
        r"""Gets the scope_value of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：流控策略作用域附加值。 不携带scope参数或scope参数取值为USER时，可不携带该字段，查询租户级流控策略。 scope参数取值为CHANNEL时，不携带该字段表示查询所有转发通道级流控策略，携带该字段表示查询该字段取值对应转发通道的流控策略。**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope参数为RULE时，不携带该字段表示查询所有转发规则级流控策略，携带该字段表示查询该字段取值对应转发规则的流控策略。 scope参数为ACTION时，不携带该字段表示查询所有转发动作级流控策略，携带该字段表示查询该字段取值对应转发动作的流控策略。

        :return: The scope_value of this ListRoutingFlowControlPolicyRequest.
        :rtype: str
        """
        return self._scope_value

    @scope_value.setter
    def scope_value(self, scope_value):
        r"""Sets the scope_value of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：流控策略作用域附加值。 不携带scope参数或scope参数取值为USER时，可不携带该字段，查询租户级流控策略。 scope参数取值为CHANNEL时，不携带该字段表示查询所有转发通道级流控策略，携带该字段表示查询该字段取值对应转发通道的流控策略。**取值范围**：HTTP_FORWARDING、DIS_FORWARDING、OBS_FORWARDING、AMQP_FORWARDING、DMS_KAFKA_FORWARDING。 scope参数为RULE时，不携带该字段表示查询所有转发规则级流控策略，携带该字段表示查询该字段取值对应转发规则的流控策略。 scope参数为ACTION时，不携带该字段表示查询所有转发动作级流控策略，携带该字段表示查询该字段取值对应转发动作的流控策略。

        :param scope_value: The scope_value of this ListRoutingFlowControlPolicyRequest.
        :type scope_value: str
        """
        self._scope_value = scope_value

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The policy_name of this ListRoutingFlowControlPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param policy_name: The policy_name of this ListRoutingFlowControlPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def limit(self):
        r"""Gets the limit of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：分页查询时每页显示的记录数。默认每页10条记录，最大设定每页50条记录。 **取值范围**：1-50的整数，默认值为10。

        :return: The limit of this ListRoutingFlowControlPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：分页查询时每页显示的记录数。默认每页10条记录，最大设定每页50条记录。 **取值范围**：1-50的整数，默认值为10。

        :param limit: The limit of this ListRoutingFlowControlPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :return: The marker of this ListRoutingFlowControlPolicyRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :param marker: The marker of this ListRoutingFlowControlPolicyRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        r"""Gets the offset of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。 - 限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :return: The offset of this ListRoutingFlowControlPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRoutingFlowControlPolicyRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。 - 限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :param offset: The offset of this ListRoutingFlowControlPolicyRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRoutingFlowControlPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
