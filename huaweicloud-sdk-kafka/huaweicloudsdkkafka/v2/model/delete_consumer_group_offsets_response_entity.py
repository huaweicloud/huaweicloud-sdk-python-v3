# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConsumerGroupOffsetsResponseEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'success': 'bool',
        'error_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'success': 'success',
        'error_code': 'error_code'
    }

    def __init__(self, name=None, success=None, error_code=None):
        r"""DeleteConsumerGroupOffsetsResponseEntity

        The model defined in huaweicloud sdk

        :param name: Topic名称
        :type name: str
        :param success: 消费位点删除是否成功
        :type success: bool
        :param error_code: 错误码
        :type error_code: str
        """
        
        

        self._name = None
        self._success = None
        self._error_code = None
        self.discriminator = None

        self.name = name
        self.success = success
        if error_code is not None:
            self.error_code = error_code

    @property
    def name(self):
        r"""Gets the name of this DeleteConsumerGroupOffsetsResponseEntity.

        Topic名称

        :return: The name of this DeleteConsumerGroupOffsetsResponseEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteConsumerGroupOffsetsResponseEntity.

        Topic名称

        :param name: The name of this DeleteConsumerGroupOffsetsResponseEntity.
        :type name: str
        """
        self._name = name

    @property
    def success(self):
        r"""Gets the success of this DeleteConsumerGroupOffsetsResponseEntity.

        消费位点删除是否成功

        :return: The success of this DeleteConsumerGroupOffsetsResponseEntity.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this DeleteConsumerGroupOffsetsResponseEntity.

        消费位点删除是否成功

        :param success: The success of this DeleteConsumerGroupOffsetsResponseEntity.
        :type success: bool
        """
        self._success = success

    @property
    def error_code(self):
        r"""Gets the error_code of this DeleteConsumerGroupOffsetsResponseEntity.

        错误码

        :return: The error_code of this DeleteConsumerGroupOffsetsResponseEntity.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DeleteConsumerGroupOffsetsResponseEntity.

        错误码

        :param error_code: The error_code of this DeleteConsumerGroupOffsetsResponseEntity.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, DeleteConsumerGroupOffsetsResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
