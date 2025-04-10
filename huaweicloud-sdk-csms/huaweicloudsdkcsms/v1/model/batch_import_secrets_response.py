# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchImportSecretsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_list': 'list[ErrorInfo]',
        'total': 'int',
        'success': 'int',
        'failed': 'int'
    }

    attribute_map = {
        'error_list': 'error_list',
        'total': 'total',
        'success': 'success',
        'failed': 'failed'
    }

    def __init__(self, error_list=None, total=None, success=None, failed=None):
        r"""BatchImportSecretsResponse

        The model defined in huaweicloud sdk

        :param error_list: 失败描述
        :type error_list: list[:class:`huaweicloudsdkcsms.v1.ErrorInfo`]
        :param total: 总条数
        :type total: int
        :param success: 成功条数
        :type success: int
        :param failed: 失败条数
        :type failed: int
        """
        
        super(BatchImportSecretsResponse, self).__init__()

        self._error_list = None
        self._total = None
        self._success = None
        self._failed = None
        self.discriminator = None

        if error_list is not None:
            self.error_list = error_list
        if total is not None:
            self.total = total
        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed

    @property
    def error_list(self):
        r"""Gets the error_list of this BatchImportSecretsResponse.

        失败描述

        :return: The error_list of this BatchImportSecretsResponse.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.ErrorInfo`]
        """
        return self._error_list

    @error_list.setter
    def error_list(self, error_list):
        r"""Sets the error_list of this BatchImportSecretsResponse.

        失败描述

        :param error_list: The error_list of this BatchImportSecretsResponse.
        :type error_list: list[:class:`huaweicloudsdkcsms.v1.ErrorInfo`]
        """
        self._error_list = error_list

    @property
    def total(self):
        r"""Gets the total of this BatchImportSecretsResponse.

        总条数

        :return: The total of this BatchImportSecretsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BatchImportSecretsResponse.

        总条数

        :param total: The total of this BatchImportSecretsResponse.
        :type total: int
        """
        self._total = total

    @property
    def success(self):
        r"""Gets the success of this BatchImportSecretsResponse.

        成功条数

        :return: The success of this BatchImportSecretsResponse.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this BatchImportSecretsResponse.

        成功条数

        :param success: The success of this BatchImportSecretsResponse.
        :type success: int
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this BatchImportSecretsResponse.

        失败条数

        :return: The failed of this BatchImportSecretsResponse.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this BatchImportSecretsResponse.

        失败条数

        :param failed: The failed of this BatchImportSecretsResponse.
        :type failed: int
        """
        self._failed = failed

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
        if not isinstance(other, BatchImportSecretsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
