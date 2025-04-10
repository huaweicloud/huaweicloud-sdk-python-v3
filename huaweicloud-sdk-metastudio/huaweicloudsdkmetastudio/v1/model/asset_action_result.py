# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetActionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ret_status': 'str',
        'asset_ids': 'list[str]',
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'ret_status': 'ret_status',
        'asset_ids': 'asset_ids',
        'error_info': 'error_info'
    }

    def __init__(self, ret_status=None, asset_ids=None, error_info=None):
        r"""AssetActionResult

        The model defined in huaweicloud sdk

        :param ret_status: 处理状态。 * SUCCESS：成功 * FAILED：失败
        :type ret_status: str
        :param asset_ids: 资产ID列表
        :type asset_ids: list[str]
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._ret_status = None
        self._asset_ids = None
        self._error_info = None
        self.discriminator = None

        if ret_status is not None:
            self.ret_status = ret_status
        if asset_ids is not None:
            self.asset_ids = asset_ids
        if error_info is not None:
            self.error_info = error_info

    @property
    def ret_status(self):
        r"""Gets the ret_status of this AssetActionResult.

        处理状态。 * SUCCESS：成功 * FAILED：失败

        :return: The ret_status of this AssetActionResult.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        r"""Sets the ret_status of this AssetActionResult.

        处理状态。 * SUCCESS：成功 * FAILED：失败

        :param ret_status: The ret_status of this AssetActionResult.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def asset_ids(self):
        r"""Gets the asset_ids of this AssetActionResult.

        资产ID列表

        :return: The asset_ids of this AssetActionResult.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        r"""Sets the asset_ids of this AssetActionResult.

        资产ID列表

        :param asset_ids: The asset_ids of this AssetActionResult.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

    @property
    def error_info(self):
        r"""Gets the error_info of this AssetActionResult.

        :return: The error_info of this AssetActionResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this AssetActionResult.

        :param error_info: The error_info of this AssetActionResult.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

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
        if not isinstance(other, AssetActionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
