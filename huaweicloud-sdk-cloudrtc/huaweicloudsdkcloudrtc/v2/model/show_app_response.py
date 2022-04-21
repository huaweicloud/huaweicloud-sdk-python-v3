# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_id': 'str',
        'state': 'AppState',
        'scope': 'str',
        'tenant_name': 'str',
        'domain': 'str',
        'create_time': 'str',
        'authentication': 'AppAuth',
        'callbacks': 'AppCallbacks',
        'auto_record_mode': 'AppAutoRecordMode',
        'x_request_id': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_id': 'app_id',
        'state': 'state',
        'scope': 'scope',
        'tenant_name': 'tenant_name',
        'domain': 'domain',
        'create_time': 'create_time',
        'authentication': 'authentication',
        'callbacks': 'callbacks',
        'auto_record_mode': 'auto_record_mode',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, app_name=None, app_id=None, state=None, scope=None, tenant_name=None, domain=None, create_time=None, authentication=None, callbacks=None, auto_record_mode=None, x_request_id=None):
        """ShowAppResponse

        The model defined in huaweicloud sdk

        :param app_name: app名称
        :type app_name: str
        :param app_id: 应用id
        :type app_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        :param scope: RTC覆盖范围。  取值如下：    - DOMESTIC：国内范围。   - OVERSEA：海外范围。   - GLOBAL：全球范围。 
        :type scope: str
        :param tenant_name: 账号名
        :type tenant_name: str
        :param domain: 域名，App对应域名
        :type domain: str
        :param create_time: 创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type create_time: str
        :param authentication: 
        :type authentication: :class:`huaweicloudsdkcloudrtc.v2.AppAuth`
        :param callbacks: 
        :type callbacks: :class:`huaweicloudsdkcloudrtc.v2.AppCallbacks`
        :param auto_record_mode: 
        :type auto_record_mode: :class:`huaweicloudsdkcloudrtc.v2.AppAutoRecordMode`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAppResponse, self).__init__()

        self._app_name = None
        self._app_id = None
        self._state = None
        self._scope = None
        self._tenant_name = None
        self._domain = None
        self._create_time = None
        self._authentication = None
        self._callbacks = None
        self._auto_record_mode = None
        self._x_request_id = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if state is not None:
            self.state = state
        if scope is not None:
            self.scope = scope
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if domain is not None:
            self.domain = domain
        if create_time is not None:
            self.create_time = create_time
        if authentication is not None:
            self.authentication = authentication
        if callbacks is not None:
            self.callbacks = callbacks
        if auto_record_mode is not None:
            self.auto_record_mode = auto_record_mode
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def app_name(self):
        """Gets the app_name of this ShowAppResponse.

        app名称

        :return: The app_name of this ShowAppResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowAppResponse.

        app名称

        :param app_name: The app_name of this ShowAppResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this ShowAppResponse.

        应用id

        :return: The app_id of this ShowAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowAppResponse.

        应用id

        :param app_id: The app_id of this ShowAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def state(self):
        """Gets the state of this ShowAppResponse.


        :return: The state of this ShowAppResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowAppResponse.


        :param state: The state of this ShowAppResponse.
        :type state: :class:`huaweicloudsdkcloudrtc.v2.AppState`
        """
        self._state = state

    @property
    def scope(self):
        """Gets the scope of this ShowAppResponse.

        RTC覆盖范围。  取值如下：    - DOMESTIC：国内范围。   - OVERSEA：海外范围。   - GLOBAL：全球范围。 

        :return: The scope of this ShowAppResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ShowAppResponse.

        RTC覆盖范围。  取值如下：    - DOMESTIC：国内范围。   - OVERSEA：海外范围。   - GLOBAL：全球范围。 

        :param scope: The scope of this ShowAppResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def tenant_name(self):
        """Gets the tenant_name of this ShowAppResponse.

        账号名

        :return: The tenant_name of this ShowAppResponse.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this ShowAppResponse.

        账号名

        :param tenant_name: The tenant_name of this ShowAppResponse.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def domain(self):
        """Gets the domain of this ShowAppResponse.

        域名，App对应域名

        :return: The domain of this ShowAppResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowAppResponse.

        域名，App对应域名

        :param domain: The domain of this ShowAppResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The create_time of this ShowAppResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param create_time: The create_time of this ShowAppResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def authentication(self):
        """Gets the authentication of this ShowAppResponse.


        :return: The authentication of this ShowAppResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppAuth`
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ShowAppResponse.


        :param authentication: The authentication of this ShowAppResponse.
        :type authentication: :class:`huaweicloudsdkcloudrtc.v2.AppAuth`
        """
        self._authentication = authentication

    @property
    def callbacks(self):
        """Gets the callbacks of this ShowAppResponse.


        :return: The callbacks of this ShowAppResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppCallbacks`
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """Sets the callbacks of this ShowAppResponse.


        :param callbacks: The callbacks of this ShowAppResponse.
        :type callbacks: :class:`huaweicloudsdkcloudrtc.v2.AppCallbacks`
        """
        self._callbacks = callbacks

    @property
    def auto_record_mode(self):
        """Gets the auto_record_mode of this ShowAppResponse.


        :return: The auto_record_mode of this ShowAppResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.AppAutoRecordMode`
        """
        return self._auto_record_mode

    @auto_record_mode.setter
    def auto_record_mode(self, auto_record_mode):
        """Sets the auto_record_mode of this ShowAppResponse.


        :param auto_record_mode: The auto_record_mode of this ShowAppResponse.
        :type auto_record_mode: :class:`huaweicloudsdkcloudrtc.v2.AppAutoRecordMode`
        """
        self._auto_record_mode = auto_record_mode

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowAppResponse.


        :return: The x_request_id of this ShowAppResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowAppResponse.


        :param x_request_id: The x_request_id of this ShowAppResponse.
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
        if not isinstance(other, ShowAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
