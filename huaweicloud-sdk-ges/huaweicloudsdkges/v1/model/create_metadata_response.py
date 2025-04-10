# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_message': 'str',
        'error_code': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, error_message=None, error_code=None, id=None, name=None):
        r"""CreateMetadataResponse

        The model defined in huaweicloud sdk

        :param error_message: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。
        :type error_message: str
        :param error_code: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。
        :type error_code: str
        :param id: 元数据ID。
        :type id: str
        :param name: 元数据名字。
        :type name: str
        """
        
        super(CreateMetadataResponse, self).__init__()

        self._error_message = None
        self._error_code = None
        self._id = None
        self._name = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def error_message(self):
        r"""Gets the error_message of this CreateMetadataResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this CreateMetadataResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this CreateMetadataResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this CreateMetadataResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        r"""Gets the error_code of this CreateMetadataResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this CreateMetadataResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreateMetadataResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this CreateMetadataResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def id(self):
        r"""Gets the id of this CreateMetadataResponse.

        元数据ID。

        :return: The id of this CreateMetadataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateMetadataResponse.

        元数据ID。

        :param id: The id of this CreateMetadataResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateMetadataResponse.

        元数据名字。

        :return: The name of this CreateMetadataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMetadataResponse.

        元数据名字。

        :param name: The name of this CreateMetadataResponse.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
