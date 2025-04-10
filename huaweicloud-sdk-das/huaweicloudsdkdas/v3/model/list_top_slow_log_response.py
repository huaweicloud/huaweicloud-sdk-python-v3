# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSlowLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_slow_log_list': 'list[TopSlowLogTopSlowLogList]'
    }

    attribute_map = {
        'top_slow_log_list': 'top_slow_log_list'
    }

    def __init__(self, top_slow_log_list=None):
        r"""ListTopSlowLogResponse

        The model defined in huaweicloud sdk

        :param top_slow_log_list: TOP慢SQL列表
        :type top_slow_log_list: list[:class:`huaweicloudsdkdas.v3.TopSlowLogTopSlowLogList`]
        """
        
        super(ListTopSlowLogResponse, self).__init__()

        self._top_slow_log_list = None
        self.discriminator = None

        if top_slow_log_list is not None:
            self.top_slow_log_list = top_slow_log_list

    @property
    def top_slow_log_list(self):
        r"""Gets the top_slow_log_list of this ListTopSlowLogResponse.

        TOP慢SQL列表

        :return: The top_slow_log_list of this ListTopSlowLogResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopSlowLogTopSlowLogList`]
        """
        return self._top_slow_log_list

    @top_slow_log_list.setter
    def top_slow_log_list(self, top_slow_log_list):
        r"""Sets the top_slow_log_list of this ListTopSlowLogResponse.

        TOP慢SQL列表

        :param top_slow_log_list: The top_slow_log_list of this ListTopSlowLogResponse.
        :type top_slow_log_list: list[:class:`huaweicloudsdkdas.v3.TopSlowLogTopSlowLogList`]
        """
        self._top_slow_log_list = top_slow_log_list

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
        if not isinstance(other, ListTopSlowLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
