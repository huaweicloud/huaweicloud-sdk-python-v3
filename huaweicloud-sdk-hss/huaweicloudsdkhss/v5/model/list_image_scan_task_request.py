# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageScanTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'global_image_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'task_type': 'str',
        'task_name': 'str',
        'task_id': 'str',
        'create_time': 'int',
        'end_time': 'int',
        'task_status': 'str',
        'scan_scope': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'global_image_type': 'global_image_type',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'task_type': 'task_type',
        'task_name': 'task_name',
        'task_id': 'task_id',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'task_status': 'task_status',
        'scan_scope': 'scan_scope'
    }

    def __init__(self, enterprise_project_id=None, global_image_type=None, offset=None, limit=None, type=None, task_type=None, task_name=None, task_id=None, create_time=None, end_time=None, task_status=None, scan_scope=None):
        r"""ListImageScanTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param global_image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 
        :type global_image_type: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param type: **参数解释**: 任务总类型 **约束限制**: 不涉及 **取值范围**: - image_sync：镜像同步。 - image_scan：镜像扫描。  **默认取值**: 不涉及 
        :type type: str
        :param task_type: **参数解释**: 任务细分类型 **约束限制**: 不涉及 **取值范围**: - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。  **默认取值**: 不涉及 
        :type task_type: str
        :param task_name: **参数解释**： 模糊匹配任务名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type task_name: str
        :param task_id: **参数解释**： 任务id **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 
        :type task_id: str
        :param create_time: **参数解释**： 任务创建时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 
        :type create_time: int
        :param end_time: **参数解释**： 任务结束时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 
        :type end_time: int
        :param task_status: **参数解释**: 任务情况 **约束限制**: 不涉及 **取值范围**: - scanning：扫描中。 - finished：完成。  **默认取值**: 不涉及 
        :type task_status: str
        :param scan_scope: **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 
        :type scan_scope: int
        """
        
        

        self._enterprise_project_id = None
        self._global_image_type = None
        self._offset = None
        self._limit = None
        self._type = None
        self._task_type = None
        self._task_name = None
        self._task_id = None
        self._create_time = None
        self._end_time = None
        self._task_status = None
        self._scan_scope = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_image_type is not None:
            self.global_image_type = global_image_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type
        if task_type is not None:
            self.task_type = task_type
        if task_name is not None:
            self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if task_status is not None:
            self.task_status = task_status
        if scan_scope is not None:
            self.scan_scope = scan_scope

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageScanTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_image_type(self):
        r"""Gets the global_image_type of this ListImageScanTaskRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :return: The global_image_type of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._global_image_type

    @global_image_type.setter
    def global_image_type(self, global_image_type):
        r"""Sets the global_image_type of this ListImageScanTaskRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :param global_image_type: The global_image_type of this ListImageScanTaskRequest.
        :type global_image_type: str
        """
        self._global_image_type = global_image_type

    @property
    def offset(self):
        r"""Gets the offset of this ListImageScanTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageScanTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageScanTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageScanTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageScanTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageScanTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageScanTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageScanTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListImageScanTaskRequest.

        **参数解释**: 任务总类型 **约束限制**: 不涉及 **取值范围**: - image_sync：镜像同步。 - image_scan：镜像扫描。  **默认取值**: 不涉及 

        :return: The type of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListImageScanTaskRequest.

        **参数解释**: 任务总类型 **约束限制**: 不涉及 **取值范围**: - image_sync：镜像同步。 - image_scan：镜像扫描。  **默认取值**: 不涉及 

        :param type: The type of this ListImageScanTaskRequest.
        :type type: str
        """
        self._type = type

    @property
    def task_type(self):
        r"""Gets the task_type of this ListImageScanTaskRequest.

        **参数解释**: 任务细分类型 **约束限制**: 不涉及 **取值范围**: - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。  **默认取值**: 不涉及 

        :return: The task_type of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListImageScanTaskRequest.

        **参数解释**: 任务细分类型 **约束限制**: 不涉及 **取值范围**: - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。  **默认取值**: 不涉及 

        :param task_type: The task_type of this ListImageScanTaskRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_name(self):
        r"""Gets the task_name of this ListImageScanTaskRequest.

        **参数解释**： 模糊匹配任务名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The task_name of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListImageScanTaskRequest.

        **参数解释**： 模糊匹配任务名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param task_name: The task_name of this ListImageScanTaskRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        r"""Gets the task_id of this ListImageScanTaskRequest.

        **参数解释**： 任务id **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :return: The task_id of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListImageScanTaskRequest.

        **参数解释**： 任务id **约束限制**： 不涉及 **取值范围**： 字符长度1-256位 **默认取值**： 不涉及 

        :param task_id: The task_id of this ListImageScanTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListImageScanTaskRequest.

        **参数解释**： 任务创建时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 

        :return: The create_time of this ListImageScanTaskRequest.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListImageScanTaskRequest.

        **参数解释**： 任务创建时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 

        :param create_time: The create_time of this ListImageScanTaskRequest.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListImageScanTaskRequest.

        **参数解释**： 任务结束时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 

        :return: The end_time of this ListImageScanTaskRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListImageScanTaskRequest.

        **参数解释**： 任务结束时间，时间单位毫秒（ms） **约束限制**： 不涉及 **取值范围**： 最小值0，最大值4070880000000 **默认取值**： 不涉及 

        :param end_time: The end_time of this ListImageScanTaskRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def task_status(self):
        r"""Gets the task_status of this ListImageScanTaskRequest.

        **参数解释**: 任务情况 **约束限制**: 不涉及 **取值范围**: - scanning：扫描中。 - finished：完成。  **默认取值**: 不涉及 

        :return: The task_status of this ListImageScanTaskRequest.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListImageScanTaskRequest.

        **参数解释**: 任务情况 **约束限制**: 不涉及 **取值范围**: - scanning：扫描中。 - finished：完成。  **默认取值**: 不涉及 

        :param task_status: The task_status of this ListImageScanTaskRequest.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def scan_scope(self):
        r"""Gets the scan_scope of this ListImageScanTaskRequest.

        **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 

        :return: The scan_scope of this ListImageScanTaskRequest.
        :rtype: int
        """
        return self._scan_scope

    @scan_scope.setter
    def scan_scope(self, scan_scope):
        r"""Sets the scan_scope of this ListImageScanTaskRequest.

        **参数解释**: 扫描风险类型 **约束限制**: 不涉及 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。  **默认取值**: 不涉及 

        :param scan_scope: The scan_scope of this ListImageScanTaskRequest.
        :type scan_scope: int
        """
        self._scan_scope = scan_scope

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
        if not isinstance(other, ListImageScanTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
