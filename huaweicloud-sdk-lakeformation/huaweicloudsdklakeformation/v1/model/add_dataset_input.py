# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDatasetInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_name': 'str',
        'description': 'str',
        'storage_type': 'str',
        'dataset_format': 'DatasetFileFormat',
        'owner': 'str',
        'owner_type': 'str',
        'owner_source': 'str',
        'location': 'str',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'dataset_name': 'dataset_name',
        'description': 'description',
        'storage_type': 'storage_type',
        'dataset_format': 'dataset_format',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'owner_source': 'owner_source',
        'location': 'location',
        'properties': 'properties'
    }

    def __init__(self, dataset_name=None, description=None, storage_type=None, dataset_format=None, owner=None, owner_type=None, owner_source=None, location=None, properties=None):
        r"""AddDatasetInput

        The model defined in huaweicloud sdk

        :param dataset_name: 数据集名称
        :type dataset_name: str
        :param description: 数据集的描述信息
        :type description: str
        :param storage_type: 数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储 EXTERNAL类型的数据集不支持创建文件分组和文件元数据。
        :type storage_type: str
        :param dataset_format: 
        :type dataset_format: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        :param owner: Dataset所有者
        :type owner: str
        :param owner_type: 所有者类型,USER-用户,GROUP-组,ROLE-角色。LakeFormation服务一期实例响应Body无该参数。
        :type owner_type: str
        :param owner_source: 所有者来源,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务一期实例响应Body无该参数。
        :type owner_source: str
        :param location: 外置存储类型的元数据存储位置
        :type location: str
        :param properties: 数据集其他属性
        :type properties: dict(str, str)
        """
        
        

        self._dataset_name = None
        self._description = None
        self._storage_type = None
        self._dataset_format = None
        self._owner = None
        self._owner_type = None
        self._owner_source = None
        self._location = None
        self._properties = None
        self.discriminator = None

        self.dataset_name = dataset_name
        if description is not None:
            self.description = description
        self.storage_type = storage_type
        if dataset_format is not None:
            self.dataset_format = dataset_format
        if owner is not None:
            self.owner = owner
        if owner_type is not None:
            self.owner_type = owner_type
        if owner_source is not None:
            self.owner_source = owner_source
        if location is not None:
            self.location = location
        if properties is not None:
            self.properties = properties

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this AddDatasetInput.

        数据集名称

        :return: The dataset_name of this AddDatasetInput.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this AddDatasetInput.

        数据集名称

        :param dataset_name: The dataset_name of this AddDatasetInput.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def description(self):
        r"""Gets the description of this AddDatasetInput.

        数据集的描述信息

        :return: The description of this AddDatasetInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddDatasetInput.

        数据集的描述信息

        :param description: The description of this AddDatasetInput.
        :type description: str
        """
        self._description = description

    @property
    def storage_type(self):
        r"""Gets the storage_type of this AddDatasetInput.

        数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储 EXTERNAL类型的数据集不支持创建文件分组和文件元数据。

        :return: The storage_type of this AddDatasetInput.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this AddDatasetInput.

        数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储 EXTERNAL类型的数据集不支持创建文件分组和文件元数据。

        :param storage_type: The storage_type of this AddDatasetInput.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def dataset_format(self):
        r"""Gets the dataset_format of this AddDatasetInput.

        :return: The dataset_format of this AddDatasetInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        return self._dataset_format

    @dataset_format.setter
    def dataset_format(self, dataset_format):
        r"""Sets the dataset_format of this AddDatasetInput.

        :param dataset_format: The dataset_format of this AddDatasetInput.
        :type dataset_format: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        self._dataset_format = dataset_format

    @property
    def owner(self):
        r"""Gets the owner of this AddDatasetInput.

        Dataset所有者

        :return: The owner of this AddDatasetInput.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this AddDatasetInput.

        Dataset所有者

        :param owner: The owner of this AddDatasetInput.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this AddDatasetInput.

        所有者类型,USER-用户,GROUP-组,ROLE-角色。LakeFormation服务一期实例响应Body无该参数。

        :return: The owner_type of this AddDatasetInput.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this AddDatasetInput.

        所有者类型,USER-用户,GROUP-组,ROLE-角色。LakeFormation服务一期实例响应Body无该参数。

        :param owner_type: The owner_type of this AddDatasetInput.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def owner_source(self):
        r"""Gets the owner_source of this AddDatasetInput.

        所有者来源,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务一期实例响应Body无该参数。

        :return: The owner_source of this AddDatasetInput.
        :rtype: str
        """
        return self._owner_source

    @owner_source.setter
    def owner_source(self, owner_source):
        r"""Sets the owner_source of this AddDatasetInput.

        所有者来源,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务一期实例响应Body无该参数。

        :param owner_source: The owner_source of this AddDatasetInput.
        :type owner_source: str
        """
        self._owner_source = owner_source

    @property
    def location(self):
        r"""Gets the location of this AddDatasetInput.

        外置存储类型的元数据存储位置

        :return: The location of this AddDatasetInput.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this AddDatasetInput.

        外置存储类型的元数据存储位置

        :param location: The location of this AddDatasetInput.
        :type location: str
        """
        self._location = location

    @property
    def properties(self):
        r"""Gets the properties of this AddDatasetInput.

        数据集其他属性

        :return: The properties of this AddDatasetInput.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AddDatasetInput.

        数据集其他属性

        :param properties: The properties of this AddDatasetInput.
        :type properties: dict(str, str)
        """
        self._properties = properties

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddDatasetInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
