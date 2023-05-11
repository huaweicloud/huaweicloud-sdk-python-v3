# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncInvokeReservedFunctionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'content_type': 'Content-Type'
    }

    def __init__(self, instance_id=None, content_type=None):
        """AsyncInvokeReservedFunctionResponse

        The model defined in huaweicloud sdk

        :param instance_id: 预留实例id
        :type instance_id: str
        :param content_type: 
        :type content_type: str
        """
        
        super(AsyncInvokeReservedFunctionResponse, self).__init__()

        self._instance_id = None
        self._content_type = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if content_type is not None:
            self.content_type = content_type

    @property
    def instance_id(self):
        """Gets the instance_id of this AsyncInvokeReservedFunctionResponse.

        预留实例id

        :return: The instance_id of this AsyncInvokeReservedFunctionResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AsyncInvokeReservedFunctionResponse.

        预留实例id

        :param instance_id: The instance_id of this AsyncInvokeReservedFunctionResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def content_type(self):
        """Gets the content_type of this AsyncInvokeReservedFunctionResponse.

        :return: The content_type of this AsyncInvokeReservedFunctionResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AsyncInvokeReservedFunctionResponse.

        :param content_type: The content_type of this AsyncInvokeReservedFunctionResponse.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, AsyncInvokeReservedFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
