# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateBlockDeviceMappingOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'str',
        'source_type': 'str',
        'encrypted': 'bool',
        'cmk_id': 'str',
        'volume_type': 'str',
        'volume_size': 'int',
        'attachment': 'TemplateBlockDeviceMappingAttachmentOption'
    }

    attribute_map = {
        'source_id': 'source_id',
        'source_type': 'source_type',
        'encrypted': 'encrypted',
        'cmk_id': 'cmk_id',
        'volume_type': 'volume_type',
        'volume_size': 'volume_size',
        'attachment': 'attachment'
    }

    def __init__(self, source_id=None, source_type=None, encrypted=None, cmk_id=None, volume_type=None, volume_size=None, attachment=None):
        r"""TemplateBlockDeviceMappingOption

        The model defined in huaweicloud sdk

        :param source_id: 虚拟机卷数据源类型：blank, image_id
        :type source_id: str
        :param source_type: 卷设备源头类型
        :type source_type: str
        :param encrypted: 是否加密
        :type encrypted: bool
        :param cmk_id: 秘钥ID
        :type cmk_id: str
        :param volume_type: 卷类型
        :type volume_type: str
        :param volume_size: 卷大小
        :type volume_size: int
        :param attachment: 
        :type attachment: :class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingAttachmentOption`
        """
        
        

        self._source_id = None
        self._source_type = None
        self._encrypted = None
        self._cmk_id = None
        self._volume_type = None
        self._volume_size = None
        self._attachment = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if source_type is not None:
            self.source_type = source_type
        if encrypted is not None:
            self.encrypted = encrypted
        if cmk_id is not None:
            self.cmk_id = cmk_id
        if volume_type is not None:
            self.volume_type = volume_type
        if volume_size is not None:
            self.volume_size = volume_size
        if attachment is not None:
            self.attachment = attachment

    @property
    def source_id(self):
        r"""Gets the source_id of this TemplateBlockDeviceMappingOption.

        虚拟机卷数据源类型：blank, image_id

        :return: The source_id of this TemplateBlockDeviceMappingOption.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this TemplateBlockDeviceMappingOption.

        虚拟机卷数据源类型：blank, image_id

        :param source_id: The source_id of this TemplateBlockDeviceMappingOption.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_type(self):
        r"""Gets the source_type of this TemplateBlockDeviceMappingOption.

        卷设备源头类型

        :return: The source_type of this TemplateBlockDeviceMappingOption.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this TemplateBlockDeviceMappingOption.

        卷设备源头类型

        :param source_type: The source_type of this TemplateBlockDeviceMappingOption.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def encrypted(self):
        r"""Gets the encrypted of this TemplateBlockDeviceMappingOption.

        是否加密

        :return: The encrypted of this TemplateBlockDeviceMappingOption.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this TemplateBlockDeviceMappingOption.

        是否加密

        :param encrypted: The encrypted of this TemplateBlockDeviceMappingOption.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def cmk_id(self):
        r"""Gets the cmk_id of this TemplateBlockDeviceMappingOption.

        秘钥ID

        :return: The cmk_id of this TemplateBlockDeviceMappingOption.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        r"""Sets the cmk_id of this TemplateBlockDeviceMappingOption.

        秘钥ID

        :param cmk_id: The cmk_id of this TemplateBlockDeviceMappingOption.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def volume_type(self):
        r"""Gets the volume_type of this TemplateBlockDeviceMappingOption.

        卷类型

        :return: The volume_type of this TemplateBlockDeviceMappingOption.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this TemplateBlockDeviceMappingOption.

        卷类型

        :param volume_type: The volume_type of this TemplateBlockDeviceMappingOption.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        r"""Gets the volume_size of this TemplateBlockDeviceMappingOption.

        卷大小

        :return: The volume_size of this TemplateBlockDeviceMappingOption.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this TemplateBlockDeviceMappingOption.

        卷大小

        :param volume_size: The volume_size of this TemplateBlockDeviceMappingOption.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def attachment(self):
        r"""Gets the attachment of this TemplateBlockDeviceMappingOption.

        :return: The attachment of this TemplateBlockDeviceMappingOption.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingAttachmentOption`
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        r"""Sets the attachment of this TemplateBlockDeviceMappingOption.

        :param attachment: The attachment of this TemplateBlockDeviceMappingOption.
        :type attachment: :class:`huaweicloudsdkecs.v2.TemplateBlockDeviceMappingAttachmentOption`
        """
        self._attachment = attachment

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
        if not isinstance(other, TemplateBlockDeviceMappingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
