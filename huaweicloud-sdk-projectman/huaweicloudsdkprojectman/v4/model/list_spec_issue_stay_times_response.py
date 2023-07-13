# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecIssueStayTimesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fails': 'list[str]',
        'data': 'list[ListSpecIssueStayTimesResponseBodyData]',
        'total_stay_time': 'int',
        'total': 'int'
    }

    attribute_map = {
        'fails': 'fails',
        'data': 'data',
        'total_stay_time': 'total_stay_time',
        'total': 'total'
    }

    def __init__(self, fails=None, data=None, total_stay_time=None, total=None):
        """ListSpecIssueStayTimesResponse

        The model defined in huaweicloud sdk

        :param fails: 计算失败的工作项id,一般指未关闭的工作项
        :type fails: list[str]
        :param data: 工作项时间数据（创建时间-关闭时间）
        :type data: list[:class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesResponseBodyData`]
        :param total_stay_time: 停留时间求和（单位：秒）
        :type total_stay_time: int
        :param total: 停留时间求和的工作项个数
        :type total: int
        """
        
        super(ListSpecIssueStayTimesResponse, self).__init__()

        self._fails = None
        self._data = None
        self._total_stay_time = None
        self._total = None
        self.discriminator = None

        if fails is not None:
            self.fails = fails
        if data is not None:
            self.data = data
        if total_stay_time is not None:
            self.total_stay_time = total_stay_time
        if total is not None:
            self.total = total

    @property
    def fails(self):
        """Gets the fails of this ListSpecIssueStayTimesResponse.

        计算失败的工作项id,一般指未关闭的工作项

        :return: The fails of this ListSpecIssueStayTimesResponse.
        :rtype: list[str]
        """
        return self._fails

    @fails.setter
    def fails(self, fails):
        """Sets the fails of this ListSpecIssueStayTimesResponse.

        计算失败的工作项id,一般指未关闭的工作项

        :param fails: The fails of this ListSpecIssueStayTimesResponse.
        :type fails: list[str]
        """
        self._fails = fails

    @property
    def data(self):
        """Gets the data of this ListSpecIssueStayTimesResponse.

        工作项时间数据（创建时间-关闭时间）

        :return: The data of this ListSpecIssueStayTimesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesResponseBodyData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListSpecIssueStayTimesResponse.

        工作项时间数据（创建时间-关闭时间）

        :param data: The data of this ListSpecIssueStayTimesResponse.
        :type data: list[:class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesResponseBodyData`]
        """
        self._data = data

    @property
    def total_stay_time(self):
        """Gets the total_stay_time of this ListSpecIssueStayTimesResponse.

        停留时间求和（单位：秒）

        :return: The total_stay_time of this ListSpecIssueStayTimesResponse.
        :rtype: int
        """
        return self._total_stay_time

    @total_stay_time.setter
    def total_stay_time(self, total_stay_time):
        """Sets the total_stay_time of this ListSpecIssueStayTimesResponse.

        停留时间求和（单位：秒）

        :param total_stay_time: The total_stay_time of this ListSpecIssueStayTimesResponse.
        :type total_stay_time: int
        """
        self._total_stay_time = total_stay_time

    @property
    def total(self):
        """Gets the total of this ListSpecIssueStayTimesResponse.

        停留时间求和的工作项个数

        :return: The total of this ListSpecIssueStayTimesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSpecIssueStayTimesResponse.

        停留时间求和的工作项个数

        :param total: The total of this ListSpecIssueStayTimesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListSpecIssueStayTimesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
