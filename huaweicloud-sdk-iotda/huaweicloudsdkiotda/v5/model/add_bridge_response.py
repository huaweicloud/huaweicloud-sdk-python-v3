# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBridgeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridge_id': 'str',
        'bridge_name': 'str',
        'auth_info': 'BridgeAuthInfo',
        'create_time': 'str'
    }

    attribute_map = {
        'bridge_id': 'bridge_id',
        'bridge_name': 'bridge_name',
        'auth_info': 'auth_info',
        'create_time': 'create_time'
    }

    def __init__(self, bridge_id=None, bridge_name=None, auth_info=None, create_time=None):
        r"""AddBridgeResponse

        The model defined in huaweicloud sdk

        :param bridge_id: 网桥ID，用于唯一标识一个网桥。在注册网桥时直接指定，或者由物联网平台分配获得。
        :type bridge_id: str
        :param bridge_name: 网桥名称。
        :type bridge_name: str
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkiotda.v5.BridgeAuthInfo`
        :param create_time: 在物联网平台注册网桥的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        """
        
        super(AddBridgeResponse, self).__init__()

        self._bridge_id = None
        self._bridge_name = None
        self._auth_info = None
        self._create_time = None
        self.discriminator = None

        if bridge_id is not None:
            self.bridge_id = bridge_id
        if bridge_name is not None:
            self.bridge_name = bridge_name
        if auth_info is not None:
            self.auth_info = auth_info
        if create_time is not None:
            self.create_time = create_time

    @property
    def bridge_id(self):
        r"""Gets the bridge_id of this AddBridgeResponse.

        网桥ID，用于唯一标识一个网桥。在注册网桥时直接指定，或者由物联网平台分配获得。

        :return: The bridge_id of this AddBridgeResponse.
        :rtype: str
        """
        return self._bridge_id

    @bridge_id.setter
    def bridge_id(self, bridge_id):
        r"""Sets the bridge_id of this AddBridgeResponse.

        网桥ID，用于唯一标识一个网桥。在注册网桥时直接指定，或者由物联网平台分配获得。

        :param bridge_id: The bridge_id of this AddBridgeResponse.
        :type bridge_id: str
        """
        self._bridge_id = bridge_id

    @property
    def bridge_name(self):
        r"""Gets the bridge_name of this AddBridgeResponse.

        网桥名称。

        :return: The bridge_name of this AddBridgeResponse.
        :rtype: str
        """
        return self._bridge_name

    @bridge_name.setter
    def bridge_name(self, bridge_name):
        r"""Sets the bridge_name of this AddBridgeResponse.

        网桥名称。

        :param bridge_name: The bridge_name of this AddBridgeResponse.
        :type bridge_name: str
        """
        self._bridge_name = bridge_name

    @property
    def auth_info(self):
        r"""Gets the auth_info of this AddBridgeResponse.

        :return: The auth_info of this AddBridgeResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.BridgeAuthInfo`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this AddBridgeResponse.

        :param auth_info: The auth_info of this AddBridgeResponse.
        :type auth_info: :class:`huaweicloudsdkiotda.v5.BridgeAuthInfo`
        """
        self._auth_info = auth_info

    @property
    def create_time(self):
        r"""Gets the create_time of this AddBridgeResponse.

        在物联网平台注册网桥的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this AddBridgeResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AddBridgeResponse.

        在物联网平台注册网桥的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this AddBridgeResponse.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, AddBridgeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
