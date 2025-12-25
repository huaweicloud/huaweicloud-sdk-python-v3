# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAdhocQueryResultResponseBodyTips:

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
        'error_key': 'str',
        'module_name': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_key': 'error_key',
        'module_name': 'module_name'
    }

    def __init__(self, error_code=None, error_key=None, module_name=None):
        r"""ShowAdhocQueryResultResponseBodyTips

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_key: 错误键
        :type error_key: str
        :param module_name: 模块名称
        :type module_name: str
        """
        
        

        self._error_code = None
        self._error_key = None
        self._module_name = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_key is not None:
            self.error_key = error_key
        if module_name is not None:
            self.module_name = module_name

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowAdhocQueryResultResponseBodyTips.

        错误码

        :return: The error_code of this ShowAdhocQueryResultResponseBodyTips.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowAdhocQueryResultResponseBodyTips.

        错误码

        :param error_code: The error_code of this ShowAdhocQueryResultResponseBodyTips.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_key(self):
        r"""Gets the error_key of this ShowAdhocQueryResultResponseBodyTips.

        错误键

        :return: The error_key of this ShowAdhocQueryResultResponseBodyTips.
        :rtype: str
        """
        return self._error_key

    @error_key.setter
    def error_key(self, error_key):
        r"""Sets the error_key of this ShowAdhocQueryResultResponseBodyTips.

        错误键

        :param error_key: The error_key of this ShowAdhocQueryResultResponseBodyTips.
        :type error_key: str
        """
        self._error_key = error_key

    @property
    def module_name(self):
        r"""Gets the module_name of this ShowAdhocQueryResultResponseBodyTips.

        模块名称

        :return: The module_name of this ShowAdhocQueryResultResponseBodyTips.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this ShowAdhocQueryResultResponseBodyTips.

        模块名称

        :param module_name: The module_name of this ShowAdhocQueryResultResponseBodyTips.
        :type module_name: str
        """
        self._module_name = module_name

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
        if not isinstance(other, ShowAdhocQueryResultResponseBodyTips):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
