# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFunctionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'config': 'bool',
        'code': 'bool'
    }

    attribute_map = {
        'config': 'config',
        'code': 'code'
    }

    def __init__(self, config=None, code=None):
        """ExportFunctionRequest - a model defined in huaweicloud sdk"""
        
        

        self._config = None
        self._code = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if code is not None:
            self.code = code

    @property
    def config(self):
        """Gets the config of this ExportFunctionRequest.

        是否导出函数配置

        :return: The config of this ExportFunctionRequest.
        :rtype: bool
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ExportFunctionRequest.

        是否导出函数配置

        :param config: The config of this ExportFunctionRequest.
        :type: bool
        """
        self._config = config

    @property
    def code(self):
        """Gets the code of this ExportFunctionRequest.

        是否导出函数代码

        :return: The code of this ExportFunctionRequest.
        :rtype: bool
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ExportFunctionRequest.

        是否导出函数代码

        :param code: The code of this ExportFunctionRequest.
        :type: bool
        """
        self._code = code

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
        if not isinstance(other, ExportFunctionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
