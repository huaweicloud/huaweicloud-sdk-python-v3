# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GovSelector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'environment': 'str',
        'app': 'str',
        'service': 'str'
    }

    attribute_map = {
        'environment': 'environment',
        'app': 'app',
        'service': 'service'
    }

    def __init__(self, environment=None, app=None, service=None):
        """GovSelector

        The model defined in huaweicloud sdk

        :param environment: 所属环境
        :type environment: str
        :param app: 所属应用
        :type app: str
        :param service: 可选，治理下发到微服务级别
        :type service: str
        """
        
        

        self._environment = None
        self._app = None
        self._service = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if app is not None:
            self.app = app
        if service is not None:
            self.service = service

    @property
    def environment(self):
        """Gets the environment of this GovSelector.

        所属环境

        :return: The environment of this GovSelector.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this GovSelector.

        所属环境

        :param environment: The environment of this GovSelector.
        :type environment: str
        """
        self._environment = environment

    @property
    def app(self):
        """Gets the app of this GovSelector.

        所属应用

        :return: The app of this GovSelector.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this GovSelector.

        所属应用

        :param app: The app of this GovSelector.
        :type app: str
        """
        self._app = app

    @property
    def service(self):
        """Gets the service of this GovSelector.

        可选，治理下发到微服务级别

        :return: The service of this GovSelector.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this GovSelector.

        可选，治理下发到微服务级别

        :param service: The service of this GovSelector.
        :type service: str
        """
        self._service = service

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
        if not isinstance(other, GovSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
