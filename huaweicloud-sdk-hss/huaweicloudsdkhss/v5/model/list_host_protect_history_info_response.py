# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostProtectHistoryInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'protect_status': 'str',
        'total_num': 'int',
        'data_list': 'list[HostProtectHistoryResponseInfo]'
    }

    attribute_map = {
        'host_name': 'host_name',
        'protect_status': 'protect_status',
        'total_num': 'total_num',
        'data_list': 'data_list'
    }

    def __init__(self, host_name=None, protect_status=None, total_num=None, data_list=None):
        """ListHostProtectHistoryInfoResponse

        The model defined in huaweicloud sdk

        :param host_name: 服务器名称
        :type host_name: str
        :param protect_status: 防护状态   - close : 未开启   - opened : 防护中
        :type protect_status: str
        :param total_num: total number
        :type total_num: int
        :param data_list: data list
        :type data_list: list[:class:`huaweicloudsdkhss.v5.HostProtectHistoryResponseInfo`]
        """
        
        super(ListHostProtectHistoryInfoResponse, self).__init__()

        self._host_name = None
        self._protect_status = None
        self._total_num = None
        self._data_list = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if protect_status is not None:
            self.protect_status = protect_status
        if total_num is not None:
            self.total_num = total_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def host_name(self):
        """Gets the host_name of this ListHostProtectHistoryInfoResponse.

        服务器名称

        :return: The host_name of this ListHostProtectHistoryInfoResponse.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListHostProtectHistoryInfoResponse.

        服务器名称

        :param host_name: The host_name of this ListHostProtectHistoryInfoResponse.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def protect_status(self):
        """Gets the protect_status of this ListHostProtectHistoryInfoResponse.

        防护状态   - close : 未开启   - opened : 防护中

        :return: The protect_status of this ListHostProtectHistoryInfoResponse.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListHostProtectHistoryInfoResponse.

        防护状态   - close : 未开启   - opened : 防护中

        :param protect_status: The protect_status of this ListHostProtectHistoryInfoResponse.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def total_num(self):
        """Gets the total_num of this ListHostProtectHistoryInfoResponse.

        total number

        :return: The total_num of this ListHostProtectHistoryInfoResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListHostProtectHistoryInfoResponse.

        total number

        :param total_num: The total_num of this ListHostProtectHistoryInfoResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def data_list(self):
        """Gets the data_list of this ListHostProtectHistoryInfoResponse.

        data list

        :return: The data_list of this ListHostProtectHistoryInfoResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostProtectHistoryResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ListHostProtectHistoryInfoResponse.

        data list

        :param data_list: The data_list of this ListHostProtectHistoryInfoResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.HostProtectHistoryResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListHostProtectHistoryInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
