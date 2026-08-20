# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewUpdateBodyV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_status': 'str',
        'status': 'str',
        'plan_end_date': 'str'
    }

    attribute_map = {
        'old_status': 'old_status',
        'status': 'status',
        'plan_end_date': 'plan_end_date'
    }

    def __init__(self, old_status=None, status=None, plan_end_date=None):
        r"""ReviewUpdateBodyV2

        The model defined in huaweicloud sdk

        :param old_status: 评审单更新前状态。 0~32个字符。
        :type old_status: str
        :param status: 评审单目标流转状态。 0~32个字符。
        :type status: str
        :param plan_end_date: 计划完成时间，unix时间戳，单位：毫秒，示例：\&quot;1759420799999\&quot;。
        :type plan_end_date: str
        """
        
        

        self._old_status = None
        self._status = None
        self._plan_end_date = None
        self.discriminator = None

        if old_status is not None:
            self.old_status = old_status
        if status is not None:
            self.status = status
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date

    @property
    def old_status(self):
        r"""Gets the old_status of this ReviewUpdateBodyV2.

        评审单更新前状态。 0~32个字符。

        :return: The old_status of this ReviewUpdateBodyV2.
        :rtype: str
        """
        return self._old_status

    @old_status.setter
    def old_status(self, old_status):
        r"""Sets the old_status of this ReviewUpdateBodyV2.

        评审单更新前状态。 0~32个字符。

        :param old_status: The old_status of this ReviewUpdateBodyV2.
        :type old_status: str
        """
        self._old_status = old_status

    @property
    def status(self):
        r"""Gets the status of this ReviewUpdateBodyV2.

        评审单目标流转状态。 0~32个字符。

        :return: The status of this ReviewUpdateBodyV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReviewUpdateBodyV2.

        评审单目标流转状态。 0~32个字符。

        :param status: The status of this ReviewUpdateBodyV2.
        :type status: str
        """
        self._status = status

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this ReviewUpdateBodyV2.

        计划完成时间，unix时间戳，单位：毫秒，示例：\"1759420799999\"。

        :return: The plan_end_date of this ReviewUpdateBodyV2.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this ReviewUpdateBodyV2.

        计划完成时间，unix时间戳，单位：毫秒，示例：\"1759420799999\"。

        :param plan_end_date: The plan_end_date of this ReviewUpdateBodyV2.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

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
        if not isinstance(other, ReviewUpdateBodyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
