# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetadataReq:

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
        'is_overwrite': 'bool',
        'ges_metadata': 'object'
    }

    attribute_map = {
        'metadata_path': 'metadataPath',
        'name': 'name',
        'description': 'description',
        'is_overwrite': 'isOverwrite',
        'ges_metadata': 'gesMetadata'
    }

    def __init__(self, metadata_path=None, name=None, description=None, is_overwrite=None, ges_metadata=None):
        """CreateMetadataReq

        The model defined in huaweicloud sdk

        :param metadata_path: 元数据存储地址。
        :type metadata_path: str
        :param name: 元数据的名字，限制为1-64个字符，且只能包含字母，数字或下划线。
        :type name: str
        :param description: 对元数据的描述。
        :type description: str
        :param is_overwrite: 是否覆盖文件。
        :type is_overwrite: bool
        :param ges_metadata: 存储metadata的消息信息的对象。
        :type ges_metadata: object
        """
        
        

        self._metadata_path = None
        self._name = None
        self._description = None
        self._is_overwrite = None
        self._ges_metadata = None
        self.discriminator = None

        self.metadata_path = metadata_path
        self.name = name
        self.description = description
        self.is_overwrite = is_overwrite
        self.ges_metadata = ges_metadata

    @property
    def metadata_path(self):
        """Gets the metadata_path of this CreateMetadataReq.

        元数据存储地址。

        :return: The metadata_path of this CreateMetadataReq.
        :rtype: str
        """
        return self._metadata_path

    @metadata_path.setter
    def metadata_path(self, metadata_path):
        """Sets the metadata_path of this CreateMetadataReq.

        元数据存储地址。

        :param metadata_path: The metadata_path of this CreateMetadataReq.
        :type metadata_path: str
        """
        self._metadata_path = metadata_path

    @property
    def name(self):
        """Gets the name of this CreateMetadataReq.

        元数据的名字，限制为1-64个字符，且只能包含字母，数字或下划线。

        :return: The name of this CreateMetadataReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMetadataReq.

        元数据的名字，限制为1-64个字符，且只能包含字母，数字或下划线。

        :param name: The name of this CreateMetadataReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateMetadataReq.

        对元数据的描述。

        :return: The description of this CreateMetadataReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateMetadataReq.

        对元数据的描述。

        :param description: The description of this CreateMetadataReq.
        :type description: str
        """
        self._description = description

    @property
    def is_overwrite(self):
        """Gets the is_overwrite of this CreateMetadataReq.

        是否覆盖文件。

        :return: The is_overwrite of this CreateMetadataReq.
        :rtype: bool
        """
        return self._is_overwrite

    @is_overwrite.setter
    def is_overwrite(self, is_overwrite):
        """Sets the is_overwrite of this CreateMetadataReq.

        是否覆盖文件。

        :param is_overwrite: The is_overwrite of this CreateMetadataReq.
        :type is_overwrite: bool
        """
        self._is_overwrite = is_overwrite

    @property
    def ges_metadata(self):
        """Gets the ges_metadata of this CreateMetadataReq.

        存储metadata的消息信息的对象。

        :return: The ges_metadata of this CreateMetadataReq.
        :rtype: object
        """
        return self._ges_metadata

    @ges_metadata.setter
    def ges_metadata(self, ges_metadata):
        """Sets the ges_metadata of this CreateMetadataReq.

        存储metadata的消息信息的对象。

        :param ges_metadata: The ges_metadata of this CreateMetadataReq.
        :type ges_metadata: object
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
        if not isinstance(other, CreateMetadataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
