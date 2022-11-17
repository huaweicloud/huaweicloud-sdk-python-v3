# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'buket': 'str',
        'key': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'buket': 'buket',
        'key': 'key'
    }

    def __init__(self, endpoint=None, buket=None, key=None):
        """ObsProperties

        The model defined in huaweicloud sdk

        :param endpoint: obs的终端地址，比如：https://obs.region_name.external_domain_name.com。
        :type endpoint: str
        :param buket: 软件包在obs的桶名。
        :type buket: str
        :param key: obs桶中的对象，一般是软件包名，有文件夹的话要加上文件夹的路径。比如test.jar或者demo/test.jar。
        :type key: str
        """
        
        

        self._endpoint = None
        self._buket = None
        self._key = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if buket is not None:
            self.buket = buket
        if key is not None:
            self.key = key

    @property
    def endpoint(self):
        """Gets the endpoint of this ObsProperties.

        obs的终端地址，比如：https://obs.region_name.external_domain_name.com。

        :return: The endpoint of this ObsProperties.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ObsProperties.

        obs的终端地址，比如：https://obs.region_name.external_domain_name.com。

        :param endpoint: The endpoint of this ObsProperties.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def buket(self):
        """Gets the buket of this ObsProperties.

        软件包在obs的桶名。

        :return: The buket of this ObsProperties.
        :rtype: str
        """
        return self._buket

    @buket.setter
    def buket(self, buket):
        """Sets the buket of this ObsProperties.

        软件包在obs的桶名。

        :param buket: The buket of this ObsProperties.
        :type buket: str
        """
        self._buket = buket

    @property
    def key(self):
        """Gets the key of this ObsProperties.

        obs桶中的对象，一般是软件包名，有文件夹的话要加上文件夹的路径。比如test.jar或者demo/test.jar。

        :return: The key of this ObsProperties.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ObsProperties.

        obs桶中的对象，一般是软件包名，有文件夹的话要加上文件夹的路径。比如test.jar或者demo/test.jar。

        :param key: The key of this ObsProperties.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, ObsProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
