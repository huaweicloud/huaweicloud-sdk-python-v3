# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationAssetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_info': 'str',
        'encryption_info': 'ReplicationEncInfo'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_info': 'asset_info',
        'encryption_info': 'encryption_info'
    }

    def __init__(self, asset_id=None, asset_info=None, encryption_info=None):
        """ReplicationAssetInfo

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_info: 加密后的资产信息。
        :type asset_info: str
        :param encryption_info: 
        :type encryption_info: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        """
        
        

        self._asset_id = None
        self._asset_info = None
        self._encryption_info = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_info is not None:
            self.asset_info = asset_info
        if encryption_info is not None:
            self.encryption_info = encryption_info

    @property
    def asset_id(self):
        """Gets the asset_id of this ReplicationAssetInfo.

        资产ID。

        :return: The asset_id of this ReplicationAssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ReplicationAssetInfo.

        资产ID。

        :param asset_id: The asset_id of this ReplicationAssetInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_info(self):
        """Gets the asset_info of this ReplicationAssetInfo.

        加密后的资产信息。

        :return: The asset_info of this ReplicationAssetInfo.
        :rtype: str
        """
        return self._asset_info

    @asset_info.setter
    def asset_info(self, asset_info):
        """Sets the asset_info of this ReplicationAssetInfo.

        加密后的资产信息。

        :param asset_info: The asset_info of this ReplicationAssetInfo.
        :type asset_info: str
        """
        self._asset_info = asset_info

    @property
    def encryption_info(self):
        """Gets the encryption_info of this ReplicationAssetInfo.

        :return: The encryption_info of this ReplicationAssetInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        """
        return self._encryption_info

    @encryption_info.setter
    def encryption_info(self, encryption_info):
        """Sets the encryption_info of this ReplicationAssetInfo.

        :param encryption_info: The encryption_info of this ReplicationAssetInfo.
        :type encryption_info: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        """
        self._encryption_info = encryption_info

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
        if not isinstance(other, ReplicationAssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
