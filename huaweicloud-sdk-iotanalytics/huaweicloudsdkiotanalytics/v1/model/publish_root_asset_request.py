# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishRootAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_asset_id': 'str'
    }

    attribute_map = {
        'root_asset_id': 'root_asset_id'
    }

    def __init__(self, root_asset_id=None):
        r"""PublishRootAssetRequest

        The model defined in huaweicloud sdk

        :param root_asset_id: 根资产ID
        :type root_asset_id: str
        """
        
        

        self._root_asset_id = None
        self.discriminator = None

        self.root_asset_id = root_asset_id

    @property
    def root_asset_id(self):
        r"""Gets the root_asset_id of this PublishRootAssetRequest.

        根资产ID

        :return: The root_asset_id of this PublishRootAssetRequest.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        r"""Sets the root_asset_id of this PublishRootAssetRequest.

        根资产ID

        :param root_asset_id: The root_asset_id of this PublishRootAssetRequest.
        :type root_asset_id: str
        """
        self._root_asset_id = root_asset_id

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
        if not isinstance(other, PublishRootAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
