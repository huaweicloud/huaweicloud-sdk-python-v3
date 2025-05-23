# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_num': 'int',
        'port_num': 'int',
        'process_num': 'int',
        'app_num': 'int',
        'auto_launch_num': 'int',
        'web_framework_num': 'int',
        'web_site_num': 'int',
        'jar_package_num': 'int',
        'kernel_module_num': 'int',
        'web_service_num': 'int',
        'web_app_num': 'int',
        'database_num': 'int'
    }

    attribute_map = {
        'account_num': 'account_num',
        'port_num': 'port_num',
        'process_num': 'process_num',
        'app_num': 'app_num',
        'auto_launch_num': 'auto_launch_num',
        'web_framework_num': 'web_framework_num',
        'web_site_num': 'web_site_num',
        'jar_package_num': 'jar_package_num',
        'kernel_module_num': 'kernel_module_num',
        'web_service_num': 'web_service_num',
        'web_app_num': 'web_app_num',
        'database_num': 'database_num'
    }

    def __init__(self, account_num=None, port_num=None, process_num=None, app_num=None, auto_launch_num=None, web_framework_num=None, web_site_num=None, jar_package_num=None, kernel_module_num=None, web_service_num=None, web_app_num=None, database_num=None):
        r"""ShowAssetStatisticResponse

        The model defined in huaweicloud sdk

        :param account_num: 主机账号数量
        :type account_num: int
        :param port_num: 开放端口数量
        :type port_num: int
        :param process_num: 进程数量
        :type process_num: int
        :param app_num: 软件数量
        :type app_num: int
        :param auto_launch_num: 自启动进程数量
        :type auto_launch_num: int
        :param web_framework_num: web框架数量
        :type web_framework_num: int
        :param web_site_num: Web站点数量
        :type web_site_num: int
        :param jar_package_num: Jar包数量
        :type jar_package_num: int
        :param kernel_module_num: 内核模块数量
        :type kernel_module_num: int
        :param web_service_num: web服务数量
        :type web_service_num: int
        :param web_app_num: web应用数量
        :type web_app_num: int
        :param database_num: 数据库数量
        :type database_num: int
        """
        
        super(ShowAssetStatisticResponse, self).__init__()

        self._account_num = None
        self._port_num = None
        self._process_num = None
        self._app_num = None
        self._auto_launch_num = None
        self._web_framework_num = None
        self._web_site_num = None
        self._jar_package_num = None
        self._kernel_module_num = None
        self._web_service_num = None
        self._web_app_num = None
        self._database_num = None
        self.discriminator = None

        if account_num is not None:
            self.account_num = account_num
        if port_num is not None:
            self.port_num = port_num
        if process_num is not None:
            self.process_num = process_num
        if app_num is not None:
            self.app_num = app_num
        if auto_launch_num is not None:
            self.auto_launch_num = auto_launch_num
        if web_framework_num is not None:
            self.web_framework_num = web_framework_num
        if web_site_num is not None:
            self.web_site_num = web_site_num
        if jar_package_num is not None:
            self.jar_package_num = jar_package_num
        if kernel_module_num is not None:
            self.kernel_module_num = kernel_module_num
        if web_service_num is not None:
            self.web_service_num = web_service_num
        if web_app_num is not None:
            self.web_app_num = web_app_num
        if database_num is not None:
            self.database_num = database_num

    @property
    def account_num(self):
        r"""Gets the account_num of this ShowAssetStatisticResponse.

        主机账号数量

        :return: The account_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._account_num

    @account_num.setter
    def account_num(self, account_num):
        r"""Sets the account_num of this ShowAssetStatisticResponse.

        主机账号数量

        :param account_num: The account_num of this ShowAssetStatisticResponse.
        :type account_num: int
        """
        self._account_num = account_num

    @property
    def port_num(self):
        r"""Gets the port_num of this ShowAssetStatisticResponse.

        开放端口数量

        :return: The port_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._port_num

    @port_num.setter
    def port_num(self, port_num):
        r"""Sets the port_num of this ShowAssetStatisticResponse.

        开放端口数量

        :param port_num: The port_num of this ShowAssetStatisticResponse.
        :type port_num: int
        """
        self._port_num = port_num

    @property
    def process_num(self):
        r"""Gets the process_num of this ShowAssetStatisticResponse.

        进程数量

        :return: The process_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._process_num

    @process_num.setter
    def process_num(self, process_num):
        r"""Sets the process_num of this ShowAssetStatisticResponse.

        进程数量

        :param process_num: The process_num of this ShowAssetStatisticResponse.
        :type process_num: int
        """
        self._process_num = process_num

    @property
    def app_num(self):
        r"""Gets the app_num of this ShowAssetStatisticResponse.

        软件数量

        :return: The app_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._app_num

    @app_num.setter
    def app_num(self, app_num):
        r"""Sets the app_num of this ShowAssetStatisticResponse.

        软件数量

        :param app_num: The app_num of this ShowAssetStatisticResponse.
        :type app_num: int
        """
        self._app_num = app_num

    @property
    def auto_launch_num(self):
        r"""Gets the auto_launch_num of this ShowAssetStatisticResponse.

        自启动进程数量

        :return: The auto_launch_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._auto_launch_num

    @auto_launch_num.setter
    def auto_launch_num(self, auto_launch_num):
        r"""Sets the auto_launch_num of this ShowAssetStatisticResponse.

        自启动进程数量

        :param auto_launch_num: The auto_launch_num of this ShowAssetStatisticResponse.
        :type auto_launch_num: int
        """
        self._auto_launch_num = auto_launch_num

    @property
    def web_framework_num(self):
        r"""Gets the web_framework_num of this ShowAssetStatisticResponse.

        web框架数量

        :return: The web_framework_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._web_framework_num

    @web_framework_num.setter
    def web_framework_num(self, web_framework_num):
        r"""Sets the web_framework_num of this ShowAssetStatisticResponse.

        web框架数量

        :param web_framework_num: The web_framework_num of this ShowAssetStatisticResponse.
        :type web_framework_num: int
        """
        self._web_framework_num = web_framework_num

    @property
    def web_site_num(self):
        r"""Gets the web_site_num of this ShowAssetStatisticResponse.

        Web站点数量

        :return: The web_site_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._web_site_num

    @web_site_num.setter
    def web_site_num(self, web_site_num):
        r"""Sets the web_site_num of this ShowAssetStatisticResponse.

        Web站点数量

        :param web_site_num: The web_site_num of this ShowAssetStatisticResponse.
        :type web_site_num: int
        """
        self._web_site_num = web_site_num

    @property
    def jar_package_num(self):
        r"""Gets the jar_package_num of this ShowAssetStatisticResponse.

        Jar包数量

        :return: The jar_package_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._jar_package_num

    @jar_package_num.setter
    def jar_package_num(self, jar_package_num):
        r"""Sets the jar_package_num of this ShowAssetStatisticResponse.

        Jar包数量

        :param jar_package_num: The jar_package_num of this ShowAssetStatisticResponse.
        :type jar_package_num: int
        """
        self._jar_package_num = jar_package_num

    @property
    def kernel_module_num(self):
        r"""Gets the kernel_module_num of this ShowAssetStatisticResponse.

        内核模块数量

        :return: The kernel_module_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._kernel_module_num

    @kernel_module_num.setter
    def kernel_module_num(self, kernel_module_num):
        r"""Sets the kernel_module_num of this ShowAssetStatisticResponse.

        内核模块数量

        :param kernel_module_num: The kernel_module_num of this ShowAssetStatisticResponse.
        :type kernel_module_num: int
        """
        self._kernel_module_num = kernel_module_num

    @property
    def web_service_num(self):
        r"""Gets the web_service_num of this ShowAssetStatisticResponse.

        web服务数量

        :return: The web_service_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._web_service_num

    @web_service_num.setter
    def web_service_num(self, web_service_num):
        r"""Sets the web_service_num of this ShowAssetStatisticResponse.

        web服务数量

        :param web_service_num: The web_service_num of this ShowAssetStatisticResponse.
        :type web_service_num: int
        """
        self._web_service_num = web_service_num

    @property
    def web_app_num(self):
        r"""Gets the web_app_num of this ShowAssetStatisticResponse.

        web应用数量

        :return: The web_app_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._web_app_num

    @web_app_num.setter
    def web_app_num(self, web_app_num):
        r"""Sets the web_app_num of this ShowAssetStatisticResponse.

        web应用数量

        :param web_app_num: The web_app_num of this ShowAssetStatisticResponse.
        :type web_app_num: int
        """
        self._web_app_num = web_app_num

    @property
    def database_num(self):
        r"""Gets the database_num of this ShowAssetStatisticResponse.

        数据库数量

        :return: The database_num of this ShowAssetStatisticResponse.
        :rtype: int
        """
        return self._database_num

    @database_num.setter
    def database_num(self, database_num):
        r"""Sets the database_num of this ShowAssetStatisticResponse.

        数据库数量

        :param database_num: The database_num of this ShowAssetStatisticResponse.
        :type database_num: int
        """
        self._database_num = database_num

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
        if not isinstance(other, ShowAssetStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
