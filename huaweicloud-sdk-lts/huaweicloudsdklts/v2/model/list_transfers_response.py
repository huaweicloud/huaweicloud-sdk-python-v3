# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransfersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_transfers': 'list[CreateTransferResponseBody]'
    }

    attribute_map = {
        'log_transfers': 'log_transfers'
    }

    def __init__(self, log_transfers=None):
        """ListTransfersResponse

        The model defined in huaweicloud sdk

        :param log_transfers: 查询日志转储信息数组
        :type log_transfers: list[:class:`huaweicloudsdklts.v2.CreateTransferResponseBody`]
        """
        
        super(ListTransfersResponse, self).__init__()

        self._log_transfers = None
        self.discriminator = None

        if log_transfers is not None:
            self.log_transfers = log_transfers

    @property
    def log_transfers(self):
        """Gets the log_transfers of this ListTransfersResponse.

        查询日志转储信息数组

        :return: The log_transfers of this ListTransfersResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.CreateTransferResponseBody`]
        """
        return self._log_transfers

    @log_transfers.setter
    def log_transfers(self, log_transfers):
        """Sets the log_transfers of this ListTransfersResponse.

        查询日志转储信息数组

        :param log_transfers: The log_transfers of this ListTransfersResponse.
        :type log_transfers: list[:class:`huaweicloudsdklts.v2.CreateTransferResponseBody`]
        """
        self._log_transfers = log_transfers

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
        if not isinstance(other, ListTransfersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
