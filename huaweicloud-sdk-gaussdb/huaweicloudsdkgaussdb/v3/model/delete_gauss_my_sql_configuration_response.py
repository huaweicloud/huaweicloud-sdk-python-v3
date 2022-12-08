# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGaussMySqlConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_id': 'str',
        'configuration_name': 'str'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'configuration_name': 'configuration_name'
    }

    def __init__(self, configuration_id=None, configuration_name=None):
        """DeleteGaussMySqlConfigurationResponse

        The model defined in huaweicloud sdk

        :param configuration_id: 参数模板ID。
        :type configuration_id: str
        :param configuration_name: 参数模板名称。
        :type configuration_name: str
        """
        
        super(DeleteGaussMySqlConfigurationResponse, self).__init__()

        self._configuration_id = None
        self._configuration_name = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if configuration_name is not None:
            self.configuration_name = configuration_name

    @property
    def configuration_id(self):
        """Gets the configuration_id of this DeleteGaussMySqlConfigurationResponse.

        参数模板ID。

        :return: The configuration_id of this DeleteGaussMySqlConfigurationResponse.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this DeleteGaussMySqlConfigurationResponse.

        参数模板ID。

        :param configuration_id: The configuration_id of this DeleteGaussMySqlConfigurationResponse.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def configuration_name(self):
        """Gets the configuration_name of this DeleteGaussMySqlConfigurationResponse.

        参数模板名称。

        :return: The configuration_name of this DeleteGaussMySqlConfigurationResponse.
        :rtype: str
        """
        return self._configuration_name

    @configuration_name.setter
    def configuration_name(self, configuration_name):
        """Sets the configuration_name of this DeleteGaussMySqlConfigurationResponse.

        参数模板名称。

        :param configuration_name: The configuration_name of this DeleteGaussMySqlConfigurationResponse.
        :type configuration_name: str
        """
        self._configuration_name = configuration_name

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
        if not isinstance(other, DeleteGaussMySqlConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
