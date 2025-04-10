# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddAccountsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_all_legal_count': 'bool',
        'x_request_id': 'str'
    }

    attribute_map = {
        'is_all_legal_count': 'is_all_legal_count',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, is_all_legal_count=None, x_request_id=None):
        r"""BatchAddAccountsResponse

        The model defined in huaweicloud sdk

        :param is_all_legal_count: 批量添加账号结果   - true ：成功   - false ：失败
        :type is_all_legal_count: bool
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(BatchAddAccountsResponse, self).__init__()

        self._is_all_legal_count = None
        self._x_request_id = None
        self.discriminator = None

        if is_all_legal_count is not None:
            self.is_all_legal_count = is_all_legal_count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def is_all_legal_count(self):
        r"""Gets the is_all_legal_count of this BatchAddAccountsResponse.

        批量添加账号结果   - true ：成功   - false ：失败

        :return: The is_all_legal_count of this BatchAddAccountsResponse.
        :rtype: bool
        """
        return self._is_all_legal_count

    @is_all_legal_count.setter
    def is_all_legal_count(self, is_all_legal_count):
        r"""Sets the is_all_legal_count of this BatchAddAccountsResponse.

        批量添加账号结果   - true ：成功   - false ：失败

        :param is_all_legal_count: The is_all_legal_count of this BatchAddAccountsResponse.
        :type is_all_legal_count: bool
        """
        self._is_all_legal_count = is_all_legal_count

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this BatchAddAccountsResponse.

        :return: The x_request_id of this BatchAddAccountsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this BatchAddAccountsResponse.

        :param x_request_id: The x_request_id of this BatchAddAccountsResponse.
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
        if not isinstance(other, BatchAddAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
