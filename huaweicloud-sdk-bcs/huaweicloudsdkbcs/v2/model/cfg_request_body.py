# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CfgRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chaincode_name': 'str',
        'cert_path': 'str',
        'channel_name': 'str',
        'peer_orgs': 'dict(str, list[str])',
        'union_info': 'dict(str, list[str])',
        'is_multi_chan': 'bool',
        'channel_chaincode': 'dict(str, list[str])'
    }

    attribute_map = {
        'chaincode_name': 'chaincode_name',
        'cert_path': 'cert_path',
        'channel_name': 'channel_name',
        'peer_orgs': 'peer_orgs',
        'union_info': 'union_info',
        'is_multi_chan': 'is_multi_chan',
        'channel_chaincode': 'channel_chaincode'
    }

    def __init__(self, chaincode_name=None, cert_path=None, channel_name=None, peer_orgs=None, union_info=None, is_multi_chan=None, channel_chaincode=None):
        """CfgRequestBody

        The model defined in huaweicloud sdk

        :param chaincode_name: 链代码名称，以小写字母开头，支持小写字母和数字，长度6-25位
        :type chaincode_name: str
        :param cert_path: SDK配置文件存放路径
        :type cert_path: str
        :param channel_name: 通道名称
        :type channel_name: str
        :param peer_orgs: key：组织名，value：该组织下需要下载的peer节点信息，peer节点请按照0,1,2的顺序升序填写
        :type peer_orgs: dict(str, list[str])
        :param union_info: key：联盟成员名称，value：该联盟成员peer组织名称hash值数组
        :type union_info: dict(str, list[str])
        :param is_multi_chan: 是否是多通道请求，如此处设成true则必须传入channel_chaincode，chaincode_name和channel_name设为空即可
        :type is_multi_chan: bool
        :param channel_chaincode: key：通道名称，value：该通道对应的链代码数组
        :type channel_chaincode: dict(str, list[str])
        """
        
        

        self._chaincode_name = None
        self._cert_path = None
        self._channel_name = None
        self._peer_orgs = None
        self._union_info = None
        self._is_multi_chan = None
        self._channel_chaincode = None
        self.discriminator = None

        self.chaincode_name = chaincode_name
        self.cert_path = cert_path
        self.channel_name = channel_name
        self.peer_orgs = peer_orgs
        if union_info is not None:
            self.union_info = union_info
        if is_multi_chan is not None:
            self.is_multi_chan = is_multi_chan
        if channel_chaincode is not None:
            self.channel_chaincode = channel_chaincode

    @property
    def chaincode_name(self):
        """Gets the chaincode_name of this CfgRequestBody.

        链代码名称，以小写字母开头，支持小写字母和数字，长度6-25位

        :return: The chaincode_name of this CfgRequestBody.
        :rtype: str
        """
        return self._chaincode_name

    @chaincode_name.setter
    def chaincode_name(self, chaincode_name):
        """Sets the chaincode_name of this CfgRequestBody.

        链代码名称，以小写字母开头，支持小写字母和数字，长度6-25位

        :param chaincode_name: The chaincode_name of this CfgRequestBody.
        :type chaincode_name: str
        """
        self._chaincode_name = chaincode_name

    @property
    def cert_path(self):
        """Gets the cert_path of this CfgRequestBody.

        SDK配置文件存放路径

        :return: The cert_path of this CfgRequestBody.
        :rtype: str
        """
        return self._cert_path

    @cert_path.setter
    def cert_path(self, cert_path):
        """Sets the cert_path of this CfgRequestBody.

        SDK配置文件存放路径

        :param cert_path: The cert_path of this CfgRequestBody.
        :type cert_path: str
        """
        self._cert_path = cert_path

    @property
    def channel_name(self):
        """Gets the channel_name of this CfgRequestBody.

        通道名称

        :return: The channel_name of this CfgRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this CfgRequestBody.

        通道名称

        :param channel_name: The channel_name of this CfgRequestBody.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def peer_orgs(self):
        """Gets the peer_orgs of this CfgRequestBody.

        key：组织名，value：该组织下需要下载的peer节点信息，peer节点请按照0,1,2的顺序升序填写

        :return: The peer_orgs of this CfgRequestBody.
        :rtype: dict(str, list[str])
        """
        return self._peer_orgs

    @peer_orgs.setter
    def peer_orgs(self, peer_orgs):
        """Sets the peer_orgs of this CfgRequestBody.

        key：组织名，value：该组织下需要下载的peer节点信息，peer节点请按照0,1,2的顺序升序填写

        :param peer_orgs: The peer_orgs of this CfgRequestBody.
        :type peer_orgs: dict(str, list[str])
        """
        self._peer_orgs = peer_orgs

    @property
    def union_info(self):
        """Gets the union_info of this CfgRequestBody.

        key：联盟成员名称，value：该联盟成员peer组织名称hash值数组

        :return: The union_info of this CfgRequestBody.
        :rtype: dict(str, list[str])
        """
        return self._union_info

    @union_info.setter
    def union_info(self, union_info):
        """Sets the union_info of this CfgRequestBody.

        key：联盟成员名称，value：该联盟成员peer组织名称hash值数组

        :param union_info: The union_info of this CfgRequestBody.
        :type union_info: dict(str, list[str])
        """
        self._union_info = union_info

    @property
    def is_multi_chan(self):
        """Gets the is_multi_chan of this CfgRequestBody.

        是否是多通道请求，如此处设成true则必须传入channel_chaincode，chaincode_name和channel_name设为空即可

        :return: The is_multi_chan of this CfgRequestBody.
        :rtype: bool
        """
        return self._is_multi_chan

    @is_multi_chan.setter
    def is_multi_chan(self, is_multi_chan):
        """Sets the is_multi_chan of this CfgRequestBody.

        是否是多通道请求，如此处设成true则必须传入channel_chaincode，chaincode_name和channel_name设为空即可

        :param is_multi_chan: The is_multi_chan of this CfgRequestBody.
        :type is_multi_chan: bool
        """
        self._is_multi_chan = is_multi_chan

    @property
    def channel_chaincode(self):
        """Gets the channel_chaincode of this CfgRequestBody.

        key：通道名称，value：该通道对应的链代码数组

        :return: The channel_chaincode of this CfgRequestBody.
        :rtype: dict(str, list[str])
        """
        return self._channel_chaincode

    @channel_chaincode.setter
    def channel_chaincode(self, channel_chaincode):
        """Sets the channel_chaincode of this CfgRequestBody.

        key：通道名称，value：该通道对应的链代码数组

        :param channel_chaincode: The channel_chaincode of this CfgRequestBody.
        :type channel_chaincode: dict(str, list[str])
        """
        self._channel_chaincode = channel_chaincode

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
        if not isinstance(other, CfgRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
