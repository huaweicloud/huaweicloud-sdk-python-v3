# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsSqlJobVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_status': 'str',
        'create_time': 'datetime',
        'creator_id': 'str',
        'creator_name': 'str',
        'deleted': 'bool',
        'description': 'str',
        'domain_id': 'str',
        'id': 'str',
        'job_type': 'str',
        'league_id': 'str',
        'name': 'str',
        'update_time': 'datetime',
        'update_user_id': 'str',
        'update_user_name': 'str'
    }

    attribute_map = {
        'approval_status': 'approval_status',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'deleted': 'deleted',
        'description': 'description',
        'domain_id': 'domain_id',
        'id': 'id',
        'job_type': 'job_type',
        'league_id': 'league_id',
        'name': 'name',
        'update_time': 'update_time',
        'update_user_id': 'update_user_id',
        'update_user_name': 'update_user_name'
    }

    def __init__(self, approval_status=None, create_time=None, creator_id=None, creator_name=None, deleted=None, description=None, domain_id=None, id=None, job_type=None, league_id=None, name=None, update_time=None, update_user_id=None, update_user_name=None):
        """TicsSqlJobVo

        The model defined in huaweicloud sdk

        :param approval_status: 作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销
        :type approval_status: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param creator_id: 创建人id
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param deleted: 删除标记
        :type deleted: bool
        :param description: 作业描述
        :type description: str
        :param domain_id: 作业发起方domainId
        :type domain_id: str
        :param id: 作业id
        :type id: str
        :param job_type: 作业类型，SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换
        :type job_type: str
        :param league_id: 联盟id
        :type league_id: str
        :param name: 作业名称
        :type name: str
        :param update_time: 变更时间
        :type update_time: datetime
        :param update_user_id: 变更人id
        :type update_user_id: str
        :param update_user_name: 变更人名称
        :type update_user_name: str
        """
        
        

        self._approval_status = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._deleted = None
        self._description = None
        self._domain_id = None
        self._id = None
        self._job_type = None
        self._league_id = None
        self._name = None
        self._update_time = None
        self._update_user_id = None
        self._update_user_name = None
        self.discriminator = None

        if approval_status is not None:
            self.approval_status = approval_status
        self.create_time = create_time
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.deleted = deleted
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        self.id = id
        self.job_type = job_type
        self.league_id = league_id
        self.name = name
        if update_time is not None:
            self.update_time = update_time
        if update_user_id is not None:
            self.update_user_id = update_user_id
        if update_user_name is not None:
            self.update_user_name = update_user_name

    @property
    def approval_status(self):
        """Gets the approval_status of this TicsSqlJobVo.

        作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销

        :return: The approval_status of this TicsSqlJobVo.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this TicsSqlJobVo.

        作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销

        :param approval_status: The approval_status of this TicsSqlJobVo.
        :type approval_status: str
        """
        self._approval_status = approval_status

    @property
    def create_time(self):
        """Gets the create_time of this TicsSqlJobVo.

        创建时间

        :return: The create_time of this TicsSqlJobVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsSqlJobVo.

        创建时间

        :param create_time: The create_time of this TicsSqlJobVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        """Gets the creator_id of this TicsSqlJobVo.

        创建人id

        :return: The creator_id of this TicsSqlJobVo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TicsSqlJobVo.

        创建人id

        :param creator_id: The creator_id of this TicsSqlJobVo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this TicsSqlJobVo.

        创建人名称

        :return: The creator_name of this TicsSqlJobVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TicsSqlJobVo.

        创建人名称

        :param creator_name: The creator_name of this TicsSqlJobVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def deleted(self):
        """Gets the deleted of this TicsSqlJobVo.

        删除标记

        :return: The deleted of this TicsSqlJobVo.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TicsSqlJobVo.

        删除标记

        :param deleted: The deleted of this TicsSqlJobVo.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this TicsSqlJobVo.

        作业描述

        :return: The description of this TicsSqlJobVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TicsSqlJobVo.

        作业描述

        :param description: The description of this TicsSqlJobVo.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this TicsSqlJobVo.

        作业发起方domainId

        :return: The domain_id of this TicsSqlJobVo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this TicsSqlJobVo.

        作业发起方domainId

        :param domain_id: The domain_id of this TicsSqlJobVo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this TicsSqlJobVo.

        作业id

        :return: The id of this TicsSqlJobVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsSqlJobVo.

        作业id

        :param id: The id of this TicsSqlJobVo.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        """Gets the job_type of this TicsSqlJobVo.

        作业类型，SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换

        :return: The job_type of this TicsSqlJobVo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this TicsSqlJobVo.

        作业类型，SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换

        :param job_type: The job_type of this TicsSqlJobVo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def league_id(self):
        """Gets the league_id of this TicsSqlJobVo.

        联盟id

        :return: The league_id of this TicsSqlJobVo.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this TicsSqlJobVo.

        联盟id

        :param league_id: The league_id of this TicsSqlJobVo.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def name(self):
        """Gets the name of this TicsSqlJobVo.

        作业名称

        :return: The name of this TicsSqlJobVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TicsSqlJobVo.

        作业名称

        :param name: The name of this TicsSqlJobVo.
        :type name: str
        """
        self._name = name

    @property
    def update_time(self):
        """Gets the update_time of this TicsSqlJobVo.

        变更时间

        :return: The update_time of this TicsSqlJobVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TicsSqlJobVo.

        变更时间

        :param update_time: The update_time of this TicsSqlJobVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_user_id(self):
        """Gets the update_user_id of this TicsSqlJobVo.

        变更人id

        :return: The update_user_id of this TicsSqlJobVo.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        """Sets the update_user_id of this TicsSqlJobVo.

        变更人id

        :param update_user_id: The update_user_id of this TicsSqlJobVo.
        :type update_user_id: str
        """
        self._update_user_id = update_user_id

    @property
    def update_user_name(self):
        """Gets the update_user_name of this TicsSqlJobVo.

        变更人名称

        :return: The update_user_name of this TicsSqlJobVo.
        :rtype: str
        """
        return self._update_user_name

    @update_user_name.setter
    def update_user_name(self, update_user_name):
        """Sets the update_user_name of this TicsSqlJobVo.

        变更人名称

        :param update_user_name: The update_user_name of this TicsSqlJobVo.
        :type update_user_name: str
        """
        self._update_user_name = update_user_name

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
        if not isinstance(other, TicsSqlJobVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
