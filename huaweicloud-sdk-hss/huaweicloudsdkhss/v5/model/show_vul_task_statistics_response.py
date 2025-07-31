# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulTaskStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unread_task_num': 'int'
    }

    attribute_map = {
        'unread_task_num': 'unread_task_num'
    }

    def __init__(self, unread_task_num=None):
        r"""ShowVulTaskStatisticsResponse

        The model defined in huaweicloud sdk

        :param unread_task_num: 未读的已完成的任务
        :type unread_task_num: int
        """
        
        super(ShowVulTaskStatisticsResponse, self).__init__()

        self._unread_task_num = None
        self.discriminator = None

        if unread_task_num is not None:
            self.unread_task_num = unread_task_num

    @property
    def unread_task_num(self):
        r"""Gets the unread_task_num of this ShowVulTaskStatisticsResponse.

        未读的已完成的任务

        :return: The unread_task_num of this ShowVulTaskStatisticsResponse.
        :rtype: int
        """
        return self._unread_task_num

    @unread_task_num.setter
    def unread_task_num(self, unread_task_num):
        r"""Sets the unread_task_num of this ShowVulTaskStatisticsResponse.

        未读的已完成的任务

        :param unread_task_num: The unread_task_num of this ShowVulTaskStatisticsResponse.
        :type unread_task_num: int
        """
        self._unread_task_num = unread_task_num

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
        if not isinstance(other, ShowVulTaskStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
