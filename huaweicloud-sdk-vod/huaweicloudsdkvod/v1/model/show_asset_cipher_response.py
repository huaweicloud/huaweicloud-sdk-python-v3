# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetCipherResponse(SdkResponse):

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
        'edk': 'str',
        'dk': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'edk': 'edk',
        'dk': 'dk'
    }

    def __init__(self, asset_id=None, edk=None, dk=None):
        """ShowAssetCipherResponse

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param edk: 密钥密文。
        :type edk: str
        :param dk: 密钥明文。
        :type dk: str
        """
        
        super(ShowAssetCipherResponse, self).__init__()

        self._asset_id = None
        self._edk = None
        self._dk = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if edk is not None:
            self.edk = edk
        if dk is not None:
            self.dk = dk

    @property
    def asset_id(self):
        """Gets the asset_id of this ShowAssetCipherResponse.

        媒资ID。

        :return: The asset_id of this ShowAssetCipherResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ShowAssetCipherResponse.

        媒资ID。

        :param asset_id: The asset_id of this ShowAssetCipherResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def edk(self):
        """Gets the edk of this ShowAssetCipherResponse.

        密钥密文。

        :return: The edk of this ShowAssetCipherResponse.
        :rtype: str
        """
        return self._edk

    @edk.setter
    def edk(self, edk):
        """Sets the edk of this ShowAssetCipherResponse.

        密钥密文。

        :param edk: The edk of this ShowAssetCipherResponse.
        :type edk: str
        """
        self._edk = edk

    @property
    def dk(self):
        """Gets the dk of this ShowAssetCipherResponse.

        密钥明文。

        :return: The dk of this ShowAssetCipherResponse.
        :rtype: str
        """
        return self._dk

    @dk.setter
    def dk(self, dk):
        """Sets the dk of this ShowAssetCipherResponse.

        密钥明文。

        :param dk: The dk of this ShowAssetCipherResponse.
        :type dk: str
        """
        self._dk = dk

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
        if not isinstance(other, ShowAssetCipherResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
