# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFromObsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata_path': 'str',
        'name': 'str',
        'description': 'str',
        'encryption': 'UploadFromObsReqEncryption'
    }

    attribute_map = {
        'metadata_path': 'metadata_path',
        'name': 'name',
        'description': 'description',
        'encryption': 'encryption'
    }

    def __init__(self, metadata_path=None, name=None, description=None, encryption=None):
        """UploadFromObsReq

        The model defined in huaweicloud sdk

        :param metadata_path: 元数据存储地址。
        :type metadata_path: str
        :param name: 元数据的名字。
        :type name: str
        :param description: 对元数据的描述。
        :type description: str
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkges.v2.UploadFromObsReqEncryption`
        """
        
        

        self._metadata_path = None
        self._name = None
        self._description = None
        self._encryption = None
        self.discriminator = None

        self.metadata_path = metadata_path
        self.name = name
        if description is not None:
            self.description = description
        if encryption is not None:
            self.encryption = encryption

    @property
    def metadata_path(self):
        """Gets the metadata_path of this UploadFromObsReq.

        元数据存储地址。

        :return: The metadata_path of this UploadFromObsReq.
        :rtype: str
        """
        return self._metadata_path

    @metadata_path.setter
    def metadata_path(self, metadata_path):
        """Sets the metadata_path of this UploadFromObsReq.

        元数据存储地址。

        :param metadata_path: The metadata_path of this UploadFromObsReq.
        :type metadata_path: str
        """
        self._metadata_path = metadata_path

    @property
    def name(self):
        """Gets the name of this UploadFromObsReq.

        元数据的名字。

        :return: The name of this UploadFromObsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadFromObsReq.

        元数据的名字。

        :param name: The name of this UploadFromObsReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UploadFromObsReq.

        对元数据的描述。

        :return: The description of this UploadFromObsReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UploadFromObsReq.

        对元数据的描述。

        :param description: The description of this UploadFromObsReq.
        :type description: str
        """
        self._description = description

    @property
    def encryption(self):
        """Gets the encryption of this UploadFromObsReq.

        :return: The encryption of this UploadFromObsReq.
        :rtype: :class:`huaweicloudsdkges.v2.UploadFromObsReqEncryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this UploadFromObsReq.

        :param encryption: The encryption of this UploadFromObsReq.
        :type encryption: :class:`huaweicloudsdkges.v2.UploadFromObsReqEncryption`
        """
        self._encryption = encryption

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
        if not isinstance(other, UploadFromObsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
