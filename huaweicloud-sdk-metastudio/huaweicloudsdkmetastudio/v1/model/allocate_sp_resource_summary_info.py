# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllocateSpResourceSummaryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'resource_num': 'float',
        'resource_used_num': 'float',
        'resource_remind_quota': 'float'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'resource_num': 'resource_num',
        'resource_used_num': 'resource_used_num',
        'resource_remind_quota': 'resource_remind_quota'
    }

    def __init__(self, resource_spec_code=None, resource_num=None, resource_used_num=None, resource_remind_quota=None):
        r"""AllocateSpResourceSummaryInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param resource_num: 资源数量。
        :type resource_num: float
        :param resource_used_num: 资源已使用数量。
        :type resource_used_num: float
        :param resource_remind_quota: 资源在TMS上的剩余量
        :type resource_remind_quota: float
        """
        
        

        self._resource_spec_code = None
        self._resource_num = None
        self._resource_used_num = None
        self._resource_remind_quota = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_num is not None:
            self.resource_num = resource_num
        if resource_used_num is not None:
            self.resource_used_num = resource_used_num
        if resource_remind_quota is not None:
            self.resource_remind_quota = resource_remind_quota

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this AllocateSpResourceSummaryInfo.

        资源规格编码

        :return: The resource_spec_code of this AllocateSpResourceSummaryInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this AllocateSpResourceSummaryInfo.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this AllocateSpResourceSummaryInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_num(self):
        r"""Gets the resource_num of this AllocateSpResourceSummaryInfo.

        资源数量。

        :return: The resource_num of this AllocateSpResourceSummaryInfo.
        :rtype: float
        """
        return self._resource_num

    @resource_num.setter
    def resource_num(self, resource_num):
        r"""Sets the resource_num of this AllocateSpResourceSummaryInfo.

        资源数量。

        :param resource_num: The resource_num of this AllocateSpResourceSummaryInfo.
        :type resource_num: float
        """
        self._resource_num = resource_num

    @property
    def resource_used_num(self):
        r"""Gets the resource_used_num of this AllocateSpResourceSummaryInfo.

        资源已使用数量。

        :return: The resource_used_num of this AllocateSpResourceSummaryInfo.
        :rtype: float
        """
        return self._resource_used_num

    @resource_used_num.setter
    def resource_used_num(self, resource_used_num):
        r"""Sets the resource_used_num of this AllocateSpResourceSummaryInfo.

        资源已使用数量。

        :param resource_used_num: The resource_used_num of this AllocateSpResourceSummaryInfo.
        :type resource_used_num: float
        """
        self._resource_used_num = resource_used_num

    @property
    def resource_remind_quota(self):
        r"""Gets the resource_remind_quota of this AllocateSpResourceSummaryInfo.

        资源在TMS上的剩余量

        :return: The resource_remind_quota of this AllocateSpResourceSummaryInfo.
        :rtype: float
        """
        return self._resource_remind_quota

    @resource_remind_quota.setter
    def resource_remind_quota(self, resource_remind_quota):
        r"""Sets the resource_remind_quota of this AllocateSpResourceSummaryInfo.

        资源在TMS上的剩余量

        :param resource_remind_quota: The resource_remind_quota of this AllocateSpResourceSummaryInfo.
        :type resource_remind_quota: float
        """
        self._resource_remind_quota = resource_remind_quota

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
        if not isinstance(other, AllocateSpResourceSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
