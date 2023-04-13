# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineAssetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relative_path': 'str',
        'asset_type': 'str'
    }

    attribute_map = {
        'relative_path': 'relative_path',
        'asset_type': 'asset_type'
    }

    def __init__(self, relative_path=None, asset_type=None):
        """EngineAssetInfo

        The model defined in huaweicloud sdk

        :param relative_path: 引擎资产的相对路径信息
        :type relative_path: str
        :param asset_type: 引擎资产的类型
        :type asset_type: str
        """
        
        

        self._relative_path = None
        self._asset_type = None
        self.discriminator = None

        if relative_path is not None:
            self.relative_path = relative_path
        if asset_type is not None:
            self.asset_type = asset_type

    @property
    def relative_path(self):
        """Gets the relative_path of this EngineAssetInfo.

        引擎资产的相对路径信息

        :return: The relative_path of this EngineAssetInfo.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this EngineAssetInfo.

        引擎资产的相对路径信息

        :param relative_path: The relative_path of this EngineAssetInfo.
        :type relative_path: str
        """
        self._relative_path = relative_path

    @property
    def asset_type(self):
        """Gets the asset_type of this EngineAssetInfo.

        引擎资产的类型

        :return: The asset_type of this EngineAssetInfo.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this EngineAssetInfo.

        引擎资产的类型

        :param asset_type: The asset_type of this EngineAssetInfo.
        :type asset_type: str
        """
        self._asset_type = asset_type

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
        if not isinstance(other, EngineAssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
