# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowInformationAboutDatabaseProxyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'proxy': 'Proxy',
        'master_instance': 'MasterInstance',
        'readonly_instances': 'list[ReadonlyInstances]'
    }

    attribute_map = {
        'proxy': 'proxy',
        'master_instance': 'master_instance',
        'readonly_instances': 'readonly_instances'
    }

    def __init__(self, proxy=None, master_instance=None, readonly_instances=None):
        """ShowInformationAboutDatabaseProxyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._proxy = None
        self._master_instance = None
        self._readonly_instances = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if master_instance is not None:
            self.master_instance = master_instance
        if readonly_instances is not None:
            self.readonly_instances = readonly_instances

    @property
    def proxy(self):
        """Gets the proxy of this ShowInformationAboutDatabaseProxyResponse.


        :return: The proxy of this ShowInformationAboutDatabaseProxyResponse.
        :rtype: Proxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ShowInformationAboutDatabaseProxyResponse.


        :param proxy: The proxy of this ShowInformationAboutDatabaseProxyResponse.
        :type: Proxy
        """
        self._proxy = proxy

    @property
    def master_instance(self):
        """Gets the master_instance of this ShowInformationAboutDatabaseProxyResponse.


        :return: The master_instance of this ShowInformationAboutDatabaseProxyResponse.
        :rtype: MasterInstance
        """
        return self._master_instance

    @master_instance.setter
    def master_instance(self, master_instance):
        """Sets the master_instance of this ShowInformationAboutDatabaseProxyResponse.


        :param master_instance: The master_instance of this ShowInformationAboutDatabaseProxyResponse.
        :type: MasterInstance
        """
        self._master_instance = master_instance

    @property
    def readonly_instances(self):
        """Gets the readonly_instances of this ShowInformationAboutDatabaseProxyResponse.

        只读实例信息

        :return: The readonly_instances of this ShowInformationAboutDatabaseProxyResponse.
        :rtype: list[ReadonlyInstances]
        """
        return self._readonly_instances

    @readonly_instances.setter
    def readonly_instances(self, readonly_instances):
        """Sets the readonly_instances of this ShowInformationAboutDatabaseProxyResponse.

        只读实例信息

        :param readonly_instances: The readonly_instances of this ShowInformationAboutDatabaseProxyResponse.
        :type: list[ReadonlyInstances]
        """
        self._readonly_instances = readonly_instances

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
        if not isinstance(other, ShowInformationAboutDatabaseProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
