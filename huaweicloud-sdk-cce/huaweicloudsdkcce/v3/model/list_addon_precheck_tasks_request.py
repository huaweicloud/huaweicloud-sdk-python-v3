# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddonPrecheckTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'type': 'str',
        'task_id': 'str',
        'addon_instance_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'type': 'type',
        'task_id': 'task_id',
        'addon_instance_id': 'addon_instance_id'
    }

    def __init__(self, cluster_id=None, type=None, task_id=None, addon_instance_id=None):
        r"""ListAddonPrecheckTasksRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param type: **参数解释：** 根据插件检查类型筛选结果 **约束限制：** 不涉及 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 
        :type type: str
        :param task_id: **参数解释：** 根据插件检查任务ID筛选结果，插件检查任务ID可以通过[批量创建插件检查任务](BatchCreateAddonPrecheck.xml)中的status.items[].metadata.taskID字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type task_id: str
        :param addon_instance_id: **参数解释：** 根据插件实例ID筛选结果，实例ID可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type addon_instance_id: str
        """
        
        

        self._cluster_id = None
        self._type = None
        self._task_id = None
        self._addon_instance_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if type is not None:
            self.type = type
        if task_id is not None:
            self.task_id = task_id
        if addon_instance_id is not None:
            self.addon_instance_id = addon_instance_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAddonPrecheckTasksRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ListAddonPrecheckTasksRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAddonPrecheckTasksRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ListAddonPrecheckTasksRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件检查类型筛选结果 **约束限制：** 不涉及 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 

        :return: The type of this ListAddonPrecheckTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件检查类型筛选结果 **约束限制：** 不涉及 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  **默认取值：** 不涉及 

        :param type: The type of this ListAddonPrecheckTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def task_id(self):
        r"""Gets the task_id of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件检查任务ID筛选结果，插件检查任务ID可以通过[批量创建插件检查任务](BatchCreateAddonPrecheck.xml)中的status.items[].metadata.taskID字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The task_id of this ListAddonPrecheckTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件检查任务ID筛选结果，插件检查任务ID可以通过[批量创建插件检查任务](BatchCreateAddonPrecheck.xml)中的status.items[].metadata.taskID字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param task_id: The task_id of this ListAddonPrecheckTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def addon_instance_id(self):
        r"""Gets the addon_instance_id of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件实例ID筛选结果，实例ID可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The addon_instance_id of this ListAddonPrecheckTasksRequest.
        :rtype: str
        """
        return self._addon_instance_id

    @addon_instance_id.setter
    def addon_instance_id(self, addon_instance_id):
        r"""Sets the addon_instance_id of this ListAddonPrecheckTasksRequest.

        **参数解释：** 根据插件实例ID筛选结果，实例ID可以通过[获取AddonInstance列表](cce_02_0326.xml)中的items[].metadata.uid字段获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param addon_instance_id: The addon_instance_id of this ListAddonPrecheckTasksRequest.
        :type addon_instance_id: str
        """
        self._addon_instance_id = addon_instance_id

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
        if not isinstance(other, ListAddonPrecheckTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
