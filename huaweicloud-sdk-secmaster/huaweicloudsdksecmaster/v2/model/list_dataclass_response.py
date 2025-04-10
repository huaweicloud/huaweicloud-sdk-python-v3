# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataclassResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataclass_details': 'list[DataClassResponseBody]',
        'total': 'float',
        'x_request_id': 'str'
    }

    attribute_map = {
        'dataclass_details': 'dataclass_details',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, dataclass_details=None, total=None, x_request_id=None):
        r"""ListDataclassResponse

        The model defined in huaweicloud sdk

        :param dataclass_details: 数据类详情
        :type dataclass_details: list[:class:`huaweicloudsdksecmaster.v2.DataClassResponseBody`]
        :param total: 数据总量
        :type total: float
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListDataclassResponse, self).__init__()

        self._dataclass_details = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if dataclass_details is not None:
            self.dataclass_details = dataclass_details
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def dataclass_details(self):
        r"""Gets the dataclass_details of this ListDataclassResponse.

        数据类详情

        :return: The dataclass_details of this ListDataclassResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.DataClassResponseBody`]
        """
        return self._dataclass_details

    @dataclass_details.setter
    def dataclass_details(self, dataclass_details):
        r"""Sets the dataclass_details of this ListDataclassResponse.

        数据类详情

        :param dataclass_details: The dataclass_details of this ListDataclassResponse.
        :type dataclass_details: list[:class:`huaweicloudsdksecmaster.v2.DataClassResponseBody`]
        """
        self._dataclass_details = dataclass_details

    @property
    def total(self):
        r"""Gets the total of this ListDataclassResponse.

        数据总量

        :return: The total of this ListDataclassResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDataclassResponse.

        数据总量

        :param total: The total of this ListDataclassResponse.
        :type total: float
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListDataclassResponse.

        :return: The x_request_id of this ListDataclassResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListDataclassResponse.

        :param x_request_id: The x_request_id of this ListDataclassResponse.
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
        if not isinstance(other, ListDataclassResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
