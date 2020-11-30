# coding: utf-8

import pprint
import re

import six





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
        'union_info': 'dict(str, list[str])'
    }

    attribute_map = {
        'chaincode_name': 'chaincode_name',
        'cert_path': 'cert_path',
        'channel_name': 'channel_name',
        'peer_orgs': 'peer_orgs',
        'union_info': 'union_info'
    }

    def __init__(self, chaincode_name=None, cert_path=None, channel_name=None, peer_orgs=None, union_info=None):
        """CfgRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._chaincode_name = None
        self._cert_path = None
        self._channel_name = None
        self._peer_orgs = None
        self._union_info = None
        self.discriminator = None

        self.chaincode_name = chaincode_name
        self.cert_path = cert_path
        self.channel_name = channel_name
        self.peer_orgs = peer_orgs
        if union_info is not None:
            self.union_info = union_info

    @property
    def chaincode_name(self):
        """Gets the chaincode_name of this CfgRequestBody.

        链代码名称

        :return: The chaincode_name of this CfgRequestBody.
        :rtype: str
        """
        return self._chaincode_name

    @chaincode_name.setter
    def chaincode_name(self, chaincode_name):
        """Sets the chaincode_name of this CfgRequestBody.

        链代码名称

        :param chaincode_name: The chaincode_name of this CfgRequestBody.
        :type: str
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
        :type: str
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
        :type: str
        """
        self._channel_name = channel_name

    @property
    def peer_orgs(self):
        """Gets the peer_orgs of this CfgRequestBody.

        key：组织名，value：该组织下需要下载的peer节点信息

        :return: The peer_orgs of this CfgRequestBody.
        :rtype: dict(str, list[str])
        """
        return self._peer_orgs

    @peer_orgs.setter
    def peer_orgs(self, peer_orgs):
        """Sets the peer_orgs of this CfgRequestBody.

        key：组织名，value：该组织下需要下载的peer节点信息

        :param peer_orgs: The peer_orgs of this CfgRequestBody.
        :type: dict(str, list[str])
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
        :type: dict(str, list[str])
        """
        self._union_info = union_info

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CfgRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
