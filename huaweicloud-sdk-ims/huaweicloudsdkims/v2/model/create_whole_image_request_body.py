# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWholeImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_tags': 'list[TagKeyValue]',
        'instance_id': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'backup_id': 'str',
        'whole_image_type': 'str',
        'max_ram': 'int',
        'min_ram': 'int',
        'vault_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_tags': 'image_tags',
        'instance_id': 'instance_id',
        'name': 'name',
        'tags': 'tags',
        'backup_id': 'backup_id',
        'whole_image_type': 'whole_image_type',
        'max_ram': 'max_ram',
        'min_ram': 'min_ram',
        'vault_id': 'vault_id'
    }

    def __init__(self, description=None, enterprise_project_id=None, image_tags=None, instance_id=None, name=None, tags=None, backup_id=None, whole_image_type=None, max_ram=None, min_ram=None, vault_id=None):
        r"""CreateWholeImageRequestBody

        The model defined in huaweicloud sdk

        :param description: 镜像描述信息。 支持字母、数字、中文等，不支持回车、&lt;、 &gt;，长度不能超过1024个字符。
        :type description: str
        :param enterprise_project_id: 表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。
        :type enterprise_project_id: str
        :param image_tags: 新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。
        :type image_tags: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        :param instance_id: 弹性云服务器ID。使用弹性云服务器制作整机镜像时使用此参数且必填。 如果使用备份创建整机镜像，该参数应换成backup_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。
        :type instance_id: str
        :param name: 镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。
        :type name: str
        :param tags: 镜像标签列表。tags和image_tags只能使用一个。
        :type tags: list[str]
        :param backup_id: 使用云服务器备份创建整机镜像使用此参数且必填。 如果使用ECS创建整机镜像，则该参数应传为instance_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。
        :type backup_id: str
        :param whole_image_type: 使用备份创建整机镜像时，该字段区分是CBR服务的备份还是CSBS服务的备份，取值为：CBR/CSBS。 使用ECS创建整机镜像时，该字段不填
        :type whole_image_type: str
        :param max_ram: 表示镜像支持的最大内存，单位为MB，默认不设置。
        :type max_ram: int
        :param min_ram: 表示镜像支持的最小内存，单位为MB，默认为0。
        :type min_ram: int
        :param vault_id: 表示云服务器待加入的或已加入的存储库的ID。 使用云服务器创建整机镜像的过程为：先创建一个备份，再将备份创建为整机镜像。如果这个备份为CBR，vault_id为必填项；如果备份为CSBS，vault_id参数可不填。
        :type vault_id: str
        """
        
        

        self._description = None
        self._enterprise_project_id = None
        self._image_tags = None
        self._instance_id = None
        self._name = None
        self._tags = None
        self._backup_id = None
        self._whole_image_type = None
        self._max_ram = None
        self._min_ram = None
        self._vault_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_tags is not None:
            self.image_tags = image_tags
        self.instance_id = instance_id
        self.name = name
        if tags is not None:
            self.tags = tags
        if backup_id is not None:
            self.backup_id = backup_id
        if whole_image_type is not None:
            self.whole_image_type = whole_image_type
        if max_ram is not None:
            self.max_ram = max_ram
        if min_ram is not None:
            self.min_ram = min_ram
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def description(self):
        r"""Gets the description of this CreateWholeImageRequestBody.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :return: The description of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWholeImageRequestBody.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :param description: The description of this CreateWholeImageRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateWholeImageRequestBody.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :return: The enterprise_project_id of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateWholeImageRequestBody.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this CreateWholeImageRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_tags(self):
        r"""Gets the image_tags of this CreateWholeImageRequestBody.

        新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :return: The image_tags of this CreateWholeImageRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        r"""Sets the image_tags of this CreateWholeImageRequestBody.

        新规范的镜像标签列表。默认为空。tags和image_tags只能使用一个。

        :param image_tags: The image_tags of this CreateWholeImageRequestBody.
        :type image_tags: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        self._image_tags = image_tags

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateWholeImageRequestBody.

        弹性云服务器ID。使用弹性云服务器制作整机镜像时使用此参数且必填。 如果使用备份创建整机镜像，该参数应换成backup_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。

        :return: The instance_id of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateWholeImageRequestBody.

        弹性云服务器ID。使用弹性云服务器制作整机镜像时使用此参数且必填。 如果使用备份创建整机镜像，该参数应换成backup_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。

        :param instance_id: The instance_id of this CreateWholeImageRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this CreateWholeImageRequestBody.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :return: The name of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWholeImageRequestBody.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :param name: The name of this CreateWholeImageRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this CreateWholeImageRequestBody.

        镜像标签列表。tags和image_tags只能使用一个。

        :return: The tags of this CreateWholeImageRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateWholeImageRequestBody.

        镜像标签列表。tags和image_tags只能使用一个。

        :param tags: The tags of this CreateWholeImageRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def backup_id(self):
        r"""Gets the backup_id of this CreateWholeImageRequestBody.

        使用云服务器备份创建整机镜像使用此参数且必填。 如果使用ECS创建整机镜像，则该参数应传为instance_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。

        :return: The backup_id of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this CreateWholeImageRequestBody.

        使用云服务器备份创建整机镜像使用此参数且必填。 如果使用ECS创建整机镜像，则该参数应传为instance_id。 非必填的原因是需要兼容“使用备份创建整机镜像”和“使用弹性云服务器制作整机镜像”两种场景的body体。

        :param backup_id: The backup_id of this CreateWholeImageRequestBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def whole_image_type(self):
        r"""Gets the whole_image_type of this CreateWholeImageRequestBody.

        使用备份创建整机镜像时，该字段区分是CBR服务的备份还是CSBS服务的备份，取值为：CBR/CSBS。 使用ECS创建整机镜像时，该字段不填

        :return: The whole_image_type of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._whole_image_type

    @whole_image_type.setter
    def whole_image_type(self, whole_image_type):
        r"""Sets the whole_image_type of this CreateWholeImageRequestBody.

        使用备份创建整机镜像时，该字段区分是CBR服务的备份还是CSBS服务的备份，取值为：CBR/CSBS。 使用ECS创建整机镜像时，该字段不填

        :param whole_image_type: The whole_image_type of this CreateWholeImageRequestBody.
        :type whole_image_type: str
        """
        self._whole_image_type = whole_image_type

    @property
    def max_ram(self):
        r"""Gets the max_ram of this CreateWholeImageRequestBody.

        表示镜像支持的最大内存，单位为MB，默认不设置。

        :return: The max_ram of this CreateWholeImageRequestBody.
        :rtype: int
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        r"""Sets the max_ram of this CreateWholeImageRequestBody.

        表示镜像支持的最大内存，单位为MB，默认不设置。

        :param max_ram: The max_ram of this CreateWholeImageRequestBody.
        :type max_ram: int
        """
        self._max_ram = max_ram

    @property
    def min_ram(self):
        r"""Gets the min_ram of this CreateWholeImageRequestBody.

        表示镜像支持的最小内存，单位为MB，默认为0。

        :return: The min_ram of this CreateWholeImageRequestBody.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this CreateWholeImageRequestBody.

        表示镜像支持的最小内存，单位为MB，默认为0。

        :param min_ram: The min_ram of this CreateWholeImageRequestBody.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def vault_id(self):
        r"""Gets the vault_id of this CreateWholeImageRequestBody.

        表示云服务器待加入的或已加入的存储库的ID。 使用云服务器创建整机镜像的过程为：先创建一个备份，再将备份创建为整机镜像。如果这个备份为CBR，vault_id为必填项；如果备份为CSBS，vault_id参数可不填。

        :return: The vault_id of this CreateWholeImageRequestBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this CreateWholeImageRequestBody.

        表示云服务器待加入的或已加入的存储库的ID。 使用云服务器创建整机镜像的过程为：先创建一个备份，再将备份创建为整机镜像。如果这个备份为CBR，vault_id为必填项；如果备份为CSBS，vault_id参数可不填。

        :param vault_id: The vault_id of this CreateWholeImageRequestBody.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, CreateWholeImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
