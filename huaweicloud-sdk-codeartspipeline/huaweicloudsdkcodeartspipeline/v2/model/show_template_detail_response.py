# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'is_build_in': 'bool',
        'region': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'create_time': 'str',
        'last_modify_time': 'str',
        'is_watch': 'bool',
        'description': 'str',
        'parameter': 'list[TemplateParam]',
        'flow': 'dict(str, dict(str, str))',
        'states': 'dict(str, TemplateState)'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'is_build_in': 'is_build_in',
        'region': 'region',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time',
        'is_watch': 'is_watch',
        'description': 'description',
        'parameter': 'parameter',
        'flow': 'flow',
        'states': 'states'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, user_id=None, user_name=None, domain_id=None, domain_name=None, is_build_in=None, region=None, project_id=None, project_name=None, create_time=None, last_modify_time=None, is_watch=None, description=None, parameter=None, flow=None, states=None):
        r"""ShowTemplateDetailResponse

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名字
        :type template_name: str
        :param template_type: 模板类型
        :type template_type: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名字
        :type user_name: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param domain_name: 租户名字
        :type domain_name: str
        :param is_build_in: 是否内置模板
        :type is_build_in: bool
        :param region: region
        :type region: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名字
        :type project_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param last_modify_time: 修改时间
        :type last_modify_time: str
        :param is_watch: 是否关注
        :type is_watch: bool
        :param description: 模板描述
        :type description: str
        :param parameter: 模板参数
        :type parameter: list[:class:`huaweicloudsdkcodeartspipeline.v2.TemplateParam`]
        :param flow: 编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以&#39;state_数字&#39;标识。value为该阶段内任务(以&#39;Task_数字&#39;标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type flow: dict(str, dict(str, str))
        :param states: 编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type states: dict(str, TemplateState)
        """
        
        super(ShowTemplateDetailResponse, self).__init__()

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._user_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._is_build_in = None
        self._region = None
        self._project_id = None
        self._project_name = None
        self._create_time = None
        self._last_modify_time = None
        self._is_watch = None
        self._description = None
        self._parameter = None
        self._flow = None
        self._states = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if is_build_in is not None:
            self.is_build_in = is_build_in
        if region is not None:
            self.region = region
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        if is_watch is not None:
            self.is_watch = is_watch
        if description is not None:
            self.description = description
        if parameter is not None:
            self.parameter = parameter
        if flow is not None:
            self.flow = flow
        if states is not None:
            self.states = states

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowTemplateDetailResponse.

        模板ID

        :return: The template_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowTemplateDetailResponse.

        模板ID

        :param template_id: The template_id of this ShowTemplateDetailResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowTemplateDetailResponse.

        模板名字

        :return: The template_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowTemplateDetailResponse.

        模板名字

        :param template_name: The template_name of this ShowTemplateDetailResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ShowTemplateDetailResponse.

        模板类型

        :return: The template_type of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ShowTemplateDetailResponse.

        模板类型

        :param template_type: The template_type of this ShowTemplateDetailResponse.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowTemplateDetailResponse.

        用户ID

        :return: The user_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowTemplateDetailResponse.

        用户ID

        :param user_id: The user_id of this ShowTemplateDetailResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowTemplateDetailResponse.

        用户名字

        :return: The user_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowTemplateDetailResponse.

        用户名字

        :param user_name: The user_name of this ShowTemplateDetailResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowTemplateDetailResponse.

        租户ID

        :return: The domain_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowTemplateDetailResponse.

        租户ID

        :param domain_id: The domain_id of this ShowTemplateDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowTemplateDetailResponse.

        租户名字

        :return: The domain_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowTemplateDetailResponse.

        租户名字

        :param domain_name: The domain_name of this ShowTemplateDetailResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def is_build_in(self):
        r"""Gets the is_build_in of this ShowTemplateDetailResponse.

        是否内置模板

        :return: The is_build_in of this ShowTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_build_in

    @is_build_in.setter
    def is_build_in(self, is_build_in):
        r"""Sets the is_build_in of this ShowTemplateDetailResponse.

        是否内置模板

        :param is_build_in: The is_build_in of this ShowTemplateDetailResponse.
        :type is_build_in: bool
        """
        self._is_build_in = is_build_in

    @property
    def region(self):
        r"""Gets the region of this ShowTemplateDetailResponse.

        region

        :return: The region of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowTemplateDetailResponse.

        region

        :param region: The region of this ShowTemplateDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTemplateDetailResponse.

        项目ID

        :return: The project_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTemplateDetailResponse.

        项目ID

        :param project_id: The project_id of this ShowTemplateDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowTemplateDetailResponse.

        项目名字

        :return: The project_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowTemplateDetailResponse.

        项目名字

        :param project_name: The project_name of this ShowTemplateDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowTemplateDetailResponse.

        创建时间

        :return: The create_time of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowTemplateDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowTemplateDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        r"""Gets the last_modify_time of this ShowTemplateDetailResponse.

        修改时间

        :return: The last_modify_time of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        r"""Sets the last_modify_time of this ShowTemplateDetailResponse.

        修改时间

        :param last_modify_time: The last_modify_time of this ShowTemplateDetailResponse.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    @property
    def is_watch(self):
        r"""Gets the is_watch of this ShowTemplateDetailResponse.

        是否关注

        :return: The is_watch of this ShowTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_watch

    @is_watch.setter
    def is_watch(self, is_watch):
        r"""Sets the is_watch of this ShowTemplateDetailResponse.

        是否关注

        :param is_watch: The is_watch of this ShowTemplateDetailResponse.
        :type is_watch: bool
        """
        self._is_watch = is_watch

    @property
    def description(self):
        r"""Gets the description of this ShowTemplateDetailResponse.

        模板描述

        :return: The description of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowTemplateDetailResponse.

        模板描述

        :param description: The description of this ShowTemplateDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def parameter(self):
        r"""Gets the parameter of this ShowTemplateDetailResponse.

        模板参数

        :return: The parameter of this ShowTemplateDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.TemplateParam`]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        r"""Sets the parameter of this ShowTemplateDetailResponse.

        模板参数

        :param parameter: The parameter of this ShowTemplateDetailResponse.
        :type parameter: list[:class:`huaweicloudsdkcodeartspipeline.v2.TemplateParam`]
        """
        self._parameter = parameter

    @property
    def flow(self):
        r"""Gets the flow of this ShowTemplateDetailResponse.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The flow of this ShowTemplateDetailResponse.
        :rtype: dict(str, dict(str, str))
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        r"""Sets the flow of this ShowTemplateDetailResponse.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param flow: The flow of this ShowTemplateDetailResponse.
        :type flow: dict(str, dict(str, str))
        """
        self._flow = flow

    @property
    def states(self):
        r"""Gets the states of this ShowTemplateDetailResponse.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The states of this ShowTemplateDetailResponse.
        :rtype: dict(str, TemplateState)
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this ShowTemplateDetailResponse.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param states: The states of this ShowTemplateDetailResponse.
        :type states: dict(str, TemplateState)
        """
        self._states = states

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
        if not isinstance(other, ShowTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
