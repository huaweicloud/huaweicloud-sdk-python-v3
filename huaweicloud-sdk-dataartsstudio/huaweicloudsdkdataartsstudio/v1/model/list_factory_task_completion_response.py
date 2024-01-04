# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryTaskCompletionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'yesterday': 'list[ListFactoryTaskCompletionResYesterday]',
        'average': 'list[ListFactoryTaskCompletionResAverage]',
        'today': 'list[ListFactoryTaskCompletionResToday]'
    }

    attribute_map = {
        'yesterday': 'yesterday',
        'average': 'average',
        'today': 'today'
    }

    def __init__(self, yesterday=None, average=None, today=None):
        """ListFactoryTaskCompletionResponse

        The model defined in huaweicloud sdk

        :param yesterday: 昨天的任务信息
        :type yesterday: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResYesterday`]
        :param average: 近7天的平均任务信息
        :type average: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResAverage`]
        :param today: 当天的任务信息
        :type today: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResToday`]
        """
        
        super(ListFactoryTaskCompletionResponse, self).__init__()

        self._yesterday = None
        self._average = None
        self._today = None
        self.discriminator = None

        if yesterday is not None:
            self.yesterday = yesterday
        if average is not None:
            self.average = average
        if today is not None:
            self.today = today

    @property
    def yesterday(self):
        """Gets the yesterday of this ListFactoryTaskCompletionResponse.

        昨天的任务信息

        :return: The yesterday of this ListFactoryTaskCompletionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResYesterday`]
        """
        return self._yesterday

    @yesterday.setter
    def yesterday(self, yesterday):
        """Sets the yesterday of this ListFactoryTaskCompletionResponse.

        昨天的任务信息

        :param yesterday: The yesterday of this ListFactoryTaskCompletionResponse.
        :type yesterday: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResYesterday`]
        """
        self._yesterday = yesterday

    @property
    def average(self):
        """Gets the average of this ListFactoryTaskCompletionResponse.

        近7天的平均任务信息

        :return: The average of this ListFactoryTaskCompletionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResAverage`]
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this ListFactoryTaskCompletionResponse.

        近7天的平均任务信息

        :param average: The average of this ListFactoryTaskCompletionResponse.
        :type average: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResAverage`]
        """
        self._average = average

    @property
    def today(self):
        """Gets the today of this ListFactoryTaskCompletionResponse.

        当天的任务信息

        :return: The today of this ListFactoryTaskCompletionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResToday`]
        """
        return self._today

    @today.setter
    def today(self, today):
        """Sets the today of this ListFactoryTaskCompletionResponse.

        当天的任务信息

        :param today: The today of this ListFactoryTaskCompletionResponse.
        :type today: list[:class:`huaweicloudsdkdataartsstudio.v1.ListFactoryTaskCompletionResToday`]
        """
        self._today = today

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
        if not isinstance(other, ListFactoryTaskCompletionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
