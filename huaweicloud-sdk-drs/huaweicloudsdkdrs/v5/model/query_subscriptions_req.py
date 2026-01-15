# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySubscriptionsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'name': 'str',
        'status': 'str',
        'enterprise_project_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'instance_ids': 'list[str]',
        'instance_ip': 'str',
        'tags': 'dict(str, str)',
        'service_name': 'str',
        'description': 'str',
        'is_billing': 'bool',
        'begin_at': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'name': 'name',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'instance_ids': 'instance_ids',
        'instance_ip': 'instance_ip',
        'tags': 'tags',
        'service_name': 'service_name',
        'description': 'description',
        'is_billing': 'is_billing',
        'begin_at': 'begin_at'
    }

    def __init__(self, job_type=None, engine_type=None, net_type=None, name=None, status=None, enterprise_project_id=None, sort_key=None, sort_dir=None, instance_ids=None, instance_ip=None, tags=None, service_name=None, description=None, is_billing=None, begin_at=None):
        r"""QuerySubscriptionsReq

        The model defined in huaweicloud sdk

        :param job_type: 任务场景
        :type job_type: str
        :param engine_type: 引擎类型。
        :type engine_type: str
        :param net_type: 网络类型。
        :type net_type: str
        :param name: 任务ID或名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param enterprise_project_id: 企业项目ID。 缺省值：\&quot;\&quot;，表示查询所有企业项目任务。
        :type enterprise_project_id: str
        :param sort_key: 返回结果按该关键字排序，默认为“create_time”。
        :type sort_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为“desc”）。
        :type sort_dir: str
        :param instance_ids: 数据库实例ID列表，最多支持10个。
        :type instance_ids: list[str]
        :param instance_ip: 数据库实例IP
        :type instance_ip: str
        :param tags: 标签
        :type tags: dict(str, str)
        :param service_name: 服务名称
        :type service_name: str
        :param description: 描述
        :type description: str
        :param is_billing: 计费模式，包括是、否以及全部三种情况，不填默认为全部
        :type is_billing: bool
        :param begin_at: 消费时间
        :type begin_at: str
        """
        
        

        self._job_type = None
        self._engine_type = None
        self._net_type = None
        self._name = None
        self._status = None
        self._enterprise_project_id = None
        self._sort_key = None
        self._sort_dir = None
        self._instance_ids = None
        self._instance_ip = None
        self._tags = None
        self._service_name = None
        self._description = None
        self._is_billing = None
        self._begin_at = None
        self.discriminator = None

        self.job_type = job_type
        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if instance_ip is not None:
            self.instance_ip = instance_ip
        if tags is not None:
            self.tags = tags
        if service_name is not None:
            self.service_name = service_name
        if description is not None:
            self.description = description
        if is_billing is not None:
            self.is_billing = is_billing
        if begin_at is not None:
            self.begin_at = begin_at

    @property
    def job_type(self):
        r"""Gets the job_type of this QuerySubscriptionsReq.

        任务场景

        :return: The job_type of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this QuerySubscriptionsReq.

        任务场景

        :param job_type: The job_type of this QuerySubscriptionsReq.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this QuerySubscriptionsReq.

        引擎类型。

        :return: The engine_type of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this QuerySubscriptionsReq.

        引擎类型。

        :param engine_type: The engine_type of this QuerySubscriptionsReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        r"""Gets the net_type of this QuerySubscriptionsReq.

        网络类型。

        :return: The net_type of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this QuerySubscriptionsReq.

        网络类型。

        :param net_type: The net_type of this QuerySubscriptionsReq.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def name(self):
        r"""Gets the name of this QuerySubscriptionsReq.

        任务ID或名称。

        :return: The name of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QuerySubscriptionsReq.

        任务ID或名称。

        :param name: The name of this QuerySubscriptionsReq.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this QuerySubscriptionsReq.

        任务状态。

        :return: The status of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QuerySubscriptionsReq.

        任务状态。

        :param status: The status of this QuerySubscriptionsReq.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QuerySubscriptionsReq.

        企业项目ID。 缺省值：\"\"，表示查询所有企业项目任务。

        :return: The enterprise_project_id of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QuerySubscriptionsReq.

        企业项目ID。 缺省值：\"\"，表示查询所有企业项目任务。

        :param enterprise_project_id: The enterprise_project_id of this QuerySubscriptionsReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this QuerySubscriptionsReq.

        返回结果按该关键字排序，默认为“create_time”。

        :return: The sort_key of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this QuerySubscriptionsReq.

        返回结果按该关键字排序，默认为“create_time”。

        :param sort_key: The sort_key of this QuerySubscriptionsReq.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this QuerySubscriptionsReq.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :return: The sort_dir of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this QuerySubscriptionsReq.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :param sort_dir: The sort_dir of this QuerySubscriptionsReq.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this QuerySubscriptionsReq.

        数据库实例ID列表，最多支持10个。

        :return: The instance_ids of this QuerySubscriptionsReq.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this QuerySubscriptionsReq.

        数据库实例ID列表，最多支持10个。

        :param instance_ids: The instance_ids of this QuerySubscriptionsReq.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def instance_ip(self):
        r"""Gets the instance_ip of this QuerySubscriptionsReq.

        数据库实例IP

        :return: The instance_ip of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        r"""Sets the instance_ip of this QuerySubscriptionsReq.

        数据库实例IP

        :param instance_ip: The instance_ip of this QuerySubscriptionsReq.
        :type instance_ip: str
        """
        self._instance_ip = instance_ip

    @property
    def tags(self):
        r"""Gets the tags of this QuerySubscriptionsReq.

        标签

        :return: The tags of this QuerySubscriptionsReq.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QuerySubscriptionsReq.

        标签

        :param tags: The tags of this QuerySubscriptionsReq.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def service_name(self):
        r"""Gets the service_name of this QuerySubscriptionsReq.

        服务名称

        :return: The service_name of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this QuerySubscriptionsReq.

        服务名称

        :param service_name: The service_name of this QuerySubscriptionsReq.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def description(self):
        r"""Gets the description of this QuerySubscriptionsReq.

        描述

        :return: The description of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QuerySubscriptionsReq.

        描述

        :param description: The description of this QuerySubscriptionsReq.
        :type description: str
        """
        self._description = description

    @property
    def is_billing(self):
        r"""Gets the is_billing of this QuerySubscriptionsReq.

        计费模式，包括是、否以及全部三种情况，不填默认为全部

        :return: The is_billing of this QuerySubscriptionsReq.
        :rtype: bool
        """
        return self._is_billing

    @is_billing.setter
    def is_billing(self, is_billing):
        r"""Sets the is_billing of this QuerySubscriptionsReq.

        计费模式，包括是、否以及全部三种情况，不填默认为全部

        :param is_billing: The is_billing of this QuerySubscriptionsReq.
        :type is_billing: bool
        """
        self._is_billing = is_billing

    @property
    def begin_at(self):
        r"""Gets the begin_at of this QuerySubscriptionsReq.

        消费时间

        :return: The begin_at of this QuerySubscriptionsReq.
        :rtype: str
        """
        return self._begin_at

    @begin_at.setter
    def begin_at(self, begin_at):
        r"""Sets the begin_at of this QuerySubscriptionsReq.

        消费时间

        :param begin_at: The begin_at of this QuerySubscriptionsReq.
        :type begin_at: str
        """
        self._begin_at = begin_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuerySubscriptionsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
