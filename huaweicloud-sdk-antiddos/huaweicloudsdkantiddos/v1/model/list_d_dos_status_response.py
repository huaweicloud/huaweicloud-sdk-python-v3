# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDosStatusResponse(SdkResponse):

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
        'ddos_status': 'list[DDosStatus]'
    }

    attribute_map = {
        'total': 'total',
        'ddos_status': 'ddosStatus'
    }

    def __init__(self, total=None, ddos_status=None):
        """ListDDosStatusResponse

        The model defined in huaweicloud sdk

        :param total: 弹性IP总数
        :type total: int
        :param ddos_status: 防护状态列表
        :type ddos_status: list[:class:`huaweicloudsdkantiddos.v1.DDosStatus`]
        """
        
        super(ListDDosStatusResponse, self).__init__()

        self._total = None
        self._ddos_status = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if ddos_status is not None:
            self.ddos_status = ddos_status

    @property
    def total(self):
        """Gets the total of this ListDDosStatusResponse.

        弹性IP总数

        :return: The total of this ListDDosStatusResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDDosStatusResponse.

        弹性IP总数

        :param total: The total of this ListDDosStatusResponse.
        :type total: int
        """
        self._total = total

    @property
    def ddos_status(self):
        """Gets the ddos_status of this ListDDosStatusResponse.

        防护状态列表

        :return: The ddos_status of this ListDDosStatusResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.DDosStatus`]
        """
        return self._ddos_status

    @ddos_status.setter
    def ddos_status(self, ddos_status):
        """Sets the ddos_status of this ListDDosStatusResponse.

        防护状态列表

        :param ddos_status: The ddos_status of this ListDDosStatusResponse.
        :type ddos_status: list[:class:`huaweicloudsdkantiddos.v1.DDosStatus`]
        """
        self._ddos_status = ddos_status

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
        if not isinstance(other, ListDDosStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
