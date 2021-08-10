# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryJobsReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cur_page': 'int',
        'per_page': 'int',
        'db_use_type': 'str',
        'engine_type': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'net_type': 'str',
        'service_name': 'str',
        'status': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'db_use_type': 'db_use_type',
        'engine_type': 'engine_type',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'net_type': 'net_type',
        'service_name': 'service_name',
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, cur_page=None, per_page=None, db_use_type=None, engine_type=None, enterprise_project_id=None, name=None, net_type=None, service_name=None, status=None, tags=None):
        """QueryJobsReq - a model defined in huaweicloud sdk"""
        
        

        self._cur_page = None
        self._per_page = None
        self._db_use_type = None
        self._engine_type = None
        self._enterprise_project_id = None
        self._name = None
        self._net_type = None
        self._service_name = None
        self._status = None
        self._tags = None
        self.discriminator = None

        self.cur_page = cur_page
        self.per_page = per_page
        self.db_use_type = db_use_type
        if engine_type is not None:
            self.engine_type = engine_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if net_type is not None:
            self.net_type = net_type
        if service_name is not None:
            self.service_name = service_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def cur_page(self):
        """Gets the cur_page of this QueryJobsReq.

        第几页

        :return: The cur_page of this QueryJobsReq.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        """Sets the cur_page of this QueryJobsReq.

        第几页

        :param cur_page: The cur_page of this QueryJobsReq.
        :type: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        """Gets the per_page of this QueryJobsReq.

        每页记录数

        :return: The per_page of this QueryJobsReq.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this QueryJobsReq.

        每页记录数

        :param per_page: The per_page of this QueryJobsReq.
        :type: int
        """
        self._per_page = per_page

    @property
    def db_use_type(self):
        """Gets the db_use_type of this QueryJobsReq.

        迁移场景，migration:实时迁移,sync:实时同步,cloudDataGuard:实时灾备

        :return: The db_use_type of this QueryJobsReq.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this QueryJobsReq.

        迁移场景，migration:实时迁移,sync:实时同步,cloudDataGuard:实时灾备

        :param db_use_type: The db_use_type of this QueryJobsReq.
        :type: str
        """
        self._db_use_type = db_use_type

    @property
    def engine_type(self):
        """Gets the engine_type of this QueryJobsReq.

        引擎类型,mysql：迁移，同步使用。mongodb：迁移使用。cloudDataGuard-mysql：灾备使用。

        :return: The engine_type of this QueryJobsReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this QueryJobsReq.

        引擎类型,mysql：迁移，同步使用。mongodb：迁移使用。cloudDataGuard-mysql：灾备使用。

        :param engine_type: The engine_type of this QueryJobsReq.
        :type: str
        """
        self._engine_type = engine_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this QueryJobsReq.

        企业项目

        :return: The enterprise_project_id of this QueryJobsReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this QueryJobsReq.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this QueryJobsReq.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this QueryJobsReq.

        name或id

        :return: The name of this QueryJobsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryJobsReq.

        name或id

        :param name: The name of this QueryJobsReq.
        :type: str
        """
        self._name = name

    @property
    def net_type(self):
        """Gets the net_type of this QueryJobsReq.

        网络类型

        :return: The net_type of this QueryJobsReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this QueryJobsReq.

        网络类型

        :param net_type: The net_type of this QueryJobsReq.
        :type: str
        """
        self._net_type = net_type

    @property
    def service_name(self):
        """Gets the service_name of this QueryJobsReq.

        开启EPS时使用，值为eps

        :return: The service_name of this QueryJobsReq.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this QueryJobsReq.

        开启EPS时使用，值为eps

        :param service_name: The service_name of this QueryJobsReq.
        :type: str
        """
        self._service_name = service_name

    @property
    def status(self):
        """Gets the status of this QueryJobsReq.

        状态，CREATING：创建中,CREATE_FAILED: 创建失败,CONFIGURATION: 配置中,STARTJOBING: 启动中,WAITING_FOR_START：等待启动中,START_JOB_FAILED：任务启动失败,FULL_TRANSFER_STARTED：全量迁移中 灾备场景为初始化,FULL_TRANSFER_FAILED：全量迁移失败  灾备场景为初始化失败,FULL_TRANSFER_COMPLETE：全量迁移完成 灾备场景为初始化完成,INCRE_TRANSFER_STARTED：增量迁移中 灾备场景为灾备中,INCRE_TRANSFER_FAILED：增量迁移失败 灾备场景为灾备异常,RELEASE_RESOURCE_STARTED：结束任务中,RELEASE_RESOURCE_FAILED：结束任务失败,RELEASE_RESOURCE_COMPLETE：已结束,CHANGE_JOB_STARTED：任务变更中,CHANGE_JOB_FAILED：任务变更失败,CHILD_TRANSFER_STARTING：子任务启动中,CHILD_TRANSFER_STARTED：子任务迁移中,CHILD_TRANSFER_COMPLETE：子任务迁移完成,CHILD_TRANSFER_FAILED：子任务迁移失败,RELEASE_CHILD_TRANSFER_STARTED：子任务结束中,RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束

        :return: The status of this QueryJobsReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryJobsReq.

        状态，CREATING：创建中,CREATE_FAILED: 创建失败,CONFIGURATION: 配置中,STARTJOBING: 启动中,WAITING_FOR_START：等待启动中,START_JOB_FAILED：任务启动失败,FULL_TRANSFER_STARTED：全量迁移中 灾备场景为初始化,FULL_TRANSFER_FAILED：全量迁移失败  灾备场景为初始化失败,FULL_TRANSFER_COMPLETE：全量迁移完成 灾备场景为初始化完成,INCRE_TRANSFER_STARTED：增量迁移中 灾备场景为灾备中,INCRE_TRANSFER_FAILED：增量迁移失败 灾备场景为灾备异常,RELEASE_RESOURCE_STARTED：结束任务中,RELEASE_RESOURCE_FAILED：结束任务失败,RELEASE_RESOURCE_COMPLETE：已结束,CHANGE_JOB_STARTED：任务变更中,CHANGE_JOB_FAILED：任务变更失败,CHILD_TRANSFER_STARTING：子任务启动中,CHILD_TRANSFER_STARTED：子任务迁移中,CHILD_TRANSFER_COMPLETE：子任务迁移完成,CHILD_TRANSFER_FAILED：子任务迁移失败,RELEASE_CHILD_TRANSFER_STARTED：子任务结束中,RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束

        :param status: The status of this QueryJobsReq.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this QueryJobsReq.

        标签

        :return: The tags of this QueryJobsReq.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryJobsReq.

        标签

        :param tags: The tags of this QueryJobsReq.
        :type: dict(str, str)
        """
        self._tags = tags

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
        if not isinstance(other, QueryJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
