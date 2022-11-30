# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchTemplateByIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approve_info': 'ApproveInfo',
        'create_by': 'str',
        'create_time': 'int',
        'enterprise_project_id': 'str',
        'id': 'str',
        'is_collect': 'bool',
        'is_publish': 'bool',
        'job_id': 'str',
        'job_version': 'int',
        'name': 'str',
        'need_synchronize': 'bool',
        'nodes': 'list[Node]',
        'parameters': 'list[Parameter]',
        'project_id': 'str',
        'quote': 'list[str]',
        'rate_control': 'RateControl',
        'share_type': 'str',
        'steps': 'list[Step]',
        'update_by': 'str',
        'update_time': 'int',
        'version': 'str'
    }

    attribute_map = {
        'approve_info': 'approve_info',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'is_collect': 'is_collect',
        'is_publish': 'is_publish',
        'job_id': 'job_id',
        'job_version': 'job_version',
        'name': 'name',
        'need_synchronize': 'need_synchronize',
        'nodes': 'nodes',
        'parameters': 'parameters',
        'project_id': 'project_id',
        'quote': 'quote',
        'rate_control': 'rate_control',
        'share_type': 'share_type',
        'steps': 'steps',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'version': 'version'
    }

    def __init__(self, approve_info=None, create_by=None, create_time=None, enterprise_project_id=None, id=None, is_collect=None, is_publish=None, job_id=None, job_version=None, name=None, need_synchronize=None, nodes=None, parameters=None, project_id=None, quote=None, rate_control=None, share_type=None, steps=None, update_by=None, update_time=None, version=None):
        """SearchTemplateByIdResponse

        The model defined in huaweicloud sdk

        :param approve_info: 
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        :param create_by: 模板创人，从接口调用传入的token中获取。
        :type create_by: str
        :param create_time: 模板创建时间，为utc时间毫秒数。
        :type create_time: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param id: 模板id，唯一标识，根据project_id和template_name生成。
        :type id: str
        :param is_collect: 模板是否收藏，不允许更新模板时修改，更改收藏状态调用单独的更新模板收藏状态接口
        :type is_collect: bool
        :param is_publish: 是否发布成服务
        :type is_publish: bool
        :param job_id: 作业id
        :type job_id: str
        :param job_version: 作业版本
        :type job_version: int
        :param name: 模板名称，需要满足：。 不允许更新模板时修改
        :type name: str
        :param need_synchronize: 是否需要同步
        :type need_synchronize: bool
        :param nodes: 任务执行时需要的参数列表。
        :type nodes: list[:class:`huaweicloudsdkaom.v1.Node`]
        :param parameters: 任务执行时需要的参数列表。
        :type parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        :param project_id: 项目id
        :type project_id: str
        :param quote: 引用参数
        :type quote: list[str]
        :param rate_control: 
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        :param share_type: 默认模板为public，自定义模板为private
        :type share_type: str
        :param steps: 作业步骤
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        :param update_by: 模板更新人，从接口调用传入的token中获取。
        :type update_by: str
        :param update_time: 模板更新时间，为utc时间毫秒数。
        :type update_time: int
        :param version: 模板版本
        :type version: str
        """
        
        super(SearchTemplateByIdResponse, self).__init__()

        self._approve_info = None
        self._create_by = None
        self._create_time = None
        self._enterprise_project_id = None
        self._id = None
        self._is_collect = None
        self._is_publish = None
        self._job_id = None
        self._job_version = None
        self._name = None
        self._need_synchronize = None
        self._nodes = None
        self._parameters = None
        self._project_id = None
        self._quote = None
        self._rate_control = None
        self._share_type = None
        self._steps = None
        self._update_by = None
        self._update_time = None
        self._version = None
        self.discriminator = None

        if approve_info is not None:
            self.approve_info = approve_info
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if is_collect is not None:
            self.is_collect = is_collect
        if is_publish is not None:
            self.is_publish = is_publish
        if job_id is not None:
            self.job_id = job_id
        if job_version is not None:
            self.job_version = job_version
        if name is not None:
            self.name = name
        if need_synchronize is not None:
            self.need_synchronize = need_synchronize
        if nodes is not None:
            self.nodes = nodes
        if parameters is not None:
            self.parameters = parameters
        if project_id is not None:
            self.project_id = project_id
        if quote is not None:
            self.quote = quote
        if rate_control is not None:
            self.rate_control = rate_control
        if share_type is not None:
            self.share_type = share_type
        if steps is not None:
            self.steps = steps
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version

    @property
    def approve_info(self):
        """Gets the approve_info of this SearchTemplateByIdResponse.

        :return: The approve_info of this SearchTemplateByIdResponse.
        :rtype: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        return self._approve_info

    @approve_info.setter
    def approve_info(self, approve_info):
        """Sets the approve_info of this SearchTemplateByIdResponse.

        :param approve_info: The approve_info of this SearchTemplateByIdResponse.
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        self._approve_info = approve_info

    @property
    def create_by(self):
        """Gets the create_by of this SearchTemplateByIdResponse.

        模板创人，从接口调用传入的token中获取。

        :return: The create_by of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this SearchTemplateByIdResponse.

        模板创人，从接口调用传入的token中获取。

        :param create_by: The create_by of this SearchTemplateByIdResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this SearchTemplateByIdResponse.

        模板创建时间，为utc时间毫秒数。

        :return: The create_time of this SearchTemplateByIdResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SearchTemplateByIdResponse.

        模板创建时间，为utc时间毫秒数。

        :param create_time: The create_time of this SearchTemplateByIdResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SearchTemplateByIdResponse.

        企业项目id

        :return: The enterprise_project_id of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SearchTemplateByIdResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this SearchTemplateByIdResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this SearchTemplateByIdResponse.

        模板id，唯一标识，根据project_id和template_name生成。

        :return: The id of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchTemplateByIdResponse.

        模板id，唯一标识，根据project_id和template_name生成。

        :param id: The id of this SearchTemplateByIdResponse.
        :type id: str
        """
        self._id = id

    @property
    def is_collect(self):
        """Gets the is_collect of this SearchTemplateByIdResponse.

        模板是否收藏，不允许更新模板时修改，更改收藏状态调用单独的更新模板收藏状态接口

        :return: The is_collect of this SearchTemplateByIdResponse.
        :rtype: bool
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        """Sets the is_collect of this SearchTemplateByIdResponse.

        模板是否收藏，不允许更新模板时修改，更改收藏状态调用单独的更新模板收藏状态接口

        :param is_collect: The is_collect of this SearchTemplateByIdResponse.
        :type is_collect: bool
        """
        self._is_collect = is_collect

    @property
    def is_publish(self):
        """Gets the is_publish of this SearchTemplateByIdResponse.

        是否发布成服务

        :return: The is_publish of this SearchTemplateByIdResponse.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this SearchTemplateByIdResponse.

        是否发布成服务

        :param is_publish: The is_publish of this SearchTemplateByIdResponse.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def job_id(self):
        """Gets the job_id of this SearchTemplateByIdResponse.

        作业id

        :return: The job_id of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SearchTemplateByIdResponse.

        作业id

        :param job_id: The job_id of this SearchTemplateByIdResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_version(self):
        """Gets the job_version of this SearchTemplateByIdResponse.

        作业版本

        :return: The job_version of this SearchTemplateByIdResponse.
        :rtype: int
        """
        return self._job_version

    @job_version.setter
    def job_version(self, job_version):
        """Sets the job_version of this SearchTemplateByIdResponse.

        作业版本

        :param job_version: The job_version of this SearchTemplateByIdResponse.
        :type job_version: int
        """
        self._job_version = job_version

    @property
    def name(self):
        """Gets the name of this SearchTemplateByIdResponse.

        模板名称，需要满足：。 不允许更新模板时修改

        :return: The name of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchTemplateByIdResponse.

        模板名称，需要满足：。 不允许更新模板时修改

        :param name: The name of this SearchTemplateByIdResponse.
        :type name: str
        """
        self._name = name

    @property
    def need_synchronize(self):
        """Gets the need_synchronize of this SearchTemplateByIdResponse.

        是否需要同步

        :return: The need_synchronize of this SearchTemplateByIdResponse.
        :rtype: bool
        """
        return self._need_synchronize

    @need_synchronize.setter
    def need_synchronize(self, need_synchronize):
        """Sets the need_synchronize of this SearchTemplateByIdResponse.

        是否需要同步

        :param need_synchronize: The need_synchronize of this SearchTemplateByIdResponse.
        :type need_synchronize: bool
        """
        self._need_synchronize = need_synchronize

    @property
    def nodes(self):
        """Gets the nodes of this SearchTemplateByIdResponse.

        任务执行时需要的参数列表。

        :return: The nodes of this SearchTemplateByIdResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this SearchTemplateByIdResponse.

        任务执行时需要的参数列表。

        :param nodes: The nodes of this SearchTemplateByIdResponse.
        :type nodes: list[:class:`huaweicloudsdkaom.v1.Node`]
        """
        self._nodes = nodes

    @property
    def parameters(self):
        """Gets the parameters of this SearchTemplateByIdResponse.

        任务执行时需要的参数列表。

        :return: The parameters of this SearchTemplateByIdResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SearchTemplateByIdResponse.

        任务执行时需要的参数列表。

        :param parameters: The parameters of this SearchTemplateByIdResponse.
        :type parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        self._parameters = parameters

    @property
    def project_id(self):
        """Gets the project_id of this SearchTemplateByIdResponse.

        项目id

        :return: The project_id of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchTemplateByIdResponse.

        项目id

        :param project_id: The project_id of this SearchTemplateByIdResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def quote(self):
        """Gets the quote of this SearchTemplateByIdResponse.

        引用参数

        :return: The quote of this SearchTemplateByIdResponse.
        :rtype: list[str]
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this SearchTemplateByIdResponse.

        引用参数

        :param quote: The quote of this SearchTemplateByIdResponse.
        :type quote: list[str]
        """
        self._quote = quote

    @property
    def rate_control(self):
        """Gets the rate_control of this SearchTemplateByIdResponse.

        :return: The rate_control of this SearchTemplateByIdResponse.
        :rtype: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        return self._rate_control

    @rate_control.setter
    def rate_control(self, rate_control):
        """Sets the rate_control of this SearchTemplateByIdResponse.

        :param rate_control: The rate_control of this SearchTemplateByIdResponse.
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        self._rate_control = rate_control

    @property
    def share_type(self):
        """Gets the share_type of this SearchTemplateByIdResponse.

        默认模板为public，自定义模板为private

        :return: The share_type of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this SearchTemplateByIdResponse.

        默认模板为public，自定义模板为private

        :param share_type: The share_type of this SearchTemplateByIdResponse.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def steps(self):
        """Gets the steps of this SearchTemplateByIdResponse.

        作业步骤

        :return: The steps of this SearchTemplateByIdResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this SearchTemplateByIdResponse.

        作业步骤

        :param steps: The steps of this SearchTemplateByIdResponse.
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        self._steps = steps

    @property
    def update_by(self):
        """Gets the update_by of this SearchTemplateByIdResponse.

        模板更新人，从接口调用传入的token中获取。

        :return: The update_by of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this SearchTemplateByIdResponse.

        模板更新人，从接口调用传入的token中获取。

        :param update_by: The update_by of this SearchTemplateByIdResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this SearchTemplateByIdResponse.

        模板更新时间，为utc时间毫秒数。

        :return: The update_time of this SearchTemplateByIdResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SearchTemplateByIdResponse.

        模板更新时间，为utc时间毫秒数。

        :param update_time: The update_time of this SearchTemplateByIdResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def version(self):
        """Gets the version of this SearchTemplateByIdResponse.

        模板版本

        :return: The version of this SearchTemplateByIdResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SearchTemplateByIdResponse.

        模板版本

        :param version: The version of this SearchTemplateByIdResponse.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, SearchTemplateByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
