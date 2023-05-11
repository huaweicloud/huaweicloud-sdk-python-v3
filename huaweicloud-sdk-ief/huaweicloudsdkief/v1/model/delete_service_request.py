# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteServiceRequest:

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
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, service_id=None, ief_instance_id=None):
        """DeleteServiceRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务ID
        :type service_id: str
        :param ief_instance_id: 铂金版实例ID
        :type ief_instance_id: str
        """
        
        

        self._service_id = None
        self._ief_instance_id = None
        self.discriminator = None

        self.service_id = service_id
        self.ief_instance_id = ief_instance_id

    @property
    def service_id(self):
        """Gets the service_id of this DeleteServiceRequest.

        服务ID

        :return: The service_id of this DeleteServiceRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DeleteServiceRequest.

        服务ID

        :param service_id: The service_id of this DeleteServiceRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this DeleteServiceRequest.

        铂金版实例ID

        :return: The ief_instance_id of this DeleteServiceRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this DeleteServiceRequest.

        铂金版实例ID

        :param ief_instance_id: The ief_instance_id of this DeleteServiceRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, DeleteServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
