# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IteratorVersionInfo:

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
        'number': 'str',
        'owner': 'str',
        'version': 'str',
        'description': 'str',
        'iterations': 'list[str]',
        'is_master': 'str',
        'pbi_id': 'str',
        'pbi_name': 'str',
        'plan_start_date': 'str',
        'plan_start_timestamp': 'int',
        'plan_end_date': 'str',
        'plan_end_timestamp': 'int',
        'asyn_git': 'str',
        'project_uuid': 'str',
        'project_name': 'str',
        'current_stage': 'str',
        'service_types': 'list[str]',
        'issue_list': 'list[WorkItemInfo]',
        'risk_rating': 'int',
        'risk_des': 'str',
        'is_update_risk': 'str',
        'pi_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'owner': 'owner',
        'version': 'version',
        'description': 'description',
        'iterations': 'iterations',
        'is_master': 'is_master',
        'pbi_id': 'pbi_id',
        'pbi_name': 'pbi_name',
        'plan_start_date': 'plan_start_date',
        'plan_start_timestamp': 'plan_start_timestamp',
        'plan_end_date': 'plan_end_date',
        'plan_end_timestamp': 'plan_end_timestamp',
        'asyn_git': 'asyn_git',
        'project_uuid': 'project_uuid',
        'project_name': 'project_name',
        'current_stage': 'current_stage',
        'service_types': 'service_types',
        'issue_list': 'issue_list',
        'risk_rating': 'risk_rating',
        'risk_des': 'risk_des',
        'is_update_risk': 'is_update_risk',
        'pi_id': 'pi_id'
    }

    def __init__(self, name=None, number=None, owner=None, version=None, description=None, iterations=None, is_master=None, pbi_id=None, pbi_name=None, plan_start_date=None, plan_start_timestamp=None, plan_end_date=None, plan_end_timestamp=None, asyn_git=None, project_uuid=None, project_name=None, current_stage=None, service_types=None, issue_list=None, risk_rating=None, risk_des=None, is_update_risk=None, pi_id=None):
        """IteratorVersionInfo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param number: 开发分支名称
        :type number: str
        :param owner: 处理者ID
        :type owner: str
        :param version: 待测版本
        :type version: str
        :param description: 描述
        :type description: str
        :param iterations: 关联迭代
        :type iterations: list[str]
        :param is_master: 是否为Master分支
        :type is_master: str
        :param pbi_id: PBI ID
        :type pbi_id: str
        :param pbi_name: PBI信息
        :type pbi_name: str
        :param plan_start_date: 开始时间
        :type plan_start_date: str
        :param plan_start_timestamp: 开始时间戳
        :type plan_start_timestamp: int
        :param plan_end_date: 结束时间
        :type plan_end_date: str
        :param plan_end_timestamp: 结束时间戳
        :type plan_end_timestamp: int
        :param asyn_git: 是否同步git库
        :type asyn_git: str
        :param project_uuid: 项目ID（云龙场景，传入微服务ID）
        :type project_uuid: str
        :param project_name: 项目名称（云龙场景，传入微服务名）
        :type project_name: str
        :param current_stage: 当前所处阶段
        :type current_stage: str
        :param service_types: 测试类型
        :type service_types: list[str]
        :param issue_list: 关联需求
        :type issue_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        :param risk_rating: 风险等级
        :type risk_rating: int
        :param risk_des: 风险描述
        :type risk_des: str
        :param is_update_risk: 编辑风险信息标记
        :type is_update_risk: str
        :param pi_id: pi的id，层级关系：pi -&gt; 迭代 -&gt; 需求
        :type pi_id: str
        """
        
        

        self._name = None
        self._number = None
        self._owner = None
        self._version = None
        self._description = None
        self._iterations = None
        self._is_master = None
        self._pbi_id = None
        self._pbi_name = None
        self._plan_start_date = None
        self._plan_start_timestamp = None
        self._plan_end_date = None
        self._plan_end_timestamp = None
        self._asyn_git = None
        self._project_uuid = None
        self._project_name = None
        self._current_stage = None
        self._service_types = None
        self._issue_list = None
        self._risk_rating = None
        self._risk_des = None
        self._is_update_risk = None
        self._pi_id = None
        self.discriminator = None

        self.name = name
        if number is not None:
            self.number = number
        if owner is not None:
            self.owner = owner
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if iterations is not None:
            self.iterations = iterations
        if is_master is not None:
            self.is_master = is_master
        if pbi_id is not None:
            self.pbi_id = pbi_id
        if pbi_name is not None:
            self.pbi_name = pbi_name
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_start_timestamp is not None:
            self.plan_start_timestamp = plan_start_timestamp
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if plan_end_timestamp is not None:
            self.plan_end_timestamp = plan_end_timestamp
        if asyn_git is not None:
            self.asyn_git = asyn_git
        self.project_uuid = project_uuid
        if project_name is not None:
            self.project_name = project_name
        if current_stage is not None:
            self.current_stage = current_stage
        if service_types is not None:
            self.service_types = service_types
        if issue_list is not None:
            self.issue_list = issue_list
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if risk_des is not None:
            self.risk_des = risk_des
        if is_update_risk is not None:
            self.is_update_risk = is_update_risk
        if pi_id is not None:
            self.pi_id = pi_id

    @property
    def name(self):
        """Gets the name of this IteratorVersionInfo.

        名称

        :return: The name of this IteratorVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IteratorVersionInfo.

        名称

        :param name: The name of this IteratorVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        """Gets the number of this IteratorVersionInfo.

        开发分支名称

        :return: The number of this IteratorVersionInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this IteratorVersionInfo.

        开发分支名称

        :param number: The number of this IteratorVersionInfo.
        :type number: str
        """
        self._number = number

    @property
    def owner(self):
        """Gets the owner of this IteratorVersionInfo.

        处理者ID

        :return: The owner of this IteratorVersionInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IteratorVersionInfo.

        处理者ID

        :param owner: The owner of this IteratorVersionInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def version(self):
        """Gets the version of this IteratorVersionInfo.

        待测版本

        :return: The version of this IteratorVersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IteratorVersionInfo.

        待测版本

        :param version: The version of this IteratorVersionInfo.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this IteratorVersionInfo.

        描述

        :return: The description of this IteratorVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IteratorVersionInfo.

        描述

        :param description: The description of this IteratorVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def iterations(self):
        """Gets the iterations of this IteratorVersionInfo.

        关联迭代

        :return: The iterations of this IteratorVersionInfo.
        :rtype: list[str]
        """
        return self._iterations

    @iterations.setter
    def iterations(self, iterations):
        """Sets the iterations of this IteratorVersionInfo.

        关联迭代

        :param iterations: The iterations of this IteratorVersionInfo.
        :type iterations: list[str]
        """
        self._iterations = iterations

    @property
    def is_master(self):
        """Gets the is_master of this IteratorVersionInfo.

        是否为Master分支

        :return: The is_master of this IteratorVersionInfo.
        :rtype: str
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """Sets the is_master of this IteratorVersionInfo.

        是否为Master分支

        :param is_master: The is_master of this IteratorVersionInfo.
        :type is_master: str
        """
        self._is_master = is_master

    @property
    def pbi_id(self):
        """Gets the pbi_id of this IteratorVersionInfo.

        PBI ID

        :return: The pbi_id of this IteratorVersionInfo.
        :rtype: str
        """
        return self._pbi_id

    @pbi_id.setter
    def pbi_id(self, pbi_id):
        """Sets the pbi_id of this IteratorVersionInfo.

        PBI ID

        :param pbi_id: The pbi_id of this IteratorVersionInfo.
        :type pbi_id: str
        """
        self._pbi_id = pbi_id

    @property
    def pbi_name(self):
        """Gets the pbi_name of this IteratorVersionInfo.

        PBI信息

        :return: The pbi_name of this IteratorVersionInfo.
        :rtype: str
        """
        return self._pbi_name

    @pbi_name.setter
    def pbi_name(self, pbi_name):
        """Sets the pbi_name of this IteratorVersionInfo.

        PBI信息

        :param pbi_name: The pbi_name of this IteratorVersionInfo.
        :type pbi_name: str
        """
        self._pbi_name = pbi_name

    @property
    def plan_start_date(self):
        """Gets the plan_start_date of this IteratorVersionInfo.

        开始时间

        :return: The plan_start_date of this IteratorVersionInfo.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        """Sets the plan_start_date of this IteratorVersionInfo.

        开始时间

        :param plan_start_date: The plan_start_date of this IteratorVersionInfo.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_start_timestamp(self):
        """Gets the plan_start_timestamp of this IteratorVersionInfo.

        开始时间戳

        :return: The plan_start_timestamp of this IteratorVersionInfo.
        :rtype: int
        """
        return self._plan_start_timestamp

    @plan_start_timestamp.setter
    def plan_start_timestamp(self, plan_start_timestamp):
        """Sets the plan_start_timestamp of this IteratorVersionInfo.

        开始时间戳

        :param plan_start_timestamp: The plan_start_timestamp of this IteratorVersionInfo.
        :type plan_start_timestamp: int
        """
        self._plan_start_timestamp = plan_start_timestamp

    @property
    def plan_end_date(self):
        """Gets the plan_end_date of this IteratorVersionInfo.

        结束时间

        :return: The plan_end_date of this IteratorVersionInfo.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        """Sets the plan_end_date of this IteratorVersionInfo.

        结束时间

        :param plan_end_date: The plan_end_date of this IteratorVersionInfo.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def plan_end_timestamp(self):
        """Gets the plan_end_timestamp of this IteratorVersionInfo.

        结束时间戳

        :return: The plan_end_timestamp of this IteratorVersionInfo.
        :rtype: int
        """
        return self._plan_end_timestamp

    @plan_end_timestamp.setter
    def plan_end_timestamp(self, plan_end_timestamp):
        """Sets the plan_end_timestamp of this IteratorVersionInfo.

        结束时间戳

        :param plan_end_timestamp: The plan_end_timestamp of this IteratorVersionInfo.
        :type plan_end_timestamp: int
        """
        self._plan_end_timestamp = plan_end_timestamp

    @property
    def asyn_git(self):
        """Gets the asyn_git of this IteratorVersionInfo.

        是否同步git库

        :return: The asyn_git of this IteratorVersionInfo.
        :rtype: str
        """
        return self._asyn_git

    @asyn_git.setter
    def asyn_git(self, asyn_git):
        """Sets the asyn_git of this IteratorVersionInfo.

        是否同步git库

        :param asyn_git: The asyn_git of this IteratorVersionInfo.
        :type asyn_git: str
        """
        self._asyn_git = asyn_git

    @property
    def project_uuid(self):
        """Gets the project_uuid of this IteratorVersionInfo.

        项目ID（云龙场景，传入微服务ID）

        :return: The project_uuid of this IteratorVersionInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this IteratorVersionInfo.

        项目ID（云龙场景，传入微服务ID）

        :param project_uuid: The project_uuid of this IteratorVersionInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def project_name(self):
        """Gets the project_name of this IteratorVersionInfo.

        项目名称（云龙场景，传入微服务名）

        :return: The project_name of this IteratorVersionInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this IteratorVersionInfo.

        项目名称（云龙场景，传入微服务名）

        :param project_name: The project_name of this IteratorVersionInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def current_stage(self):
        """Gets the current_stage of this IteratorVersionInfo.

        当前所处阶段

        :return: The current_stage of this IteratorVersionInfo.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this IteratorVersionInfo.

        当前所处阶段

        :param current_stage: The current_stage of this IteratorVersionInfo.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def service_types(self):
        """Gets the service_types of this IteratorVersionInfo.

        测试类型

        :return: The service_types of this IteratorVersionInfo.
        :rtype: list[str]
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        """Sets the service_types of this IteratorVersionInfo.

        测试类型

        :param service_types: The service_types of this IteratorVersionInfo.
        :type service_types: list[str]
        """
        self._service_types = service_types

    @property
    def issue_list(self):
        """Gets the issue_list of this IteratorVersionInfo.

        关联需求

        :return: The issue_list of this IteratorVersionInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        return self._issue_list

    @issue_list.setter
    def issue_list(self, issue_list):
        """Sets the issue_list of this IteratorVersionInfo.

        关联需求

        :param issue_list: The issue_list of this IteratorVersionInfo.
        :type issue_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        self._issue_list = issue_list

    @property
    def risk_rating(self):
        """Gets the risk_rating of this IteratorVersionInfo.

        风险等级

        :return: The risk_rating of this IteratorVersionInfo.
        :rtype: int
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this IteratorVersionInfo.

        风险等级

        :param risk_rating: The risk_rating of this IteratorVersionInfo.
        :type risk_rating: int
        """
        self._risk_rating = risk_rating

    @property
    def risk_des(self):
        """Gets the risk_des of this IteratorVersionInfo.

        风险描述

        :return: The risk_des of this IteratorVersionInfo.
        :rtype: str
        """
        return self._risk_des

    @risk_des.setter
    def risk_des(self, risk_des):
        """Sets the risk_des of this IteratorVersionInfo.

        风险描述

        :param risk_des: The risk_des of this IteratorVersionInfo.
        :type risk_des: str
        """
        self._risk_des = risk_des

    @property
    def is_update_risk(self):
        """Gets the is_update_risk of this IteratorVersionInfo.

        编辑风险信息标记

        :return: The is_update_risk of this IteratorVersionInfo.
        :rtype: str
        """
        return self._is_update_risk

    @is_update_risk.setter
    def is_update_risk(self, is_update_risk):
        """Sets the is_update_risk of this IteratorVersionInfo.

        编辑风险信息标记

        :param is_update_risk: The is_update_risk of this IteratorVersionInfo.
        :type is_update_risk: str
        """
        self._is_update_risk = is_update_risk

    @property
    def pi_id(self):
        """Gets the pi_id of this IteratorVersionInfo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :return: The pi_id of this IteratorVersionInfo.
        :rtype: str
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id):
        """Sets the pi_id of this IteratorVersionInfo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :param pi_id: The pi_id of this IteratorVersionInfo.
        :type pi_id: str
        """
        self._pi_id = pi_id

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
        if not isinstance(other, IteratorVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
