# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VmOperateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, desktop_id=None, desktop_name=None, error_code=None, error_msg=None):
        """VmOperateResult

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param error_code: 操作失败的错误码。
        :type error_code: str
        :param error_msg: 操作失败的原因描述。
        :type error_msg: str
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def desktop_id(self):
        """Gets the desktop_id of this VmOperateResult.

        桌面ID。

        :return: The desktop_id of this VmOperateResult.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this VmOperateResult.

        桌面ID。

        :param desktop_id: The desktop_id of this VmOperateResult.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this VmOperateResult.

        桌面名称。

        :return: The desktop_name of this VmOperateResult.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this VmOperateResult.

        桌面名称。

        :param desktop_name: The desktop_name of this VmOperateResult.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def error_code(self):
        """Gets the error_code of this VmOperateResult.

        操作失败的错误码。

        :return: The error_code of this VmOperateResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this VmOperateResult.

        操作失败的错误码。

        :param error_code: The error_code of this VmOperateResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this VmOperateResult.

        操作失败的原因描述。

        :return: The error_msg of this VmOperateResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this VmOperateResult.

        操作失败的原因描述。

        :param error_msg: The error_msg of this VmOperateResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, VmOperateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
