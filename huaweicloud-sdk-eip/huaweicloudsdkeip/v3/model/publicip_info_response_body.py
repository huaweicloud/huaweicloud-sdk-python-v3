# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_address': 'str',
        'publicip_id': 'str',
        'publicip_type': 'str',
        'publicipv6_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'publicip_address': 'publicip_address',
        'publicip_id': 'publicip_id',
        'publicip_type': 'publicip_type',
        'publicipv6_address': 'publicipv6_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, publicip_address=None, publicip_id=None, publicip_type=None, publicipv6_address=None, ip_version=None):
        r"""PublicipInfoResponseBody

        The model defined in huaweicloud sdk

        :param publicip_address: - 功能说明：弹性公网IPV4或IPv6的公网地址
        :type publicip_address: str
        :param publicip_id: - 功能说明：带宽对应的弹性公网IPV4或IPv6的唯一标识
        :type publicip_id: str
        :param publicip_type: - 功能说明：EIP的类型  - [取值范围：5_bgp](tag:hk_g42,g42,hk_sbc,sbc)  - [取值范围：5_chinamobile](tag:cmcc)  - [取值范围：5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt)  - [取值范围：    - eu-de: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）、5_gray（Dedicated Load Balancer）    - eu-nl: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt_test) - [取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP），5_youxuanbgp（优选BGP）    - 华南-广州：5_bgp、5_sbgp    - 华东-上海一：5_bgp、5_sbgp    - 华东-上海二：5_bgp、5_sbgp    - 华北-北京一：5_bgp、5_sbgp    - 中国-香港：5_bgp、5_youxuanbgp    - 亚太-曼谷：5_bgp    - 亚太-新加坡：5_bgp    - 非洲-约翰内斯堡：5_bgp    - 西南-贵阳一：5_sbgp    - 华北-北京四：5_bgp、5_sbgp    - 拉美-圣地亚哥：5_bgp    - 拉美-圣保罗一：5_bgp    - 拉美-墨西哥城一：5_bgp    - 拉美-布宜诺斯艾利一：5_bgp    - 拉美-利马一：5_bgp    - 拉美-圣地亚哥二： 5_bgp  ](tag:hws,hws_hk)  - 约束：     - 必须是系统具体支持的类型。     - publicip_id为IPv4端口，所以[\&quot;publicip_type\&quot;](tag:cmcc,ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,hws_hk,hws_ocb,ocb,tlf,tm,hk_g42,g42,hk_sbc,sbc)[\&quot;type\&quot;](tag:hws)字段未给定时，默认为[5_bgp](tag:ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,g42,hk_g42,hk_sbc,hws,hws_hk,hws_ocb,mix,ocb,sbc,tlf,tm)[5_chinamobile](tag:cmcc)。
        :type publicip_type: str
        :param publicipv6_address: - 功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址
        :type publicipv6_address: str
        :param ip_version: - 功能说明：IP版本信息 - 取值范围：  4：IPv4；  6：IPv6
        :type ip_version: int
        """
        
        

        self._publicip_address = None
        self._publicip_id = None
        self._publicip_type = None
        self._publicipv6_address = None
        self._ip_version = None
        self.discriminator = None

        if publicip_address is not None:
            self.publicip_address = publicip_address
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_type is not None:
            self.publicip_type = publicip_type
        if publicipv6_address is not None:
            self.publicipv6_address = publicipv6_address
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def publicip_address(self):
        r"""Gets the publicip_address of this PublicipInfoResponseBody.

        - 功能说明：弹性公网IPV4或IPv6的公网地址

        :return: The publicip_address of this PublicipInfoResponseBody.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        r"""Sets the publicip_address of this PublicipInfoResponseBody.

        - 功能说明：弹性公网IPV4或IPv6的公网地址

        :param publicip_address: The publicip_address of this PublicipInfoResponseBody.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this PublicipInfoResponseBody.

        - 功能说明：带宽对应的弹性公网IPV4或IPv6的唯一标识

        :return: The publicip_id of this PublicipInfoResponseBody.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this PublicipInfoResponseBody.

        - 功能说明：带宽对应的弹性公网IPV4或IPv6的唯一标识

        :param publicip_id: The publicip_id of this PublicipInfoResponseBody.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_type(self):
        r"""Gets the publicip_type of this PublicipInfoResponseBody.

        - 功能说明：EIP的类型  - [取值范围：5_bgp](tag:hk_g42,g42,hk_sbc,sbc)  - [取值范围：5_chinamobile](tag:cmcc)  - [取值范围：5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt)  - [取值范围：    - eu-de: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）、5_gray（Dedicated Load Balancer）    - eu-nl: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt_test) - [取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP），5_youxuanbgp（优选BGP）    - 华南-广州：5_bgp、5_sbgp    - 华东-上海一：5_bgp、5_sbgp    - 华东-上海二：5_bgp、5_sbgp    - 华北-北京一：5_bgp、5_sbgp    - 中国-香港：5_bgp、5_youxuanbgp    - 亚太-曼谷：5_bgp    - 亚太-新加坡：5_bgp    - 非洲-约翰内斯堡：5_bgp    - 西南-贵阳一：5_sbgp    - 华北-北京四：5_bgp、5_sbgp    - 拉美-圣地亚哥：5_bgp    - 拉美-圣保罗一：5_bgp    - 拉美-墨西哥城一：5_bgp    - 拉美-布宜诺斯艾利一：5_bgp    - 拉美-利马一：5_bgp    - 拉美-圣地亚哥二： 5_bgp  ](tag:hws,hws_hk)  - 约束：     - 必须是系统具体支持的类型。     - publicip_id为IPv4端口，所以[\"publicip_type\"](tag:cmcc,ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,hws_hk,hws_ocb,ocb,tlf,tm,hk_g42,g42,hk_sbc,sbc)[\"type\"](tag:hws)字段未给定时，默认为[5_bgp](tag:ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,g42,hk_g42,hk_sbc,hws,hws_hk,hws_ocb,mix,ocb,sbc,tlf,tm)[5_chinamobile](tag:cmcc)。

        :return: The publicip_type of this PublicipInfoResponseBody.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        r"""Sets the publicip_type of this PublicipInfoResponseBody.

        - 功能说明：EIP的类型  - [取值范围：5_bgp](tag:hk_g42,g42,hk_sbc,sbc)  - [取值范围：5_chinamobile](tag:cmcc)  - [取值范围：5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt)  - [取值范围：    - eu-de: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）、5_gray（Dedicated Load Balancer）    - eu-nl: 5_bgp（Dynamic BGP）、5_mainbgp（Mail BGP）](tag:dt_test) - [取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP），5_youxuanbgp（优选BGP）    - 华南-广州：5_bgp、5_sbgp    - 华东-上海一：5_bgp、5_sbgp    - 华东-上海二：5_bgp、5_sbgp    - 华北-北京一：5_bgp、5_sbgp    - 中国-香港：5_bgp、5_youxuanbgp    - 亚太-曼谷：5_bgp    - 亚太-新加坡：5_bgp    - 非洲-约翰内斯堡：5_bgp    - 西南-贵阳一：5_sbgp    - 华北-北京四：5_bgp、5_sbgp    - 拉美-圣地亚哥：5_bgp    - 拉美-圣保罗一：5_bgp    - 拉美-墨西哥城一：5_bgp    - 拉美-布宜诺斯艾利一：5_bgp    - 拉美-利马一：5_bgp    - 拉美-圣地亚哥二： 5_bgp  ](tag:hws,hws_hk)  - 约束：     - 必须是系统具体支持的类型。     - publicip_id为IPv4端口，所以[\"publicip_type\"](tag:cmcc,ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,hws_hk,hws_ocb,ocb,tlf,tm,hk_g42,g42,hk_sbc,sbc)[\"type\"](tag:hws)字段未给定时，默认为[5_bgp](tag:ctc,dt,dt_test,fcs,fcs_dt,fcs_vm,g42,hk_g42,hk_sbc,hws,hws_hk,hws_ocb,mix,ocb,sbc,tlf,tm)[5_chinamobile](tag:cmcc)。

        :param publicip_type: The publicip_type of this PublicipInfoResponseBody.
        :type publicip_type: str
        """
        self._publicip_type = publicip_type

    @property
    def publicipv6_address(self):
        r"""Gets the publicipv6_address of this PublicipInfoResponseBody.

        - 功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :return: The publicipv6_address of this PublicipInfoResponseBody.
        :rtype: str
        """
        return self._publicipv6_address

    @publicipv6_address.setter
    def publicipv6_address(self, publicipv6_address):
        r"""Sets the publicipv6_address of this PublicipInfoResponseBody.

        - 功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :param publicipv6_address: The publicipv6_address of this PublicipInfoResponseBody.
        :type publicipv6_address: str
        """
        self._publicipv6_address = publicipv6_address

    @property
    def ip_version(self):
        r"""Gets the ip_version of this PublicipInfoResponseBody.

        - 功能说明：IP版本信息 - 取值范围：  4：IPv4；  6：IPv6

        :return: The ip_version of this PublicipInfoResponseBody.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this PublicipInfoResponseBody.

        - 功能说明：IP版本信息 - 取值范围：  4：IPv4；  6：IPv6

        :param ip_version: The ip_version of this PublicipInfoResponseBody.
        :type ip_version: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, PublicipInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
