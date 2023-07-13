# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWtpProtectHostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[WtpProtectHostResponseInfo]',
        'total_num': 'int'
    }

    attribute_map = {
        'data_list': 'data_list',
        'total_num': 'total_num'
    }

    def __init__(self, data_list=None, total_num=None):
        """ListWtpProtectHostResponse

        The model defined in huaweicloud sdk

        :param data_list: data list
        :type data_list: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostResponseInfo`]
        :param total_num: total number
        :type total_num: int
        """
        
        super(ListWtpProtectHostResponse, self).__init__()

        self._data_list = None
        self._total_num = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def data_list(self):
        """Gets the data_list of this ListWtpProtectHostResponse.

        data list

        :return: The data_list of this ListWtpProtectHostResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ListWtpProtectHostResponse.

        data list

        :param data_list: The data_list of this ListWtpProtectHostResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostResponseInfo`]
        """
        self._data_list = data_list

    @property
    def total_num(self):
        """Gets the total_num of this ListWtpProtectHostResponse.

        total number

        :return: The total_num of this ListWtpProtectHostResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListWtpProtectHostResponse.

        total number

        :param total_num: The total_num of this ListWtpProtectHostResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ListWtpProtectHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
