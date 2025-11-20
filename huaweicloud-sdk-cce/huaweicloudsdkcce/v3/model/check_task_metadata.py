# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTaskMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'task_id': 'str',
        'addon_template_name': 'str',
        'addon_instance_name': 'str',
        'addon_instance_id': 'str',
        'create_time_stamp': 'str',
        'expire_time_stamp': 'str'
    }

    attribute_map = {
        'type': 'type',
        'task_id': 'taskID',
        'addon_template_name': 'addonTemplateName',
        'addon_instance_name': 'addonInstanceName',
        'addon_instance_id': 'addonInstanceID',
        'create_time_stamp': 'createTimeStamp',
        'expire_time_stamp': 'expireTimeStamp'
    }

    def __init__(self, type=None, task_id=None, addon_template_name=None, addon_instance_name=None, addon_instance_id=None, create_time_stamp=None, expire_time_stamp=None):
        r"""CheckTaskMetadata

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 插件检查类型 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  
        :type type: str
        :param task_id: **参数解释：** 插件检查任务ID，用于任务检查结果查询 **取值范围：** 不涉及 
        :type task_id: str
        :param addon_template_name: **参数解释：** 插件模板名称 **取值范围：** cce服务提供的插件模板，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].metadata.name字段获取 
        :type addon_template_name: str
        :param addon_instance_name: **参数解释：** 插件实例名称 **取值范围：** 不涉及 
        :type addon_instance_name: str
        :param addon_instance_id: **参数解释：** 插件实例ID **取值范围：** 不涉及 
        :type addon_instance_id: str
        :param create_time_stamp: **参数解释：** 插件检查任务创建时间 **取值范围：** 不涉及 
        :type create_time_stamp: str
        :param expire_time_stamp: **参数解释：** 插件检查任务超时时间，仅终态（Failed/Success）任务存在此字段 **取值范围：** 不涉及 
        :type expire_time_stamp: str
        """
        
        

        self._type = None
        self._task_id = None
        self._addon_template_name = None
        self._addon_instance_name = None
        self._addon_instance_id = None
        self._create_time_stamp = None
        self._expire_time_stamp = None
        self.discriminator = None

        self.type = type
        self.task_id = task_id
        self.addon_template_name = addon_template_name
        if addon_instance_name is not None:
            self.addon_instance_name = addon_instance_name
        if addon_instance_id is not None:
            self.addon_instance_id = addon_instance_id
        self.create_time_stamp = create_time_stamp
        if expire_time_stamp is not None:
            self.expire_time_stamp = expire_time_stamp

    @property
    def type(self):
        r"""Gets the type of this CheckTaskMetadata.

        **参数解释：** 插件检查类型 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  

        :return: The type of this CheckTaskMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CheckTaskMetadata.

        **参数解释：** 插件检查类型 **取值范围：** - addonStatic: 运行中插件巡检 - addonUpgrade: 插件升级前检查  

        :param type: The type of this CheckTaskMetadata.
        :type type: str
        """
        self._type = type

    @property
    def task_id(self):
        r"""Gets the task_id of this CheckTaskMetadata.

        **参数解释：** 插件检查任务ID，用于任务检查结果查询 **取值范围：** 不涉及 

        :return: The task_id of this CheckTaskMetadata.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CheckTaskMetadata.

        **参数解释：** 插件检查任务ID，用于任务检查结果查询 **取值范围：** 不涉及 

        :param task_id: The task_id of this CheckTaskMetadata.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this CheckTaskMetadata.

        **参数解释：** 插件模板名称 **取值范围：** cce服务提供的插件模板，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].metadata.name字段获取 

        :return: The addon_template_name of this CheckTaskMetadata.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this CheckTaskMetadata.

        **参数解释：** 插件模板名称 **取值范围：** cce服务提供的插件模板，可以通过[查询AddonTemplates列表](cce_02_0321.xml)中的items[].metadata.name字段获取 

        :param addon_template_name: The addon_template_name of this CheckTaskMetadata.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def addon_instance_name(self):
        r"""Gets the addon_instance_name of this CheckTaskMetadata.

        **参数解释：** 插件实例名称 **取值范围：** 不涉及 

        :return: The addon_instance_name of this CheckTaskMetadata.
        :rtype: str
        """
        return self._addon_instance_name

    @addon_instance_name.setter
    def addon_instance_name(self, addon_instance_name):
        r"""Sets the addon_instance_name of this CheckTaskMetadata.

        **参数解释：** 插件实例名称 **取值范围：** 不涉及 

        :param addon_instance_name: The addon_instance_name of this CheckTaskMetadata.
        :type addon_instance_name: str
        """
        self._addon_instance_name = addon_instance_name

    @property
    def addon_instance_id(self):
        r"""Gets the addon_instance_id of this CheckTaskMetadata.

        **参数解释：** 插件实例ID **取值范围：** 不涉及 

        :return: The addon_instance_id of this CheckTaskMetadata.
        :rtype: str
        """
        return self._addon_instance_id

    @addon_instance_id.setter
    def addon_instance_id(self, addon_instance_id):
        r"""Sets the addon_instance_id of this CheckTaskMetadata.

        **参数解释：** 插件实例ID **取值范围：** 不涉及 

        :param addon_instance_id: The addon_instance_id of this CheckTaskMetadata.
        :type addon_instance_id: str
        """
        self._addon_instance_id = addon_instance_id

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this CheckTaskMetadata.

        **参数解释：** 插件检查任务创建时间 **取值范围：** 不涉及 

        :return: The create_time_stamp of this CheckTaskMetadata.
        :rtype: str
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this CheckTaskMetadata.

        **参数解释：** 插件检查任务创建时间 **取值范围：** 不涉及 

        :param create_time_stamp: The create_time_stamp of this CheckTaskMetadata.
        :type create_time_stamp: str
        """
        self._create_time_stamp = create_time_stamp

    @property
    def expire_time_stamp(self):
        r"""Gets the expire_time_stamp of this CheckTaskMetadata.

        **参数解释：** 插件检查任务超时时间，仅终态（Failed/Success）任务存在此字段 **取值范围：** 不涉及 

        :return: The expire_time_stamp of this CheckTaskMetadata.
        :rtype: str
        """
        return self._expire_time_stamp

    @expire_time_stamp.setter
    def expire_time_stamp(self, expire_time_stamp):
        r"""Sets the expire_time_stamp of this CheckTaskMetadata.

        **参数解释：** 插件检查任务超时时间，仅终态（Failed/Success）任务存在此字段 **取值范围：** 不涉及 

        :param expire_time_stamp: The expire_time_stamp of this CheckTaskMetadata.
        :type expire_time_stamp: str
        """
        self._expire_time_stamp = expire_time_stamp

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
        if not isinstance(other, CheckTaskMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
