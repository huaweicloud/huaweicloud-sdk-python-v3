# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_hosts': 'list[ListHostsRspDedicatedHosts]',
        'total': 'int'
    }

    attribute_map = {
        'dedicated_hosts': 'dedicated_hosts',
        'total': 'total'
    }

    def __init__(self, dedicated_hosts=None, total=None):
        r"""ListHostsDetailResponse

        The model defined in huaweicloud sdk

        :param dedicated_hosts: 云办公主机列表。
        :type dedicated_hosts: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspDedicatedHosts`]
        :param total: 总共条数。
        :type total: int
        """
        
        super().__init__()

        self._dedicated_hosts = None
        self._total = None
        self.discriminator = None

        if dedicated_hosts is not None:
            self.dedicated_hosts = dedicated_hosts
        if total is not None:
            self.total = total

    @property
    def dedicated_hosts(self):
        r"""Gets the dedicated_hosts of this ListHostsDetailResponse.

        云办公主机列表。

        :return: The dedicated_hosts of this ListHostsDetailResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspDedicatedHosts`]
        """
        return self._dedicated_hosts

    @dedicated_hosts.setter
    def dedicated_hosts(self, dedicated_hosts):
        r"""Sets the dedicated_hosts of this ListHostsDetailResponse.

        云办公主机列表。

        :param dedicated_hosts: The dedicated_hosts of this ListHostsDetailResponse.
        :type dedicated_hosts: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspDedicatedHosts`]
        """
        self._dedicated_hosts = dedicated_hosts

    @property
    def total(self):
        r"""Gets the total of this ListHostsDetailResponse.

        总共条数。

        :return: The total of this ListHostsDetailResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHostsDetailResponse.

        总共条数。

        :param total: The total of this ListHostsDetailResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListHostsDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListHostsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
