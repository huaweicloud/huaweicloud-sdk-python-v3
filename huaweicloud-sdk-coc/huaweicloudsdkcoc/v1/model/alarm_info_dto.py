# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'importance': 'str',
        'come_from': 'str',
        'come_from_en': 'str',
        'transfer_rule': 'str',
        'transfer_rule_name': 'str',
        'app': 'str',
        'status': 'str',
        'owner': 'str',
        'owner_name': 'str',
        'owner_alias': 'str',
        'converge_count': 'int',
        'associate_event_id': 'str',
        'domain_id': 'str',
        'creator': 'str',
        'creator_name': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'remarks': 'str',
        'region': 'str',
        'task_type': 'str',
        'associated_task_type': 'str',
        'associated_task_id': 'str',
        'associated_task_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'importance': 'importance',
        'come_from': 'come_from',
        'come_from_en': 'come_from_en',
        'transfer_rule': 'transfer_rule',
        'transfer_rule_name': 'transfer_rule_name',
        'app': 'app',
        'status': 'status',
        'owner': 'owner',
        'owner_name': 'owner_name',
        'owner_alias': 'owner_alias',
        'converge_count': 'converge_count',
        'associate_event_id': 'associate_event_id',
        'domain_id': 'domain_id',
        'creator': 'creator',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'remarks': 'remarks',
        'region': 'region',
        'task_type': 'task_type',
        'associated_task_type': 'associated_task_type',
        'associated_task_id': 'associated_task_id',
        'associated_task_name': 'associated_task_name'
    }

    def __init__(self, id=None, name=None, importance=None, come_from=None, come_from_en=None, transfer_rule=None, transfer_rule_name=None, app=None, status=None, owner=None, owner_name=None, owner_alias=None, converge_count=None, associate_event_id=None, domain_id=None, creator=None, creator_name=None, create_time=None, update_time=None, remarks=None, region=None, task_type=None, associated_task_type=None, associated_task_id=None, associated_task_name=None):
        r"""AlarmInfoDTO

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID
        :type id: str
        :param name: 名称
        :type name: str
        :param importance: 严重类型，urgent（紧急）、major（重要）、minor（次要）、warn（提示）
        :type importance: str
        :param come_from: 数据源
        :type come_from: str
        :param come_from_en: 数据源英文名
        :type come_from_en: str
        :param transfer_rule: 流转规则id
        :type transfer_rule: str
        :param transfer_rule_name: 流转规则名
        :type transfer_rule_name: str
        :param app: 应用
        :type app: str
        :param status: 状态，告警中alarming，已解决resolved
        :type status: str
        :param owner: 责任人id
        :type owner: str
        :param owner_name: 责任人姓名
        :type owner_name: str
        :param owner_alias: 责任人别名
        :type owner_alias: str
        :param converge_count: 收敛量
        :type converge_count: int
        :param associate_event_id: 关联事件id
        :type associate_event_id: str
        :param domain_id: 租户账号
        :type domain_id: str
        :param creator: 创建人id
        :type creator: str
        :param creator_name: 创建人姓名
        :type creator_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param remarks: 备注
        :type remarks: str
        :param region: 区域regionId
        :type region: str
        :param task_type: 任务类型 ：SCRIPT脚本，RUNBOOK作业
        :type task_type: str
        :param associated_task_type: 任务类型分类 CUSTOMIZATION自定义，COMMUNAL公共
        :type associated_task_type: str
        :param associated_task_id: 脚本或作业id
        :type associated_task_id: str
        :param associated_task_name: 脚本或作业名称
        :type associated_task_name: str
        """
        
        

        self._id = None
        self._name = None
        self._importance = None
        self._come_from = None
        self._come_from_en = None
        self._transfer_rule = None
        self._transfer_rule_name = None
        self._app = None
        self._status = None
        self._owner = None
        self._owner_name = None
        self._owner_alias = None
        self._converge_count = None
        self._associate_event_id = None
        self._domain_id = None
        self._creator = None
        self._creator_name = None
        self._create_time = None
        self._update_time = None
        self._remarks = None
        self._region = None
        self._task_type = None
        self._associated_task_type = None
        self._associated_task_id = None
        self._associated_task_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if importance is not None:
            self.importance = importance
        if come_from is not None:
            self.come_from = come_from
        if come_from_en is not None:
            self.come_from_en = come_from_en
        if transfer_rule is not None:
            self.transfer_rule = transfer_rule
        if transfer_rule_name is not None:
            self.transfer_rule_name = transfer_rule_name
        if app is not None:
            self.app = app
        if status is not None:
            self.status = status
        if owner is not None:
            self.owner = owner
        if owner_name is not None:
            self.owner_name = owner_name
        if owner_alias is not None:
            self.owner_alias = owner_alias
        if converge_count is not None:
            self.converge_count = converge_count
        if associate_event_id is not None:
            self.associate_event_id = associate_event_id
        if domain_id is not None:
            self.domain_id = domain_id
        if creator is not None:
            self.creator = creator
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if remarks is not None:
            self.remarks = remarks
        if region is not None:
            self.region = region
        if task_type is not None:
            self.task_type = task_type
        if associated_task_type is not None:
            self.associated_task_type = associated_task_type
        if associated_task_id is not None:
            self.associated_task_id = associated_task_id
        if associated_task_name is not None:
            self.associated_task_name = associated_task_name

    @property
    def id(self):
        r"""Gets the id of this AlarmInfoDTO.

        唯一标识ID

        :return: The id of this AlarmInfoDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlarmInfoDTO.

        唯一标识ID

        :param id: The id of this AlarmInfoDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AlarmInfoDTO.

        名称

        :return: The name of this AlarmInfoDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmInfoDTO.

        名称

        :param name: The name of this AlarmInfoDTO.
        :type name: str
        """
        self._name = name

    @property
    def importance(self):
        r"""Gets the importance of this AlarmInfoDTO.

        严重类型，urgent（紧急）、major（重要）、minor（次要）、warn（提示）

        :return: The importance of this AlarmInfoDTO.
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        r"""Sets the importance of this AlarmInfoDTO.

        严重类型，urgent（紧急）、major（重要）、minor（次要）、warn（提示）

        :param importance: The importance of this AlarmInfoDTO.
        :type importance: str
        """
        self._importance = importance

    @property
    def come_from(self):
        r"""Gets the come_from of this AlarmInfoDTO.

        数据源

        :return: The come_from of this AlarmInfoDTO.
        :rtype: str
        """
        return self._come_from

    @come_from.setter
    def come_from(self, come_from):
        r"""Sets the come_from of this AlarmInfoDTO.

        数据源

        :param come_from: The come_from of this AlarmInfoDTO.
        :type come_from: str
        """
        self._come_from = come_from

    @property
    def come_from_en(self):
        r"""Gets the come_from_en of this AlarmInfoDTO.

        数据源英文名

        :return: The come_from_en of this AlarmInfoDTO.
        :rtype: str
        """
        return self._come_from_en

    @come_from_en.setter
    def come_from_en(self, come_from_en):
        r"""Sets the come_from_en of this AlarmInfoDTO.

        数据源英文名

        :param come_from_en: The come_from_en of this AlarmInfoDTO.
        :type come_from_en: str
        """
        self._come_from_en = come_from_en

    @property
    def transfer_rule(self):
        r"""Gets the transfer_rule of this AlarmInfoDTO.

        流转规则id

        :return: The transfer_rule of this AlarmInfoDTO.
        :rtype: str
        """
        return self._transfer_rule

    @transfer_rule.setter
    def transfer_rule(self, transfer_rule):
        r"""Sets the transfer_rule of this AlarmInfoDTO.

        流转规则id

        :param transfer_rule: The transfer_rule of this AlarmInfoDTO.
        :type transfer_rule: str
        """
        self._transfer_rule = transfer_rule

    @property
    def transfer_rule_name(self):
        r"""Gets the transfer_rule_name of this AlarmInfoDTO.

        流转规则名

        :return: The transfer_rule_name of this AlarmInfoDTO.
        :rtype: str
        """
        return self._transfer_rule_name

    @transfer_rule_name.setter
    def transfer_rule_name(self, transfer_rule_name):
        r"""Sets the transfer_rule_name of this AlarmInfoDTO.

        流转规则名

        :param transfer_rule_name: The transfer_rule_name of this AlarmInfoDTO.
        :type transfer_rule_name: str
        """
        self._transfer_rule_name = transfer_rule_name

    @property
    def app(self):
        r"""Gets the app of this AlarmInfoDTO.

        应用

        :return: The app of this AlarmInfoDTO.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this AlarmInfoDTO.

        应用

        :param app: The app of this AlarmInfoDTO.
        :type app: str
        """
        self._app = app

    @property
    def status(self):
        r"""Gets the status of this AlarmInfoDTO.

        状态，告警中alarming，已解决resolved

        :return: The status of this AlarmInfoDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmInfoDTO.

        状态，告警中alarming，已解决resolved

        :param status: The status of this AlarmInfoDTO.
        :type status: str
        """
        self._status = status

    @property
    def owner(self):
        r"""Gets the owner of this AlarmInfoDTO.

        责任人id

        :return: The owner of this AlarmInfoDTO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this AlarmInfoDTO.

        责任人id

        :param owner: The owner of this AlarmInfoDTO.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_name(self):
        r"""Gets the owner_name of this AlarmInfoDTO.

        责任人姓名

        :return: The owner_name of this AlarmInfoDTO.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this AlarmInfoDTO.

        责任人姓名

        :param owner_name: The owner_name of this AlarmInfoDTO.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def owner_alias(self):
        r"""Gets the owner_alias of this AlarmInfoDTO.

        责任人别名

        :return: The owner_alias of this AlarmInfoDTO.
        :rtype: str
        """
        return self._owner_alias

    @owner_alias.setter
    def owner_alias(self, owner_alias):
        r"""Sets the owner_alias of this AlarmInfoDTO.

        责任人别名

        :param owner_alias: The owner_alias of this AlarmInfoDTO.
        :type owner_alias: str
        """
        self._owner_alias = owner_alias

    @property
    def converge_count(self):
        r"""Gets the converge_count of this AlarmInfoDTO.

        收敛量

        :return: The converge_count of this AlarmInfoDTO.
        :rtype: int
        """
        return self._converge_count

    @converge_count.setter
    def converge_count(self, converge_count):
        r"""Sets the converge_count of this AlarmInfoDTO.

        收敛量

        :param converge_count: The converge_count of this AlarmInfoDTO.
        :type converge_count: int
        """
        self._converge_count = converge_count

    @property
    def associate_event_id(self):
        r"""Gets the associate_event_id of this AlarmInfoDTO.

        关联事件id

        :return: The associate_event_id of this AlarmInfoDTO.
        :rtype: str
        """
        return self._associate_event_id

    @associate_event_id.setter
    def associate_event_id(self, associate_event_id):
        r"""Sets the associate_event_id of this AlarmInfoDTO.

        关联事件id

        :param associate_event_id: The associate_event_id of this AlarmInfoDTO.
        :type associate_event_id: str
        """
        self._associate_event_id = associate_event_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AlarmInfoDTO.

        租户账号

        :return: The domain_id of this AlarmInfoDTO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AlarmInfoDTO.

        租户账号

        :param domain_id: The domain_id of this AlarmInfoDTO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def creator(self):
        r"""Gets the creator of this AlarmInfoDTO.

        创建人id

        :return: The creator of this AlarmInfoDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this AlarmInfoDTO.

        创建人id

        :param creator: The creator of this AlarmInfoDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_name(self):
        r"""Gets the creator_name of this AlarmInfoDTO.

        创建人姓名

        :return: The creator_name of this AlarmInfoDTO.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this AlarmInfoDTO.

        创建人姓名

        :param creator_name: The creator_name of this AlarmInfoDTO.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this AlarmInfoDTO.

        创建时间

        :return: The create_time of this AlarmInfoDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlarmInfoDTO.

        创建时间

        :param create_time: The create_time of this AlarmInfoDTO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AlarmInfoDTO.

        更新时间

        :return: The update_time of this AlarmInfoDTO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlarmInfoDTO.

        更新时间

        :param update_time: The update_time of this AlarmInfoDTO.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def remarks(self):
        r"""Gets the remarks of this AlarmInfoDTO.

        备注

        :return: The remarks of this AlarmInfoDTO.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this AlarmInfoDTO.

        备注

        :param remarks: The remarks of this AlarmInfoDTO.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def region(self):
        r"""Gets the region of this AlarmInfoDTO.

        区域regionId

        :return: The region of this AlarmInfoDTO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AlarmInfoDTO.

        区域regionId

        :param region: The region of this AlarmInfoDTO.
        :type region: str
        """
        self._region = region

    @property
    def task_type(self):
        r"""Gets the task_type of this AlarmInfoDTO.

        任务类型 ：SCRIPT脚本，RUNBOOK作业

        :return: The task_type of this AlarmInfoDTO.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this AlarmInfoDTO.

        任务类型 ：SCRIPT脚本，RUNBOOK作业

        :param task_type: The task_type of this AlarmInfoDTO.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this AlarmInfoDTO.

        任务类型分类 CUSTOMIZATION自定义，COMMUNAL公共

        :return: The associated_task_type of this AlarmInfoDTO.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this AlarmInfoDTO.

        任务类型分类 CUSTOMIZATION自定义，COMMUNAL公共

        :param associated_task_type: The associated_task_type of this AlarmInfoDTO.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def associated_task_id(self):
        r"""Gets the associated_task_id of this AlarmInfoDTO.

        脚本或作业id

        :return: The associated_task_id of this AlarmInfoDTO.
        :rtype: str
        """
        return self._associated_task_id

    @associated_task_id.setter
    def associated_task_id(self, associated_task_id):
        r"""Sets the associated_task_id of this AlarmInfoDTO.

        脚本或作业id

        :param associated_task_id: The associated_task_id of this AlarmInfoDTO.
        :type associated_task_id: str
        """
        self._associated_task_id = associated_task_id

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this AlarmInfoDTO.

        脚本或作业名称

        :return: The associated_task_name of this AlarmInfoDTO.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this AlarmInfoDTO.

        脚本或作业名称

        :param associated_task_name: The associated_task_name of this AlarmInfoDTO.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

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
        if not isinstance(other, AlarmInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
