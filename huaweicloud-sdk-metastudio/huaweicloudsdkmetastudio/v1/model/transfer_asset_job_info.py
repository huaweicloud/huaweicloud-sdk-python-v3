# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferAssetJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'transfer_type': 'str',
        'transfer_assets': 'list[DigitalAssetSummary]',
        'state': 'str',
        'src_project_id': 'str',
        'dest_project_id': 'str',
        'memo': 'str',
        'reason': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'expire_time': 'str',
        'is_need_billing': 'bool',
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'job_id': 'job_id',
        'transfer_type': 'transfer_type',
        'transfer_assets': 'transfer_assets',
        'state': 'state',
        'src_project_id': 'src_project_id',
        'dest_project_id': 'dest_project_id',
        'memo': 'memo',
        'reason': 'reason',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'expire_time': 'expire_time',
        'is_need_billing': 'is_need_billing',
        'error_info': 'error_info'
    }

    def __init__(self, job_id=None, transfer_type=None, transfer_assets=None, state=None, src_project_id=None, dest_project_id=None, memo=None, reason=None, start_time=None, finish_time=None, expire_time=None, is_need_billing=None, error_info=None):
        r"""TransferAssetJobInfo

        The model defined in huaweicloud sdk

        :param job_id: 转移资产任务ID
        :type job_id: str
        :param transfer_type: **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回
        :type transfer_type: str
        :param transfer_assets: 转移资产列表
        :type transfer_assets: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        :param state: 任务状态 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败
        :type state: str
        :param src_project_id: 源用户ID
        :type src_project_id: str
        :param dest_project_id: 目标用户ID
        :type dest_project_id: str
        :param memo: 备注信息
        :type memo: str
        :param reason: 冻结/解冻原因。
        :type reason: str
        :param start_time: 资产转移开始时间
        :type start_time: str
        :param finish_time: 资产转移完成时间
        :type finish_time: str
        :param expire_time: 资产转移过期时间
        :type expire_time: str
        :param is_need_billing: 资产转移时，是否需要从接收方扣减资源（产生计费话单）
        :type is_need_billing: bool
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._job_id = None
        self._transfer_type = None
        self._transfer_assets = None
        self._state = None
        self._src_project_id = None
        self._dest_project_id = None
        self._memo = None
        self._reason = None
        self._start_time = None
        self._finish_time = None
        self._expire_time = None
        self._is_need_billing = None
        self._error_info = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if transfer_type is not None:
            self.transfer_type = transfer_type
        if transfer_assets is not None:
            self.transfer_assets = transfer_assets
        if state is not None:
            self.state = state
        if src_project_id is not None:
            self.src_project_id = src_project_id
        if dest_project_id is not None:
            self.dest_project_id = dest_project_id
        if memo is not None:
            self.memo = memo
        if reason is not None:
            self.reason = reason
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if expire_time is not None:
            self.expire_time = expire_time
        if is_need_billing is not None:
            self.is_need_billing = is_need_billing
        if error_info is not None:
            self.error_info = error_info

    @property
    def job_id(self):
        r"""Gets the job_id of this TransferAssetJobInfo.

        转移资产任务ID

        :return: The job_id of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TransferAssetJobInfo.

        转移资产任务ID

        :param job_id: The job_id of this TransferAssetJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this TransferAssetJobInfo.

        **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回

        :return: The transfer_type of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this TransferAssetJobInfo.

        **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回

        :param transfer_type: The transfer_type of this TransferAssetJobInfo.
        :type transfer_type: str
        """
        self._transfer_type = transfer_type

    @property
    def transfer_assets(self):
        r"""Gets the transfer_assets of this TransferAssetJobInfo.

        转移资产列表

        :return: The transfer_assets of this TransferAssetJobInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        """
        return self._transfer_assets

    @transfer_assets.setter
    def transfer_assets(self, transfer_assets):
        r"""Sets the transfer_assets of this TransferAssetJobInfo.

        转移资产列表

        :param transfer_assets: The transfer_assets of this TransferAssetJobInfo.
        :type transfer_assets: list[:class:`huaweicloudsdkmetastudio.v1.DigitalAssetSummary`]
        """
        self._transfer_assets = transfer_assets

    @property
    def state(self):
        r"""Gets the state of this TransferAssetJobInfo.

        任务状态 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败

        :return: The state of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TransferAssetJobInfo.

        任务状态 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败

        :param state: The state of this TransferAssetJobInfo.
        :type state: str
        """
        self._state = state

    @property
    def src_project_id(self):
        r"""Gets the src_project_id of this TransferAssetJobInfo.

        源用户ID

        :return: The src_project_id of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._src_project_id

    @src_project_id.setter
    def src_project_id(self, src_project_id):
        r"""Sets the src_project_id of this TransferAssetJobInfo.

        源用户ID

        :param src_project_id: The src_project_id of this TransferAssetJobInfo.
        :type src_project_id: str
        """
        self._src_project_id = src_project_id

    @property
    def dest_project_id(self):
        r"""Gets the dest_project_id of this TransferAssetJobInfo.

        目标用户ID

        :return: The dest_project_id of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._dest_project_id

    @dest_project_id.setter
    def dest_project_id(self, dest_project_id):
        r"""Sets the dest_project_id of this TransferAssetJobInfo.

        目标用户ID

        :param dest_project_id: The dest_project_id of this TransferAssetJobInfo.
        :type dest_project_id: str
        """
        self._dest_project_id = dest_project_id

    @property
    def memo(self):
        r"""Gets the memo of this TransferAssetJobInfo.

        备注信息

        :return: The memo of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this TransferAssetJobInfo.

        备注信息

        :param memo: The memo of this TransferAssetJobInfo.
        :type memo: str
        """
        self._memo = memo

    @property
    def reason(self):
        r"""Gets the reason of this TransferAssetJobInfo.

        冻结/解冻原因。

        :return: The reason of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this TransferAssetJobInfo.

        冻结/解冻原因。

        :param reason: The reason of this TransferAssetJobInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def start_time(self):
        r"""Gets the start_time of this TransferAssetJobInfo.

        资产转移开始时间

        :return: The start_time of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TransferAssetJobInfo.

        资产转移开始时间

        :param start_time: The start_time of this TransferAssetJobInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this TransferAssetJobInfo.

        资产转移完成时间

        :return: The finish_time of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this TransferAssetJobInfo.

        资产转移完成时间

        :param finish_time: The finish_time of this TransferAssetJobInfo.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this TransferAssetJobInfo.

        资产转移过期时间

        :return: The expire_time of this TransferAssetJobInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this TransferAssetJobInfo.

        资产转移过期时间

        :param expire_time: The expire_time of this TransferAssetJobInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def is_need_billing(self):
        r"""Gets the is_need_billing of this TransferAssetJobInfo.

        资产转移时，是否需要从接收方扣减资源（产生计费话单）

        :return: The is_need_billing of this TransferAssetJobInfo.
        :rtype: bool
        """
        return self._is_need_billing

    @is_need_billing.setter
    def is_need_billing(self, is_need_billing):
        r"""Sets the is_need_billing of this TransferAssetJobInfo.

        资产转移时，是否需要从接收方扣减资源（产生计费话单）

        :param is_need_billing: The is_need_billing of this TransferAssetJobInfo.
        :type is_need_billing: bool
        """
        self._is_need_billing = is_need_billing

    @property
    def error_info(self):
        r"""Gets the error_info of this TransferAssetJobInfo.

        :return: The error_info of this TransferAssetJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this TransferAssetJobInfo.

        :param error_info: The error_info of this TransferAssetJobInfo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

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
        if not isinstance(other, TransferAssetJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
