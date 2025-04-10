# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTopRiskInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_risk_info': 'list[TopRiskInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'top_risk_info': 'top_risk_info',
        'total_count': 'total_count'
    }

    def __init__(self, top_risk_info=None, total_count=None):
        r"""ExportTopRiskInstancesResponse

        The model defined in huaweicloud sdk

        :param top_risk_info: 风险实例列表。
        :type top_risk_info: list[:class:`huaweicloudsdkdas.v3.TopRiskInfo`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ExportTopRiskInstancesResponse, self).__init__()

        self._top_risk_info = None
        self._total_count = None
        self.discriminator = None

        if top_risk_info is not None:
            self.top_risk_info = top_risk_info
        if total_count is not None:
            self.total_count = total_count

    @property
    def top_risk_info(self):
        r"""Gets the top_risk_info of this ExportTopRiskInstancesResponse.

        风险实例列表。

        :return: The top_risk_info of this ExportTopRiskInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopRiskInfo`]
        """
        return self._top_risk_info

    @top_risk_info.setter
    def top_risk_info(self, top_risk_info):
        r"""Sets the top_risk_info of this ExportTopRiskInstancesResponse.

        风险实例列表。

        :param top_risk_info: The top_risk_info of this ExportTopRiskInstancesResponse.
        :type top_risk_info: list[:class:`huaweicloudsdkdas.v3.TopRiskInfo`]
        """
        self._top_risk_info = top_risk_info

    @property
    def total_count(self):
        r"""Gets the total_count of this ExportTopRiskInstancesResponse.

        总数。

        :return: The total_count of this ExportTopRiskInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ExportTopRiskInstancesResponse.

        总数。

        :param total_count: The total_count of this ExportTopRiskInstancesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ExportTopRiskInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
