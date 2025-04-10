# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadBlockchainCertRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'org_name': 'str',
        'cert_type': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'org_name': 'org_name',
        'cert_type': 'cert_type'
    }

    def __init__(self, blockchain_id=None, org_name=None, cert_type=None):
        r"""DownloadBlockchainCertRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: blockchainID
        :type blockchain_id: str
        :param org_name: order或者peer组织名称
        :type org_name: str
        :param cert_type: 下载证书类别
        :type cert_type: str
        """
        
        

        self._blockchain_id = None
        self._org_name = None
        self._cert_type = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        self.org_name = org_name
        self.cert_type = cert_type

    @property
    def blockchain_id(self):
        r"""Gets the blockchain_id of this DownloadBlockchainCertRequest.

        blockchainID

        :return: The blockchain_id of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        r"""Sets the blockchain_id of this DownloadBlockchainCertRequest.

        blockchainID

        :param blockchain_id: The blockchain_id of this DownloadBlockchainCertRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def org_name(self):
        r"""Gets the org_name of this DownloadBlockchainCertRequest.

        order或者peer组织名称

        :return: The org_name of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        r"""Sets the org_name of this DownloadBlockchainCertRequest.

        order或者peer组织名称

        :param org_name: The org_name of this DownloadBlockchainCertRequest.
        :type org_name: str
        """
        self._org_name = org_name

    @property
    def cert_type(self):
        r"""Gets the cert_type of this DownloadBlockchainCertRequest.

        下载证书类别

        :return: The cert_type of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        r"""Sets the cert_type of this DownloadBlockchainCertRequest.

        下载证书类别

        :param cert_type: The cert_type of this DownloadBlockchainCertRequest.
        :type cert_type: str
        """
        self._cert_type = cert_type

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
        if not isinstance(other, DownloadBlockchainCertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
