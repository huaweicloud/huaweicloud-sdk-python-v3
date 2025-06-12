# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResizeVolumesResponse(SdkResponse):

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
        'order_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'order_id': 'order_id'
    }

    def __init__(self, job_id=None, order_id=None):
        r"""BatchResizeVolumesResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID，云硬盘为按需计费时返回该参数。 &gt; 说明： &gt;  &gt; 如果需要查询job的状态，请参考：\&quot;[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\&quot;。
        :type job_id: str
        :param order_id: 订单ID，云硬盘为包周期计费时返回该参数。 &gt; 说明： &gt;  &gt; - 如果您需要支付订单，请参考：\&quot;[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\&quot;。
        :type order_id: str
        """
        
        super(BatchResizeVolumesResponse, self).__init__()

        self._job_id = None
        self._order_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchResizeVolumesResponse.

        任务ID，云硬盘为按需计费时返回该参数。 > 说明： >  > 如果需要查询job的状态，请参考：\"[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\"。

        :return: The job_id of this BatchResizeVolumesResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchResizeVolumesResponse.

        任务ID，云硬盘为按需计费时返回该参数。 > 说明： >  > 如果需要查询job的状态，请参考：\"[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\"。

        :param job_id: The job_id of this BatchResizeVolumesResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this BatchResizeVolumesResponse.

        订单ID，云硬盘为包周期计费时返回该参数。 > 说明： >  > - 如果您需要支付订单，请参考：\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。

        :return: The order_id of this BatchResizeVolumesResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this BatchResizeVolumesResponse.

        订单ID，云硬盘为包周期计费时返回该参数。 > 说明： >  > - 如果您需要支付订单，请参考：\"[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\"。

        :param order_id: The order_id of this BatchResizeVolumesResponse.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, BatchResizeVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
