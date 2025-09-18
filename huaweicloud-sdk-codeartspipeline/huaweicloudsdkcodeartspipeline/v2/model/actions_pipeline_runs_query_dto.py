# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionsPipelineRunsQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'str',
        'https_url': 'str',
        'pipeline_name': 'str',
        'file_path': 'str',
        'pipeline_run_name': 'str',
        'event': 'str',
        'actor': 'str',
        'branch': 'str',
        'status': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'https_url': 'https_url',
        'pipeline_name': 'pipeline_name',
        'file_path': 'file_path',
        'pipeline_run_name': 'pipeline_run_name',
        'event': 'event',
        'actor': 'actor',
        'branch': 'branch',
        'status': 'status'
    }

    def __init__(self, page=None, page_size=None, https_url=None, pipeline_name=None, file_path=None, pipeline_run_name=None, event=None, actor=None, branch=None, status=None):
        r"""ActionsPipelineRunsQueryDTO

        The model defined in huaweicloud sdk

        :param page: **参数解释**： 分页查询页码。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不涉及。 
        :type page: int
        :param page_size: **参数解释**： 每页的查询数量。 **约束限制**： 不涉及。 **取值范围**： 固定20。 **默认取值**： 不涉及。 
        :type page_size: str
        :param https_url: **参数解释**： 代码源地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type https_url: str
        :param pipeline_name: **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type pipeline_name: str
        :param file_path: **参数解释**： 文件所处路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type file_path: str
        :param pipeline_run_name: **参数解释**： 流水线运行人名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type pipeline_run_name: str
        :param event: **参数解释**： 流水线触发类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type event: str
        :param actor: **参数解释**： 流水线创建者名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type actor: str
        :param branch: **参数解释**： 代码源分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type branch: str
        :param status: **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type status: str
        """
        
        

        self._page = None
        self._page_size = None
        self._https_url = None
        self._pipeline_name = None
        self._file_path = None
        self._pipeline_run_name = None
        self._event = None
        self._actor = None
        self._branch = None
        self._status = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        self.https_url = https_url
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if file_path is not None:
            self.file_path = file_path
        if pipeline_run_name is not None:
            self.pipeline_run_name = pipeline_run_name
        if event is not None:
            self.event = event
        if actor is not None:
            self.actor = actor
        if branch is not None:
            self.branch = branch
        if status is not None:
            self.status = status

    @property
    def page(self):
        r"""Gets the page of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 分页查询页码。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不涉及。 

        :return: The page of this ActionsPipelineRunsQueryDTO.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 分页查询页码。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不涉及。 

        :param page: The page of this ActionsPipelineRunsQueryDTO.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 每页的查询数量。 **约束限制**： 不涉及。 **取值范围**： 固定20。 **默认取值**： 不涉及。 

        :return: The page_size of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 每页的查询数量。 **约束限制**： 不涉及。 **取值范围**： 固定20。 **默认取值**： 不涉及。 

        :param page_size: The page_size of this ActionsPipelineRunsQueryDTO.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def https_url(self):
        r"""Gets the https_url of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 代码源地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The https_url of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        r"""Sets the https_url of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 代码源地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param https_url: The https_url of this ActionsPipelineRunsQueryDTO.
        :type https_url: str
        """
        self._https_url = https_url

    @property
    def pipeline_name(self):
        r"""Gets the pipeline_name of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The pipeline_name of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        r"""Sets the pipeline_name of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param pipeline_name: The pipeline_name of this ActionsPipelineRunsQueryDTO.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 文件所处路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The file_path of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 文件所处路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param file_path: The file_path of this ActionsPipelineRunsQueryDTO.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def pipeline_run_name(self):
        r"""Gets the pipeline_run_name of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线运行人名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The pipeline_run_name of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._pipeline_run_name

    @pipeline_run_name.setter
    def pipeline_run_name(self, pipeline_run_name):
        r"""Sets the pipeline_run_name of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线运行人名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param pipeline_run_name: The pipeline_run_name of this ActionsPipelineRunsQueryDTO.
        :type pipeline_run_name: str
        """
        self._pipeline_run_name = pipeline_run_name

    @property
    def event(self):
        r"""Gets the event of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线触发类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The event of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线触发类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param event: The event of this ActionsPipelineRunsQueryDTO.
        :type event: str
        """
        self._event = event

    @property
    def actor(self):
        r"""Gets the actor of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线创建者名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The actor of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        r"""Sets the actor of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线创建者名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param actor: The actor of this ActionsPipelineRunsQueryDTO.
        :type actor: str
        """
        self._actor = actor

    @property
    def branch(self):
        r"""Gets the branch of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 代码源分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The branch of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 代码源分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param branch: The branch of this ActionsPipelineRunsQueryDTO.
        :type branch: str
        """
        self._branch = branch

    @property
    def status(self):
        r"""Gets the status of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The status of this ActionsPipelineRunsQueryDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ActionsPipelineRunsQueryDTO.

        **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param status: The status of this ActionsPipelineRunsQueryDTO.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ActionsPipelineRunsQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
