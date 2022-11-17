# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGatewayResponseV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'responses': 'dict(str, ResponseInfoResp)',
        'id': 'str',
        'default': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'responses': 'responses',
        'id': 'id',
        'default': 'default',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, name=None, responses=None, id=None, default=None, create_time=None, update_time=None):
        """UpdateGatewayResponseV2Response

        The model defined in huaweicloud sdk

        :param name: 响应名称
        :type name: str
        :param responses: 错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX  每项错误类型均为一个JSON体
        :type responses: dict(str, ResponseInfoResp)
        :param id: 响应ID
        :type id: str
        :param default: 是否为分组默认响应
        :type default: bool
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 修改时间
        :type update_time: datetime
        """
        
        super(UpdateGatewayResponseV2Response, self).__init__()

        self._name = None
        self._responses = None
        self._id = None
        self._default = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if responses is not None:
            self.responses = responses
        if id is not None:
            self.id = id
        if default is not None:
            self.default = default
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def name(self):
        """Gets the name of this UpdateGatewayResponseV2Response.

        响应名称

        :return: The name of this UpdateGatewayResponseV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateGatewayResponseV2Response.

        响应名称

        :param name: The name of this UpdateGatewayResponseV2Response.
        :type name: str
        """
        self._name = name

    @property
    def responses(self):
        """Gets the responses of this UpdateGatewayResponseV2Response.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX  每项错误类型均为一个JSON体

        :return: The responses of this UpdateGatewayResponseV2Response.
        :rtype: dict(str, ResponseInfoResp)
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this UpdateGatewayResponseV2Response.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX  每项错误类型均为一个JSON体

        :param responses: The responses of this UpdateGatewayResponseV2Response.
        :type responses: dict(str, ResponseInfoResp)
        """
        self._responses = responses

    @property
    def id(self):
        """Gets the id of this UpdateGatewayResponseV2Response.

        响应ID

        :return: The id of this UpdateGatewayResponseV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateGatewayResponseV2Response.

        响应ID

        :param id: The id of this UpdateGatewayResponseV2Response.
        :type id: str
        """
        self._id = id

    @property
    def default(self):
        """Gets the default of this UpdateGatewayResponseV2Response.

        是否为分组默认响应

        :return: The default of this UpdateGatewayResponseV2Response.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this UpdateGatewayResponseV2Response.

        是否为分组默认响应

        :param default: The default of this UpdateGatewayResponseV2Response.
        :type default: bool
        """
        self._default = default

    @property
    def create_time(self):
        """Gets the create_time of this UpdateGatewayResponseV2Response.

        创建时间

        :return: The create_time of this UpdateGatewayResponseV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateGatewayResponseV2Response.

        创建时间

        :param create_time: The create_time of this UpdateGatewayResponseV2Response.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateGatewayResponseV2Response.

        修改时间

        :return: The update_time of this UpdateGatewayResponseV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateGatewayResponseV2Response.

        修改时间

        :param update_time: The update_time of this UpdateGatewayResponseV2Response.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateGatewayResponseV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
