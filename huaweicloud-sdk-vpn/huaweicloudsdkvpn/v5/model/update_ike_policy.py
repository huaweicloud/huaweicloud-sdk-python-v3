# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIkePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ike_version': 'str',
        'phase1_negotiation_mode': 'str',
        'authentication_algorithm': 'str',
        'encryption_algorithm': 'str',
        'dh_group': 'str',
        'lifetime_seconds': 'int',
        'local_id_type': 'str',
        'local_id': 'str',
        'peer_id_type': 'str',
        'peer_id': 'str',
        'dpd': 'UpdateDpd'
    }

    attribute_map = {
        'ike_version': 'ike_version',
        'phase1_negotiation_mode': 'phase1_negotiation_mode',
        'authentication_algorithm': 'authentication_algorithm',
        'encryption_algorithm': 'encryption_algorithm',
        'dh_group': 'dh_group',
        'lifetime_seconds': 'lifetime_seconds',
        'local_id_type': 'local_id_type',
        'local_id': 'local_id',
        'peer_id_type': 'peer_id_type',
        'peer_id': 'peer_id',
        'dpd': 'dpd'
    }

    def __init__(self, ike_version=None, phase1_negotiation_mode=None, authentication_algorithm=None, encryption_algorithm=None, dh_group=None, lifetime_seconds=None, local_id_type=None, local_id=None, peer_id_type=None, peer_id=None, dpd=None):
        """UpdateIkePolicy

        The model defined in huaweicloud sdk

        :param ike_version: IKE协商版本
        :type ike_version: str
        :param phase1_negotiation_mode: 协商模式，ike版本为v1时生效
        :type phase1_negotiation_mode: str
        :param authentication_algorithm: 认证算法，SHA1和MD5安全性较低，请慎用
        :type authentication_algorithm: str
        :param encryption_algorithm: 加密算法，3DES安全性较低，请慎用
        :type encryption_algorithm: str
        :param dh_group: DH密钥组
        :type dh_group: str
        :param lifetime_seconds: 表示SA的生存周期，当该生存周期超时后IKE SA将自动更新
        :type lifetime_seconds: int
        :param local_id_type: 本端ID类型
        :type local_id_type: str
        :param local_id: 本端ID
        :type local_id: str
        :param peer_id_type: 对端ID类型
        :type peer_id_type: str
        :param peer_id: 对端ID
        :type peer_id: str
        :param dpd: 
        :type dpd: :class:`huaweicloudsdkvpn.v5.UpdateDpd`
        """
        
        

        self._ike_version = None
        self._phase1_negotiation_mode = None
        self._authentication_algorithm = None
        self._encryption_algorithm = None
        self._dh_group = None
        self._lifetime_seconds = None
        self._local_id_type = None
        self._local_id = None
        self._peer_id_type = None
        self._peer_id = None
        self._dpd = None
        self.discriminator = None

        if ike_version is not None:
            self.ike_version = ike_version
        if phase1_negotiation_mode is not None:
            self.phase1_negotiation_mode = phase1_negotiation_mode
        if authentication_algorithm is not None:
            self.authentication_algorithm = authentication_algorithm
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if dh_group is not None:
            self.dh_group = dh_group
        if lifetime_seconds is not None:
            self.lifetime_seconds = lifetime_seconds
        if local_id_type is not None:
            self.local_id_type = local_id_type
        if local_id is not None:
            self.local_id = local_id
        if peer_id_type is not None:
            self.peer_id_type = peer_id_type
        if peer_id is not None:
            self.peer_id = peer_id
        if dpd is not None:
            self.dpd = dpd

    @property
    def ike_version(self):
        """Gets the ike_version of this UpdateIkePolicy.

        IKE协商版本

        :return: The ike_version of this UpdateIkePolicy.
        :rtype: str
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """Sets the ike_version of this UpdateIkePolicy.

        IKE协商版本

        :param ike_version: The ike_version of this UpdateIkePolicy.
        :type ike_version: str
        """
        self._ike_version = ike_version

    @property
    def phase1_negotiation_mode(self):
        """Gets the phase1_negotiation_mode of this UpdateIkePolicy.

        协商模式，ike版本为v1时生效

        :return: The phase1_negotiation_mode of this UpdateIkePolicy.
        :rtype: str
        """
        return self._phase1_negotiation_mode

    @phase1_negotiation_mode.setter
    def phase1_negotiation_mode(self, phase1_negotiation_mode):
        """Sets the phase1_negotiation_mode of this UpdateIkePolicy.

        协商模式，ike版本为v1时生效

        :param phase1_negotiation_mode: The phase1_negotiation_mode of this UpdateIkePolicy.
        :type phase1_negotiation_mode: str
        """
        self._phase1_negotiation_mode = phase1_negotiation_mode

    @property
    def authentication_algorithm(self):
        """Gets the authentication_algorithm of this UpdateIkePolicy.

        认证算法，SHA1和MD5安全性较低，请慎用

        :return: The authentication_algorithm of this UpdateIkePolicy.
        :rtype: str
        """
        return self._authentication_algorithm

    @authentication_algorithm.setter
    def authentication_algorithm(self, authentication_algorithm):
        """Sets the authentication_algorithm of this UpdateIkePolicy.

        认证算法，SHA1和MD5安全性较低，请慎用

        :param authentication_algorithm: The authentication_algorithm of this UpdateIkePolicy.
        :type authentication_algorithm: str
        """
        self._authentication_algorithm = authentication_algorithm

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this UpdateIkePolicy.

        加密算法，3DES安全性较低，请慎用

        :return: The encryption_algorithm of this UpdateIkePolicy.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this UpdateIkePolicy.

        加密算法，3DES安全性较低，请慎用

        :param encryption_algorithm: The encryption_algorithm of this UpdateIkePolicy.
        :type encryption_algorithm: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def dh_group(self):
        """Gets the dh_group of this UpdateIkePolicy.

        DH密钥组

        :return: The dh_group of this UpdateIkePolicy.
        :rtype: str
        """
        return self._dh_group

    @dh_group.setter
    def dh_group(self, dh_group):
        """Sets the dh_group of this UpdateIkePolicy.

        DH密钥组

        :param dh_group: The dh_group of this UpdateIkePolicy.
        :type dh_group: str
        """
        self._dh_group = dh_group

    @property
    def lifetime_seconds(self):
        """Gets the lifetime_seconds of this UpdateIkePolicy.

        表示SA的生存周期，当该生存周期超时后IKE SA将自动更新

        :return: The lifetime_seconds of this UpdateIkePolicy.
        :rtype: int
        """
        return self._lifetime_seconds

    @lifetime_seconds.setter
    def lifetime_seconds(self, lifetime_seconds):
        """Sets the lifetime_seconds of this UpdateIkePolicy.

        表示SA的生存周期，当该生存周期超时后IKE SA将自动更新

        :param lifetime_seconds: The lifetime_seconds of this UpdateIkePolicy.
        :type lifetime_seconds: int
        """
        self._lifetime_seconds = lifetime_seconds

    @property
    def local_id_type(self):
        """Gets the local_id_type of this UpdateIkePolicy.

        本端ID类型

        :return: The local_id_type of this UpdateIkePolicy.
        :rtype: str
        """
        return self._local_id_type

    @local_id_type.setter
    def local_id_type(self, local_id_type):
        """Sets the local_id_type of this UpdateIkePolicy.

        本端ID类型

        :param local_id_type: The local_id_type of this UpdateIkePolicy.
        :type local_id_type: str
        """
        self._local_id_type = local_id_type

    @property
    def local_id(self):
        """Gets the local_id of this UpdateIkePolicy.

        本端ID

        :return: The local_id of this UpdateIkePolicy.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this UpdateIkePolicy.

        本端ID

        :param local_id: The local_id of this UpdateIkePolicy.
        :type local_id: str
        """
        self._local_id = local_id

    @property
    def peer_id_type(self):
        """Gets the peer_id_type of this UpdateIkePolicy.

        对端ID类型

        :return: The peer_id_type of this UpdateIkePolicy.
        :rtype: str
        """
        return self._peer_id_type

    @peer_id_type.setter
    def peer_id_type(self, peer_id_type):
        """Sets the peer_id_type of this UpdateIkePolicy.

        对端ID类型

        :param peer_id_type: The peer_id_type of this UpdateIkePolicy.
        :type peer_id_type: str
        """
        self._peer_id_type = peer_id_type

    @property
    def peer_id(self):
        """Gets the peer_id of this UpdateIkePolicy.

        对端ID

        :return: The peer_id of this UpdateIkePolicy.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this UpdateIkePolicy.

        对端ID

        :param peer_id: The peer_id of this UpdateIkePolicy.
        :type peer_id: str
        """
        self._peer_id = peer_id

    @property
    def dpd(self):
        """Gets the dpd of this UpdateIkePolicy.

        :return: The dpd of this UpdateIkePolicy.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateDpd`
        """
        return self._dpd

    @dpd.setter
    def dpd(self, dpd):
        """Sets the dpd of this UpdateIkePolicy.

        :param dpd: The dpd of this UpdateIkePolicy.
        :type dpd: :class:`huaweicloudsdkvpn.v5.UpdateDpd`
        """
        self._dpd = dpd

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
        if not isinstance(other, UpdateIkePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
