# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificatesHttpsInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'https': 'list[HttpsDetail]'
    }

    attribute_map = {
        'total': 'total',
        'https': 'https'
    }

    def __init__(self, total=None, https=None):
        """ShowCertificatesHttpsInfoResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果总数
        :type total: int
        :param https: https对象。
        :type https: list[:class:`huaweicloudsdkcdn.v1.HttpsDetail`]
        """
        
        super(ShowCertificatesHttpsInfoResponse, self).__init__()

        self._total = None
        self._https = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if https is not None:
            self.https = https

    @property
    def total(self):
        """Gets the total of this ShowCertificatesHttpsInfoResponse.

        查询结果总数

        :return: The total of this ShowCertificatesHttpsInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowCertificatesHttpsInfoResponse.

        查询结果总数

        :param total: The total of this ShowCertificatesHttpsInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def https(self):
        """Gets the https of this ShowCertificatesHttpsInfoResponse.

        https对象。

        :return: The https of this ShowCertificatesHttpsInfoResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.HttpsDetail`]
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this ShowCertificatesHttpsInfoResponse.

        https对象。

        :param https: The https of this ShowCertificatesHttpsInfoResponse.
        :type https: list[:class:`huaweicloudsdkcdn.v1.HttpsDetail`]
        """
        self._https = https

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
        if not isinstance(other, ShowCertificatesHttpsInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
