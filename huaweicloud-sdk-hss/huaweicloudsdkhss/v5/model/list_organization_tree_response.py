# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'data_list': 'list[OrganizationNodeResponseInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total_num': 'total_num',
        'data_list': 'data_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total_num=None, data_list=None, x_request_id=None):
        r"""ListOrganizationTreeResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param data_list: 事件列表详情
        :type data_list: list[:class:`huaweicloudsdkhss.v5.OrganizationNodeResponseInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListOrganizationTreeResponse, self).__init__()

        self._total_num = None
        self._data_list = None
        self._x_request_id = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if data_list is not None:
            self.data_list = data_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total_num(self):
        r"""Gets the total_num of this ListOrganizationTreeResponse.

        总数

        :return: The total_num of this ListOrganizationTreeResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListOrganizationTreeResponse.

        总数

        :param total_num: The total_num of this ListOrganizationTreeResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListOrganizationTreeResponse.

        事件列表详情

        :return: The data_list of this ListOrganizationTreeResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.OrganizationNodeResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListOrganizationTreeResponse.

        事件列表详情

        :param data_list: The data_list of this ListOrganizationTreeResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.OrganizationNodeResponseInfo`]
        """
        self._data_list = data_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListOrganizationTreeResponse.

        :return: The x_request_id of this ListOrganizationTreeResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListOrganizationTreeResponse.

        :param x_request_id: The x_request_id of this ListOrganizationTreeResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListOrganizationTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
