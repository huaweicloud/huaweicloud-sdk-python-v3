# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckStarrocksParamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_starrocks_params_responce': 'list[ParamGroupParameterDifferences]'
    }

    attribute_map = {
        'check_starrocks_params_responce': 'check_starrocks_params_responce'
    }

    def __init__(self, check_starrocks_params_responce=None):
        """CheckStarrocksParamsResponse

        The model defined in huaweicloud sdk

        :param check_starrocks_params_responce: 参数之间区别的集合。
        :type check_starrocks_params_responce: list[:class:`huaweicloudsdkgaussdb.v3.ParamGroupParameterDifferences`]
        """
        
        super(CheckStarrocksParamsResponse, self).__init__()

        self._check_starrocks_params_responce = None
        self.discriminator = None

        if check_starrocks_params_responce is not None:
            self.check_starrocks_params_responce = check_starrocks_params_responce

    @property
    def check_starrocks_params_responce(self):
        """Gets the check_starrocks_params_responce of this CheckStarrocksParamsResponse.

        参数之间区别的集合。

        :return: The check_starrocks_params_responce of this CheckStarrocksParamsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ParamGroupParameterDifferences`]
        """
        return self._check_starrocks_params_responce

    @check_starrocks_params_responce.setter
    def check_starrocks_params_responce(self, check_starrocks_params_responce):
        """Sets the check_starrocks_params_responce of this CheckStarrocksParamsResponse.

        参数之间区别的集合。

        :param check_starrocks_params_responce: The check_starrocks_params_responce of this CheckStarrocksParamsResponse.
        :type check_starrocks_params_responce: list[:class:`huaweicloudsdkgaussdb.v3.ParamGroupParameterDifferences`]
        """
        self._check_starrocks_params_responce = check_starrocks_params_responce

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
        if not isinstance(other, CheckStarrocksParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
