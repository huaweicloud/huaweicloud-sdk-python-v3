# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'ief_instance_id': 'str',
        'in_using': 'bool',
        'name': 'str',
        'source': 'str',
        'source_resource': 'dict(str, str)',
        'target': 'str',
        'target_resource': 'dict(str, str)'
    }

    attribute_map = {
        'description': 'description',
        'ief_instance_id': 'ief_instance_id',
        'in_using': 'in_using',
        'name': 'name',
        'source': 'source',
        'source_resource': 'source_resource',
        'target': 'target',
        'target_resource': 'target_resource'
    }

    def __init__(self, description=None, ief_instance_id=None, in_using=None, name=None, source=None, source_resource=None, target=None, target_resource=None):
        """RuleConfig

        The model defined in huaweicloud sdk

        :param description: 规则描述，最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param ief_instance_id: 铂金版实例ID，如果为空则表示是专业版实例。
        :type ief_instance_id: str
        :param in_using: 是否启用规则，默认为true（启用）
        :type in_using: bool
        :param name: 规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的规则名唯一
        :type name: str
        :param source: 源端点ID
        :type source: str
        :param source_resource: 源端点资源。示例： - rest: {\&quot;path\&quot;:\&quot;&lt;standard uri format&gt;\&quot;} - eventbus: {\&quot;topic\&quot;:\&quot;&lt;project id&gt;/nodes/&lt;node id&gt;/user/&lt;租户自定义且满足eventbus topic要求的字符串&gt;\&quot;,\&quot;node_id\&quot;:\&quot;&lt;node id&gt;\&quot;}
        :type source_resource: dict(str, str)
        :param target: 目的端点ID
        :type target: str
        :param target_resource: 目的端点资源。示例： - dis: {\&quot;channel\&quot;: \&quot;dis channel name\&quot;} - servicebus: {\&quot;path\&quot;: \&quot;/request path\&quot;} - apigw: {\&quot;resource\&quot;: \&quot;http://ssss.com\&quot;} - eventbus: {\&quot;topic\&quot;: \&quot;/xxxx\&quot;}
        :type target_resource: dict(str, str)
        """
        
        

        self._description = None
        self._ief_instance_id = None
        self._in_using = None
        self._name = None
        self._source = None
        self._source_resource = None
        self._target = None
        self._target_resource = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if in_using is not None:
            self.in_using = in_using
        self.name = name
        self.source = source
        self.source_resource = source_resource
        self.target = target
        self.target_resource = target_resource

    @property
    def description(self):
        """Gets the description of this RuleConfig.

        规则描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this RuleConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleConfig.

        规则描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this RuleConfig.
        :type description: str
        """
        self._description = description

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this RuleConfig.

        铂金版实例ID，如果为空则表示是专业版实例。

        :return: The ief_instance_id of this RuleConfig.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this RuleConfig.

        铂金版实例ID，如果为空则表示是专业版实例。

        :param ief_instance_id: The ief_instance_id of this RuleConfig.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def in_using(self):
        """Gets the in_using of this RuleConfig.

        是否启用规则，默认为true（启用）

        :return: The in_using of this RuleConfig.
        :rtype: bool
        """
        return self._in_using

    @in_using.setter
    def in_using(self, in_using):
        """Sets the in_using of this RuleConfig.

        是否启用规则，默认为true（启用）

        :param in_using: The in_using of this RuleConfig.
        :type in_using: bool
        """
        self._in_using = in_using

    @property
    def name(self):
        """Gets the name of this RuleConfig.

        规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的规则名唯一

        :return: The name of this RuleConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleConfig.

        规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的规则名唯一

        :param name: The name of this RuleConfig.
        :type name: str
        """
        self._name = name

    @property
    def source(self):
        """Gets the source of this RuleConfig.

        源端点ID

        :return: The source of this RuleConfig.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RuleConfig.

        源端点ID

        :param source: The source of this RuleConfig.
        :type source: str
        """
        self._source = source

    @property
    def source_resource(self):
        """Gets the source_resource of this RuleConfig.

        源端点资源。示例： - rest: {\"path\":\"<standard uri format>\"} - eventbus: {\"topic\":\"<project id>/nodes/<node id>/user/<租户自定义且满足eventbus topic要求的字符串>\",\"node_id\":\"<node id>\"}

        :return: The source_resource of this RuleConfig.
        :rtype: dict(str, str)
        """
        return self._source_resource

    @source_resource.setter
    def source_resource(self, source_resource):
        """Sets the source_resource of this RuleConfig.

        源端点资源。示例： - rest: {\"path\":\"<standard uri format>\"} - eventbus: {\"topic\":\"<project id>/nodes/<node id>/user/<租户自定义且满足eventbus topic要求的字符串>\",\"node_id\":\"<node id>\"}

        :param source_resource: The source_resource of this RuleConfig.
        :type source_resource: dict(str, str)
        """
        self._source_resource = source_resource

    @property
    def target(self):
        """Gets the target of this RuleConfig.

        目的端点ID

        :return: The target of this RuleConfig.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RuleConfig.

        目的端点ID

        :param target: The target of this RuleConfig.
        :type target: str
        """
        self._target = target

    @property
    def target_resource(self):
        """Gets the target_resource of this RuleConfig.

        目的端点资源。示例： - dis: {\"channel\": \"dis channel name\"} - servicebus: {\"path\": \"/request path\"} - apigw: {\"resource\": \"http://ssss.com\"} - eventbus: {\"topic\": \"/xxxx\"}

        :return: The target_resource of this RuleConfig.
        :rtype: dict(str, str)
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        """Sets the target_resource of this RuleConfig.

        目的端点资源。示例： - dis: {\"channel\": \"dis channel name\"} - servicebus: {\"path\": \"/request path\"} - apigw: {\"resource\": \"http://ssss.com\"} - eventbus: {\"topic\": \"/xxxx\"}

        :param target_resource: The target_resource of this RuleConfig.
        :type target_resource: dict(str, str)
        """
        self._target_resource = target_resource

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
        if not isinstance(other, RuleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
