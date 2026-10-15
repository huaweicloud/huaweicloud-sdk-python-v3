# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetResultDto:

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
        'success': 'bool',
        'error_msg': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'success': 'success',
        'error_msg': 'error_msg'
    }

    def __init__(self, instance_id=None, success=None, error_msg=None):
        r"""BatchSetResultDto

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param success: 是否设置成功（true-成功 false-失败）。
        :type success: bool
        :param error_msg: 失败时的错误信息，成功时为null。
        :type error_msg: str
        """
        
        

        self._instance_id = None
        self._success = None
        self._error_msg = None
        self.discriminator = None

        self.instance_id = instance_id
        self.success = success
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchSetResultDto.

        实例ID。

        :return: The instance_id of this BatchSetResultDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchSetResultDto.

        实例ID。

        :param instance_id: The instance_id of this BatchSetResultDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def success(self):
        r"""Gets the success of this BatchSetResultDto.

        是否设置成功（true-成功 false-失败）。

        :return: The success of this BatchSetResultDto.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this BatchSetResultDto.

        是否设置成功（true-成功 false-失败）。

        :param success: The success of this BatchSetResultDto.
        :type success: bool
        """
        self._success = success

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchSetResultDto.

        失败时的错误信息，成功时为null。

        :return: The error_msg of this BatchSetResultDto.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchSetResultDto.

        失败时的错误信息，成功时为null。

        :param error_msg: The error_msg of this BatchSetResultDto.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, BatchSetResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
