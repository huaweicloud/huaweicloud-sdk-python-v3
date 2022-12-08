# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetStackMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_id': 'str',
        'stack_name': 'str',
        'description': 'str',
        'vars_structure': 'list[VarsStructure]',
        'vars_uri_content': 'str',
        'vars_body': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'enable_deletion_protection': 'bool',
        'enable_auto_rollback': 'bool',
        'status': 'str',
        'status_message': 'str',
        'agencies': 'list[Agency]'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'stack_name': 'stack_name',
        'description': 'description',
        'vars_structure': 'vars_structure',
        'vars_uri_content': 'vars_uri_content',
        'vars_body': 'vars_body',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enable_deletion_protection': 'enable_deletion_protection',
        'enable_auto_rollback': 'enable_auto_rollback',
        'status': 'status',
        'status_message': 'status_message',
        'agencies': 'agencies'
    }

    def __init__(self, stack_id=None, stack_name=None, description=None, vars_structure=None, vars_uri_content=None, vars_body=None, create_time=None, update_time=None, enable_deletion_protection=None, enable_auto_rollback=None, status=None, status_message=None, agencies=None):
        """GetStackMetadataResponse

        The model defined in huaweicloud sdk

        :param stack_id: 栈的唯一Id
        :type stack_id: str
        :param stack_name: 栈的名字
        :type stack_name: str
        :param description: 栈的描述，此描述为用户在创建资源栈时指定
        :type description: str
        :param vars_structure: 参数列表
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        :param vars_uri_content: vars文件中的内容
        :type vars_uri_content: str
        :param vars_body: terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容
        :type vars_body: str
        :param create_time: 栈的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param update_time: 由于栈可以被更新，此处为上次更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type update_time: str
        :param enable_deletion_protection: 资源栈删除保护的目标状态
        :type enable_deletion_protection: bool
        :param enable_auto_rollback: 资源栈是否开启自动回滚的标识位
        :type enable_auto_rollback: bool
        :param status: 资源栈的执行状态     * &#x60;DEPLOYMENT_IN_PROGRESS&#x60; - 正在部署     * &#x60;DEPLOYMENT_FAILED&#x60; - 部署失败。请于StatusMessage见更多详情     * &#x60;DEPLOYMENT_COMPLETE &#x60; - 部署结束     * &#x60;ROLLBACK_IN_PROGRESS&#x60; - 正在回滚     * &#x60;ROLLBACK_FAILED&#x60; - 回滚失败。请于StatusMessage见更多详情     * &#x60;ROLLBACK_COMPLETE&#x60; - 回滚完成     * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除     * &#x60;DELETION_FAILED&#x60; - 删除失败     * &#x60;CREATION_COMPLETE&#x60; - 生成完成，并没有任何部署
        :type status: str
        :param status_message: 展示更多细节的信息
        :type status_message: str
        :param agencies: 委托授权的信息
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        
        super(GetStackMetadataResponse, self).__init__()

        self._stack_id = None
        self._stack_name = None
        self._description = None
        self._vars_structure = None
        self._vars_uri_content = None
        self._vars_body = None
        self._create_time = None
        self._update_time = None
        self._enable_deletion_protection = None
        self._enable_auto_rollback = None
        self._status = None
        self._status_message = None
        self._agencies = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if stack_name is not None:
            self.stack_name = stack_name
        if description is not None:
            self.description = description
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if vars_uri_content is not None:
            self.vars_uri_content = vars_uri_content
        if vars_body is not None:
            self.vars_body = vars_body
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if enable_deletion_protection is not None:
            self.enable_deletion_protection = enable_deletion_protection
        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if agencies is not None:
            self.agencies = agencies

    @property
    def stack_id(self):
        """Gets the stack_id of this GetStackMetadataResponse.

        栈的唯一Id

        :return: The stack_id of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this GetStackMetadataResponse.

        栈的唯一Id

        :param stack_id: The stack_id of this GetStackMetadataResponse.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def stack_name(self):
        """Gets the stack_name of this GetStackMetadataResponse.

        栈的名字

        :return: The stack_name of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this GetStackMetadataResponse.

        栈的名字

        :param stack_name: The stack_name of this GetStackMetadataResponse.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def description(self):
        """Gets the description of this GetStackMetadataResponse.

        栈的描述，此描述为用户在创建资源栈时指定

        :return: The description of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetStackMetadataResponse.

        栈的描述，此描述为用户在创建资源栈时指定

        :param description: The description of this GetStackMetadataResponse.
        :type description: str
        """
        self._description = description

    @property
    def vars_structure(self):
        """Gets the vars_structure of this GetStackMetadataResponse.

        参数列表

        :return: The vars_structure of this GetStackMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this GetStackMetadataResponse.

        参数列表

        :param vars_structure: The vars_structure of this GetStackMetadataResponse.
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def vars_uri_content(self):
        """Gets the vars_uri_content of this GetStackMetadataResponse.

        vars文件中的内容

        :return: The vars_uri_content of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._vars_uri_content

    @vars_uri_content.setter
    def vars_uri_content(self, vars_uri_content):
        """Sets the vars_uri_content of this GetStackMetadataResponse.

        vars文件中的内容

        :param vars_uri_content: The vars_uri_content of this GetStackMetadataResponse.
        :type vars_uri_content: str
        """
        self._vars_uri_content = vars_uri_content

    @property
    def vars_body(self):
        """Gets the vars_body of this GetStackMetadataResponse.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容

        :return: The vars_body of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this GetStackMetadataResponse.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容

        :param vars_body: The vars_body of this GetStackMetadataResponse.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def create_time(self):
        """Gets the create_time of this GetStackMetadataResponse.

        栈的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetStackMetadataResponse.

        栈的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this GetStackMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetStackMetadataResponse.

        由于栈可以被更新，此处为上次更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The update_time of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetStackMetadataResponse.

        由于栈可以被更新，此处为上次更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param update_time: The update_time of this GetStackMetadataResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def enable_deletion_protection(self):
        """Gets the enable_deletion_protection of this GetStackMetadataResponse.

        资源栈删除保护的目标状态

        :return: The enable_deletion_protection of this GetStackMetadataResponse.
        :rtype: bool
        """
        return self._enable_deletion_protection

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, enable_deletion_protection):
        """Sets the enable_deletion_protection of this GetStackMetadataResponse.

        资源栈删除保护的目标状态

        :param enable_deletion_protection: The enable_deletion_protection of this GetStackMetadataResponse.
        :type enable_deletion_protection: bool
        """
        self._enable_deletion_protection = enable_deletion_protection

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this GetStackMetadataResponse.

        资源栈是否开启自动回滚的标识位

        :return: The enable_auto_rollback of this GetStackMetadataResponse.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this GetStackMetadataResponse.

        资源栈是否开启自动回滚的标识位

        :param enable_auto_rollback: The enable_auto_rollback of this GetStackMetadataResponse.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

    @property
    def status(self):
        """Gets the status of this GetStackMetadataResponse.

        资源栈的执行状态     * `DEPLOYMENT_IN_PROGRESS` - 正在部署     * `DEPLOYMENT_FAILED` - 部署失败。请于StatusMessage见更多详情     * `DEPLOYMENT_COMPLETE ` - 部署结束     * `ROLLBACK_IN_PROGRESS` - 正在回滚     * `ROLLBACK_FAILED` - 回滚失败。请于StatusMessage见更多详情     * `ROLLBACK_COMPLETE` - 回滚完成     * `DELETION_IN_PROGRESS` - 正在删除     * `DELETION_FAILED` - 删除失败     * `CREATION_COMPLETE` - 生成完成，并没有任何部署

        :return: The status of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetStackMetadataResponse.

        资源栈的执行状态     * `DEPLOYMENT_IN_PROGRESS` - 正在部署     * `DEPLOYMENT_FAILED` - 部署失败。请于StatusMessage见更多详情     * `DEPLOYMENT_COMPLETE ` - 部署结束     * `ROLLBACK_IN_PROGRESS` - 正在回滚     * `ROLLBACK_FAILED` - 回滚失败。请于StatusMessage见更多详情     * `ROLLBACK_COMPLETE` - 回滚完成     * `DELETION_IN_PROGRESS` - 正在删除     * `DELETION_FAILED` - 删除失败     * `CREATION_COMPLETE` - 生成完成，并没有任何部署

        :param status: The status of this GetStackMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this GetStackMetadataResponse.

        展示更多细节的信息

        :return: The status_message of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this GetStackMetadataResponse.

        展示更多细节的信息

        :param status_message: The status_message of this GetStackMetadataResponse.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def agencies(self):
        """Gets the agencies of this GetStackMetadataResponse.

        委托授权的信息

        :return: The agencies of this GetStackMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this GetStackMetadataResponse.

        委托授权的信息

        :param agencies: The agencies of this GetStackMetadataResponse.
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        self._agencies = agencies

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
        if not isinstance(other, GetStackMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
