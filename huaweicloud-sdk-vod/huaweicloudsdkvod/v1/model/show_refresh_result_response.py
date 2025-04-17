# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRefreshResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'refresh_results': 'list[RefreshResult]'
    }

    attribute_map = {
        'refresh_results': 'refresh_results'
    }

    def __init__(self, refresh_results=None):
        r"""ShowRefreshResultResponse

        The model defined in huaweicloud sdk

        :param refresh_results: 刷新任务结果
        :type refresh_results: list[:class:`huaweicloudsdkvod.v1.RefreshResult`]
        """
        
        super(ShowRefreshResultResponse, self).__init__()

        self._refresh_results = None
        self.discriminator = None

        if refresh_results is not None:
            self.refresh_results = refresh_results

    @property
    def refresh_results(self):
        r"""Gets the refresh_results of this ShowRefreshResultResponse.

        刷新任务结果

        :return: The refresh_results of this ShowRefreshResultResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.RefreshResult`]
        """
        return self._refresh_results

    @refresh_results.setter
    def refresh_results(self, refresh_results):
        r"""Sets the refresh_results of this ShowRefreshResultResponse.

        刷新任务结果

        :param refresh_results: The refresh_results of this ShowRefreshResultResponse.
        :type refresh_results: list[:class:`huaweicloudsdkvod.v1.RefreshResult`]
        """
        self._refresh_results = refresh_results

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
        if not isinstance(other, ShowRefreshResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
