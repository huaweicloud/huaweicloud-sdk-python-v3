# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMultiAccountTransferAmountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'amount_infos': 'list[TransferAmountInfoV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'amount_infos': 'amount_infos'
    }

    def __init__(self, total_count=None, amount_infos=None):
        """ShowMultiAccountTransferAmountResponse

        The model defined in huaweicloud sdk

        :param total_count: 记录条数。
        :type total_count: int
        :param amount_infos: 可拨款余额信息，如果是余额账户，只会有一条记录。 具体请参见表2。
        :type amount_infos: list[:class:`huaweicloudsdkbss.v2.TransferAmountInfoV2`]
        """
        
        super(ShowMultiAccountTransferAmountResponse, self).__init__()

        self._total_count = None
        self._amount_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if amount_infos is not None:
            self.amount_infos = amount_infos

    @property
    def total_count(self):
        """Gets the total_count of this ShowMultiAccountTransferAmountResponse.

        记录条数。

        :return: The total_count of this ShowMultiAccountTransferAmountResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowMultiAccountTransferAmountResponse.

        记录条数。

        :param total_count: The total_count of this ShowMultiAccountTransferAmountResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def amount_infos(self):
        """Gets the amount_infos of this ShowMultiAccountTransferAmountResponse.

        可拨款余额信息，如果是余额账户，只会有一条记录。 具体请参见表2。

        :return: The amount_infos of this ShowMultiAccountTransferAmountResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.TransferAmountInfoV2`]
        """
        return self._amount_infos

    @amount_infos.setter
    def amount_infos(self, amount_infos):
        """Sets the amount_infos of this ShowMultiAccountTransferAmountResponse.

        可拨款余额信息，如果是余额账户，只会有一条记录。 具体请参见表2。

        :param amount_infos: The amount_infos of this ShowMultiAccountTransferAmountResponse.
        :type amount_infos: list[:class:`huaweicloudsdkbss.v2.TransferAmountInfoV2`]
        """
        self._amount_infos = amount_infos

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
        if not isinstance(other, ShowMultiAccountTransferAmountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
