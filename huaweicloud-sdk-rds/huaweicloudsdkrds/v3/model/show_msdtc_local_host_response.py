# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMsdtcLocalHostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'hosts': 'list[MsdtcHostResult]'
    }

    attribute_map = {
        'status': 'status',
        'hosts': 'hosts'
    }

    def __init__(self, status=None, hosts=None):
        r"""ShowMsdtcLocalHostResponse

        The model defined in huaweicloud sdk

        :param status: 查询状态 processing:查询中 success：查询成功 fail:查询失败
        :type status: str
        :param hosts: host信息列表
        :type hosts: list[:class:`huaweicloudsdkrds.v3.MsdtcHostResult`]
        """
        
        super().__init__()

        self._status = None
        self._hosts = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if hosts is not None:
            self.hosts = hosts

    @property
    def status(self):
        r"""Gets the status of this ShowMsdtcLocalHostResponse.

        查询状态 processing:查询中 success：查询成功 fail:查询失败

        :return: The status of this ShowMsdtcLocalHostResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMsdtcLocalHostResponse.

        查询状态 processing:查询中 success：查询成功 fail:查询失败

        :param status: The status of this ShowMsdtcLocalHostResponse.
        :type status: str
        """
        self._status = status

    @property
    def hosts(self):
        r"""Gets the hosts of this ShowMsdtcLocalHostResponse.

        host信息列表

        :return: The hosts of this ShowMsdtcLocalHostResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MsdtcHostResult`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ShowMsdtcLocalHostResponse.

        host信息列表

        :param hosts: The hosts of this ShowMsdtcLocalHostResponse.
        :type hosts: list[:class:`huaweicloudsdkrds.v3.MsdtcHostResult`]
        """
        self._hosts = hosts

    def to_dict(self):
        import warnings
        warnings.warn("ShowMsdtcLocalHostResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMsdtcLocalHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
