# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionTypeEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'session_type': 'str',
        'resource_type': 'str',
        'cloud_service_type': 'str'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'session_type': 'session_type',
        'resource_type': 'resource_type',
        'cloud_service_type': 'cloud_service_type'
    }

    def __init__(self, resource_spec_code=None, session_type=None, resource_type=None, cloud_service_type=None):
        """SessionTypeEntity

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param session_type: 会话类型
        :type session_type: str
        :param resource_type: 资源类型字段
        :type resource_type: str
        :param cloud_service_type: 资源所属云服务类型编码
        :type cloud_service_type: str
        """
        
        

        self._resource_spec_code = None
        self._session_type = None
        self._resource_type = None
        self._cloud_service_type = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if session_type is not None:
            self.session_type = session_type
        if resource_type is not None:
            self.resource_type = resource_type
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this SessionTypeEntity.

        资源规格编码

        :return: The resource_spec_code of this SessionTypeEntity.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this SessionTypeEntity.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this SessionTypeEntity.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def session_type(self):
        """Gets the session_type of this SessionTypeEntity.

        会话类型

        :return: The session_type of this SessionTypeEntity.
        :rtype: str
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """Sets the session_type of this SessionTypeEntity.

        会话类型

        :param session_type: The session_type of this SessionTypeEntity.
        :type session_type: str
        """
        self._session_type = session_type

    @property
    def resource_type(self):
        """Gets the resource_type of this SessionTypeEntity.

        资源类型字段

        :return: The resource_type of this SessionTypeEntity.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SessionTypeEntity.

        资源类型字段

        :param resource_type: The resource_type of this SessionTypeEntity.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this SessionTypeEntity.

        资源所属云服务类型编码

        :return: The cloud_service_type of this SessionTypeEntity.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this SessionTypeEntity.

        资源所属云服务类型编码

        :param cloud_service_type: The cloud_service_type of this SessionTypeEntity.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

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
        if not isinstance(other, SessionTypeEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
