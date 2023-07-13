# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunInstanceActionResponse(SdkResponse):

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
        """RunInstanceActionResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。按需实例时仅返回任务id。
        :type job_id: str
        :param order_id: 订单id。包周期实例时仅返回订单id。
        :type order_id: str
        """
        
        super(RunInstanceActionResponse, self).__init__()

        self._job_id = None
        self._order_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def job_id(self):
        """Gets the job_id of this RunInstanceActionResponse.

        任务id。按需实例时仅返回任务id。

        :return: The job_id of this RunInstanceActionResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunInstanceActionResponse.

        任务id。按需实例时仅返回任务id。

        :param job_id: The job_id of this RunInstanceActionResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        """Gets the order_id of this RunInstanceActionResponse.

        订单id。包周期实例时仅返回订单id。

        :return: The order_id of this RunInstanceActionResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RunInstanceActionResponse.

        订单id。包周期实例时仅返回订单id。

        :param order_id: The order_id of this RunInstanceActionResponse.
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
        if not isinstance(other, RunInstanceActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
