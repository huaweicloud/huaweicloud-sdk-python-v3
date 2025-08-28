# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageScanTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'policy_id': 'str',
        'task_name': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'remain_min': 'int',
        'task_type': 'str',
        'image_type': 'str',
        'task_status': 'int',
        'scan_scope': 'int',
        'rate_limit': 'int',
        'is_all': 'bool',
        'failed_num': 'int',
        'success_num': 'int',
        'total_num': 'int',
        'risky_num': 'int',
        'sync_task_type': 'str',
        'failed_reason': 'str',
        'failed_images': 'list[ImageScanTaskInfoFailedImages]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'policy_id': 'policy_id',
        'task_name': 'task_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'remain_min': 'remain_min',
        'task_type': 'task_type',
        'image_type': 'image_type',
        'task_status': 'task_status',
        'scan_scope': 'scan_scope',
        'rate_limit': 'rate_limit',
        'is_all': 'is_all',
        'failed_num': 'failed_num',
        'success_num': 'success_num',
        'total_num': 'total_num',
        'risky_num': 'risky_num',
        'sync_task_type': 'sync_task_type',
        'failed_reason': 'failed_reason',
        'failed_images': 'failed_images'
    }

    def __init__(self, task_id=None, policy_id=None, task_name=None, begin_time=None, end_time=None, remain_min=None, task_type=None, image_type=None, task_status=None, scan_scope=None, rate_limit=None, is_all=None, failed_num=None, success_num=None, total_num=None, risky_num=None, sync_task_type=None, failed_reason=None, failed_images=None):
        r"""ImageScanTaskInfo

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**： 任务ID **取值范围**： 字符长度1-256位 
        :type task_id: str
        :param policy_id: **参数解释**： 策略ID **取值范围**： 字符长度1-256位 
        :type policy_id: str
        :param task_name: **参数解释**： 任务名称 **取值范围**： 字符长度1-256位 
        :type task_name: str
        :param begin_time: **参数解释**： 任务开始时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type begin_time: int
        :param end_time: **参数解释**： 任务结束时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type end_time: int
        :param remain_min: **参数解释**： 任务剩余时间 **取值范围**： 最小值0，最大值2147483547 
        :type remain_min: int
        :param task_type: **参数解释**： 任务细分类型 **取值范围**： - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。 
        :type task_type: str
        :param image_type: **参数解释**： 镜像类型 **取值范围**： - local：本地镜像。 - registry：仓库镜像。 
        :type image_type: str
        :param task_status: **参数解释**： 扫描进度状态 **取值范围**： - 100：扫描完成。 - 0-100：扫描进度。 - -1：扫描终止。 - -2：扫描超时。 - -3：扫描异常。 
        :type task_status: int
        :param scan_scope: **参数解释**： 扫描风险类型 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。 
        :type scan_scope: int
        :param rate_limit: **参数解释**： 扫描限速 单位：个/h **取值范围**： 最小值0，最大值1000 
        :type rate_limit: int
        :param is_all: **参数解释**： 扫描全部镜像 **取值范围**： - true：扫描全部镜像。 - false：指定镜像扫描。 
        :type is_all: bool
        :param failed_num: **参数解释**： 扫描失败镜像数量 **取值范围**： 最小值0，最大值2147483547 
        :type failed_num: int
        :param success_num: **参数解释**： 扫描成功镜像数量 **取值范围**： 最小值0，最大值2147483547 
        :type success_num: int
        :param total_num: **参数解释**： 任务关联的镜像总数 **取值范围**： 最小值0，最大值2147483547 
        :type total_num: int
        :param risky_num: **参数解释**： 有漏洞风险、基线风险、恶意文件的镜像总数 **取值范围**： 最小值0，最大值2147483547 
        :type risky_num: int
        :param sync_task_type: **参数解释**： 同步任务类型 **取值范围**： 字符长度1-256位 
        :type sync_task_type: str
        :param failed_reason: **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 
        :type failed_reason: str
        :param failed_images: **参数解释**： 失败镜像列表 **取值范围**： 最小值0，最大值2147483547 
        :type failed_images: list[:class:`huaweicloudsdkhss.v5.ImageScanTaskInfoFailedImages`]
        """
        
        

        self._task_id = None
        self._policy_id = None
        self._task_name = None
        self._begin_time = None
        self._end_time = None
        self._remain_min = None
        self._task_type = None
        self._image_type = None
        self._task_status = None
        self._scan_scope = None
        self._rate_limit = None
        self._is_all = None
        self._failed_num = None
        self._success_num = None
        self._total_num = None
        self._risky_num = None
        self._sync_task_type = None
        self._failed_reason = None
        self._failed_images = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if policy_id is not None:
            self.policy_id = policy_id
        if task_name is not None:
            self.task_name = task_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if remain_min is not None:
            self.remain_min = remain_min
        if task_type is not None:
            self.task_type = task_type
        if image_type is not None:
            self.image_type = image_type
        if task_status is not None:
            self.task_status = task_status
        if scan_scope is not None:
            self.scan_scope = scan_scope
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if is_all is not None:
            self.is_all = is_all
        if failed_num is not None:
            self.failed_num = failed_num
        if success_num is not None:
            self.success_num = success_num
        if total_num is not None:
            self.total_num = total_num
        if risky_num is not None:
            self.risky_num = risky_num
        if sync_task_type is not None:
            self.sync_task_type = sync_task_type
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_images is not None:
            self.failed_images = failed_images

    @property
    def task_id(self):
        r"""Gets the task_id of this ImageScanTaskInfo.

        **参数解释**： 任务ID **取值范围**： 字符长度1-256位 

        :return: The task_id of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ImageScanTaskInfo.

        **参数解释**： 任务ID **取值范围**： 字符长度1-256位 

        :param task_id: The task_id of this ImageScanTaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ImageScanTaskInfo.

        **参数解释**： 策略ID **取值范围**： 字符长度1-256位 

        :return: The policy_id of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ImageScanTaskInfo.

        **参数解释**： 策略ID **取值范围**： 字符长度1-256位 

        :param policy_id: The policy_id of this ImageScanTaskInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ImageScanTaskInfo.

        **参数解释**： 任务名称 **取值范围**： 字符长度1-256位 

        :return: The task_name of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ImageScanTaskInfo.

        **参数解释**： 任务名称 **取值范围**： 字符长度1-256位 

        :param task_name: The task_name of this ImageScanTaskInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ImageScanTaskInfo.

        **参数解释**： 任务开始时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The begin_time of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ImageScanTaskInfo.

        **参数解释**： 任务开始时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param begin_time: The begin_time of this ImageScanTaskInfo.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ImageScanTaskInfo.

        **参数解释**： 任务结束时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The end_time of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ImageScanTaskInfo.

        **参数解释**： 任务结束时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param end_time: The end_time of this ImageScanTaskInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def remain_min(self):
        r"""Gets the remain_min of this ImageScanTaskInfo.

        **参数解释**： 任务剩余时间 **取值范围**： 最小值0，最大值2147483547 

        :return: The remain_min of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._remain_min

    @remain_min.setter
    def remain_min(self, remain_min):
        r"""Sets the remain_min of this ImageScanTaskInfo.

        **参数解释**： 任务剩余时间 **取值范围**： 最小值0，最大值2147483547 

        :param remain_min: The remain_min of this ImageScanTaskInfo.
        :type remain_min: int
        """
        self._remain_min = remain_min

    @property
    def task_type(self):
        r"""Gets the task_type of this ImageScanTaskInfo.

        **参数解释**： 任务细分类型 **取值范围**： - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。 

        :return: The task_type of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ImageScanTaskInfo.

        **参数解释**： 任务细分类型 **取值范围**： - cycle：定时扫描。 - manual：手动扫描。 - autoSync：定时同步。 - manualSync：手动同步。 

        :param task_type: The task_type of this ImageScanTaskInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def image_type(self):
        r"""Gets the image_type of this ImageScanTaskInfo.

        **参数解释**： 镜像类型 **取值范围**： - local：本地镜像。 - registry：仓库镜像。 

        :return: The image_type of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ImageScanTaskInfo.

        **参数解释**： 镜像类型 **取值范围**： - local：本地镜像。 - registry：仓库镜像。 

        :param image_type: The image_type of this ImageScanTaskInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def task_status(self):
        r"""Gets the task_status of this ImageScanTaskInfo.

        **参数解释**： 扫描进度状态 **取值范围**： - 100：扫描完成。 - 0-100：扫描进度。 - -1：扫描终止。 - -2：扫描超时。 - -3：扫描异常。 

        :return: The task_status of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ImageScanTaskInfo.

        **参数解释**： 扫描进度状态 **取值范围**： - 100：扫描完成。 - 0-100：扫描进度。 - -1：扫描终止。 - -2：扫描超时。 - -3：扫描异常。 

        :param task_status: The task_status of this ImageScanTaskInfo.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def scan_scope(self):
        r"""Gets the scan_scope of this ImageScanTaskInfo.

        **参数解释**： 扫描风险类型 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。 

        :return: The scan_scope of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._scan_scope

    @scan_scope.setter
    def scan_scope(self, scan_scope):
        r"""Sets the scan_scope of this ImageScanTaskInfo.

        **参数解释**： 扫描风险类型 **取值范围**: - 0：none。 - 0x7fffffff：全部。 - 0x000f0000：漏洞。 - 0x0000f000：基线检查。 - 0x00000f00：恶意文件。 - 0x000000f0：敏感信息。 - 0x0000000f：软件合规。 

        :param scan_scope: The scan_scope of this ImageScanTaskInfo.
        :type scan_scope: int
        """
        self._scan_scope = scan_scope

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this ImageScanTaskInfo.

        **参数解释**： 扫描限速 单位：个/h **取值范围**： 最小值0，最大值1000 

        :return: The rate_limit of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this ImageScanTaskInfo.

        **参数解释**： 扫描限速 单位：个/h **取值范围**： 最小值0，最大值1000 

        :param rate_limit: The rate_limit of this ImageScanTaskInfo.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def is_all(self):
        r"""Gets the is_all of this ImageScanTaskInfo.

        **参数解释**： 扫描全部镜像 **取值范围**： - true：扫描全部镜像。 - false：指定镜像扫描。 

        :return: The is_all of this ImageScanTaskInfo.
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        r"""Sets the is_all of this ImageScanTaskInfo.

        **参数解释**： 扫描全部镜像 **取值范围**： - true：扫描全部镜像。 - false：指定镜像扫描。 

        :param is_all: The is_all of this ImageScanTaskInfo.
        :type is_all: bool
        """
        self._is_all = is_all

    @property
    def failed_num(self):
        r"""Gets the failed_num of this ImageScanTaskInfo.

        **参数解释**： 扫描失败镜像数量 **取值范围**： 最小值0，最大值2147483547 

        :return: The failed_num of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this ImageScanTaskInfo.

        **参数解释**： 扫描失败镜像数量 **取值范围**： 最小值0，最大值2147483547 

        :param failed_num: The failed_num of this ImageScanTaskInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def success_num(self):
        r"""Gets the success_num of this ImageScanTaskInfo.

        **参数解释**： 扫描成功镜像数量 **取值范围**： 最小值0，最大值2147483547 

        :return: The success_num of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ImageScanTaskInfo.

        **参数解释**： 扫描成功镜像数量 **取值范围**： 最小值0，最大值2147483547 

        :param success_num: The success_num of this ImageScanTaskInfo.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def total_num(self):
        r"""Gets the total_num of this ImageScanTaskInfo.

        **参数解释**： 任务关联的镜像总数 **取值范围**： 最小值0，最大值2147483547 

        :return: The total_num of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ImageScanTaskInfo.

        **参数解释**： 任务关联的镜像总数 **取值范围**： 最小值0，最大值2147483547 

        :param total_num: The total_num of this ImageScanTaskInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def risky_num(self):
        r"""Gets the risky_num of this ImageScanTaskInfo.

        **参数解释**： 有漏洞风险、基线风险、恶意文件的镜像总数 **取值范围**： 最小值0，最大值2147483547 

        :return: The risky_num of this ImageScanTaskInfo.
        :rtype: int
        """
        return self._risky_num

    @risky_num.setter
    def risky_num(self, risky_num):
        r"""Sets the risky_num of this ImageScanTaskInfo.

        **参数解释**： 有漏洞风险、基线风险、恶意文件的镜像总数 **取值范围**： 最小值0，最大值2147483547 

        :param risky_num: The risky_num of this ImageScanTaskInfo.
        :type risky_num: int
        """
        self._risky_num = risky_num

    @property
    def sync_task_type(self):
        r"""Gets the sync_task_type of this ImageScanTaskInfo.

        **参数解释**： 同步任务类型 **取值范围**： 字符长度1-256位 

        :return: The sync_task_type of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._sync_task_type

    @sync_task_type.setter
    def sync_task_type(self, sync_task_type):
        r"""Sets the sync_task_type of this ImageScanTaskInfo.

        **参数解释**： 同步任务类型 **取值范围**： 字符长度1-256位 

        :param sync_task_type: The sync_task_type of this ImageScanTaskInfo.
        :type sync_task_type: str
        """
        self._sync_task_type = sync_task_type

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ImageScanTaskInfo.

        **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 

        :return: The failed_reason of this ImageScanTaskInfo.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ImageScanTaskInfo.

        **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 

        :param failed_reason: The failed_reason of this ImageScanTaskInfo.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_images(self):
        r"""Gets the failed_images of this ImageScanTaskInfo.

        **参数解释**： 失败镜像列表 **取值范围**： 最小值0，最大值2147483547 

        :return: The failed_images of this ImageScanTaskInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageScanTaskInfoFailedImages`]
        """
        return self._failed_images

    @failed_images.setter
    def failed_images(self, failed_images):
        r"""Sets the failed_images of this ImageScanTaskInfo.

        **参数解释**： 失败镜像列表 **取值范围**： 最小值0，最大值2147483547 

        :param failed_images: The failed_images of this ImageScanTaskInfo.
        :type failed_images: list[:class:`huaweicloudsdkhss.v5.ImageScanTaskInfoFailedImages`]
        """
        self._failed_images = failed_images

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
        if not isinstance(other, ImageScanTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
