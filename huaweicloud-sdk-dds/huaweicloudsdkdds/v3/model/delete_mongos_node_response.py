# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMongosNodeResponse(SdkResponse):

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
        r"""DeleteMongosNodeResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID，仅按需实例返回该参数。
        :type job_id: str
        :param order_id: 订单ID，仅包周期实例返回该参数。
        :type order_id: str
        """
        
        super(DeleteMongosNodeResponse, self).__init__()

        self._job_id = None
        self._order_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def job_id(self):
        r"""Gets the job_id of this DeleteMongosNodeResponse.

        任务ID，仅按需实例返回该参数。

        :return: The job_id of this DeleteMongosNodeResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DeleteMongosNodeResponse.

        任务ID，仅按需实例返回该参数。

        :param job_id: The job_id of this DeleteMongosNodeResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this DeleteMongosNodeResponse.

        订单ID，仅包周期实例返回该参数。

        :return: The order_id of this DeleteMongosNodeResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this DeleteMongosNodeResponse.

        订单ID，仅包周期实例返回该参数。

        :param order_id: The order_id of this DeleteMongosNodeResponse.
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
        if not isinstance(other, DeleteMongosNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
