# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicateKeyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'replica_region': 'str',
        'key_alias': 'str',
        'key_description': 'str',
        'enterprise_project_id': 'str',
        'replica_project_id': 'str',
        'tags': 'list[TagItem]'
    }

    attribute_map = {
        'key_id': 'key_id',
        'replica_region': 'replica_region',
        'key_alias': 'key_alias',
        'key_description': 'key_description',
        'enterprise_project_id': 'enterprise_project_id',
        'replica_project_id': 'replica_project_id',
        'tags': 'tags'
    }

    def __init__(self, key_id=None, replica_region=None, key_alias=None, key_description=None, enterprise_project_id=None, replica_project_id=None, tags=None):
        r"""ReplicateKeyRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param replica_region: 复制密钥的目的区域编码。如cn-north-4。
        :type replica_region: str
        :param key_alias: 指定复制出的新密钥的别名。
        :type key_alias: str
        :param key_description: 指定复制出的新密钥的描述信息。
        :type key_description: str
        :param enterprise_project_id: 指定复制出的新密钥的企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。
        :type enterprise_project_id: str
        :param replica_project_id: 指定复制出的新密钥的项目ID。
        :type replica_project_id: str
        :param tags: 标签列表，key和value键值对的集合。
        :type tags: list[:class:`huaweicloudsdkkms.v2.TagItem`]
        """
        
        

        self._key_id = None
        self._replica_region = None
        self._key_alias = None
        self._key_description = None
        self._enterprise_project_id = None
        self._replica_project_id = None
        self._tags = None
        self.discriminator = None

        self.key_id = key_id
        self.replica_region = replica_region
        self.key_alias = key_alias
        if key_description is not None:
            self.key_description = key_description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.replica_project_id = replica_project_id
        if tags is not None:
            self.tags = tags

    @property
    def key_id(self):
        r"""Gets the key_id of this ReplicateKeyRequestBody.

        待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ReplicateKeyRequestBody.

        待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this ReplicateKeyRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def replica_region(self):
        r"""Gets the replica_region of this ReplicateKeyRequestBody.

        复制密钥的目的区域编码。如cn-north-4。

        :return: The replica_region of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._replica_region

    @replica_region.setter
    def replica_region(self, replica_region):
        r"""Sets the replica_region of this ReplicateKeyRequestBody.

        复制密钥的目的区域编码。如cn-north-4。

        :param replica_region: The replica_region of this ReplicateKeyRequestBody.
        :type replica_region: str
        """
        self._replica_region = replica_region

    @property
    def key_alias(self):
        r"""Gets the key_alias of this ReplicateKeyRequestBody.

        指定复制出的新密钥的别名。

        :return: The key_alias of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        r"""Sets the key_alias of this ReplicateKeyRequestBody.

        指定复制出的新密钥的别名。

        :param key_alias: The key_alias of this ReplicateKeyRequestBody.
        :type key_alias: str
        """
        self._key_alias = key_alias

    @property
    def key_description(self):
        r"""Gets the key_description of this ReplicateKeyRequestBody.

        指定复制出的新密钥的描述信息。

        :return: The key_description of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._key_description

    @key_description.setter
    def key_description(self, key_description):
        r"""Sets the key_description of this ReplicateKeyRequestBody.

        指定复制出的新密钥的描述信息。

        :param key_description: The key_description of this ReplicateKeyRequestBody.
        :type key_description: str
        """
        self._key_description = key_description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ReplicateKeyRequestBody.

        指定复制出的新密钥的企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。

        :return: The enterprise_project_id of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ReplicateKeyRequestBody.

        指定复制出的新密钥的企业多项目ID。 - 用户未开通企业多项目时，不需要输入该字段。 - 用户开通企业多项目时，创建资源可以输入该字段。若用户户不输入该字段，默认创建属于默认企业多项目ID（ID为“0”）的资源。 注意：若用户没有默认企业多项目ID（ID为“0”）下的创建权限，则接口报错。

        :param enterprise_project_id: The enterprise_project_id of this ReplicateKeyRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def replica_project_id(self):
        r"""Gets the replica_project_id of this ReplicateKeyRequestBody.

        指定复制出的新密钥的项目ID。

        :return: The replica_project_id of this ReplicateKeyRequestBody.
        :rtype: str
        """
        return self._replica_project_id

    @replica_project_id.setter
    def replica_project_id(self, replica_project_id):
        r"""Sets the replica_project_id of this ReplicateKeyRequestBody.

        指定复制出的新密钥的项目ID。

        :param replica_project_id: The replica_project_id of this ReplicateKeyRequestBody.
        :type replica_project_id: str
        """
        self._replica_project_id = replica_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ReplicateKeyRequestBody.

        标签列表，key和value键值对的集合。

        :return: The tags of this ReplicateKeyRequestBody.
        :rtype: list[:class:`huaweicloudsdkkms.v2.TagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ReplicateKeyRequestBody.

        标签列表，key和value键值对的集合。

        :param tags: The tags of this ReplicateKeyRequestBody.
        :type tags: list[:class:`huaweicloudsdkkms.v2.TagItem`]
        """
        self._tags = tags

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
        if not isinstance(other, ReplicateKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
