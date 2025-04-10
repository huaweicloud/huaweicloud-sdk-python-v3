# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlowBlockResponse(SdkResponse):

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
        'ips': 'list[Ips]'
    }

    attribute_map = {
        'total': 'total',
        'ips': 'ips'
    }

    def __init__(self, total=None, ips=None):
        r"""ShowFlowBlockResponse

        The model defined in huaweicloud sdk

        :param total: total
        :type total: int
        :param ips: ips
        :type ips: list[:class:`huaweicloudsdkaad.v2.Ips`]
        """
        
        super(ShowFlowBlockResponse, self).__init__()

        self._total = None
        self._ips = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if ips is not None:
            self.ips = ips

    @property
    def total(self):
        r"""Gets the total of this ShowFlowBlockResponse.

        total

        :return: The total of this ShowFlowBlockResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowFlowBlockResponse.

        total

        :param total: The total of this ShowFlowBlockResponse.
        :type total: int
        """
        self._total = total

    @property
    def ips(self):
        r"""Gets the ips of this ShowFlowBlockResponse.

        ips

        :return: The ips of this ShowFlowBlockResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.Ips`]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this ShowFlowBlockResponse.

        ips

        :param ips: The ips of this ShowFlowBlockResponse.
        :type ips: list[:class:`huaweicloudsdkaad.v2.Ips`]
        """
        self._ips = ips

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
        if not isinstance(other, ShowFlowBlockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
