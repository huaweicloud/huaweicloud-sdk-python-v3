# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_list': 'list[ImportIpInfo]',
        'failed_ip_list': 'list[ImportIpInfo]',
        'failed_code': 'str',
        'failed_message': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'ip_list': 'ip_list',
        'failed_ip_list': 'failed_ip_list',
        'failed_code': 'failed_code',
        'failed_message': 'failed_message',
        'total_count': 'total_count'
    }

    def __init__(self, ip_list=None, failed_ip_list=None, failed_code=None, failed_message=None, total_count=None):
        r"""ImportIpResponse

        The model defined in huaweicloud sdk

        :param ip_list: ip成功列表。
        :type ip_list: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        :param failed_ip_list: ip失败列表。
        :type failed_ip_list: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        :param failed_code: 错误码。
        :type failed_code: str
        :param failed_message: 错误码。
        :type failed_message: str
        :param total_count: ip列表数量。
        :type total_count: int
        """
        
        super().__init__()

        self._ip_list = None
        self._failed_ip_list = None
        self._failed_code = None
        self._failed_message = None
        self._total_count = None
        self.discriminator = None

        if ip_list is not None:
            self.ip_list = ip_list
        if failed_ip_list is not None:
            self.failed_ip_list = failed_ip_list
        if failed_code is not None:
            self.failed_code = failed_code
        if failed_message is not None:
            self.failed_message = failed_message
        if total_count is not None:
            self.total_count = total_count

    @property
    def ip_list(self):
        r"""Gets the ip_list of this ImportIpResponse.

        ip成功列表。

        :return: The ip_list of this ImportIpResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this ImportIpResponse.

        ip成功列表。

        :param ip_list: The ip_list of this ImportIpResponse.
        :type ip_list: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        """
        self._ip_list = ip_list

    @property
    def failed_ip_list(self):
        r"""Gets the failed_ip_list of this ImportIpResponse.

        ip失败列表。

        :return: The failed_ip_list of this ImportIpResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        """
        return self._failed_ip_list

    @failed_ip_list.setter
    def failed_ip_list(self, failed_ip_list):
        r"""Sets the failed_ip_list of this ImportIpResponse.

        ip失败列表。

        :param failed_ip_list: The failed_ip_list of this ImportIpResponse.
        :type failed_ip_list: list[:class:`huaweicloudsdkworkspace.v2.ImportIpInfo`]
        """
        self._failed_ip_list = failed_ip_list

    @property
    def failed_code(self):
        r"""Gets the failed_code of this ImportIpResponse.

        错误码。

        :return: The failed_code of this ImportIpResponse.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        r"""Sets the failed_code of this ImportIpResponse.

        错误码。

        :param failed_code: The failed_code of this ImportIpResponse.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def failed_message(self):
        r"""Gets the failed_message of this ImportIpResponse.

        错误码。

        :return: The failed_message of this ImportIpResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this ImportIpResponse.

        错误码。

        :param failed_message: The failed_message of this ImportIpResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def total_count(self):
        r"""Gets the total_count of this ImportIpResponse.

        ip列表数量。

        :return: The total_count of this ImportIpResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ImportIpResponse.

        ip列表数量。

        :param total_count: The total_count of this ImportIpResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ImportIpResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
