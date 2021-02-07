# coding: utf-8

import pprint
import re

import six





class AddApplication:


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
        'instance_id': 'str',
        'service_name': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_id': 'app_id',
        'instance_id': 'instance_id',
        'service_name': 'service_name'
    }

    def __init__(self, app_name=None, app_id=None, instance_id=None, service_name=None):
        """AddApplication - a model defined in huaweicloud sdk"""
        
        

        self._app_name = None
        self._app_id = None
        self._instance_id = None
        self._service_name = None
        self.discriminator = None

        self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if instance_id is not None:
            self.instance_id = instance_id
        if service_name is not None:
            self.service_name = service_name

    @property
    def app_name(self):
        """Gets the app_name of this AddApplication.

        资源空间名称。

        :return: The app_name of this AddApplication.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AddApplication.

        资源空间名称。

        :param app_name: The app_name of this AddApplication.
        :type: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this AddApplication.

        资源空间ID。

        :return: The app_id of this AddApplication.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddApplication.

        资源空间ID。

        :param app_id: The app_id of this AddApplication.
        :type: str
        """
        self._app_id = app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this AddApplication.

        迁移前实例ID。

        :return: The instance_id of this AddApplication.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AddApplication.

        迁移前实例ID。

        :param instance_id: The instance_id of this AddApplication.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def service_name(self):
        """Gets the service_name of this AddApplication.

        对接的服务名,IoTDA代表华为云设备接入云服务，CTNBGW代表天翼云设备接入服务

        :return: The service_name of this AddApplication.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this AddApplication.

        对接的服务名,IoTDA代表华为云设备接入云服务，CTNBGW代表天翼云设备接入服务

        :param service_name: The service_name of this AddApplication.
        :type: str
        """
        self._service_name = service_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
