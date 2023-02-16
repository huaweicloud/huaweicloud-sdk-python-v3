# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceUnderNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rf_resource_type': 'str',
        'type': 'str',
        'body': 'PageResourceListParam'
    }

    attribute_map = {
        'rf_resource_type': 'rf_resource_type',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, rf_resource_type=None, type=None, body=None):
        """ListResourceUnderNodeRequest

        The model defined in huaweicloud sdk

        :param rf_resource_type: 云服务资源；同rms服务的provider
        :type rf_resource_type: str
        :param type: 云服务资源类型；同rms服务的type
        :type type: str
        :param body: Body of the ListResourceUnderNodeRequest
        :type body: :class:`huaweicloudsdkaom.v3.PageResourceListParam`
        """
        
        

        self._rf_resource_type = None
        self._type = None
        self._body = None
        self.discriminator = None

        self.rf_resource_type = rf_resource_type
        self.type = type
        if body is not None:
            self.body = body

    @property
    def rf_resource_type(self):
        """Gets the rf_resource_type of this ListResourceUnderNodeRequest.

        云服务资源；同rms服务的provider

        :return: The rf_resource_type of this ListResourceUnderNodeRequest.
        :rtype: str
        """
        return self._rf_resource_type

    @rf_resource_type.setter
    def rf_resource_type(self, rf_resource_type):
        """Sets the rf_resource_type of this ListResourceUnderNodeRequest.

        云服务资源；同rms服务的provider

        :param rf_resource_type: The rf_resource_type of this ListResourceUnderNodeRequest.
        :type rf_resource_type: str
        """
        self._rf_resource_type = rf_resource_type

    @property
    def type(self):
        """Gets the type of this ListResourceUnderNodeRequest.

        云服务资源类型；同rms服务的type

        :return: The type of this ListResourceUnderNodeRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListResourceUnderNodeRequest.

        云服务资源类型；同rms服务的type

        :param type: The type of this ListResourceUnderNodeRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        """Gets the body of this ListResourceUnderNodeRequest.

        :return: The body of this ListResourceUnderNodeRequest.
        :rtype: :class:`huaweicloudsdkaom.v3.PageResourceListParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListResourceUnderNodeRequest.

        :param body: The body of this ListResourceUnderNodeRequest.
        :type body: :class:`huaweicloudsdkaom.v3.PageResourceListParam`
        """
        self._body = body

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
        if not isinstance(other, ListResourceUnderNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
