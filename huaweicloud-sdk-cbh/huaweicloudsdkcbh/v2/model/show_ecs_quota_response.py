# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEcsQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_v6': 'str',
        'status': 'str'
    }

    attribute_map = {
        'status_v6': 'status_v6',
        'status': 'status'
    }

    def __init__(self, status_v6=None, status=None):
        """ShowEcsQuotaResponse

        The model defined in huaweicloud sdk

        :param status_v6: 支持IPv6云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用
        :type status_v6: str
        :param status: 云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用
        :type status: str
        """
        
        super(ShowEcsQuotaResponse, self).__init__()

        self._status_v6 = None
        self._status = None
        self.discriminator = None

        if status_v6 is not None:
            self.status_v6 = status_v6
        if status is not None:
            self.status = status

    @property
    def status_v6(self):
        """Gets the status_v6 of this ShowEcsQuotaResponse.

        支持IPv6云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用

        :return: The status_v6 of this ShowEcsQuotaResponse.
        :rtype: str
        """
        return self._status_v6

    @status_v6.setter
    def status_v6(self, status_v6):
        """Sets the status_v6 of this ShowEcsQuotaResponse.

        支持IPv6云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用

        :param status_v6: The status_v6 of this ShowEcsQuotaResponse.
        :type status_v6: str
        """
        self._status_v6 = status_v6

    @property
    def status(self):
        """Gets the status of this ShowEcsQuotaResponse.

        云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用

        :return: The status of this ShowEcsQuotaResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEcsQuotaResponse.

        云堡垒机实例规格资源状态。 - sellout：售罄 - normal：正常商用

        :param status: The status of this ShowEcsQuotaResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowEcsQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
