# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHookResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'callback_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'callback_url': 'callback_url'
    }

    def __init__(self, id=None, type=None, callback_url=None):
        r"""CreateHookResponse

        The model defined in huaweicloud sdk

        :param id: hook ID。
        :type id: str
        :param type: hook类型。
        :type type: str
        :param callback_url: 回滚URL。
        :type callback_url: str
        """
        
        super().__init__()

        self._id = None
        self._type = None
        self._callback_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if callback_url is not None:
            self.callback_url = callback_url

    @property
    def id(self):
        r"""Gets the id of this CreateHookResponse.

        hook ID。

        :return: The id of this CreateHookResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateHookResponse.

        hook ID。

        :param id: The id of this CreateHookResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this CreateHookResponse.

        hook类型。

        :return: The type of this CreateHookResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateHookResponse.

        hook类型。

        :param type: The type of this CreateHookResponse.
        :type type: str
        """
        self._type = type

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CreateHookResponse.

        回滚URL。

        :return: The callback_url of this CreateHookResponse.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CreateHookResponse.

        回滚URL。

        :param callback_url: The callback_url of this CreateHookResponse.
        :type callback_url: str
        """
        self._callback_url = callback_url

    def to_dict(self):
        import warnings
        warnings.warn("CreateHookResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateHookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
