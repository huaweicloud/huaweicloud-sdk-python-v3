# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobHistoryParametersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'parameter_history_config_list': 'list[ListJobHistoryParameter]'
    }

    attribute_map = {
        'count': 'count',
        'parameter_history_config_list': 'parameter_history_config_list'
    }

    def __init__(self, count=None, parameter_history_config_list=None):
        """ListJobHistoryParametersResponse

        The model defined in huaweicloud sdk

        :param count: 历史记录总数。
        :type count: int
        :param parameter_history_config_list: 任务参数历史修改列表
        :type parameter_history_config_list: list[:class:`huaweicloudsdkdrs.v5.ListJobHistoryParameter`]
        """
        
        super(ListJobHistoryParametersResponse, self).__init__()

        self._count = None
        self._parameter_history_config_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if parameter_history_config_list is not None:
            self.parameter_history_config_list = parameter_history_config_list

    @property
    def count(self):
        """Gets the count of this ListJobHistoryParametersResponse.

        历史记录总数。

        :return: The count of this ListJobHistoryParametersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListJobHistoryParametersResponse.

        历史记录总数。

        :param count: The count of this ListJobHistoryParametersResponse.
        :type count: int
        """
        self._count = count

    @property
    def parameter_history_config_list(self):
        """Gets the parameter_history_config_list of this ListJobHistoryParametersResponse.

        任务参数历史修改列表

        :return: The parameter_history_config_list of this ListJobHistoryParametersResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ListJobHistoryParameter`]
        """
        return self._parameter_history_config_list

    @parameter_history_config_list.setter
    def parameter_history_config_list(self, parameter_history_config_list):
        """Sets the parameter_history_config_list of this ListJobHistoryParametersResponse.

        任务参数历史修改列表

        :param parameter_history_config_list: The parameter_history_config_list of this ListJobHistoryParametersResponse.
        :type parameter_history_config_list: list[:class:`huaweicloudsdkdrs.v5.ListJobHistoryParameter`]
        """
        self._parameter_history_config_list = parameter_history_config_list

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
        if not isinstance(other, ListJobHistoryParametersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
