# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisReportResp:

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
        'creat_at': 'int',
        'abnormal_item_sum': 'int',
        'faulted_node_sum': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'group_name': 'group_name',
        'consumer_nums': 'consumer_nums',
        'status': 'status',
        'creat_at': 'creat_at',
        'abnormal_item_sum': 'abnormal_item_sum',
        'faulted_node_sum': 'faulted_node_sum'
    }

    def __init__(self, report_id=None, group_name=None, consumer_nums=None, status=None, creat_at=None, abnormal_item_sum=None, faulted_node_sum=None):
        r"""DiagnosisReportResp

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**： 报告ID。 **取值范围**： 不涉及。
        :type report_id: str
        :param group_name: **参数解释**： 消费组名称。 **取值范围**： 不涉及。
        :type group_name: str
        :param consumer_nums: **参数解释**： 消费者数量。 **取值范围**： 不涉及。
        :type consumer_nums: int
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param creat_at: **参数解释**： 生成时间。 **取值范围**： 不涉及。
        :type creat_at: int
        :param abnormal_item_sum: **参数解释**： 异常项数量。 **取值范围**： 不涉及。
        :type abnormal_item_sum: int
        :param faulted_node_sum: **参数解释**： 异常节点数量。 **取值范围**： 不涉及。
        :type faulted_node_sum: int
        """
        
        

        self._report_id = None
        self._group_name = None
        self._consumer_nums = None
        self._status = None
        self._creat_at = None
        self._abnormal_item_sum = None
        self._faulted_node_sum = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if group_name is not None:
            self.group_name = group_name
        if consumer_nums is not None:
            self.consumer_nums = consumer_nums
        if status is not None:
            self.status = status
        if creat_at is not None:
            self.creat_at = creat_at
        if abnormal_item_sum is not None:
            self.abnormal_item_sum = abnormal_item_sum
        if faulted_node_sum is not None:
            self.faulted_node_sum = faulted_node_sum

    @property
    def report_id(self):
        r"""Gets the report_id of this DiagnosisReportResp.

        **参数解释**： 报告ID。 **取值范围**： 不涉及。

        :return: The report_id of this DiagnosisReportResp.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this DiagnosisReportResp.

        **参数解释**： 报告ID。 **取值范围**： 不涉及。

        :param report_id: The report_id of this DiagnosisReportResp.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def group_name(self):
        r"""Gets the group_name of this DiagnosisReportResp.

        **参数解释**： 消费组名称。 **取值范围**： 不涉及。

        :return: The group_name of this DiagnosisReportResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DiagnosisReportResp.

        **参数解释**： 消费组名称。 **取值范围**： 不涉及。

        :param group_name: The group_name of this DiagnosisReportResp.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def consumer_nums(self):
        r"""Gets the consumer_nums of this DiagnosisReportResp.

        **参数解释**： 消费者数量。 **取值范围**： 不涉及。

        :return: The consumer_nums of this DiagnosisReportResp.
        :rtype: int
        """
        return self._consumer_nums

    @consumer_nums.setter
    def consumer_nums(self, consumer_nums):
        r"""Sets the consumer_nums of this DiagnosisReportResp.

        **参数解释**： 消费者数量。 **取值范围**： 不涉及。

        :param consumer_nums: The consumer_nums of this DiagnosisReportResp.
        :type consumer_nums: int
        """
        self._consumer_nums = consumer_nums

    @property
    def status(self):
        r"""Gets the status of this DiagnosisReportResp.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this DiagnosisReportResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DiagnosisReportResp.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this DiagnosisReportResp.
        :type status: str
        """
        self._status = status

    @property
    def creat_at(self):
        r"""Gets the creat_at of this DiagnosisReportResp.

        **参数解释**： 生成时间。 **取值范围**： 不涉及。

        :return: The creat_at of this DiagnosisReportResp.
        :rtype: int
        """
        return self._creat_at

    @creat_at.setter
    def creat_at(self, creat_at):
        r"""Sets the creat_at of this DiagnosisReportResp.

        **参数解释**： 生成时间。 **取值范围**： 不涉及。

        :param creat_at: The creat_at of this DiagnosisReportResp.
        :type creat_at: int
        """
        self._creat_at = creat_at

    @property
    def abnormal_item_sum(self):
        r"""Gets the abnormal_item_sum of this DiagnosisReportResp.

        **参数解释**： 异常项数量。 **取值范围**： 不涉及。

        :return: The abnormal_item_sum of this DiagnosisReportResp.
        :rtype: int
        """
        return self._abnormal_item_sum

    @abnormal_item_sum.setter
    def abnormal_item_sum(self, abnormal_item_sum):
        r"""Sets the abnormal_item_sum of this DiagnosisReportResp.

        **参数解释**： 异常项数量。 **取值范围**： 不涉及。

        :param abnormal_item_sum: The abnormal_item_sum of this DiagnosisReportResp.
        :type abnormal_item_sum: int
        """
        self._abnormal_item_sum = abnormal_item_sum

    @property
    def faulted_node_sum(self):
        r"""Gets the faulted_node_sum of this DiagnosisReportResp.

        **参数解释**： 异常节点数量。 **取值范围**： 不涉及。

        :return: The faulted_node_sum of this DiagnosisReportResp.
        :rtype: int
        """
        return self._faulted_node_sum

    @faulted_node_sum.setter
    def faulted_node_sum(self, faulted_node_sum):
        r"""Sets the faulted_node_sum of this DiagnosisReportResp.

        **参数解释**： 异常节点数量。 **取值范围**： 不涉及。

        :param faulted_node_sum: The faulted_node_sum of this DiagnosisReportResp.
        :type faulted_node_sum: int
        """
        self._faulted_node_sum = faulted_node_sum

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
        if not isinstance(other, DiagnosisReportResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
