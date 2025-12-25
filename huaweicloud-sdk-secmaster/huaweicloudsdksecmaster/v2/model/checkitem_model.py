# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckitemModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'aggregation_handle_status': 'str',
        'audit_procedure': 'str',
        'impact': 'str',
        'cloud_server': 'str',
        'description': 'str',
        'level': 'str',
        'method': 'int',
        'name': 'str',
        'source': 'int',
        'workflow_id': 'str',
        'spec_checkitem_list': 'list[SpecCheckitemModel]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'aggregation_handle_status': 'aggregation_handle_status',
        'audit_procedure': 'audit_procedure',
        'impact': 'impact',
        'cloud_server': 'cloud_server',
        'description': 'description',
        'level': 'level',
        'method': 'method',
        'name': 'name',
        'source': 'source',
        'workflow_id': 'workflow_id',
        'spec_checkitem_list': 'spec_checkitem_list'
    }

    def __init__(self, uuid=None, aggregation_handle_status=None, audit_procedure=None, impact=None, cloud_server=None, description=None, level=None, method=None, name=None, source=None, workflow_id=None, spec_checkitem_list=None):
        r"""CheckitemModel

        The model defined in huaweicloud sdk

        :param uuid: 检查项的id
        :type uuid: str
        :param aggregation_handle_status: 检查项结果聚合状态
        :type aggregation_handle_status: str
        :param audit_procedure: 检查项的检查过程
        :type audit_procedure: str
        :param impact: 检查项的影响
        :type impact: str
        :param cloud_server: 检查项所属云服务
        :type cloud_server: str
        :param description: 对检查项的描述
        :type description: str
        :param level: 表示该检查项的严重程度 informational：提示 low: 低危 medium：中危 high: 高危 fatal：致命
        :type level: str
        :param method: 表示该检查项的检查方式 0：自动项 3: 剧本流程/logic app
        :type method: int
        :param name: 检查项的名称
        :type name: str
        :param source: 表示该检查项的来源 0：默认/default 2: 剧本流程/playbook
        :type source: int
        :param workflow_id: **参数解释**: 流程ID **约束限制**: 不涉及
        :type workflow_id: str
        :param spec_checkitem_list: 检查项所属遵从包的信息
        :type spec_checkitem_list: list[:class:`huaweicloudsdksecmaster.v2.SpecCheckitemModel`]
        """
        
        

        self._uuid = None
        self._aggregation_handle_status = None
        self._audit_procedure = None
        self._impact = None
        self._cloud_server = None
        self._description = None
        self._level = None
        self._method = None
        self._name = None
        self._source = None
        self._workflow_id = None
        self._spec_checkitem_list = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if aggregation_handle_status is not None:
            self.aggregation_handle_status = aggregation_handle_status
        if audit_procedure is not None:
            self.audit_procedure = audit_procedure
        if impact is not None:
            self.impact = impact
        self.cloud_server = cloud_server
        self.description = description
        self.level = level
        self.method = method
        self.name = name
        if source is not None:
            self.source = source
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if spec_checkitem_list is not None:
            self.spec_checkitem_list = spec_checkitem_list

    @property
    def uuid(self):
        r"""Gets the uuid of this CheckitemModel.

        检查项的id

        :return: The uuid of this CheckitemModel.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this CheckitemModel.

        检查项的id

        :param uuid: The uuid of this CheckitemModel.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def aggregation_handle_status(self):
        r"""Gets the aggregation_handle_status of this CheckitemModel.

        检查项结果聚合状态

        :return: The aggregation_handle_status of this CheckitemModel.
        :rtype: str
        """
        return self._aggregation_handle_status

    @aggregation_handle_status.setter
    def aggregation_handle_status(self, aggregation_handle_status):
        r"""Sets the aggregation_handle_status of this CheckitemModel.

        检查项结果聚合状态

        :param aggregation_handle_status: The aggregation_handle_status of this CheckitemModel.
        :type aggregation_handle_status: str
        """
        self._aggregation_handle_status = aggregation_handle_status

    @property
    def audit_procedure(self):
        r"""Gets the audit_procedure of this CheckitemModel.

        检查项的检查过程

        :return: The audit_procedure of this CheckitemModel.
        :rtype: str
        """
        return self._audit_procedure

    @audit_procedure.setter
    def audit_procedure(self, audit_procedure):
        r"""Sets the audit_procedure of this CheckitemModel.

        检查项的检查过程

        :param audit_procedure: The audit_procedure of this CheckitemModel.
        :type audit_procedure: str
        """
        self._audit_procedure = audit_procedure

    @property
    def impact(self):
        r"""Gets the impact of this CheckitemModel.

        检查项的影响

        :return: The impact of this CheckitemModel.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        r"""Sets the impact of this CheckitemModel.

        检查项的影响

        :param impact: The impact of this CheckitemModel.
        :type impact: str
        """
        self._impact = impact

    @property
    def cloud_server(self):
        r"""Gets the cloud_server of this CheckitemModel.

        检查项所属云服务

        :return: The cloud_server of this CheckitemModel.
        :rtype: str
        """
        return self._cloud_server

    @cloud_server.setter
    def cloud_server(self, cloud_server):
        r"""Sets the cloud_server of this CheckitemModel.

        检查项所属云服务

        :param cloud_server: The cloud_server of this CheckitemModel.
        :type cloud_server: str
        """
        self._cloud_server = cloud_server

    @property
    def description(self):
        r"""Gets the description of this CheckitemModel.

        对检查项的描述

        :return: The description of this CheckitemModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CheckitemModel.

        对检查项的描述

        :param description: The description of this CheckitemModel.
        :type description: str
        """
        self._description = description

    @property
    def level(self):
        r"""Gets the level of this CheckitemModel.

        表示该检查项的严重程度 informational：提示 low: 低危 medium：中危 high: 高危 fatal：致命

        :return: The level of this CheckitemModel.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CheckitemModel.

        表示该检查项的严重程度 informational：提示 low: 低危 medium：中危 high: 高危 fatal：致命

        :param level: The level of this CheckitemModel.
        :type level: str
        """
        self._level = level

    @property
    def method(self):
        r"""Gets the method of this CheckitemModel.

        表示该检查项的检查方式 0：自动项 3: 剧本流程/logic app

        :return: The method of this CheckitemModel.
        :rtype: int
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this CheckitemModel.

        表示该检查项的检查方式 0：自动项 3: 剧本流程/logic app

        :param method: The method of this CheckitemModel.
        :type method: int
        """
        self._method = method

    @property
    def name(self):
        r"""Gets the name of this CheckitemModel.

        检查项的名称

        :return: The name of this CheckitemModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckitemModel.

        检查项的名称

        :param name: The name of this CheckitemModel.
        :type name: str
        """
        self._name = name

    @property
    def source(self):
        r"""Gets the source of this CheckitemModel.

        表示该检查项的来源 0：默认/default 2: 剧本流程/playbook

        :return: The source of this CheckitemModel.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CheckitemModel.

        表示该检查项的来源 0：默认/default 2: 剧本流程/playbook

        :param source: The source of this CheckitemModel.
        :type source: int
        """
        self._source = source

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CheckitemModel.

        **参数解释**: 流程ID **约束限制**: 不涉及

        :return: The workflow_id of this CheckitemModel.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CheckitemModel.

        **参数解释**: 流程ID **约束限制**: 不涉及

        :param workflow_id: The workflow_id of this CheckitemModel.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def spec_checkitem_list(self):
        r"""Gets the spec_checkitem_list of this CheckitemModel.

        检查项所属遵从包的信息

        :return: The spec_checkitem_list of this CheckitemModel.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.SpecCheckitemModel`]
        """
        return self._spec_checkitem_list

    @spec_checkitem_list.setter
    def spec_checkitem_list(self, spec_checkitem_list):
        r"""Sets the spec_checkitem_list of this CheckitemModel.

        检查项所属遵从包的信息

        :param spec_checkitem_list: The spec_checkitem_list of this CheckitemModel.
        :type spec_checkitem_list: list[:class:`huaweicloudsdksecmaster.v2.SpecCheckitemModel`]
        """
        self._spec_checkitem_list = spec_checkitem_list

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
        if not isinstance(other, CheckitemModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
