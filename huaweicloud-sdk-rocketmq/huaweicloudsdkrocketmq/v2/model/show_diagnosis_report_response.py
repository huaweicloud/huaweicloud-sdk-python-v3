# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'group_name': 'str',
        'consumer_nums': 'int',
        'status': 'str',
        'created_at': 'int',
        'abnormal_item_sum': 'int',
        'faulted_node_sum': 'int',
        'online': 'bool',
        'message_accumulation': 'int',
        'subscription_consistency': 'bool',
        'duplicate_client_id': 'bool',
        'different_consumer_type': 'bool',
        'subscriptions': 'list[SubscriptionEntity]',
        'diagnosis_node_report_list': 'list[DiagnosisNodeReportEntity]'
    }

    attribute_map = {
        'report_id': 'report_id',
        'group_name': 'group_name',
        'consumer_nums': 'consumer_nums',
        'status': 'status',
        'created_at': 'created_at',
        'abnormal_item_sum': 'abnormal_item_sum',
        'faulted_node_sum': 'faulted_node_sum',
        'online': 'online',
        'message_accumulation': 'message_accumulation',
        'subscription_consistency': 'subscription_consistency',
        'duplicate_client_id': 'duplicate_client_id',
        'different_consumer_type': 'different_consumer_type',
        'subscriptions': 'subscriptions',
        'diagnosis_node_report_list': 'diagnosis_node_report_list'
    }

    def __init__(self, report_id=None, group_name=None, consumer_nums=None, status=None, created_at=None, abnormal_item_sum=None, faulted_node_sum=None, online=None, message_accumulation=None, subscription_consistency=None, duplicate_client_id=None, different_consumer_type=None, subscriptions=None, diagnosis_node_report_list=None):
        r"""ShowDiagnosisReportResponse

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**： 报告ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type report_id: str
        :param group_name: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group_name: str
        :param consumer_nums: **参数解释**： 消费者数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type consumer_nums: int
        :param status: **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： - diagnosing：诊断中。 - failed：诊断失败。 - deleted：手动删除。 - finished：诊断完成。 - normal：诊断结果正常。 - abnormal：诊断结果异常。 **默认取值**： 不涉及。
        :type status: str
        :param created_at: **参数解释**： 生成时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type created_at: int
        :param abnormal_item_sum: **参数解释**： 异常项数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type abnormal_item_sum: int
        :param faulted_node_sum: **参数解释**： 异常节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type faulted_node_sum: int
        :param online: **参数解释**： 是否在线。 **取值范围**： - True：在线。 - False：不在线。
        :type online: bool
        :param message_accumulation: **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type message_accumulation: int
        :param subscription_consistency: **参数解释**： 订阅一致性。 **约束限制**： 不涉及。 **取值范围**： - True：订阅关系一致。 - False：订阅关系不一致。 **默认取值**： 不涉及。
        :type subscription_consistency: bool
        :param duplicate_client_id: **参数解释**： 是否存在重复的客户端ID。 **约束限制**： 不涉及。 **取值范围**： - True：存在重复的客户端ID。 - False：不存在重复的客户端ID。 **默认取值**： 不涉及。
        :type duplicate_client_id: bool
        :param different_consumer_type: **参数解释**： 是否存在不一致的消费类型。 **约束限制**： 不涉及。 **取值范围**： - True：存在不一致的消费类型。 - False：不存在不一致的消费类型。 **默认取值**： 不涉及。
        :type different_consumer_type: bool
        :param subscriptions: **参数解释**： 订阅者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type subscriptions: list[:class:`huaweicloudsdkrocketmq.v2.SubscriptionEntity`]
        :param diagnosis_node_report_list: **参数解释**： 诊断节点报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type diagnosis_node_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisNodeReportEntity`]
        """
        
        super().__init__()

        self._report_id = None
        self._group_name = None
        self._consumer_nums = None
        self._status = None
        self._created_at = None
        self._abnormal_item_sum = None
        self._faulted_node_sum = None
        self._online = None
        self._message_accumulation = None
        self._subscription_consistency = None
        self._duplicate_client_id = None
        self._different_consumer_type = None
        self._subscriptions = None
        self._diagnosis_node_report_list = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if group_name is not None:
            self.group_name = group_name
        if consumer_nums is not None:
            self.consumer_nums = consumer_nums
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if abnormal_item_sum is not None:
            self.abnormal_item_sum = abnormal_item_sum
        if faulted_node_sum is not None:
            self.faulted_node_sum = faulted_node_sum
        if online is not None:
            self.online = online
        if message_accumulation is not None:
            self.message_accumulation = message_accumulation
        if subscription_consistency is not None:
            self.subscription_consistency = subscription_consistency
        if duplicate_client_id is not None:
            self.duplicate_client_id = duplicate_client_id
        if different_consumer_type is not None:
            self.different_consumer_type = different_consumer_type
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if diagnosis_node_report_list is not None:
            self.diagnosis_node_report_list = diagnosis_node_report_list

    @property
    def report_id(self):
        r"""Gets the report_id of this ShowDiagnosisReportResponse.

        **参数解释**： 报告ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The report_id of this ShowDiagnosisReportResponse.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ShowDiagnosisReportResponse.

        **参数解释**： 报告ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param report_id: The report_id of this ShowDiagnosisReportResponse.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowDiagnosisReportResponse.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group_name of this ShowDiagnosisReportResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowDiagnosisReportResponse.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group_name: The group_name of this ShowDiagnosisReportResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def consumer_nums(self):
        r"""Gets the consumer_nums of this ShowDiagnosisReportResponse.

        **参数解释**： 消费者数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The consumer_nums of this ShowDiagnosisReportResponse.
        :rtype: int
        """
        return self._consumer_nums

    @consumer_nums.setter
    def consumer_nums(self, consumer_nums):
        r"""Sets the consumer_nums of this ShowDiagnosisReportResponse.

        **参数解释**： 消费者数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param consumer_nums: The consumer_nums of this ShowDiagnosisReportResponse.
        :type consumer_nums: int
        """
        self._consumer_nums = consumer_nums

    @property
    def status(self):
        r"""Gets the status of this ShowDiagnosisReportResponse.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： - diagnosing：诊断中。 - failed：诊断失败。 - deleted：手动删除。 - finished：诊断完成。 - normal：诊断结果正常。 - abnormal：诊断结果异常。 **默认取值**： 不涉及。

        :return: The status of this ShowDiagnosisReportResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDiagnosisReportResponse.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： - diagnosing：诊断中。 - failed：诊断失败。 - deleted：手动删除。 - finished：诊断完成。 - normal：诊断结果正常。 - abnormal：诊断结果异常。 **默认取值**： 不涉及。

        :param status: The status of this ShowDiagnosisReportResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowDiagnosisReportResponse.

        **参数解释**： 生成时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The created_at of this ShowDiagnosisReportResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowDiagnosisReportResponse.

        **参数解释**： 生成时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param created_at: The created_at of this ShowDiagnosisReportResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def abnormal_item_sum(self):
        r"""Gets the abnormal_item_sum of this ShowDiagnosisReportResponse.

        **参数解释**： 异常项数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The abnormal_item_sum of this ShowDiagnosisReportResponse.
        :rtype: int
        """
        return self._abnormal_item_sum

    @abnormal_item_sum.setter
    def abnormal_item_sum(self, abnormal_item_sum):
        r"""Sets the abnormal_item_sum of this ShowDiagnosisReportResponse.

        **参数解释**： 异常项数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param abnormal_item_sum: The abnormal_item_sum of this ShowDiagnosisReportResponse.
        :type abnormal_item_sum: int
        """
        self._abnormal_item_sum = abnormal_item_sum

    @property
    def faulted_node_sum(self):
        r"""Gets the faulted_node_sum of this ShowDiagnosisReportResponse.

        **参数解释**： 异常节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The faulted_node_sum of this ShowDiagnosisReportResponse.
        :rtype: int
        """
        return self._faulted_node_sum

    @faulted_node_sum.setter
    def faulted_node_sum(self, faulted_node_sum):
        r"""Sets the faulted_node_sum of this ShowDiagnosisReportResponse.

        **参数解释**： 异常节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param faulted_node_sum: The faulted_node_sum of this ShowDiagnosisReportResponse.
        :type faulted_node_sum: int
        """
        self._faulted_node_sum = faulted_node_sum

    @property
    def online(self):
        r"""Gets the online of this ShowDiagnosisReportResponse.

        **参数解释**： 是否在线。 **取值范围**： - True：在线。 - False：不在线。

        :return: The online of this ShowDiagnosisReportResponse.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        r"""Sets the online of this ShowDiagnosisReportResponse.

        **参数解释**： 是否在线。 **取值范围**： - True：在线。 - False：不在线。

        :param online: The online of this ShowDiagnosisReportResponse.
        :type online: bool
        """
        self._online = online

    @property
    def message_accumulation(self):
        r"""Gets the message_accumulation of this ShowDiagnosisReportResponse.

        **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The message_accumulation of this ShowDiagnosisReportResponse.
        :rtype: int
        """
        return self._message_accumulation

    @message_accumulation.setter
    def message_accumulation(self, message_accumulation):
        r"""Sets the message_accumulation of this ShowDiagnosisReportResponse.

        **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param message_accumulation: The message_accumulation of this ShowDiagnosisReportResponse.
        :type message_accumulation: int
        """
        self._message_accumulation = message_accumulation

    @property
    def subscription_consistency(self):
        r"""Gets the subscription_consistency of this ShowDiagnosisReportResponse.

        **参数解释**： 订阅一致性。 **约束限制**： 不涉及。 **取值范围**： - True：订阅关系一致。 - False：订阅关系不一致。 **默认取值**： 不涉及。

        :return: The subscription_consistency of this ShowDiagnosisReportResponse.
        :rtype: bool
        """
        return self._subscription_consistency

    @subscription_consistency.setter
    def subscription_consistency(self, subscription_consistency):
        r"""Sets the subscription_consistency of this ShowDiagnosisReportResponse.

        **参数解释**： 订阅一致性。 **约束限制**： 不涉及。 **取值范围**： - True：订阅关系一致。 - False：订阅关系不一致。 **默认取值**： 不涉及。

        :param subscription_consistency: The subscription_consistency of this ShowDiagnosisReportResponse.
        :type subscription_consistency: bool
        """
        self._subscription_consistency = subscription_consistency

    @property
    def duplicate_client_id(self):
        r"""Gets the duplicate_client_id of this ShowDiagnosisReportResponse.

        **参数解释**： 是否存在重复的客户端ID。 **约束限制**： 不涉及。 **取值范围**： - True：存在重复的客户端ID。 - False：不存在重复的客户端ID。 **默认取值**： 不涉及。

        :return: The duplicate_client_id of this ShowDiagnosisReportResponse.
        :rtype: bool
        """
        return self._duplicate_client_id

    @duplicate_client_id.setter
    def duplicate_client_id(self, duplicate_client_id):
        r"""Sets the duplicate_client_id of this ShowDiagnosisReportResponse.

        **参数解释**： 是否存在重复的客户端ID。 **约束限制**： 不涉及。 **取值范围**： - True：存在重复的客户端ID。 - False：不存在重复的客户端ID。 **默认取值**： 不涉及。

        :param duplicate_client_id: The duplicate_client_id of this ShowDiagnosisReportResponse.
        :type duplicate_client_id: bool
        """
        self._duplicate_client_id = duplicate_client_id

    @property
    def different_consumer_type(self):
        r"""Gets the different_consumer_type of this ShowDiagnosisReportResponse.

        **参数解释**： 是否存在不一致的消费类型。 **约束限制**： 不涉及。 **取值范围**： - True：存在不一致的消费类型。 - False：不存在不一致的消费类型。 **默认取值**： 不涉及。

        :return: The different_consumer_type of this ShowDiagnosisReportResponse.
        :rtype: bool
        """
        return self._different_consumer_type

    @different_consumer_type.setter
    def different_consumer_type(self, different_consumer_type):
        r"""Sets the different_consumer_type of this ShowDiagnosisReportResponse.

        **参数解释**： 是否存在不一致的消费类型。 **约束限制**： 不涉及。 **取值范围**： - True：存在不一致的消费类型。 - False：不存在不一致的消费类型。 **默认取值**： 不涉及。

        :param different_consumer_type: The different_consumer_type of this ShowDiagnosisReportResponse.
        :type different_consumer_type: bool
        """
        self._different_consumer_type = different_consumer_type

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this ShowDiagnosisReportResponse.

        **参数解释**： 订阅者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The subscriptions of this ShowDiagnosisReportResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.SubscriptionEntity`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this ShowDiagnosisReportResponse.

        **参数解释**： 订阅者列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param subscriptions: The subscriptions of this ShowDiagnosisReportResponse.
        :type subscriptions: list[:class:`huaweicloudsdkrocketmq.v2.SubscriptionEntity`]
        """
        self._subscriptions = subscriptions

    @property
    def diagnosis_node_report_list(self):
        r"""Gets the diagnosis_node_report_list of this ShowDiagnosisReportResponse.

        **参数解释**： 诊断节点报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The diagnosis_node_report_list of this ShowDiagnosisReportResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisNodeReportEntity`]
        """
        return self._diagnosis_node_report_list

    @diagnosis_node_report_list.setter
    def diagnosis_node_report_list(self, diagnosis_node_report_list):
        r"""Sets the diagnosis_node_report_list of this ShowDiagnosisReportResponse.

        **参数解释**： 诊断节点报告列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param diagnosis_node_report_list: The diagnosis_node_report_list of this ShowDiagnosisReportResponse.
        :type diagnosis_node_report_list: list[:class:`huaweicloudsdkrocketmq.v2.DiagnosisNodeReportEntity`]
        """
        self._diagnosis_node_report_list = diagnosis_node_report_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowDiagnosisReportResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDiagnosisReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
