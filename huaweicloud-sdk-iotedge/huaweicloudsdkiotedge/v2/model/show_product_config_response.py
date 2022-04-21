# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProductConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'service_type': 'str',
        'description': 'str',
        'properties': 'list[object]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'service_type': 'service_type',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, service_id=None, service_type=None, description=None, properties=None):
        """ShowProductConfigResponse

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param service_type: 服务类型
        :type service_type: str
        :param description: 描述
        :type description: str
        :param properties: 属性
        :type properties: list[object]
        """
        
        super(ShowProductConfigResponse, self).__init__()

        self._service_id = None
        self._service_type = None
        self._description = None
        self._properties = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if service_type is not None:
            self.service_type = service_type
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def service_id(self):
        """Gets the service_id of this ShowProductConfigResponse.

        服务id

        :return: The service_id of this ShowProductConfigResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ShowProductConfigResponse.

        服务id

        :param service_id: The service_id of this ShowProductConfigResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this ShowProductConfigResponse.

        服务类型

        :return: The service_type of this ShowProductConfigResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ShowProductConfigResponse.

        服务类型

        :param service_type: The service_type of this ShowProductConfigResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def description(self):
        """Gets the description of this ShowProductConfigResponse.

        描述

        :return: The description of this ShowProductConfigResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowProductConfigResponse.

        描述

        :param description: The description of this ShowProductConfigResponse.
        :type description: str
        """
        self._description = description

    @property
    def properties(self):
        """Gets the properties of this ShowProductConfigResponse.

        属性

        :return: The properties of this ShowProductConfigResponse.
        :rtype: list[object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShowProductConfigResponse.

        属性

        :param properties: The properties of this ShowProductConfigResponse.
        :type properties: list[object]
        """
        self._properties = properties

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
        if not isinstance(other, ShowProductConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
