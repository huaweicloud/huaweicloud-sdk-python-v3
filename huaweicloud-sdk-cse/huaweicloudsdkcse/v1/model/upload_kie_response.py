# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadKieResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[GetKieConfigs]',
        'failure': 'list[DocFailedOfUpload]'
    }

    attribute_map = {
        'success': 'success',
        'failure': 'failure'
    }

    def __init__(self, success=None, failure=None):
        """UploadKieResponse

        The model defined in huaweicloud sdk

        :param success: 导入成功的配置项列表。
        :type success: list[:class:`huaweicloudsdkcse.v1.GetKieConfigs`]
        :param failure: 导入失败的配置项及其错误列表。
        :type failure: list[:class:`huaweicloudsdkcse.v1.DocFailedOfUpload`]
        """
        
        super(UploadKieResponse, self).__init__()

        self._success = None
        self._failure = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure

    @property
    def success(self):
        """Gets the success of this UploadKieResponse.

        导入成功的配置项列表。

        :return: The success of this UploadKieResponse.
        :rtype: list[:class:`huaweicloudsdkcse.v1.GetKieConfigs`]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UploadKieResponse.

        导入成功的配置项列表。

        :param success: The success of this UploadKieResponse.
        :type success: list[:class:`huaweicloudsdkcse.v1.GetKieConfigs`]
        """
        self._success = success

    @property
    def failure(self):
        """Gets the failure of this UploadKieResponse.

        导入失败的配置项及其错误列表。

        :return: The failure of this UploadKieResponse.
        :rtype: list[:class:`huaweicloudsdkcse.v1.DocFailedOfUpload`]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this UploadKieResponse.

        导入失败的配置项及其错误列表。

        :param failure: The failure of this UploadKieResponse.
        :type failure: list[:class:`huaweicloudsdkcse.v1.DocFailedOfUpload`]
        """
        self._failure = failure

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
        if not isinstance(other, UploadKieResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
