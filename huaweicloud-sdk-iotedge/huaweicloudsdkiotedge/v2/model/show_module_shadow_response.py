# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModuleShadowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'properties': 'object',
        'properties_update_time': 'object'
    }

    attribute_map = {
        'properties': 'properties',
        'properties_update_time': 'properties_update_time'
    }

    def __init__(self, properties=None, properties_update_time=None):
        r"""ShowModuleShadowResponse

        The model defined in huaweicloud sdk

        :param properties: 应用配置内容
        :type properties: object
        :param properties_update_time: 应用配置更新时间
        :type properties_update_time: object
        """
        
        super(ShowModuleShadowResponse, self).__init__()

        self._properties = None
        self._properties_update_time = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if properties_update_time is not None:
            self.properties_update_time = properties_update_time

    @property
    def properties(self):
        r"""Gets the properties of this ShowModuleShadowResponse.

        应用配置内容

        :return: The properties of this ShowModuleShadowResponse.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ShowModuleShadowResponse.

        应用配置内容

        :param properties: The properties of this ShowModuleShadowResponse.
        :type properties: object
        """
        self._properties = properties

    @property
    def properties_update_time(self):
        r"""Gets the properties_update_time of this ShowModuleShadowResponse.

        应用配置更新时间

        :return: The properties_update_time of this ShowModuleShadowResponse.
        :rtype: object
        """
        return self._properties_update_time

    @properties_update_time.setter
    def properties_update_time(self, properties_update_time):
        r"""Sets the properties_update_time of this ShowModuleShadowResponse.

        应用配置更新时间

        :param properties_update_time: The properties_update_time of this ShowModuleShadowResponse.
        :type properties_update_time: object
        """
        self._properties_update_time = properties_update_time

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
        if not isinstance(other, ShowModuleShadowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
