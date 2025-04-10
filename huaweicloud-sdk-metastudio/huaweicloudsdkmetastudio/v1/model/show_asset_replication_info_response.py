# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetReplicationInfoResponse(SdkResponse):

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
        'encryption_info': 'ReplicationEncInfo',
        'expire_time': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_info': 'asset_info',
        'encryption_info': 'encryption_info',
        'expire_time': 'expire_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, asset_id=None, asset_info=None, encryption_info=None, expire_time=None, x_request_id=None):
        r"""ShowAssetReplicationInfoResponse

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_info: 加密后的资产信息。
        :type asset_info: str
        :param encryption_info: 
        :type encryption_info: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        :param expire_time: 过期时间
        :type expire_time: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAssetReplicationInfoResponse, self).__init__()

        self._asset_id = None
        self._asset_info = None
        self._encryption_info = None
        self._expire_time = None
        self._x_request_id = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_info is not None:
            self.asset_info = asset_info
        if encryption_info is not None:
            self.encryption_info = encryption_info
        if expire_time is not None:
            self.expire_time = expire_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ShowAssetReplicationInfoResponse.

        资产ID。

        :return: The asset_id of this ShowAssetReplicationInfoResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ShowAssetReplicationInfoResponse.

        资产ID。

        :param asset_id: The asset_id of this ShowAssetReplicationInfoResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_info(self):
        r"""Gets the asset_info of this ShowAssetReplicationInfoResponse.

        加密后的资产信息。

        :return: The asset_info of this ShowAssetReplicationInfoResponse.
        :rtype: str
        """
        return self._asset_info

    @asset_info.setter
    def asset_info(self, asset_info):
        r"""Sets the asset_info of this ShowAssetReplicationInfoResponse.

        加密后的资产信息。

        :param asset_info: The asset_info of this ShowAssetReplicationInfoResponse.
        :type asset_info: str
        """
        self._asset_info = asset_info

    @property
    def encryption_info(self):
        r"""Gets the encryption_info of this ShowAssetReplicationInfoResponse.

        :return: The encryption_info of this ShowAssetReplicationInfoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        """
        return self._encryption_info

    @encryption_info.setter
    def encryption_info(self, encryption_info):
        r"""Sets the encryption_info of this ShowAssetReplicationInfoResponse.

        :param encryption_info: The encryption_info of this ShowAssetReplicationInfoResponse.
        :type encryption_info: :class:`huaweicloudsdkmetastudio.v1.ReplicationEncInfo`
        """
        self._encryption_info = encryption_info

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowAssetReplicationInfoResponse.

        过期时间

        :return: The expire_time of this ShowAssetReplicationInfoResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowAssetReplicationInfoResponse.

        过期时间

        :param expire_time: The expire_time of this ShowAssetReplicationInfoResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowAssetReplicationInfoResponse.

        :return: The x_request_id of this ShowAssetReplicationInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowAssetReplicationInfoResponse.

        :param x_request_id: The x_request_id of this ShowAssetReplicationInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowAssetReplicationInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
