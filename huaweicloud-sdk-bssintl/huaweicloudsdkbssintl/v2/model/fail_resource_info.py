# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'resource_id': 'resource_id'
    }

    def __init__(self, error_code=None, error_msg=None, resource_id=None):
        """FailResourceInfo

        The model defined in huaweicloud sdk

        :param error_code: |参数名称：错误码| |参数约束及描述：错误码|
        :type error_code: str
        :param error_msg: |参数名称：错误描述| |参数约束及描述：错误描述|
        :type error_msg: str
        :param resource_id: |参数名称：资源ID| |参数约束及描述：资源ID|
        :type resource_id: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._resource_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def error_code(self):
        """Gets the error_code of this FailResourceInfo.

        |参数名称：错误码| |参数约束及描述：错误码|

        :return: The error_code of this FailResourceInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this FailResourceInfo.

        |参数名称：错误码| |参数约束及描述：错误码|

        :param error_code: The error_code of this FailResourceInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this FailResourceInfo.

        |参数名称：错误描述| |参数约束及描述：错误描述|

        :return: The error_msg of this FailResourceInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this FailResourceInfo.

        |参数名称：错误描述| |参数约束及描述：错误描述|

        :param error_msg: The error_msg of this FailResourceInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def resource_id(self):
        """Gets the resource_id of this FailResourceInfo.

        |参数名称：资源ID| |参数约束及描述：资源ID|

        :return: The resource_id of this FailResourceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FailResourceInfo.

        |参数名称：资源ID| |参数约束及描述：资源ID|

        :param resource_id: The resource_id of this FailResourceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, FailResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
