# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceChangeLevelItem:

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
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'result': 'result',
        'message': 'message'
    }

    def __init__(self, id=None, result=None, message=None):
        r"""ResourceChangeLevelItem

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param result: 结果：succeed-成功，failed-失败
        :type result: str
        :param message: 错误信息
        :type message: str
        """
        
        

        self._id = None
        self._result = None
        self._message = None
        self.discriminator = None

        self.id = id
        self.result = result
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this ResourceChangeLevelItem.

        资源ID

        :return: The id of this ResourceChangeLevelItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceChangeLevelItem.

        资源ID

        :param id: The id of this ResourceChangeLevelItem.
        :type id: str
        """
        self._id = id

    @property
    def result(self):
        r"""Gets the result of this ResourceChangeLevelItem.

        结果：succeed-成功，failed-失败

        :return: The result of this ResourceChangeLevelItem.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ResourceChangeLevelItem.

        结果：succeed-成功，failed-失败

        :param result: The result of this ResourceChangeLevelItem.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this ResourceChangeLevelItem.

        错误信息

        :return: The message of this ResourceChangeLevelItem.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ResourceChangeLevelItem.

        错误信息

        :param message: The message of this ResourceChangeLevelItem.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ResourceChangeLevelItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
