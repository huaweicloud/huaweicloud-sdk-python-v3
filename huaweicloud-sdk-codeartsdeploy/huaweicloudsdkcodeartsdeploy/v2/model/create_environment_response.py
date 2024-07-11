# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnvironmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id'
    }

    def __init__(self, status=None, id=None):
        """CreateEnvironmentResponse

        The model defined in huaweicloud sdk

        :param status: 请求成功失败状态
        :type status: str
        :param id: 环境id
        :type id: str
        """
        
        super(CreateEnvironmentResponse, self).__init__()

        self._status = None
        self._id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if id is not None:
            self.id = id

    @property
    def status(self):
        """Gets the status of this CreateEnvironmentResponse.

        请求成功失败状态

        :return: The status of this CreateEnvironmentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateEnvironmentResponse.

        请求成功失败状态

        :param status: The status of this CreateEnvironmentResponse.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this CreateEnvironmentResponse.

        环境id

        :return: The id of this CreateEnvironmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEnvironmentResponse.

        环境id

        :param id: The id of this CreateEnvironmentResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CreateEnvironmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
