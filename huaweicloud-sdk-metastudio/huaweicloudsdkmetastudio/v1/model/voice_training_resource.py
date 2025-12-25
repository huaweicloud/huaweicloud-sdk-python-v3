# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceTrainingResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_type': 'str',
        'resource_source': 'str',
        'asset_id': 'str',
        'resource_id': 'str',
        'resource_nums': 'int',
        'resource_available_nums': 'int',
        'resource_type': 'str',
        'charge_mode': 'str',
        'expire_time': 'str',
        'status': 'int'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'resource_source': 'resource_source',
        'asset_id': 'asset_id',
        'resource_id': 'resource_id',
        'resource_nums': 'resource_nums',
        'resource_available_nums': 'resource_available_nums',
        'resource_type': 'resource_type',
        'charge_mode': 'charge_mode',
        'expire_time': 'expire_time',
        'status': 'status'
    }

    def __init__(self, operation_type=None, resource_source=None, asset_id=None, resource_id=None, resource_nums=None, resource_available_nums=None, resource_type=None, charge_mode=None, expire_time=None, status=None):
        r"""VoiceTrainingResource

        The model defined in huaweicloud sdk

        :param operation_type: 资源操作类型。 * ADD: 新增资源 * UPDATE：更新资源 * FREEZE：停用资源 * UNFREEZE：启用资源 * REBIND: 重新绑定资源
        :type operation_type: str
        :param resource_source: 资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 &gt; * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。
        :type resource_source: str
        :param asset_id: 资产ID。
        :type asset_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_nums: 资源数量。声音模型训练个数。
        :type resource_nums: int
        :param resource_available_nums: 可用资源数量。可用声音模型训练个数。
        :type resource_available_nums: int
        :param resource_type: 资源类型。 * BASIC: 基础版 * MIDDLE: 进阶版 * ADVANCE：高级版 * THIRD_PARTY：第三方出门问问 * THIRD_PARTY_LJZN: 第三方逻辑智能 * TTS_CMWW：TTS资源 * TTS_LJZN: 逻辑智能TTS资源 * FLEXUS: Flexus版资源
        :type resource_type: str
        :param charge_mode: 资源计费类型。 * ON_DEMAND:按需计费，目前只有进阶版声音，最多制作三个任务 * PERIODIC: 包周期 * ONE_TIME：一次性计费 &gt; * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源。
        :type charge_mode: str
        :param expire_time: 资源过期时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type expire_time: str
        :param status: 资源状态
        :type status: int
        """
        
        

        self._operation_type = None
        self._resource_source = None
        self._asset_id = None
        self._resource_id = None
        self._resource_nums = None
        self._resource_available_nums = None
        self._resource_type = None
        self._charge_mode = None
        self._expire_time = None
        self._status = None
        self.discriminator = None

        if operation_type is not None:
            self.operation_type = operation_type
        if resource_source is not None:
            self.resource_source = resource_source
        if asset_id is not None:
            self.asset_id = asset_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_nums is not None:
            self.resource_nums = resource_nums
        if resource_available_nums is not None:
            self.resource_available_nums = resource_available_nums
        if resource_type is not None:
            self.resource_type = resource_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status

    @property
    def operation_type(self):
        r"""Gets the operation_type of this VoiceTrainingResource.

        资源操作类型。 * ADD: 新增资源 * UPDATE：更新资源 * FREEZE：停用资源 * UNFREEZE：启用资源 * REBIND: 重新绑定资源

        :return: The operation_type of this VoiceTrainingResource.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this VoiceTrainingResource.

        资源操作类型。 * ADD: 新增资源 * UPDATE：更新资源 * FREEZE：停用资源 * UNFREEZE：启用资源 * REBIND: 重新绑定资源

        :param operation_type: The operation_type of this VoiceTrainingResource.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def resource_source(self):
        r"""Gets the resource_source of this VoiceTrainingResource.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 > * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。

        :return: The resource_source of this VoiceTrainingResource.
        :rtype: str
        """
        return self._resource_source

    @resource_source.setter
    def resource_source(self, resource_source):
        r"""Sets the resource_source of this VoiceTrainingResource.

        资源来源。 * PURCHASED: 购买 * SP_ALLOCATED：SP分配 * ADMIN_ALLOCATED：系统管理员分配 > * 开通按需；购买按需套餐包、一次性资源、包周期等都属于PURCHASED。

        :param resource_source: The resource_source of this VoiceTrainingResource.
        :type resource_source: str
        """
        self._resource_source = resource_source

    @property
    def asset_id(self):
        r"""Gets the asset_id of this VoiceTrainingResource.

        资产ID。

        :return: The asset_id of this VoiceTrainingResource.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this VoiceTrainingResource.

        资产ID。

        :param asset_id: The asset_id of this VoiceTrainingResource.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this VoiceTrainingResource.

        资源ID。

        :return: The resource_id of this VoiceTrainingResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this VoiceTrainingResource.

        资源ID。

        :param resource_id: The resource_id of this VoiceTrainingResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_nums(self):
        r"""Gets the resource_nums of this VoiceTrainingResource.

        资源数量。声音模型训练个数。

        :return: The resource_nums of this VoiceTrainingResource.
        :rtype: int
        """
        return self._resource_nums

    @resource_nums.setter
    def resource_nums(self, resource_nums):
        r"""Sets the resource_nums of this VoiceTrainingResource.

        资源数量。声音模型训练个数。

        :param resource_nums: The resource_nums of this VoiceTrainingResource.
        :type resource_nums: int
        """
        self._resource_nums = resource_nums

    @property
    def resource_available_nums(self):
        r"""Gets the resource_available_nums of this VoiceTrainingResource.

        可用资源数量。可用声音模型训练个数。

        :return: The resource_available_nums of this VoiceTrainingResource.
        :rtype: int
        """
        return self._resource_available_nums

    @resource_available_nums.setter
    def resource_available_nums(self, resource_available_nums):
        r"""Sets the resource_available_nums of this VoiceTrainingResource.

        可用资源数量。可用声音模型训练个数。

        :param resource_available_nums: The resource_available_nums of this VoiceTrainingResource.
        :type resource_available_nums: int
        """
        self._resource_available_nums = resource_available_nums

    @property
    def resource_type(self):
        r"""Gets the resource_type of this VoiceTrainingResource.

        资源类型。 * BASIC: 基础版 * MIDDLE: 进阶版 * ADVANCE：高级版 * THIRD_PARTY：第三方出门问问 * THIRD_PARTY_LJZN: 第三方逻辑智能 * TTS_CMWW：TTS资源 * TTS_LJZN: 逻辑智能TTS资源 * FLEXUS: Flexus版资源

        :return: The resource_type of this VoiceTrainingResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this VoiceTrainingResource.

        资源类型。 * BASIC: 基础版 * MIDDLE: 进阶版 * ADVANCE：高级版 * THIRD_PARTY：第三方出门问问 * THIRD_PARTY_LJZN: 第三方逻辑智能 * TTS_CMWW：TTS资源 * TTS_LJZN: 逻辑智能TTS资源 * FLEXUS: Flexus版资源

        :param resource_type: The resource_type of this VoiceTrainingResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this VoiceTrainingResource.

        资源计费类型。 * ON_DEMAND:按需计费，目前只有进阶版声音，最多制作三个任务 * PERIODIC: 包周期 * ONE_TIME：一次性计费 > * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源。

        :return: The charge_mode of this VoiceTrainingResource.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this VoiceTrainingResource.

        资源计费类型。 * ON_DEMAND:按需计费，目前只有进阶版声音，最多制作三个任务 * PERIODIC: 包周期 * ONE_TIME：一次性计费 > * 一次性计费包括：租户订购的一次性资源，SP管理员分配给租户的一次性资源。

        :param charge_mode: The charge_mode of this VoiceTrainingResource.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def expire_time(self):
        r"""Gets the expire_time of this VoiceTrainingResource.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The expire_time of this VoiceTrainingResource.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this VoiceTrainingResource.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param expire_time: The expire_time of this VoiceTrainingResource.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def status(self):
        r"""Gets the status of this VoiceTrainingResource.

        资源状态

        :return: The status of this VoiceTrainingResource.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VoiceTrainingResource.

        资源状态

        :param status: The status of this VoiceTrainingResource.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, VoiceTrainingResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
