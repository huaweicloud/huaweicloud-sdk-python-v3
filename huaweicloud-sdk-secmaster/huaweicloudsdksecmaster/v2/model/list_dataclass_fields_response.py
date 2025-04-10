# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataclassFieldsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_details': 'list[FieldResponseBody]',
        'total': 'float',
        'x_request_id': 'str'
    }

    attribute_map = {
        'field_details': 'field_details',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, field_details=None, total=None, x_request_id=None):
        r"""ListDataclassFieldsResponse

        The model defined in huaweicloud sdk

        :param field_details: list of informations of field
        :type field_details: list[:class:`huaweicloudsdksecmaster.v2.FieldResponseBody`]
        :param total: 数据总量
        :type total: float
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListDataclassFieldsResponse, self).__init__()

        self._field_details = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if field_details is not None:
            self.field_details = field_details
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def field_details(self):
        r"""Gets the field_details of this ListDataclassFieldsResponse.

        list of informations of field

        :return: The field_details of this ListDataclassFieldsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.FieldResponseBody`]
        """
        return self._field_details

    @field_details.setter
    def field_details(self, field_details):
        r"""Sets the field_details of this ListDataclassFieldsResponse.

        list of informations of field

        :param field_details: The field_details of this ListDataclassFieldsResponse.
        :type field_details: list[:class:`huaweicloudsdksecmaster.v2.FieldResponseBody`]
        """
        self._field_details = field_details

    @property
    def total(self):
        r"""Gets the total of this ListDataclassFieldsResponse.

        数据总量

        :return: The total of this ListDataclassFieldsResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDataclassFieldsResponse.

        数据总量

        :param total: The total of this ListDataclassFieldsResponse.
        :type total: float
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListDataclassFieldsResponse.

        :return: The x_request_id of this ListDataclassFieldsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListDataclassFieldsResponse.

        :param x_request_id: The x_request_id of this ListDataclassFieldsResponse.
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
        if not isinstance(other, ListDataclassFieldsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
