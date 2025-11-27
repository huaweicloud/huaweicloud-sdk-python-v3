# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDocumentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, data=None, x_request_id=None):
        r"""UpdateDocumentResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释：** 编辑作业，系统返回的作业id。 **取值范围：** 不涉及。
        :type data: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def data(self):
        r"""Gets the data of this UpdateDocumentResponse.

        **参数解释：** 编辑作业，系统返回的作业id。 **取值范围：** 不涉及。

        :return: The data of this UpdateDocumentResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this UpdateDocumentResponse.

        **参数解释：** 编辑作业，系统返回的作业id。 **取值范围：** 不涉及。

        :param data: The data of this UpdateDocumentResponse.
        :type data: str
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateDocumentResponse.

        :return: The x_request_id of this UpdateDocumentResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateDocumentResponse.

        :param x_request_id: The x_request_id of this UpdateDocumentResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateDocumentResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDocumentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
