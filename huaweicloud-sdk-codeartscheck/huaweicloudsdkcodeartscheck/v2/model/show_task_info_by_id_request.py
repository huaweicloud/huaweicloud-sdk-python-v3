# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskInfoByIdRequest:

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
        'merge_id': 'str',
        'job_id': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'merge_id': 'merge_id',
        'job_id': 'job_id',
        'operator': 'operator'
    }

    def __init__(self, task_id=None, merge_id=None, job_id=None, operator=None):
        r"""ShowTaskInfoByIdRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。
        :type task_id: str
        :param merge_id: **参数解释：** 合并请求ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。
        :type merge_id: str
        :param job_id: **参数解释：** 执行记录ID，即每一次执行版本级或门禁级扫描的唯一ID。通过[[执行检查任务](https://support.huaweicloud.com/api-codecheck/RunTaskV2.html)](tag:hws)[[执行检查任务](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/RunTaskV2.html)](tag:hws_hk)[执行检查任务](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口的返回值可获取执行记录ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~64]个字符。 **默认取值：** 不涉及。
        :type job_id: str
        :param operator: **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。
        :type operator: str
        """
        
        

        self._task_id = None
        self._merge_id = None
        self._job_id = None
        self._operator = None
        self.discriminator = None

        self.task_id = task_id
        if merge_id is not None:
            self.merge_id = merge_id
        if job_id is not None:
            self.job_id = job_id
        if operator is not None:
            self.operator = operator

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :return: The task_id of this ShowTaskInfoByIdRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ShowTaskInfoByIdRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def merge_id(self):
        r"""Gets the merge_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 合并请求ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :return: The merge_id of this ShowTaskInfoByIdRequest.
        :rtype: str
        """
        return self._merge_id

    @merge_id.setter
    def merge_id(self, merge_id):
        r"""Sets the merge_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 合并请求ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :param merge_id: The merge_id of this ShowTaskInfoByIdRequest.
        :type merge_id: str
        """
        self._merge_id = merge_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 执行记录ID，即每一次执行版本级或门禁级扫描的唯一ID。通过[[执行检查任务](https://support.huaweicloud.com/api-codecheck/RunTaskV2.html)](tag:hws)[[执行检查任务](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/RunTaskV2.html)](tag:hws_hk)[执行检查任务](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口的返回值可获取执行记录ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~64]个字符。 **默认取值：** 不涉及。

        :return: The job_id of this ShowTaskInfoByIdRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTaskInfoByIdRequest.

        **参数解释：** 执行记录ID，即每一次执行版本级或门禁级扫描的唯一ID。通过[[执行检查任务](https://support.huaweicloud.com/api-codecheck/RunTaskV2.html)](tag:hws)[[执行检查任务](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/RunTaskV2.html)](tag:hws_hk)[执行检查任务](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口的返回值可获取执行记录ID。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~64]个字符。 **默认取值：** 不涉及。

        :param job_id: The job_id of this ShowTaskInfoByIdRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def operator(self):
        r"""Gets the operator of this ShowTaskInfoByIdRequest.

        **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :return: The operator of this ShowTaskInfoByIdRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ShowTaskInfoByIdRequest.

        **参数解释：** 操作者。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :param operator: The operator of this ShowTaskInfoByIdRequest.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, ShowTaskInfoByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
