# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRetention:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'algorithm': 'str',
        'rules': 'list[RetentionRuleResponseBody]',
        'trigger': 'TriggerConfig',
        'enabled': 'bool',
        'name': 'str',
        'namespace_id': 'int',
        'namespace_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'algorithm': 'algorithm',
        'rules': 'rules',
        'trigger': 'trigger',
        'enabled': 'enabled',
        'name': 'name',
        'namespace_id': 'namespace_id',
        'namespace_name': 'namespace_name'
    }

    def __init__(self, id=None, algorithm=None, rules=None, trigger=None, enabled=None, name=None, namespace_id=None, namespace_name=None):
        r"""ImageRetention

        The model defined in huaweicloud sdk

        :param id: 老化策略ID
        :type id: int
        :param algorithm: 算法
        :type algorithm: str
        :param rules: 匹配规则
        :type rules: list[:class:`huaweicloudsdkswr.v2.RetentionRuleResponseBody`]
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param enabled: 是否开启策略
        :type enabled: bool
        :param name: 策略名称
        :type name: str
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param namespace_name: 命名空间名
        :type namespace_name: str
        """
        
        

        self._id = None
        self._algorithm = None
        self._rules = None
        self._trigger = None
        self._enabled = None
        self._name = None
        self._namespace_id = None
        self._namespace_name = None
        self.discriminator = None

        self.id = id
        self.algorithm = algorithm
        self.rules = rules
        self.trigger = trigger
        self.enabled = enabled
        self.name = name
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    @property
    def id(self):
        r"""Gets the id of this ImageRetention.

        老化策略ID

        :return: The id of this ImageRetention.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageRetention.

        老化策略ID

        :param id: The id of this ImageRetention.
        :type id: int
        """
        self._id = id

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ImageRetention.

        算法

        :return: The algorithm of this ImageRetention.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ImageRetention.

        算法

        :param algorithm: The algorithm of this ImageRetention.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def rules(self):
        r"""Gets the rules of this ImageRetention.

        匹配规则

        :return: The rules of this ImageRetention.
        :rtype: list[:class:`huaweicloudsdkswr.v2.RetentionRuleResponseBody`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ImageRetention.

        匹配规则

        :param rules: The rules of this ImageRetention.
        :type rules: list[:class:`huaweicloudsdkswr.v2.RetentionRuleResponseBody`]
        """
        self._rules = rules

    @property
    def trigger(self):
        r"""Gets the trigger of this ImageRetention.

        :return: The trigger of this ImageRetention.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this ImageRetention.

        :param trigger: The trigger of this ImageRetention.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def enabled(self):
        r"""Gets the enabled of this ImageRetention.

        是否开启策略

        :return: The enabled of this ImageRetention.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ImageRetention.

        是否开启策略

        :param enabled: The enabled of this ImageRetention.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this ImageRetention.

        策略名称

        :return: The name of this ImageRetention.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageRetention.

        策略名称

        :param name: The name of this ImageRetention.
        :type name: str
        """
        self._name = name

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ImageRetention.

        命名空间ID

        :return: The namespace_id of this ImageRetention.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ImageRetention.

        命名空间ID

        :param namespace_id: The namespace_id of this ImageRetention.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ImageRetention.

        命名空间名

        :return: The namespace_name of this ImageRetention.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ImageRetention.

        命名空间名

        :param namespace_name: The namespace_name of this ImageRetention.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

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
        if not isinstance(other, ImageRetention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
