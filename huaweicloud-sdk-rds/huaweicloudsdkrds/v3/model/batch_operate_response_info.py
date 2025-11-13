# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'result': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'result': 'result',
        'error_message': 'error_message'
    }

    def __init__(self, id=None, result=None, error_message=None):
        r"""BatchOperateResponseInfo

        The model defined in huaweicloud sdk

        :param id: 订阅ID。
        :type id: str
        :param result: 执行结果。success，failure
        :type result: str
        :param error_message: 失败报错。
        :type error_message: str
        """
        
        

        self._id = None
        self._result = None
        self._error_message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if result is not None:
            self.result = result
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        r"""Gets the id of this BatchOperateResponseInfo.

        订阅ID。

        :return: The id of this BatchOperateResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchOperateResponseInfo.

        订阅ID。

        :param id: The id of this BatchOperateResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def result(self):
        r"""Gets the result of this BatchOperateResponseInfo.

        执行结果。success，failure

        :return: The result of this BatchOperateResponseInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BatchOperateResponseInfo.

        执行结果。success，failure

        :param result: The result of this BatchOperateResponseInfo.
        :type result: str
        """
        self._result = result

    @property
    def error_message(self):
        r"""Gets the error_message of this BatchOperateResponseInfo.

        失败报错。

        :return: The error_message of this BatchOperateResponseInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this BatchOperateResponseInfo.

        失败报错。

        :param error_message: The error_message of this BatchOperateResponseInfo.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, BatchOperateResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
