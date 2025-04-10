# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'das_conn_info_list': 'list[ApiListConnectionsInfoRespDasConnInfoList]'
    }

    attribute_map = {
        'total_record': 'total_record',
        'das_conn_info_list': 'das_conn_info_list'
    }

    def __init__(self, total_record=None, das_conn_info_list=None):
        r"""ListConnectionsResponse

        The model defined in huaweicloud sdk

        :param total_record: 总记录数目
        :type total_record: int
        :param das_conn_info_list: 连接信息列表
        :type das_conn_info_list: list[:class:`huaweicloudsdkdas.v3.ApiListConnectionsInfoRespDasConnInfoList`]
        """
        
        super(ListConnectionsResponse, self).__init__()

        self._total_record = None
        self._das_conn_info_list = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if das_conn_info_list is not None:
            self.das_conn_info_list = das_conn_info_list

    @property
    def total_record(self):
        r"""Gets the total_record of this ListConnectionsResponse.

        总记录数目

        :return: The total_record of this ListConnectionsResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        r"""Sets the total_record of this ListConnectionsResponse.

        总记录数目

        :param total_record: The total_record of this ListConnectionsResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def das_conn_info_list(self):
        r"""Gets the das_conn_info_list of this ListConnectionsResponse.

        连接信息列表

        :return: The das_conn_info_list of this ListConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ApiListConnectionsInfoRespDasConnInfoList`]
        """
        return self._das_conn_info_list

    @das_conn_info_list.setter
    def das_conn_info_list(self, das_conn_info_list):
        r"""Sets the das_conn_info_list of this ListConnectionsResponse.

        连接信息列表

        :param das_conn_info_list: The das_conn_info_list of this ListConnectionsResponse.
        :type das_conn_info_list: list[:class:`huaweicloudsdkdas.v3.ApiListConnectionsInfoRespDasConnInfoList`]
        """
        self._das_conn_info_list = das_conn_info_list

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
        if not isinstance(other, ListConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
