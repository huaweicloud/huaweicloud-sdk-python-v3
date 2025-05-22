# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOfflineKeyAnalysisTaskResponse(SdkResponse):

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
        'instance_id': 'str',
        'node_id': 'str',
        'backup_id': 'str',
        'group_name': 'str',
        'node_ip': 'str',
        'node_ipv6': 'str',
        'node_type': 'str',
        'analysis_type': 'str',
        'started_at': 'str',
        'finished_at': 'str',
        'largest_key_prefixes': 'list[LargestKeyPrefix]',
        'largest_keys': 'list[LargestKey]',
        'total_bytes': 'int',
        'total_num': 'int',
        'type_bytes': 'list[KeyTypeByte]',
        'type_num': 'list[KeyTypeNum]'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'backup_id': 'backup_id',
        'group_name': 'group_name',
        'node_ip': 'node_ip',
        'node_ipv6': 'node_ipv6',
        'node_type': 'node_type',
        'analysis_type': 'analysis_type',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'largest_key_prefixes': 'largest_key_prefixes',
        'largest_keys': 'largest_keys',
        'total_bytes': 'total_bytes',
        'total_num': 'total_num',
        'type_bytes': 'type_bytes',
        'type_num': 'type_num'
    }

    def __init__(self, id=None, instance_id=None, node_id=None, backup_id=None, group_name=None, node_ip=None, node_ipv6=None, node_type=None, analysis_type=None, started_at=None, finished_at=None, largest_key_prefixes=None, largest_keys=None, total_bytes=None, total_num=None, type_bytes=None, type_num=None):
        r"""ShowOfflineKeyAnalysisTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 
        :type id: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。 
        :type instance_id: str
        :param node_id: **参数解释**： 节点ID。 **取值范围**： 不涉及。 
        :type node_id: str
        :param backup_id: **参数解释**： 备份ID。 **取值范围**： 不涉及。 
        :type backup_id: str
        :param group_name: **参数解释**： 分片名称。 **取值范围**： 不涉及。 
        :type group_name: str
        :param node_ip: **参数解释**： 节点ipv4地址。 **取值范围**： 不涉及。 
        :type node_ip: str
        :param node_ipv6: **参数解释**： 节点ipv6地址。 **取值范围**： 不涉及。 
        :type node_ipv6: str
        :param node_type: **参数解释**： 节点类型。 **取值范围**： master：主节点 slave：从节点 
        :type node_type: str
        :param analysis_type: **参数解释**： 分析类型。 **取值范围**： new_backup：新建备份并分析。 old_backup：历史备份文件分析。 
        :type analysis_type: str
        :param started_at: **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 
        :type started_at: str
        :param finished_at: **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 
        :type finished_at: str
        :param largest_key_prefixes: **参数解释**： 前缀Key列表。 
        :type largest_key_prefixes: list[:class:`huaweicloudsdkdcs.v2.LargestKeyPrefix`]
        :param largest_keys: **参数解释**： 大key列表。 
        :type largest_keys: list[:class:`huaweicloudsdkdcs.v2.LargestKey`]
        :param total_bytes: **参数解释**： Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 
        :type total_bytes: int
        :param total_num: **参数解释**： Key的总数。 **取值范围**： 不涉及。 
        :type total_num: int
        :param type_bytes: **参数解释**： 每种类型key的总大小，单位：Bytes。 **取值范围**： 不涉及。 
        :type type_bytes: list[:class:`huaweicloudsdkdcs.v2.KeyTypeByte`]
        :param type_num: **参数解释**： 每种类型key总数。 **取值范围**： 不涉及。 
        :type type_num: list[:class:`huaweicloudsdkdcs.v2.KeyTypeNum`]
        """
        
        super(ShowOfflineKeyAnalysisTaskResponse, self).__init__()

        self._id = None
        self._instance_id = None
        self._node_id = None
        self._backup_id = None
        self._group_name = None
        self._node_ip = None
        self._node_ipv6 = None
        self._node_type = None
        self._analysis_type = None
        self._started_at = None
        self._finished_at = None
        self._largest_key_prefixes = None
        self._largest_keys = None
        self._total_bytes = None
        self._total_num = None
        self._type_bytes = None
        self._type_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if backup_id is not None:
            self.backup_id = backup_id
        if group_name is not None:
            self.group_name = group_name
        if node_ip is not None:
            self.node_ip = node_ip
        if node_ipv6 is not None:
            self.node_ipv6 = node_ipv6
        if node_type is not None:
            self.node_type = node_type
        if analysis_type is not None:
            self.analysis_type = analysis_type
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if largest_key_prefixes is not None:
            self.largest_key_prefixes = largest_key_prefixes
        if largest_keys is not None:
            self.largest_keys = largest_keys
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if total_num is not None:
            self.total_num = total_num
        if type_bytes is not None:
            self.type_bytes = type_bytes
        if type_num is not None:
            self.type_num = type_num

    @property
    def id(self):
        r"""Gets the id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 

        :return: The id of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 

        :param id: The id of this ShowOfflineKeyAnalysisTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。 

        :return: The instance_id of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。 

        :param instance_id: The instance_id of this ShowOfflineKeyAnalysisTaskResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。 

        :return: The node_id of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。 

        :param node_id: The node_id of this ShowOfflineKeyAnalysisTaskResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 备份ID。 **取值范围**： 不涉及。 

        :return: The backup_id of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 备份ID。 **取值范围**： 不涉及。 

        :param backup_id: The backup_id of this ShowOfflineKeyAnalysisTaskResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分片名称。 **取值范围**： 不涉及。 

        :return: The group_name of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分片名称。 **取值范围**： 不涉及。 

        :param group_name: The group_name of this ShowOfflineKeyAnalysisTaskResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def node_ip(self):
        r"""Gets the node_ip of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ipv4地址。 **取值范围**： 不涉及。 

        :return: The node_ip of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        r"""Sets the node_ip of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ipv4地址。 **取值范围**： 不涉及。 

        :param node_ip: The node_ip of this ShowOfflineKeyAnalysisTaskResponse.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def node_ipv6(self):
        r"""Gets the node_ipv6 of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ipv6地址。 **取值范围**： 不涉及。 

        :return: The node_ipv6 of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._node_ipv6

    @node_ipv6.setter
    def node_ipv6(self, node_ipv6):
        r"""Sets the node_ipv6 of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点ipv6地址。 **取值范围**： 不涉及。 

        :param node_ipv6: The node_ipv6 of this ShowOfflineKeyAnalysisTaskResponse.
        :type node_ipv6: str
        """
        self._node_ipv6 = node_ipv6

    @property
    def node_type(self):
        r"""Gets the node_type of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点类型。 **取值范围**： master：主节点 slave：从节点 

        :return: The node_type of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 节点类型。 **取值范围**： master：主节点 slave：从节点 

        :param node_type: The node_type of this ShowOfflineKeyAnalysisTaskResponse.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def analysis_type(self):
        r"""Gets the analysis_type of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析类型。 **取值范围**： new_backup：新建备份并分析。 old_backup：历史备份文件分析。 

        :return: The analysis_type of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._analysis_type

    @analysis_type.setter
    def analysis_type(self, analysis_type):
        r"""Sets the analysis_type of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析类型。 **取值范围**： new_backup：新建备份并分析。 old_backup：历史备份文件分析。 

        :param analysis_type: The analysis_type of this ShowOfflineKeyAnalysisTaskResponse.
        :type analysis_type: str
        """
        self._analysis_type = analysis_type

    @property
    def started_at(self):
        r"""Gets the started_at of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 

        :return: The started_at of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 

        :param started_at: The started_at of this ShowOfflineKeyAnalysisTaskResponse.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 

        :return: The finished_at of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 

        :param finished_at: The finished_at of this ShowOfflineKeyAnalysisTaskResponse.
        :type finished_at: str
        """
        self._finished_at = finished_at

    @property
    def largest_key_prefixes(self):
        r"""Gets the largest_key_prefixes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 前缀Key列表。 

        :return: The largest_key_prefixes of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.LargestKeyPrefix`]
        """
        return self._largest_key_prefixes

    @largest_key_prefixes.setter
    def largest_key_prefixes(self, largest_key_prefixes):
        r"""Sets the largest_key_prefixes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 前缀Key列表。 

        :param largest_key_prefixes: The largest_key_prefixes of this ShowOfflineKeyAnalysisTaskResponse.
        :type largest_key_prefixes: list[:class:`huaweicloudsdkdcs.v2.LargestKeyPrefix`]
        """
        self._largest_key_prefixes = largest_key_prefixes

    @property
    def largest_keys(self):
        r"""Gets the largest_keys of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 大key列表。 

        :return: The largest_keys of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.LargestKey`]
        """
        return self._largest_keys

    @largest_keys.setter
    def largest_keys(self, largest_keys):
        r"""Sets the largest_keys of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 大key列表。 

        :param largest_keys: The largest_keys of this ShowOfflineKeyAnalysisTaskResponse.
        :type largest_keys: list[:class:`huaweicloudsdkdcs.v2.LargestKey`]
        """
        self._largest_keys = largest_keys

    @property
    def total_bytes(self):
        r"""Gets the total_bytes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :return: The total_bytes of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: int
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        r"""Sets the total_bytes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :param total_bytes: The total_bytes of this ShowOfflineKeyAnalysisTaskResponse.
        :type total_bytes: int
        """
        self._total_bytes = total_bytes

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： Key的总数。 **取值范围**： 不涉及。 

        :return: The total_num of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： Key的总数。 **取值范围**： 不涉及。 

        :param total_num: The total_num of this ShowOfflineKeyAnalysisTaskResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def type_bytes(self):
        r"""Gets the type_bytes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 每种类型key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :return: The type_bytes of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.KeyTypeByte`]
        """
        return self._type_bytes

    @type_bytes.setter
    def type_bytes(self, type_bytes):
        r"""Sets the type_bytes of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 每种类型key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :param type_bytes: The type_bytes of this ShowOfflineKeyAnalysisTaskResponse.
        :type type_bytes: list[:class:`huaweicloudsdkdcs.v2.KeyTypeByte`]
        """
        self._type_bytes = type_bytes

    @property
    def type_num(self):
        r"""Gets the type_num of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 每种类型key总数。 **取值范围**： 不涉及。 

        :return: The type_num of this ShowOfflineKeyAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.KeyTypeNum`]
        """
        return self._type_num

    @type_num.setter
    def type_num(self, type_num):
        r"""Sets the type_num of this ShowOfflineKeyAnalysisTaskResponse.

        **参数解释**： 每种类型key总数。 **取值范围**： 不涉及。 

        :param type_num: The type_num of this ShowOfflineKeyAnalysisTaskResponse.
        :type type_num: list[:class:`huaweicloudsdkdcs.v2.KeyTypeNum`]
        """
        self._type_num = type_num

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
        if not isinstance(other, ShowOfflineKeyAnalysisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
