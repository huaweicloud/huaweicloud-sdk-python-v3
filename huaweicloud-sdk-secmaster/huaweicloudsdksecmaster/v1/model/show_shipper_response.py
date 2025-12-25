# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'data': 'ShowShipperResponseBodyData',
        'msg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'msg': 'msg'
    }

    def __init__(self, code=None, data=None, msg=None):
        r"""ShowShipperResponse

        The model defined in huaweicloud sdk

        :param code: 状态码
        :type code: int
        :param data: 
        :type data: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyData`
        :param msg: 响应消息
        :type msg: str
        """
        
        super().__init__()

        self._code = None
        self._data = None
        self._msg = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if msg is not None:
            self.msg = msg

    @property
    def code(self):
        r"""Gets the code of this ShowShipperResponse.

        状态码

        :return: The code of this ShowShipperResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowShipperResponse.

        状态码

        :param code: The code of this ShowShipperResponse.
        :type code: int
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this ShowShipperResponse.

        :return: The data of this ShowShipperResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowShipperResponse.

        :param data: The data of this ShowShipperResponse.
        :type data: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyData`
        """
        self._data = data

    @property
    def msg(self):
        r"""Gets the msg of this ShowShipperResponse.

        响应消息

        :return: The msg of this ShowShipperResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ShowShipperResponse.

        响应消息

        :param msg: The msg of this ShowShipperResponse.
        :type msg: str
        """
        self._msg = msg

    def to_dict(self):
        import warnings
        warnings.warn("ShowShipperResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowShipperResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
