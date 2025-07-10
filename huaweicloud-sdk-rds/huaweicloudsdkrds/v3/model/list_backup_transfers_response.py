# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupTransfersResponse(SdkResponse):

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
        'transfer_list': 'list[BackupTransferInfo]'
    }

    attribute_map = {
        'total': 'total',
        'transfer_list': 'transfer_list'
    }

    def __init__(self, total=None, transfer_list=None):
        r"""ListBackupTransfersResponse

        The model defined in huaweicloud sdk

        :param total: 任务数量
        :type total: int
        :param transfer_list: 任务列表
        :type transfer_list: list[:class:`huaweicloudsdkrds.v3.BackupTransferInfo`]
        """
        
        super(ListBackupTransfersResponse, self).__init__()

        self._total = None
        self._transfer_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if transfer_list is not None:
            self.transfer_list = transfer_list

    @property
    def total(self):
        r"""Gets the total of this ListBackupTransfersResponse.

        任务数量

        :return: The total of this ListBackupTransfersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListBackupTransfersResponse.

        任务数量

        :param total: The total of this ListBackupTransfersResponse.
        :type total: int
        """
        self._total = total

    @property
    def transfer_list(self):
        r"""Gets the transfer_list of this ListBackupTransfersResponse.

        任务列表

        :return: The transfer_list of this ListBackupTransfersResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.BackupTransferInfo`]
        """
        return self._transfer_list

    @transfer_list.setter
    def transfer_list(self, transfer_list):
        r"""Sets the transfer_list of this ListBackupTransfersResponse.

        任务列表

        :param transfer_list: The transfer_list of this ListBackupTransfersResponse.
        :type transfer_list: list[:class:`huaweicloudsdkrds.v3.BackupTransferInfo`]
        """
        self._transfer_list = transfer_list

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
        if not isinstance(other, ListBackupTransfersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
