# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'asset_id': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'asset_id': 'asset_id',
        'mode': 'mode'
    }

    def __init__(self, x_app_user_id=None, asset_id=None, mode=None):
        """DeleteAssetRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param asset_id: 资产ID。
        :type asset_id: str
        :param mode: 删除模式
        :type mode: str
        """
        
        

        self._x_app_user_id = None
        self._asset_id = None
        self._mode = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.asset_id = asset_id
        if mode is not None:
            self.mode = mode

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this DeleteAssetRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this DeleteAssetRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this DeleteAssetRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this DeleteAssetRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def asset_id(self):
        """Gets the asset_id of this DeleteAssetRequest.

        资产ID。

        :return: The asset_id of this DeleteAssetRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this DeleteAssetRequest.

        资产ID。

        :param asset_id: The asset_id of this DeleteAssetRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def mode(self):
        """Gets the mode of this DeleteAssetRequest.

        删除模式

        :return: The mode of this DeleteAssetRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DeleteAssetRequest.

        删除模式

        :param mode: The mode of this DeleteAssetRequest.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, DeleteAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
