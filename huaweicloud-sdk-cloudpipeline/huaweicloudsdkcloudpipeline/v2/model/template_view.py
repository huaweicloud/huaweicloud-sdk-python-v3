# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateView:

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
        'template_url': 'str',
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
        'states': 'dict(str, TemplateState)',
        'can_update': 'bool',
        'can_delete': 'bool',
        'need_hub': 'bool'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'template_url': 'template_url',
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
        'states': 'states',
        'can_update': 'can_update',
        'can_delete': 'can_delete',
        'need_hub': 'need_hub'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, template_url=None, user_id=None, user_name=None, domain_id=None, domain_name=None, is_build_in=None, region=None, project_id=None, project_name=None, create_time=None, last_modify_time=None, is_watch=None, description=None, parameter=None, flow=None, states=None, can_update=None, can_delete=None, need_hub=None):
        """TemplateView

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名字
        :type template_name: str
        :param template_type: 模板类型
        :type template_type: str
        :param template_url: 模板编辑URL
        :type template_url: str
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
        :param region: 系统模板region为Cloud Pipeline。自定义模板region为实际region
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
        :type parameter: list[:class:`huaweicloudsdkcloudpipeline.v2.TemplateParam`]
        :param flow: 编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以&#39;state_数字&#39;标识。value为该阶段内任务(以&#39;Task_数字&#39;标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type flow: dict(str, dict(str, str))
        :param states: 编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type states: dict(str, TemplateState)
        :param can_update: 是否可以修改
        :type can_update: bool
        :param can_delete: 是否可以删除
        :type can_delete: bool
        :param need_hub: 是否需要代码仓库
        :type need_hub: bool
        """
        
        

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._template_url = None
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
        self._can_update = None
        self._can_delete = None
        self._need_hub = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        self.template_url = template_url
        self.user_id = user_id
        self.user_name = user_name
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.is_build_in = is_build_in
        self.region = region
        self.project_id = project_id
        self.project_name = project_name
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.is_watch = is_watch
        self.description = description
        self.parameter = parameter
        self.flow = flow
        self.states = states
        self.can_update = can_update
        self.can_delete = can_delete
        self.need_hub = need_hub

    @property
    def template_id(self):
        """Gets the template_id of this TemplateView.

        模板ID

        :return: The template_id of this TemplateView.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateView.

        模板ID

        :param template_id: The template_id of this TemplateView.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this TemplateView.

        模板名字

        :return: The template_name of this TemplateView.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateView.

        模板名字

        :param template_name: The template_name of this TemplateView.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this TemplateView.

        模板类型

        :return: The template_type of this TemplateView.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this TemplateView.

        模板类型

        :param template_type: The template_type of this TemplateView.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def template_url(self):
        """Gets the template_url of this TemplateView.

        模板编辑URL

        :return: The template_url of this TemplateView.
        :rtype: str
        """
        return self._template_url

    @template_url.setter
    def template_url(self, template_url):
        """Sets the template_url of this TemplateView.

        模板编辑URL

        :param template_url: The template_url of this TemplateView.
        :type template_url: str
        """
        self._template_url = template_url

    @property
    def user_id(self):
        """Gets the user_id of this TemplateView.

        用户ID

        :return: The user_id of this TemplateView.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TemplateView.

        用户ID

        :param user_id: The user_id of this TemplateView.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this TemplateView.

        用户名字

        :return: The user_name of this TemplateView.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TemplateView.

        用户名字

        :param user_name: The user_name of this TemplateView.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        """Gets the domain_id of this TemplateView.

        租户ID

        :return: The domain_id of this TemplateView.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this TemplateView.

        租户ID

        :param domain_id: The domain_id of this TemplateView.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this TemplateView.

        租户名字

        :return: The domain_name of this TemplateView.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this TemplateView.

        租户名字

        :param domain_name: The domain_name of this TemplateView.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def is_build_in(self):
        """Gets the is_build_in of this TemplateView.

        是否内置模板

        :return: The is_build_in of this TemplateView.
        :rtype: bool
        """
        return self._is_build_in

    @is_build_in.setter
    def is_build_in(self, is_build_in):
        """Sets the is_build_in of this TemplateView.

        是否内置模板

        :param is_build_in: The is_build_in of this TemplateView.
        :type is_build_in: bool
        """
        self._is_build_in = is_build_in

    @property
    def region(self):
        """Gets the region of this TemplateView.

        系统模板region为Cloud Pipeline。自定义模板region为实际region

        :return: The region of this TemplateView.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TemplateView.

        系统模板region为Cloud Pipeline。自定义模板region为实际region

        :param region: The region of this TemplateView.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        """Gets the project_id of this TemplateView.

        项目ID

        :return: The project_id of this TemplateView.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplateView.

        项目ID

        :param project_id: The project_id of this TemplateView.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this TemplateView.

        项目名字

        :return: The project_name of this TemplateView.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TemplateView.

        项目名字

        :param project_name: The project_name of this TemplateView.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def create_time(self):
        """Gets the create_time of this TemplateView.

        创建时间

        :return: The create_time of this TemplateView.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TemplateView.

        创建时间

        :param create_time: The create_time of this TemplateView.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this TemplateView.

        修改时间

        :return: The last_modify_time of this TemplateView.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this TemplateView.

        修改时间

        :param last_modify_time: The last_modify_time of this TemplateView.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    @property
    def is_watch(self):
        """Gets the is_watch of this TemplateView.

        是否关注

        :return: The is_watch of this TemplateView.
        :rtype: bool
        """
        return self._is_watch

    @is_watch.setter
    def is_watch(self, is_watch):
        """Sets the is_watch of this TemplateView.

        是否关注

        :param is_watch: The is_watch of this TemplateView.
        :type is_watch: bool
        """
        self._is_watch = is_watch

    @property
    def description(self):
        """Gets the description of this TemplateView.

        模板描述

        :return: The description of this TemplateView.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateView.

        模板描述

        :param description: The description of this TemplateView.
        :type description: str
        """
        self._description = description

    @property
    def parameter(self):
        """Gets the parameter of this TemplateView.

        模板参数

        :return: The parameter of this TemplateView.
        :rtype: list[:class:`huaweicloudsdkcloudpipeline.v2.TemplateParam`]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this TemplateView.

        模板参数

        :param parameter: The parameter of this TemplateView.
        :type parameter: list[:class:`huaweicloudsdkcloudpipeline.v2.TemplateParam`]
        """
        self._parameter = parameter

    @property
    def flow(self):
        """Gets the flow of this TemplateView.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The flow of this TemplateView.
        :rtype: dict(str, dict(str, str))
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this TemplateView.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param flow: The flow of this TemplateView.
        :type flow: dict(str, dict(str, str))
        """
        self._flow = flow

    @property
    def states(self):
        """Gets the states of this TemplateView.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The states of this TemplateView.
        :rtype: dict(str, TemplateState)
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this TemplateView.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param states: The states of this TemplateView.
        :type states: dict(str, TemplateState)
        """
        self._states = states

    @property
    def can_update(self):
        """Gets the can_update of this TemplateView.

        是否可以修改

        :return: The can_update of this TemplateView.
        :rtype: bool
        """
        return self._can_update

    @can_update.setter
    def can_update(self, can_update):
        """Sets the can_update of this TemplateView.

        是否可以修改

        :param can_update: The can_update of this TemplateView.
        :type can_update: bool
        """
        self._can_update = can_update

    @property
    def can_delete(self):
        """Gets the can_delete of this TemplateView.

        是否可以删除

        :return: The can_delete of this TemplateView.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this TemplateView.

        是否可以删除

        :param can_delete: The can_delete of this TemplateView.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def need_hub(self):
        """Gets the need_hub of this TemplateView.

        是否需要代码仓库

        :return: The need_hub of this TemplateView.
        :rtype: bool
        """
        return self._need_hub

    @need_hub.setter
    def need_hub(self, need_hub):
        """Sets the need_hub of this TemplateView.

        是否需要代码仓库

        :param need_hub: The need_hub of this TemplateView.
        :type need_hub: bool
        """
        self._need_hub = need_hub

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
        if not isinstance(other, TemplateView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
