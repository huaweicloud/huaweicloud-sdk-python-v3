# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeRunInfoInnerError:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'error_body': 'NodeRunInfoInnerErrorErrorBody'
    }

    attribute_map = {
        'is_success': 'is_success',
        'error_body': 'error_body'
    }

    def __init__(self, is_success=None, error_body=None):
        r"""NodeRunInfoInnerError

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param error_body: 
        :type error_body: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerErrorErrorBody`
        """
        
        

        self._is_success = None
        self._error_body = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if error_body is not None:
            self.error_body = error_body

    @property
    def is_success(self):
        r"""Gets the is_success of this NodeRunInfoInnerError.

        是否成功

        :return: The is_success of this NodeRunInfoInnerError.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this NodeRunInfoInnerError.

        是否成功

        :param is_success: The is_success of this NodeRunInfoInnerError.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def error_body(self):
        r"""Gets the error_body of this NodeRunInfoInnerError.

        :return: The error_body of this NodeRunInfoInnerError.
        :rtype: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerErrorErrorBody`
        """
        return self._error_body

    @error_body.setter
    def error_body(self, error_body):
        r"""Sets the error_body of this NodeRunInfoInnerError.

        :param error_body: The error_body of this NodeRunInfoInnerError.
        :type error_body: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerErrorErrorBody`
        """
        self._error_body = error_body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeRunInfoInnerError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
