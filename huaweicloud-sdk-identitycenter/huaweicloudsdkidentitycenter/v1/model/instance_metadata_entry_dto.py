# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceMetadataEntryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'instance_id': 'str',
        'alias': 'str',
        'instance_urn': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'instance_id': 'instance_id',
        'alias': 'alias',
        'instance_urn': 'instance_urn'
    }

    def __init__(self, identity_store_id=None, instance_id=None, alias=None, instance_urn=None):
        r"""InstanceMetadataEntryDto

        The model defined in huaweicloud sdk

        :param identity_store_id: 关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。
        :type identity_store_id: str
        :param instance_id: Identity Center实例的全局唯一标识符（ID）
        :type instance_id: str
        :param alias: 用户为身份源标识符定义的别名
        :type alias: str
        :param instance_urn: 实例的统一资源名称（URN）
        :type instance_urn: str
        """
        
        

        self._identity_store_id = None
        self._instance_id = None
        self._alias = None
        self._instance_urn = None
        self.discriminator = None

        self.identity_store_id = identity_store_id
        self.instance_id = instance_id
        if alias is not None:
            self.alias = alias
        if instance_urn is not None:
            self.instance_urn = instance_urn

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this InstanceMetadataEntryDto.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :return: The identity_store_id of this InstanceMetadataEntryDto.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this InstanceMetadataEntryDto.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :param identity_store_id: The identity_store_id of this InstanceMetadataEntryDto.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceMetadataEntryDto.

        Identity Center实例的全局唯一标识符（ID）

        :return: The instance_id of this InstanceMetadataEntryDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceMetadataEntryDto.

        Identity Center实例的全局唯一标识符（ID）

        :param instance_id: The instance_id of this InstanceMetadataEntryDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def alias(self):
        r"""Gets the alias of this InstanceMetadataEntryDto.

        用户为身份源标识符定义的别名

        :return: The alias of this InstanceMetadataEntryDto.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this InstanceMetadataEntryDto.

        用户为身份源标识符定义的别名

        :param alias: The alias of this InstanceMetadataEntryDto.
        :type alias: str
        """
        self._alias = alias

    @property
    def instance_urn(self):
        r"""Gets the instance_urn of this InstanceMetadataEntryDto.

        实例的统一资源名称（URN）

        :return: The instance_urn of this InstanceMetadataEntryDto.
        :rtype: str
        """
        return self._instance_urn

    @instance_urn.setter
    def instance_urn(self, instance_urn):
        r"""Sets the instance_urn of this InstanceMetadataEntryDto.

        实例的统一资源名称（URN）

        :param instance_urn: The instance_urn of this InstanceMetadataEntryDto.
        :type instance_urn: str
        """
        self._instance_urn = instance_urn

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
        if not isinstance(other, InstanceMetadataEntryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
