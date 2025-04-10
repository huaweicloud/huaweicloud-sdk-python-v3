# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetadata2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encrypted': 'bool',
        'master_key_name': 'str',
        'master_key_id': 'str',
        'ges_metadata': 'ShowMetadataRespGesMetadata'
    }

    attribute_map = {
        'encrypted': 'encrypted',
        'master_key_name': 'master_key_name',
        'master_key_id': 'master_key_id',
        'ges_metadata': 'ges_metadata'
    }

    def __init__(self, encrypted=None, master_key_name=None, master_key_id=None, ges_metadata=None):
        r"""ShowMetadata2Response

        The model defined in huaweicloud sdk

        :param encrypted: 元数据是否加密
        :type encrypted: bool
        :param master_key_name: 秘钥名称
        :type master_key_name: str
        :param master_key_id: 秘钥id
        :type master_key_id: str
        :param ges_metadata: 
        :type ges_metadata: :class:`huaweicloudsdkges.v2.ShowMetadataRespGesMetadata`
        """
        
        super(ShowMetadata2Response, self).__init__()

        self._encrypted = None
        self._master_key_name = None
        self._master_key_id = None
        self._ges_metadata = None
        self.discriminator = None

        if encrypted is not None:
            self.encrypted = encrypted
        if master_key_name is not None:
            self.master_key_name = master_key_name
        if master_key_id is not None:
            self.master_key_id = master_key_id
        if ges_metadata is not None:
            self.ges_metadata = ges_metadata

    @property
    def encrypted(self):
        r"""Gets the encrypted of this ShowMetadata2Response.

        元数据是否加密

        :return: The encrypted of this ShowMetadata2Response.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this ShowMetadata2Response.

        元数据是否加密

        :param encrypted: The encrypted of this ShowMetadata2Response.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def master_key_name(self):
        r"""Gets the master_key_name of this ShowMetadata2Response.

        秘钥名称

        :return: The master_key_name of this ShowMetadata2Response.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        r"""Sets the master_key_name of this ShowMetadata2Response.

        秘钥名称

        :param master_key_name: The master_key_name of this ShowMetadata2Response.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def master_key_id(self):
        r"""Gets the master_key_id of this ShowMetadata2Response.

        秘钥id

        :return: The master_key_id of this ShowMetadata2Response.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        r"""Sets the master_key_id of this ShowMetadata2Response.

        秘钥id

        :param master_key_id: The master_key_id of this ShowMetadata2Response.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def ges_metadata(self):
        r"""Gets the ges_metadata of this ShowMetadata2Response.

        :return: The ges_metadata of this ShowMetadata2Response.
        :rtype: :class:`huaweicloudsdkges.v2.ShowMetadataRespGesMetadata`
        """
        return self._ges_metadata

    @ges_metadata.setter
    def ges_metadata(self, ges_metadata):
        r"""Sets the ges_metadata of this ShowMetadata2Response.

        :param ges_metadata: The ges_metadata of this ShowMetadata2Response.
        :type ges_metadata: :class:`huaweicloudsdkges.v2.ShowMetadataRespGesMetadata`
        """
        self._ges_metadata = ges_metadata

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
        if not isinstance(other, ShowMetadata2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
