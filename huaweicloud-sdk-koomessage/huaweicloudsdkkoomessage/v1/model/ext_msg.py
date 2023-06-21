# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtMsg:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_in_browser': 'str',
        'web_title': 'str',
        'package_name': 'str',
        'app_id': 'str',
        'browser_floor_url': 'str',
        'depend_engine_ver': 'str',
        'third_service_name': 'str'
    }

    attribute_map = {
        'open_in_browser': 'open_in_browser',
        'web_title': 'web_title',
        'package_name': 'package_name',
        'app_id': 'app_id',
        'browser_floor_url': 'browser_floor_url',
        'depend_engine_ver': 'depend_engine_ver',
        'third_service_name': 'third_service_name'
    }

    def __init__(self, open_in_browser=None, web_title=None, package_name=None, app_id=None, browser_floor_url=None, depend_engine_ver=None, third_service_name=None):
        """ExtMsg

        The model defined in huaweicloud sdk

        :param open_in_browser: 打开方式。 - 0：webView打开  - 1：浏览器打开   &gt; action_type&#x3D;OPEN_URL必填，其他不填。 
        :type open_in_browser: str
        :param web_title: 标题，必填，长度范围为1-20个字符。 &gt; action_type&#x3D;OPEN_URL必填，其他不填。 
        :type web_title: str
        :param package_name: app包名，长度范围为1-50个字符。 &gt; action_type&#x3D;OPEN_APP必填，其他不填。 
        :type package_name: str
        :param app_id: 商家应用的appid，长度范围为0-60个字符。 &gt; action_type&#x3D;OPEN_APP必填，其他不填。 
        :type app_id: str
        :param browser_floor_url: 兜底url，长度范围为0-1000个字符，支持http/https。 &gt; action_type&#x3D;OPEN_APP选填，其他不填。 
        :type browser_floor_url: str
        :param depend_engine_ver: 依赖的快应用引擎版本号，长度范围为1-50个字符。 &gt; action_type&#x3D;OPEN_QUICK必填，其他不填。 
        :type depend_engine_ver: str
        :param third_service_name: 第三方服务名，长度范围为1-50个字符。 &gt; action_type&#x3D;OPEN_QUICK必填，其他不填。 
        :type third_service_name: str
        """
        
        

        self._open_in_browser = None
        self._web_title = None
        self._package_name = None
        self._app_id = None
        self._browser_floor_url = None
        self._depend_engine_ver = None
        self._third_service_name = None
        self.discriminator = None

        if open_in_browser is not None:
            self.open_in_browser = open_in_browser
        if web_title is not None:
            self.web_title = web_title
        if package_name is not None:
            self.package_name = package_name
        if app_id is not None:
            self.app_id = app_id
        if browser_floor_url is not None:
            self.browser_floor_url = browser_floor_url
        if depend_engine_ver is not None:
            self.depend_engine_ver = depend_engine_ver
        if third_service_name is not None:
            self.third_service_name = third_service_name

    @property
    def open_in_browser(self):
        """Gets the open_in_browser of this ExtMsg.

        打开方式。 - 0：webView打开  - 1：浏览器打开   > action_type=OPEN_URL必填，其他不填。 

        :return: The open_in_browser of this ExtMsg.
        :rtype: str
        """
        return self._open_in_browser

    @open_in_browser.setter
    def open_in_browser(self, open_in_browser):
        """Sets the open_in_browser of this ExtMsg.

        打开方式。 - 0：webView打开  - 1：浏览器打开   > action_type=OPEN_URL必填，其他不填。 

        :param open_in_browser: The open_in_browser of this ExtMsg.
        :type open_in_browser: str
        """
        self._open_in_browser = open_in_browser

    @property
    def web_title(self):
        """Gets the web_title of this ExtMsg.

        标题，必填，长度范围为1-20个字符。 > action_type=OPEN_URL必填，其他不填。 

        :return: The web_title of this ExtMsg.
        :rtype: str
        """
        return self._web_title

    @web_title.setter
    def web_title(self, web_title):
        """Sets the web_title of this ExtMsg.

        标题，必填，长度范围为1-20个字符。 > action_type=OPEN_URL必填，其他不填。 

        :param web_title: The web_title of this ExtMsg.
        :type web_title: str
        """
        self._web_title = web_title

    @property
    def package_name(self):
        """Gets the package_name of this ExtMsg.

        app包名，长度范围为1-50个字符。 > action_type=OPEN_APP必填，其他不填。 

        :return: The package_name of this ExtMsg.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ExtMsg.

        app包名，长度范围为1-50个字符。 > action_type=OPEN_APP必填，其他不填。 

        :param package_name: The package_name of this ExtMsg.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def app_id(self):
        """Gets the app_id of this ExtMsg.

        商家应用的appid，长度范围为0-60个字符。 > action_type=OPEN_APP必填，其他不填。 

        :return: The app_id of this ExtMsg.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ExtMsg.

        商家应用的appid，长度范围为0-60个字符。 > action_type=OPEN_APP必填，其他不填。 

        :param app_id: The app_id of this ExtMsg.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def browser_floor_url(self):
        """Gets the browser_floor_url of this ExtMsg.

        兜底url，长度范围为0-1000个字符，支持http/https。 > action_type=OPEN_APP选填，其他不填。 

        :return: The browser_floor_url of this ExtMsg.
        :rtype: str
        """
        return self._browser_floor_url

    @browser_floor_url.setter
    def browser_floor_url(self, browser_floor_url):
        """Sets the browser_floor_url of this ExtMsg.

        兜底url，长度范围为0-1000个字符，支持http/https。 > action_type=OPEN_APP选填，其他不填。 

        :param browser_floor_url: The browser_floor_url of this ExtMsg.
        :type browser_floor_url: str
        """
        self._browser_floor_url = browser_floor_url

    @property
    def depend_engine_ver(self):
        """Gets the depend_engine_ver of this ExtMsg.

        依赖的快应用引擎版本号，长度范围为1-50个字符。 > action_type=OPEN_QUICK必填，其他不填。 

        :return: The depend_engine_ver of this ExtMsg.
        :rtype: str
        """
        return self._depend_engine_ver

    @depend_engine_ver.setter
    def depend_engine_ver(self, depend_engine_ver):
        """Sets the depend_engine_ver of this ExtMsg.

        依赖的快应用引擎版本号，长度范围为1-50个字符。 > action_type=OPEN_QUICK必填，其他不填。 

        :param depend_engine_ver: The depend_engine_ver of this ExtMsg.
        :type depend_engine_ver: str
        """
        self._depend_engine_ver = depend_engine_ver

    @property
    def third_service_name(self):
        """Gets the third_service_name of this ExtMsg.

        第三方服务名，长度范围为1-50个字符。 > action_type=OPEN_QUICK必填，其他不填。 

        :return: The third_service_name of this ExtMsg.
        :rtype: str
        """
        return self._third_service_name

    @third_service_name.setter
    def third_service_name(self, third_service_name):
        """Sets the third_service_name of this ExtMsg.

        第三方服务名，长度范围为1-50个字符。 > action_type=OPEN_QUICK必填，其他不填。 

        :param third_service_name: The third_service_name of this ExtMsg.
        :type third_service_name: str
        """
        self._third_service_name = third_service_name

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
        if not isinstance(other, ExtMsg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
