# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'fail_messages': 'int',
        'id': 'str',
        'ief_instance_id': 'str',
        'in_using': 'bool',
        'name': 'str',
        'project_id': 'str',
        'source': 'EndpointObjResp',
        'source_resource': 'dict(str, str)',
        'target': 'EndpointObjResp',
        'target_resource': 'dict(str, str)',
        'updated_at': 'str',
        'success_messages': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'fail_messages': 'fail_messages',
        'id': 'id',
        'ief_instance_id': 'ief_instance_id',
        'in_using': 'in_using',
        'name': 'name',
        'project_id': 'project_id',
        'source': 'source',
        'source_resource': 'source_resource',
        'target': 'target',
        'target_resource': 'target_resource',
        'updated_at': 'updated_at',
        'success_messages': 'success_messages'
    }

    def __init__(self, created_at=None, description=None, fail_messages=None, id=None, ief_instance_id=None, in_using=None, name=None, project_id=None, source=None, source_resource=None, target=None, target_resource=None, updated_at=None, success_messages=None):
        r"""RuleResponse

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param description: 规则描述，最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param fail_messages: 转发失败的消息数
        :type fail_messages: int
        :param id: 规则ID
        :type id: str
        :param ief_instance_id: [铂金版实例ID，如果为空则表示是专业版实例。](tag:hws,hws_hk)[铂金版实例ID](tag:hcs,hcs_sm)
        :type ief_instance_id: str
        :param in_using: 是否启用规则，默认为true（启用）
        :type in_using: bool
        :param name: 规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个账号中创建的规则名唯一
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param source: 
        :type source: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        :param source_resource: 源端点资源。示例： - rest: {\&quot;path\&quot;:\&quot;\\&lt;standard uri format\\&gt;\&quot;} - eventbus: {\&quot;topic\&quot;:\&quot;\\&lt;project id\\&gt;/nodes/\\&lt;node id\\&gt;/user/\\&lt;租户自定义且满足eventbus topic要求的字符串\\&gt;\&quot;,\&quot;node_id\&quot;:\&quot;\\&lt;node id\\&gt;\&quot;} 
        :type source_resource: dict(str, str)
        :param target: 
        :type target: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        :param target_resource: 目的端点资源，示例： - dis: {\&quot;channel\&quot;: \&quot;dis channel name\&quot;} - servicebus: {\&quot;path\&quot;: \&quot;/request path\&quot;} - apigw: {\&quot;resource\&quot;: \&quot;http://ssss.com\&quot;} - eventbus: {\&quot;topic\&quot;: \&quot;/xxxx\&quot;}
        :type target_resource: dict(str, str)
        :param updated_at: 更新时间
        :type updated_at: str
        :param success_messages: 转发成功的消息数
        :type success_messages: int
        """
        
        

        self._created_at = None
        self._description = None
        self._fail_messages = None
        self._id = None
        self._ief_instance_id = None
        self._in_using = None
        self._name = None
        self._project_id = None
        self._source = None
        self._source_resource = None
        self._target = None
        self._target_resource = None
        self._updated_at = None
        self._success_messages = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if fail_messages is not None:
            self.fail_messages = fail_messages
        if id is not None:
            self.id = id
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if in_using is not None:
            self.in_using = in_using
        self.name = name
        self.project_id = project_id
        self.source = source
        self.source_resource = source_resource
        self.target = target
        self.target_resource = target_resource
        self.updated_at = updated_at
        self.success_messages = success_messages

    @property
    def created_at(self):
        r"""Gets the created_at of this RuleResponse.

        创建时间

        :return: The created_at of this RuleResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RuleResponse.

        创建时间

        :param created_at: The created_at of this RuleResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this RuleResponse.

        规则描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this RuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RuleResponse.

        规则描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this RuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def fail_messages(self):
        r"""Gets the fail_messages of this RuleResponse.

        转发失败的消息数

        :return: The fail_messages of this RuleResponse.
        :rtype: int
        """
        return self._fail_messages

    @fail_messages.setter
    def fail_messages(self, fail_messages):
        r"""Sets the fail_messages of this RuleResponse.

        转发失败的消息数

        :param fail_messages: The fail_messages of this RuleResponse.
        :type fail_messages: int
        """
        self._fail_messages = fail_messages

    @property
    def id(self):
        r"""Gets the id of this RuleResponse.

        规则ID

        :return: The id of this RuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleResponse.

        规则ID

        :param id: The id of this RuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this RuleResponse.

        [铂金版实例ID，如果为空则表示是专业版实例。](tag:hws,hws_hk)[铂金版实例ID](tag:hcs,hcs_sm)

        :return: The ief_instance_id of this RuleResponse.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this RuleResponse.

        [铂金版实例ID，如果为空则表示是专业版实例。](tag:hws,hws_hk)[铂金版实例ID](tag:hcs,hcs_sm)

        :param ief_instance_id: The ief_instance_id of this RuleResponse.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def in_using(self):
        r"""Gets the in_using of this RuleResponse.

        是否启用规则，默认为true（启用）

        :return: The in_using of this RuleResponse.
        :rtype: bool
        """
        return self._in_using

    @in_using.setter
    def in_using(self, in_using):
        r"""Sets the in_using of this RuleResponse.

        是否启用规则，默认为true（启用）

        :param in_using: The in_using of this RuleResponse.
        :type in_using: bool
        """
        self._in_using = in_using

    @property
    def name(self):
        r"""Gets the name of this RuleResponse.

        规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个账号中创建的规则名唯一

        :return: The name of this RuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleResponse.

        规则名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个账号中创建的规则名唯一

        :param name: The name of this RuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this RuleResponse.

        项目ID

        :return: The project_id of this RuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RuleResponse.

        项目ID

        :param project_id: The project_id of this RuleResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def source(self):
        r"""Gets the source of this RuleResponse.

        :return: The source of this RuleResponse.
        :rtype: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this RuleResponse.

        :param source: The source of this RuleResponse.
        :type source: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        self._source = source

    @property
    def source_resource(self):
        r"""Gets the source_resource of this RuleResponse.

        源端点资源。示例： - rest: {\"path\":\"\\<standard uri format\\>\"} - eventbus: {\"topic\":\"\\<project id\\>/nodes/\\<node id\\>/user/\\<租户自定义且满足eventbus topic要求的字符串\\>\",\"node_id\":\"\\<node id\\>\"} 

        :return: The source_resource of this RuleResponse.
        :rtype: dict(str, str)
        """
        return self._source_resource

    @source_resource.setter
    def source_resource(self, source_resource):
        r"""Sets the source_resource of this RuleResponse.

        源端点资源。示例： - rest: {\"path\":\"\\<standard uri format\\>\"} - eventbus: {\"topic\":\"\\<project id\\>/nodes/\\<node id\\>/user/\\<租户自定义且满足eventbus topic要求的字符串\\>\",\"node_id\":\"\\<node id\\>\"} 

        :param source_resource: The source_resource of this RuleResponse.
        :type source_resource: dict(str, str)
        """
        self._source_resource = source_resource

    @property
    def target(self):
        r"""Gets the target of this RuleResponse.

        :return: The target of this RuleResponse.
        :rtype: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this RuleResponse.

        :param target: The target of this RuleResponse.
        :type target: :class:`huaweicloudsdkief.v1.EndpointObjResp`
        """
        self._target = target

    @property
    def target_resource(self):
        r"""Gets the target_resource of this RuleResponse.

        目的端点资源，示例： - dis: {\"channel\": \"dis channel name\"} - servicebus: {\"path\": \"/request path\"} - apigw: {\"resource\": \"http://ssss.com\"} - eventbus: {\"topic\": \"/xxxx\"}

        :return: The target_resource of this RuleResponse.
        :rtype: dict(str, str)
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        r"""Sets the target_resource of this RuleResponse.

        目的端点资源，示例： - dis: {\"channel\": \"dis channel name\"} - servicebus: {\"path\": \"/request path\"} - apigw: {\"resource\": \"http://ssss.com\"} - eventbus: {\"topic\": \"/xxxx\"}

        :param target_resource: The target_resource of this RuleResponse.
        :type target_resource: dict(str, str)
        """
        self._target_resource = target_resource

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RuleResponse.

        更新时间

        :return: The updated_at of this RuleResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RuleResponse.

        更新时间

        :param updated_at: The updated_at of this RuleResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def success_messages(self):
        r"""Gets the success_messages of this RuleResponse.

        转发成功的消息数

        :return: The success_messages of this RuleResponse.
        :rtype: int
        """
        return self._success_messages

    @success_messages.setter
    def success_messages(self, success_messages):
        r"""Sets the success_messages of this RuleResponse.

        转发成功的消息数

        :param success_messages: The success_messages of this RuleResponse.
        :type success_messages: int
        """
        self._success_messages = success_messages

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
        if not isinstance(other, RuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
