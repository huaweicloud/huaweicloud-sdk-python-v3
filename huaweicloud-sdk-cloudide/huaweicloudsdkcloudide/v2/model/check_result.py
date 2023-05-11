# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'errors': 'list[CheckResultError]',
        'extension_version_compare': 'str'
    }

    attribute_map = {
        'status': 'status',
        'errors': 'errors',
        'extension_version_compare': 'extension_version_compare'
    }

    def __init__(self, status=None, errors=None, extension_version_compare=None):
        """CheckResult

        The model defined in huaweicloud sdk

        :param status: 解析状态
        :type status: str
        :param errors: 检查插件错误结果集
        :type errors: list[:class:`huaweicloudsdkcloudide.v2.CheckResultError`]
        :param extension_version_compare: 插件版本信息
        :type extension_version_compare: str
        """
        
        

        self._status = None
        self._errors = None
        self._extension_version_compare = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if errors is not None:
            self.errors = errors
        if extension_version_compare is not None:
            self.extension_version_compare = extension_version_compare

    @property
    def status(self):
        """Gets the status of this CheckResult.

        解析状态

        :return: The status of this CheckResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckResult.

        解析状态

        :param status: The status of this CheckResult.
        :type status: str
        """
        self._status = status

    @property
    def errors(self):
        """Gets the errors of this CheckResult.

        检查插件错误结果集

        :return: The errors of this CheckResult.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.CheckResultError`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CheckResult.

        检查插件错误结果集

        :param errors: The errors of this CheckResult.
        :type errors: list[:class:`huaweicloudsdkcloudide.v2.CheckResultError`]
        """
        self._errors = errors

    @property
    def extension_version_compare(self):
        """Gets the extension_version_compare of this CheckResult.

        插件版本信息

        :return: The extension_version_compare of this CheckResult.
        :rtype: str
        """
        return self._extension_version_compare

    @extension_version_compare.setter
    def extension_version_compare(self, extension_version_compare):
        """Sets the extension_version_compare of this CheckResult.

        插件版本信息

        :param extension_version_compare: The extension_version_compare of this CheckResult.
        :type extension_version_compare: str
        """
        self._extension_version_compare = extension_version_compare

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
        if not isinstance(other, CheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
