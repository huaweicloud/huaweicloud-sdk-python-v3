# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessClientInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_client_infos': 'list[AccessClientInfo]',
        'total': 'int'
    }

    attribute_map = {
        'access_client_infos': 'access_client_infos',
        'total': 'total'
    }

    def __init__(self, access_client_infos=None, total=None):
        """ListAccessClientInfosResponse

        The model defined in huaweicloud sdk

        :param access_client_infos: 接入客户端信息列表
        :type access_client_infos: list[:class:`huaweicloudsdklakeformation.v1.AccessClientInfo`]
        :param total: 接入客户端信息总数
        :type total: int
        """
        
        super(ListAccessClientInfosResponse, self).__init__()

        self._access_client_infos = None
        self._total = None
        self.discriminator = None

        if access_client_infos is not None:
            self.access_client_infos = access_client_infos
        if total is not None:
            self.total = total

    @property
    def access_client_infos(self):
        """Gets the access_client_infos of this ListAccessClientInfosResponse.

        接入客户端信息列表

        :return: The access_client_infos of this ListAccessClientInfosResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.AccessClientInfo`]
        """
        return self._access_client_infos

    @access_client_infos.setter
    def access_client_infos(self, access_client_infos):
        """Sets the access_client_infos of this ListAccessClientInfosResponse.

        接入客户端信息列表

        :param access_client_infos: The access_client_infos of this ListAccessClientInfosResponse.
        :type access_client_infos: list[:class:`huaweicloudsdklakeformation.v1.AccessClientInfo`]
        """
        self._access_client_infos = access_client_infos

    @property
    def total(self):
        """Gets the total of this ListAccessClientInfosResponse.

        接入客户端信息总数

        :return: The total of this ListAccessClientInfosResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAccessClientInfosResponse.

        接入客户端信息总数

        :param total: The total of this ListAccessClientInfosResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAccessClientInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
