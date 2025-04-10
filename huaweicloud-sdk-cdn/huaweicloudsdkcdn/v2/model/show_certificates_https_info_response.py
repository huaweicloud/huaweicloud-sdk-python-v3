# coding: utf-8

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
        'https': 'list[HttpsDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'https': 'https',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, total=None, https=None, x_request_id=None):
        r"""ShowCertificatesHttpsInfoResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果总数
        :type total: int
        :param https: https配置。
        :type https: list[:class:`huaweicloudsdkcdn.v2.HttpsDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowCertificatesHttpsInfoResponse, self).__init__()

        self._total = None
        self._https = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if https is not None:
            self.https = https
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ShowCertificatesHttpsInfoResponse.

        查询结果总数

        :return: The total of this ShowCertificatesHttpsInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowCertificatesHttpsInfoResponse.

        查询结果总数

        :param total: The total of this ShowCertificatesHttpsInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def https(self):
        r"""Gets the https of this ShowCertificatesHttpsInfoResponse.

        https配置。

        :return: The https of this ShowCertificatesHttpsInfoResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.HttpsDetail`]
        """
        return self._https

    @https.setter
    def https(self, https):
        r"""Sets the https of this ShowCertificatesHttpsInfoResponse.

        https配置。

        :param https: The https of this ShowCertificatesHttpsInfoResponse.
        :type https: list[:class:`huaweicloudsdkcdn.v2.HttpsDetail`]
        """
        self._https = https

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowCertificatesHttpsInfoResponse.

        :return: The x_request_id of this ShowCertificatesHttpsInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowCertificatesHttpsInfoResponse.

        :param x_request_id: The x_request_id of this ShowCertificatesHttpsInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
