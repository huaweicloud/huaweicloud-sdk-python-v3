# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceCrossVpcIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'results': 'list[UpdateInstanceCrossVpcIpRespResults]'
    }

    attribute_map = {
        'success': 'success',
        'results': 'results'
    }

    def __init__(self, success=None, results=None):
        r"""UpdateInstanceCrossVpcIpResponse

        The model defined in huaweicloud sdk

        :param success: 修改跨VPC访问结果。
        :type success: bool
        :param results: 修改broker跨VPC访问的结果列表。
        :type results: list[:class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpRespResults`]
        """
        
        super(UpdateInstanceCrossVpcIpResponse, self).__init__()

        self._success = None
        self._results = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if results is not None:
            self.results = results

    @property
    def success(self):
        r"""Gets the success of this UpdateInstanceCrossVpcIpResponse.

        修改跨VPC访问结果。

        :return: The success of this UpdateInstanceCrossVpcIpResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this UpdateInstanceCrossVpcIpResponse.

        修改跨VPC访问结果。

        :param success: The success of this UpdateInstanceCrossVpcIpResponse.
        :type success: bool
        """
        self._success = success

    @property
    def results(self):
        r"""Gets the results of this UpdateInstanceCrossVpcIpResponse.

        修改broker跨VPC访问的结果列表。

        :return: The results of this UpdateInstanceCrossVpcIpResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpRespResults`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this UpdateInstanceCrossVpcIpResponse.

        修改broker跨VPC访问的结果列表。

        :param results: The results of this UpdateInstanceCrossVpcIpResponse.
        :type results: list[:class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpRespResults`]
        """
        self._results = results

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
        if not isinstance(other, UpdateInstanceCrossVpcIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
