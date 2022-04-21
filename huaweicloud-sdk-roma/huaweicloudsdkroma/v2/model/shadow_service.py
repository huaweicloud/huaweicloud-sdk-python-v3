# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShadowService:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'service_name': 'str',
        'properties': 'list[ShadowValue]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'service_name': 'service_name',
        'properties': 'properties'
    }

    def __init__(self, service_id=None, service_name=None, properties=None):
        """ShadowService

        The model defined in huaweicloud sdk

        :param service_id: 服务ID
        :type service_id: int
        :param service_name: 服务名称
        :type service_name: str
        :param properties: 影子值
        :type properties: list[:class:`huaweicloudsdkroma.v2.ShadowValue`]
        """
        
        

        self._service_id = None
        self._service_name = None
        self._properties = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if properties is not None:
            self.properties = properties

    @property
    def service_id(self):
        """Gets the service_id of this ShadowService.

        服务ID

        :return: The service_id of this ShadowService.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ShadowService.

        服务ID

        :param service_id: The service_id of this ShadowService.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this ShadowService.

        服务名称

        :return: The service_name of this ShadowService.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ShadowService.

        服务名称

        :param service_name: The service_name of this ShadowService.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def properties(self):
        """Gets the properties of this ShadowService.

        影子值

        :return: The properties of this ShadowService.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ShadowValue`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShadowService.

        影子值

        :param properties: The properties of this ShadowService.
        :type properties: list[:class:`huaweicloudsdkroma.v2.ShadowValue`]
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
        if not isinstance(other, ShadowService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
