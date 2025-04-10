# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailureResources:

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
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, id=None, code=None, message=None):
        r"""FailureResources

        The model defined in huaweicloud sdk

        :param id: - 功能说明：更新失败的带宽id
        :type id: str
        :param code: - 功能说明：错误码
        :type code: str
        :param message: - 功能说明：错误信息
        :type message: str
        """
        
        

        self._id = None
        self._code = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this FailureResources.

        - 功能说明：更新失败的带宽id

        :return: The id of this FailureResources.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FailureResources.

        - 功能说明：更新失败的带宽id

        :param id: The id of this FailureResources.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this FailureResources.

        - 功能说明：错误码

        :return: The code of this FailureResources.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this FailureResources.

        - 功能说明：错误码

        :param code: The code of this FailureResources.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this FailureResources.

        - 功能说明：错误信息

        :return: The message of this FailureResources.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this FailureResources.

        - 功能说明：错误信息

        :param message: The message of this FailureResources.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, FailureResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
