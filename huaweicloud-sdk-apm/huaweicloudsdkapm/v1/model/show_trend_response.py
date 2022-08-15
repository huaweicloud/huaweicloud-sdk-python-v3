# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'line_list': 'list[FrontLine]',
        'latest_data_time': 'int'
    }

    attribute_map = {
        'line_list': 'line_list',
        'latest_data_time': 'latest_data_Time'
    }

    def __init__(self, line_list=None, latest_data_time=None):
        """ShowTrendResponse

        The model defined in huaweicloud sdk

        :param line_list: 趋势图数据列表
        :type line_list: list[:class:`huaweicloudsdkapm.v1.FrontLine`]
        :param latest_data_time: 最后日期时间
        :type latest_data_time: int
        """
        
        super(ShowTrendResponse, self).__init__()

        self._line_list = None
        self._latest_data_time = None
        self.discriminator = None

        if line_list is not None:
            self.line_list = line_list
        if latest_data_time is not None:
            self.latest_data_time = latest_data_time

    @property
    def line_list(self):
        """Gets the line_list of this ShowTrendResponse.

        趋势图数据列表

        :return: The line_list of this ShowTrendResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontLine`]
        """
        return self._line_list

    @line_list.setter
    def line_list(self, line_list):
        """Sets the line_list of this ShowTrendResponse.

        趋势图数据列表

        :param line_list: The line_list of this ShowTrendResponse.
        :type line_list: list[:class:`huaweicloudsdkapm.v1.FrontLine`]
        """
        self._line_list = line_list

    @property
    def latest_data_time(self):
        """Gets the latest_data_time of this ShowTrendResponse.

        最后日期时间

        :return: The latest_data_time of this ShowTrendResponse.
        :rtype: int
        """
        return self._latest_data_time

    @latest_data_time.setter
    def latest_data_time(self, latest_data_time):
        """Sets the latest_data_time of this ShowTrendResponse.

        最后日期时间

        :param latest_data_time: The latest_data_time of this ShowTrendResponse.
        :type latest_data_time: int
        """
        self._latest_data_time = latest_data_time

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
        if not isinstance(other, ShowTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
