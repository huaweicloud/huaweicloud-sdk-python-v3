# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'crypt_key_id': 'str',
        'dedicated_flavor': 'str',
        'dedicated_storage_id': 'str',
        'expand_type': 'str',
        'hpc_bw': 'str'
    }

    attribute_map = {
        'crypt_key_id': 'crypt_key_id',
        'dedicated_flavor': 'dedicated_flavor',
        'dedicated_storage_id': 'dedicated_storage_id',
        'expand_type': 'expand_type',
        'hpc_bw': 'hpc_bw'
    }

    def __init__(self, crypt_key_id=None, dedicated_flavor=None, dedicated_storage_id=None, expand_type=None, hpc_bw=None):
        r"""Metadata

        The model defined in huaweicloud sdk

        :param crypt_key_id: 要创加密文件系统，该字段传KMS服务专业版密钥的ID。
        :type crypt_key_id: str
        :param dedicated_flavor: 创专属文件系统，要创建的虚拟机的规格。
        :type dedicated_flavor: str
        :param dedicated_storage_id: 创专属文件系统，要指定一个专属分布式存储的ID。
        :type dedicated_storage_id: str
        :param expand_type: 扩展类型；当文件系统正在创建时，该字段不返回。  - 创建增强型、20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  - 创建增强型的文件系统，包括标准型-增强版和性能型-增强版，需要填写\&quot;bandwidth\&quot;。  - 创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB文件系统，需要填写\&quot;hpc\&quot;。  - 创建HPC缓存型，需要填写\&quot;hpc_cache\&quot;。 
        :type expand_type: str
        :param hpc_bw: 文件系统的带宽规格。  创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  20MB/s/TiB，填写\&quot;20M\&quot;。 40MB/s/TiB，填写\&quot;40M\&quot;。 125MB/s/TiB，填写\&quot;125M\&quot;。 250MB/s/TiB，填写\&quot;250M\&quot;。 500MB/s/TiB，填写\&quot;500M\&quot;。 1000MB/s/TiB，填写\&quot;1000M\&quot;。 HPC缓存型，填写\&quot;2G\&quot;、\&quot;4G\&quot;、\&quot;8G\&quot;、\&quot;16G\&quot;、\&quot;24G\&quot;、\&quot;32G\&quot;或\&quot;48G\&quot;。 
        :type hpc_bw: str
        """
        
        

        self._crypt_key_id = None
        self._dedicated_flavor = None
        self._dedicated_storage_id = None
        self._expand_type = None
        self._hpc_bw = None
        self.discriminator = None

        if crypt_key_id is not None:
            self.crypt_key_id = crypt_key_id
        if dedicated_flavor is not None:
            self.dedicated_flavor = dedicated_flavor
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if expand_type is not None:
            self.expand_type = expand_type
        if hpc_bw is not None:
            self.hpc_bw = hpc_bw

    @property
    def crypt_key_id(self):
        r"""Gets the crypt_key_id of this Metadata.

        要创加密文件系统，该字段传KMS服务专业版密钥的ID。

        :return: The crypt_key_id of this Metadata.
        :rtype: str
        """
        return self._crypt_key_id

    @crypt_key_id.setter
    def crypt_key_id(self, crypt_key_id):
        r"""Sets the crypt_key_id of this Metadata.

        要创加密文件系统，该字段传KMS服务专业版密钥的ID。

        :param crypt_key_id: The crypt_key_id of this Metadata.
        :type crypt_key_id: str
        """
        self._crypt_key_id = crypt_key_id

    @property
    def dedicated_flavor(self):
        r"""Gets the dedicated_flavor of this Metadata.

        创专属文件系统，要创建的虚拟机的规格。

        :return: The dedicated_flavor of this Metadata.
        :rtype: str
        """
        return self._dedicated_flavor

    @dedicated_flavor.setter
    def dedicated_flavor(self, dedicated_flavor):
        r"""Sets the dedicated_flavor of this Metadata.

        创专属文件系统，要创建的虚拟机的规格。

        :param dedicated_flavor: The dedicated_flavor of this Metadata.
        :type dedicated_flavor: str
        """
        self._dedicated_flavor = dedicated_flavor

    @property
    def dedicated_storage_id(self):
        r"""Gets the dedicated_storage_id of this Metadata.

        创专属文件系统，要指定一个专属分布式存储的ID。

        :return: The dedicated_storage_id of this Metadata.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        r"""Sets the dedicated_storage_id of this Metadata.

        创专属文件系统，要指定一个专属分布式存储的ID。

        :param dedicated_storage_id: The dedicated_storage_id of this Metadata.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def expand_type(self):
        r"""Gets the expand_type of this Metadata.

        扩展类型；当文件系统正在创建时，该字段不返回。  - 创建增强型、20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  - 创建增强型的文件系统，包括标准型-增强版和性能型-增强版，需要填写\"bandwidth\"。  - 创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB文件系统，需要填写\"hpc\"。  - 创建HPC缓存型，需要填写\"hpc_cache\"。 

        :return: The expand_type of this Metadata.
        :rtype: str
        """
        return self._expand_type

    @expand_type.setter
    def expand_type(self, expand_type):
        r"""Sets the expand_type of this Metadata.

        扩展类型；当文件系统正在创建时，该字段不返回。  - 创建增强型、20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  - 创建增强型的文件系统，包括标准型-增强版和性能型-增强版，需要填写\"bandwidth\"。  - 创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB文件系统，需要填写\"hpc\"。  - 创建HPC缓存型，需要填写\"hpc_cache\"。 

        :param expand_type: The expand_type of this Metadata.
        :type expand_type: str
        """
        self._expand_type = expand_type

    @property
    def hpc_bw(self):
        r"""Gets the hpc_bw of this Metadata.

        文件系统的带宽规格。  创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  20MB/s/TiB，填写\"20M\"。 40MB/s/TiB，填写\"40M\"。 125MB/s/TiB，填写\"125M\"。 250MB/s/TiB，填写\"250M\"。 500MB/s/TiB，填写\"500M\"。 1000MB/s/TiB，填写\"1000M\"。 HPC缓存型，填写\"2G\"、\"4G\"、\"8G\"、\"16G\"、\"24G\"、\"32G\"或\"48G\"。 

        :return: The hpc_bw of this Metadata.
        :rtype: str
        """
        return self._hpc_bw

    @hpc_bw.setter
    def hpc_bw(self, hpc_bw):
        r"""Sets the hpc_bw of this Metadata.

        文件系统的带宽规格。  创建20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB、HPC缓存型文件系统时，该参数必填。  20MB/s/TiB，填写\"20M\"。 40MB/s/TiB，填写\"40M\"。 125MB/s/TiB，填写\"125M\"。 250MB/s/TiB，填写\"250M\"。 500MB/s/TiB，填写\"500M\"。 1000MB/s/TiB，填写\"1000M\"。 HPC缓存型，填写\"2G\"、\"4G\"、\"8G\"、\"16G\"、\"24G\"、\"32G\"或\"48G\"。 

        :param hpc_bw: The hpc_bw of this Metadata.
        :type hpc_bw: str
        """
        self._hpc_bw = hpc_bw

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
