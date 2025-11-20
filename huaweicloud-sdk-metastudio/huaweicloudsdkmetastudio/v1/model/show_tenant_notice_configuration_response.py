# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantNoticeConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'send_msg': 'bool',
        'properties': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'send_msg': 'send_msg',
        'properties': 'properties',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, type=None, send_msg=None, properties=None, x_request_id=None):
        r"""ShowTenantNoticeConfigurationResponse

        The model defined in huaweicloud sdk

        :param type: 通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知
        :type type: str
        :param send_msg: 是否发送短信。
        :type send_msg: bool
        :param properties: 通知配置项
        :type properties: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._type = None
        self._send_msg = None
        self._properties = None
        self._x_request_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if send_msg is not None:
            self.send_msg = send_msg
        if properties is not None:
            self.properties = properties
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def type(self):
        r"""Gets the type of this ShowTenantNoticeConfigurationResponse.

        通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知

        :return: The type of this ShowTenantNoticeConfigurationResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowTenantNoticeConfigurationResponse.

        通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知

        :param type: The type of this ShowTenantNoticeConfigurationResponse.
        :type type: str
        """
        self._type = type

    @property
    def send_msg(self):
        r"""Gets the send_msg of this ShowTenantNoticeConfigurationResponse.

        是否发送短信。

        :return: The send_msg of this ShowTenantNoticeConfigurationResponse.
        :rtype: bool
        """
        return self._send_msg

    @send_msg.setter
    def send_msg(self, send_msg):
        r"""Sets the send_msg of this ShowTenantNoticeConfigurationResponse.

        是否发送短信。

        :param send_msg: The send_msg of this ShowTenantNoticeConfigurationResponse.
        :type send_msg: bool
        """
        self._send_msg = send_msg

    @property
    def properties(self):
        r"""Gets the properties of this ShowTenantNoticeConfigurationResponse.

        通知配置项

        :return: The properties of this ShowTenantNoticeConfigurationResponse.
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ShowTenantNoticeConfigurationResponse.

        通知配置项

        :param properties: The properties of this ShowTenantNoticeConfigurationResponse.
        :type properties: str
        """
        self._properties = properties

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowTenantNoticeConfigurationResponse.

        :return: The x_request_id of this ShowTenantNoticeConfigurationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowTenantNoticeConfigurationResponse.

        :param x_request_id: The x_request_id of this ShowTenantNoticeConfigurationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantNoticeConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTenantNoticeConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
