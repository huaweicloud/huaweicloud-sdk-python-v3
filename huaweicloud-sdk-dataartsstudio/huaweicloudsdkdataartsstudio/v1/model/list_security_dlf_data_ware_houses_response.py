# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDlfDataWareHousesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_lists': 'list[DataWareHouseDTO]'
    }

    attribute_map = {
        'dw_lists': 'dw_lists'
    }

    def __init__(self, dw_lists=None):
        r"""ListSecurityDlfDataWareHousesResponse

        The model defined in huaweicloud sdk

        :param dw_lists: 数据开发细粒度连接列表
        :type dw_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTO`]
        """
        
        super(ListSecurityDlfDataWareHousesResponse, self).__init__()

        self._dw_lists = None
        self.discriminator = None

        if dw_lists is not None:
            self.dw_lists = dw_lists

    @property
    def dw_lists(self):
        r"""Gets the dw_lists of this ListSecurityDlfDataWareHousesResponse.

        数据开发细粒度连接列表

        :return: The dw_lists of this ListSecurityDlfDataWareHousesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTO`]
        """
        return self._dw_lists

    @dw_lists.setter
    def dw_lists(self, dw_lists):
        r"""Sets the dw_lists of this ListSecurityDlfDataWareHousesResponse.

        数据开发细粒度连接列表

        :param dw_lists: The dw_lists of this ListSecurityDlfDataWareHousesResponse.
        :type dw_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTO`]
        """
        self._dw_lists = dw_lists

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
        if not isinstance(other, ListSecurityDlfDataWareHousesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
