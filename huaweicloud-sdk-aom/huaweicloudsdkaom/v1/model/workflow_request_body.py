# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'tags': 'object',
        'template_name': 'str',
        'template_id': 'str',
        'input': 'dict(str, object)',
        'citation_urns': 'list[str]',
        'quote': 'list[str]',
        'trigger': 'Trigger',
        'job_name': 'str',
        'job_id': 'str',
        'service_scenario': 'str',
        'service_name': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'tags': 'tags',
        'template_name': 'template_name',
        'template_id': 'template_id',
        'input': 'input',
        'citation_urns': 'citation_urns',
        'quote': 'quote',
        'trigger': 'trigger',
        'job_name': 'job_name',
        'job_id': 'job_id',
        'service_scenario': 'service_scenario',
        'service_name': 'service_name',
        'task_type': 'task_type'
    }

    def __init__(self, name=None, type=None, description=None, tags=None, template_name=None, template_id=None, input=None, citation_urns=None, quote=None, trigger=None, job_name=None, job_id=None, service_scenario=None, service_name=None, task_type=None):
        """WorkflowRequestBody

        The model defined in huaweicloud sdk

        :param name: 工作流名称，需要满足：[^\\\\&gt;+&lt;^;#\&quot;\\s&amp;?%&#x3D;&#39;$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~&#x60;·？《》…]{1,64}。
        :type name: str
        :param type: 工作流类型，可以为cron/manul/event。
        :type type: str
        :param description: 工作流描述信息。
        :type description: str
        :param tags: 标签键和值列表，标签键值对数量范围是0至20。
        :type tags: object
        :param template_name: 模板名称，需要满足：[^\\\\&gt;+&lt;^;#\&quot;\\s&amp;?%&#x3D;&#39;$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~&#x60;·？《》…]{1,64}。
        :type template_name: str
        :param template_id: 模板id。
        :type template_id: str
        :param input: 任务执行时需要的参数列表。
        :type input: dict(str, object)
        :param citation_urns: 引用链接,workflow引用的工作链接。
        :type citation_urns: list[str]
        :param quote: 引用，参数引用。
        :type quote: list[str]
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkaom.v1.Trigger`
        :param job_name: 作业名称。
        :type job_name: str
        :param job_id: 作业id。
        :type job_id: str
        :param service_scenario: 服务场景分类。
        :type service_scenario: str
        :param service_name: 服务名称。
        :type service_name: str
        :param task_type: 任务类型。
        :type task_type: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._tags = None
        self._template_name = None
        self._template_id = None
        self._input = None
        self._citation_urns = None
        self._quote = None
        self._trigger = None
        self._job_name = None
        self._job_id = None
        self._service_scenario = None
        self._service_name = None
        self._task_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if template_name is not None:
            self.template_name = template_name
        if template_id is not None:
            self.template_id = template_id
        if input is not None:
            self.input = input
        if citation_urns is not None:
            self.citation_urns = citation_urns
        if quote is not None:
            self.quote = quote
        if trigger is not None:
            self.trigger = trigger
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if service_scenario is not None:
            self.service_scenario = service_scenario
        if service_name is not None:
            self.service_name = service_name
        if task_type is not None:
            self.task_type = task_type

    @property
    def name(self):
        """Gets the name of this WorkflowRequestBody.

        工作流名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :return: The name of this WorkflowRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowRequestBody.

        工作流名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :param name: The name of this WorkflowRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this WorkflowRequestBody.

        工作流类型，可以为cron/manul/event。

        :return: The type of this WorkflowRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkflowRequestBody.

        工作流类型，可以为cron/manul/event。

        :param type: The type of this WorkflowRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this WorkflowRequestBody.

        工作流描述信息。

        :return: The description of this WorkflowRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowRequestBody.

        工作流描述信息。

        :param description: The description of this WorkflowRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this WorkflowRequestBody.

        标签键和值列表，标签键值对数量范围是0至20。

        :return: The tags of this WorkflowRequestBody.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WorkflowRequestBody.

        标签键和值列表，标签键值对数量范围是0至20。

        :param tags: The tags of this WorkflowRequestBody.
        :type tags: object
        """
        self._tags = tags

    @property
    def template_name(self):
        """Gets the template_name of this WorkflowRequestBody.

        模板名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :return: The template_name of this WorkflowRequestBody.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this WorkflowRequestBody.

        模板名称，需要满足：[^\\\\>+<^;#\"\\s&?%='$￥@*/\\]\\[【】{}|:,.，。：‘’“、—！!~`·？《》…]{1,64}。

        :param template_name: The template_name of this WorkflowRequestBody.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_id(self):
        """Gets the template_id of this WorkflowRequestBody.

        模板id。

        :return: The template_id of this WorkflowRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WorkflowRequestBody.

        模板id。

        :param template_id: The template_id of this WorkflowRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def input(self):
        """Gets the input of this WorkflowRequestBody.

        任务执行时需要的参数列表。

        :return: The input of this WorkflowRequestBody.
        :rtype: dict(str, object)
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this WorkflowRequestBody.

        任务执行时需要的参数列表。

        :param input: The input of this WorkflowRequestBody.
        :type input: dict(str, object)
        """
        self._input = input

    @property
    def citation_urns(self):
        """Gets the citation_urns of this WorkflowRequestBody.

        引用链接,workflow引用的工作链接。

        :return: The citation_urns of this WorkflowRequestBody.
        :rtype: list[str]
        """
        return self._citation_urns

    @citation_urns.setter
    def citation_urns(self, citation_urns):
        """Sets the citation_urns of this WorkflowRequestBody.

        引用链接,workflow引用的工作链接。

        :param citation_urns: The citation_urns of this WorkflowRequestBody.
        :type citation_urns: list[str]
        """
        self._citation_urns = citation_urns

    @property
    def quote(self):
        """Gets the quote of this WorkflowRequestBody.

        引用，参数引用。

        :return: The quote of this WorkflowRequestBody.
        :rtype: list[str]
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this WorkflowRequestBody.

        引用，参数引用。

        :param quote: The quote of this WorkflowRequestBody.
        :type quote: list[str]
        """
        self._quote = quote

    @property
    def trigger(self):
        """Gets the trigger of this WorkflowRequestBody.

        :return: The trigger of this WorkflowRequestBody.
        :rtype: :class:`huaweicloudsdkaom.v1.Trigger`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this WorkflowRequestBody.

        :param trigger: The trigger of this WorkflowRequestBody.
        :type trigger: :class:`huaweicloudsdkaom.v1.Trigger`
        """
        self._trigger = trigger

    @property
    def job_name(self):
        """Gets the job_name of this WorkflowRequestBody.

        作业名称。

        :return: The job_name of this WorkflowRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this WorkflowRequestBody.

        作业名称。

        :param job_name: The job_name of this WorkflowRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        """Gets the job_id of this WorkflowRequestBody.

        作业id。

        :return: The job_id of this WorkflowRequestBody.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this WorkflowRequestBody.

        作业id。

        :param job_id: The job_id of this WorkflowRequestBody.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def service_scenario(self):
        """Gets the service_scenario of this WorkflowRequestBody.

        服务场景分类。

        :return: The service_scenario of this WorkflowRequestBody.
        :rtype: str
        """
        return self._service_scenario

    @service_scenario.setter
    def service_scenario(self, service_scenario):
        """Sets the service_scenario of this WorkflowRequestBody.

        服务场景分类。

        :param service_scenario: The service_scenario of this WorkflowRequestBody.
        :type service_scenario: str
        """
        self._service_scenario = service_scenario

    @property
    def service_name(self):
        """Gets the service_name of this WorkflowRequestBody.

        服务名称。

        :return: The service_name of this WorkflowRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this WorkflowRequestBody.

        服务名称。

        :param service_name: The service_name of this WorkflowRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def task_type(self):
        """Gets the task_type of this WorkflowRequestBody.

        任务类型。

        :return: The task_type of this WorkflowRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this WorkflowRequestBody.

        任务类型。

        :param task_type: The task_type of this WorkflowRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, WorkflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
