# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobSuccessRatioResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success_count': 'int',
        'total_count': 'int',
        'success_ratio': 'float'
    }

    attribute_map = {
        'success_count': 'success_count',
        'total_count': 'total_count',
        'success_ratio': 'success_ratio'
    }

    def __init__(self, success_count=None, total_count=None, success_ratio=None):
        """ShowJobSuccessRatioResponse

        The model defined in huaweicloud sdk

        :param success_count: 任务成功构建次数
        :type success_count: int
        :param total_count: 任务构建总次数
        :type total_count: int
        :param success_ratio: 任务成功率,精确到小数点后两位
        :type success_ratio: float
        """
        
        super(ShowJobSuccessRatioResponse, self).__init__()

        self._success_count = None
        self._total_count = None
        self._success_ratio = None
        self.discriminator = None

        if success_count is not None:
            self.success_count = success_count
        if total_count is not None:
            self.total_count = total_count
        if success_ratio is not None:
            self.success_ratio = success_ratio

    @property
    def success_count(self):
        """Gets the success_count of this ShowJobSuccessRatioResponse.

        任务成功构建次数

        :return: The success_count of this ShowJobSuccessRatioResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this ShowJobSuccessRatioResponse.

        任务成功构建次数

        :param success_count: The success_count of this ShowJobSuccessRatioResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def total_count(self):
        """Gets the total_count of this ShowJobSuccessRatioResponse.

        任务构建总次数

        :return: The total_count of this ShowJobSuccessRatioResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowJobSuccessRatioResponse.

        任务构建总次数

        :param total_count: The total_count of this ShowJobSuccessRatioResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_ratio(self):
        """Gets the success_ratio of this ShowJobSuccessRatioResponse.

        任务成功率,精确到小数点后两位

        :return: The success_ratio of this ShowJobSuccessRatioResponse.
        :rtype: float
        """
        return self._success_ratio

    @success_ratio.setter
    def success_ratio(self, success_ratio):
        """Sets the success_ratio of this ShowJobSuccessRatioResponse.

        任务成功率,精确到小数点后两位

        :param success_ratio: The success_ratio of this ShowJobSuccessRatioResponse.
        :type success_ratio: float
        """
        self._success_ratio = success_ratio

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
        if not isinstance(other, ShowJobSuccessRatioResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
