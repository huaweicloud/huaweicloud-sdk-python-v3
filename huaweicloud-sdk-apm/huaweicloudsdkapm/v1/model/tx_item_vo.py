# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxItemVo:

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
        'env_name': 'str',
        'tx_display_name': 'str',
        'business_id': 'int',
        'env_id': 'int',
        'app_id': 'int',
        'tx_name': 'str',
        'invoke_count': 'int',
        'total_time': 'int',
        'error_count': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'env_name': 'env_name',
        'tx_display_name': 'tx_display_name',
        'business_id': 'business_id',
        'env_id': 'env_id',
        'app_id': 'app_id',
        'tx_name': 'tx_name',
        'invoke_count': 'invoke_count',
        'total_time': 'total_time',
        'error_count': 'error_count'
    }

    def __init__(self, app_name=None, env_name=None, tx_display_name=None, business_id=None, env_id=None, app_id=None, tx_name=None, invoke_count=None, total_time=None, error_count=None):
        """TxItemVo

        The model defined in huaweicloud sdk

        :param app_name: 组件名称。
        :type app_name: str
        :param env_name: 环境名称。
        :type env_name: str
        :param tx_display_name: 事务显示名称。
        :type tx_display_name: str
        :param business_id: 应用id。
        :type business_id: int
        :param env_id: 环境id。
        :type env_id: int
        :param app_id: 组件id。
        :type app_id: int
        :param tx_name: 事务名称。
        :type tx_name: str
        :param invoke_count: 调用次数。
        :type invoke_count: int
        :param total_time: 总耗时。
        :type total_time: int
        :param error_count: 错误次数。
        :type error_count: int
        """
        
        

        self._app_name = None
        self._env_name = None
        self._tx_display_name = None
        self._business_id = None
        self._env_id = None
        self._app_id = None
        self._tx_name = None
        self._invoke_count = None
        self._total_time = None
        self._error_count = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if env_name is not None:
            self.env_name = env_name
        if tx_display_name is not None:
            self.tx_display_name = tx_display_name
        if business_id is not None:
            self.business_id = business_id
        if env_id is not None:
            self.env_id = env_id
        if app_id is not None:
            self.app_id = app_id
        if tx_name is not None:
            self.tx_name = tx_name
        if invoke_count is not None:
            self.invoke_count = invoke_count
        if total_time is not None:
            self.total_time = total_time
        if error_count is not None:
            self.error_count = error_count

    @property
    def app_name(self):
        """Gets the app_name of this TxItemVo.

        组件名称。

        :return: The app_name of this TxItemVo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this TxItemVo.

        组件名称。

        :param app_name: The app_name of this TxItemVo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def env_name(self):
        """Gets the env_name of this TxItemVo.

        环境名称。

        :return: The env_name of this TxItemVo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this TxItemVo.

        环境名称。

        :param env_name: The env_name of this TxItemVo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def tx_display_name(self):
        """Gets the tx_display_name of this TxItemVo.

        事务显示名称。

        :return: The tx_display_name of this TxItemVo.
        :rtype: str
        """
        return self._tx_display_name

    @tx_display_name.setter
    def tx_display_name(self, tx_display_name):
        """Sets the tx_display_name of this TxItemVo.

        事务显示名称。

        :param tx_display_name: The tx_display_name of this TxItemVo.
        :type tx_display_name: str
        """
        self._tx_display_name = tx_display_name

    @property
    def business_id(self):
        """Gets the business_id of this TxItemVo.

        应用id。

        :return: The business_id of this TxItemVo.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TxItemVo.

        应用id。

        :param business_id: The business_id of this TxItemVo.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_id(self):
        """Gets the env_id of this TxItemVo.

        环境id。

        :return: The env_id of this TxItemVo.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TxItemVo.

        环境id。

        :param env_id: The env_id of this TxItemVo.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def app_id(self):
        """Gets the app_id of this TxItemVo.

        组件id。

        :return: The app_id of this TxItemVo.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TxItemVo.

        组件id。

        :param app_id: The app_id of this TxItemVo.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def tx_name(self):
        """Gets the tx_name of this TxItemVo.

        事务名称。

        :return: The tx_name of this TxItemVo.
        :rtype: str
        """
        return self._tx_name

    @tx_name.setter
    def tx_name(self, tx_name):
        """Sets the tx_name of this TxItemVo.

        事务名称。

        :param tx_name: The tx_name of this TxItemVo.
        :type tx_name: str
        """
        self._tx_name = tx_name

    @property
    def invoke_count(self):
        """Gets the invoke_count of this TxItemVo.

        调用次数。

        :return: The invoke_count of this TxItemVo.
        :rtype: int
        """
        return self._invoke_count

    @invoke_count.setter
    def invoke_count(self, invoke_count):
        """Sets the invoke_count of this TxItemVo.

        调用次数。

        :param invoke_count: The invoke_count of this TxItemVo.
        :type invoke_count: int
        """
        self._invoke_count = invoke_count

    @property
    def total_time(self):
        """Gets the total_time of this TxItemVo.

        总耗时。

        :return: The total_time of this TxItemVo.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this TxItemVo.

        总耗时。

        :param total_time: The total_time of this TxItemVo.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def error_count(self):
        """Gets the error_count of this TxItemVo.

        错误次数。

        :return: The error_count of this TxItemVo.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this TxItemVo.

        错误次数。

        :param error_count: The error_count of this TxItemVo.
        :type error_count: int
        """
        self._error_count = error_count

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
        if not isinstance(other, TxItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
