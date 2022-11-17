# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclBindingBatchFailure:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bind_id': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'api_id': 'str',
        'api_name': 'str'
    }

    attribute_map = {
        'bind_id': 'bind_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'api_id': 'api_id',
        'api_name': 'api_name'
    }

    def __init__(self, bind_id=None, error_code=None, error_msg=None, api_id=None, api_name=None):
        """AclBindingBatchFailure

        The model defined in huaweicloud sdk

        :param bind_id: 解除绑定失败的API和ACL绑定关系ID
        :type bind_id: str
        :param error_code: 解除绑定失败的错误码
        :type error_code: str
        :param error_msg: 解除绑定失败的错误信息
        :type error_msg: str
        :param api_id: 解除绑定失败的API的ID
        :type api_id: str
        :param api_name: 解除绑定失败的API的名称
        :type api_name: str
        """
        
        

        self._bind_id = None
        self._error_code = None
        self._error_msg = None
        self._api_id = None
        self._api_name = None
        self.discriminator = None

        if bind_id is not None:
            self.bind_id = bind_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name

    @property
    def bind_id(self):
        """Gets the bind_id of this AclBindingBatchFailure.

        解除绑定失败的API和ACL绑定关系ID

        :return: The bind_id of this AclBindingBatchFailure.
        :rtype: str
        """
        return self._bind_id

    @bind_id.setter
    def bind_id(self, bind_id):
        """Sets the bind_id of this AclBindingBatchFailure.

        解除绑定失败的API和ACL绑定关系ID

        :param bind_id: The bind_id of this AclBindingBatchFailure.
        :type bind_id: str
        """
        self._bind_id = bind_id

    @property
    def error_code(self):
        """Gets the error_code of this AclBindingBatchFailure.

        解除绑定失败的错误码

        :return: The error_code of this AclBindingBatchFailure.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AclBindingBatchFailure.

        解除绑定失败的错误码

        :param error_code: The error_code of this AclBindingBatchFailure.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this AclBindingBatchFailure.

        解除绑定失败的错误信息

        :return: The error_msg of this AclBindingBatchFailure.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this AclBindingBatchFailure.

        解除绑定失败的错误信息

        :param error_msg: The error_msg of this AclBindingBatchFailure.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def api_id(self):
        """Gets the api_id of this AclBindingBatchFailure.

        解除绑定失败的API的ID

        :return: The api_id of this AclBindingBatchFailure.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AclBindingBatchFailure.

        解除绑定失败的API的ID

        :param api_id: The api_id of this AclBindingBatchFailure.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this AclBindingBatchFailure.

        解除绑定失败的API的名称

        :return: The api_name of this AclBindingBatchFailure.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this AclBindingBatchFailure.

        解除绑定失败的API的名称

        :param api_name: The api_name of this AclBindingBatchFailure.
        :type api_name: str
        """
        self._api_name = api_name

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
        if not isinstance(other, AclBindingBatchFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
