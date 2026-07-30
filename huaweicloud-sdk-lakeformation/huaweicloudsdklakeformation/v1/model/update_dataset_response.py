# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatasetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'catalog_id': 'str',
        'dataset_name': 'str',
        'dataset_id': 'str',
        'description': 'str',
        'database_name': 'str',
        'database_id': 'str',
        'storage_type': 'str',
        'dataset_format': 'DatasetFileFormat',
        'owner': 'str',
        'owner_type': 'str',
        'owner_source': 'str',
        'location': 'str',
        'properties': 'dict(str, str)',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'catalog_id': 'catalog_id',
        'dataset_name': 'dataset_name',
        'dataset_id': 'dataset_id',
        'description': 'description',
        'database_name': 'database_name',
        'database_id': 'database_id',
        'storage_type': 'storage_type',
        'dataset_format': 'dataset_format',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'owner_source': 'owner_source',
        'location': 'location',
        'properties': 'properties',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, catalog_name=None, catalog_id=None, dataset_name=None, dataset_id=None, description=None, database_name=None, database_id=None, storage_type=None, dataset_format=None, owner=None, owner_type=None, owner_source=None, location=None, properties=None, create_time=None, update_time=None):
        r"""UpdateDatasetResponse

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名称
        :type catalog_name: str
        :param catalog_id: catalogID
        :type catalog_id: str
        :param dataset_name: 数据集名称
        :type dataset_name: str
        :param dataset_id: DatasetID
        :type dataset_id: str
        :param description: 数据集的描述信息
        :type description: str
        :param database_name: 数据库名称。
        :type database_name: str
        :param database_id: 数据库ID。
        :type database_id: str
        :param storage_type: 数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储
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
        :param create_time: 数据集创建时间
        :type create_time: datetime
        :param update_time: 数据集修改时间
        :type update_time: datetime
        """
        
        super().__init__()

        self._catalog_name = None
        self._catalog_id = None
        self._dataset_name = None
        self._dataset_id = None
        self._description = None
        self._database_name = None
        self._database_id = None
        self._storage_type = None
        self._dataset_format = None
        self._owner = None
        self._owner_type = None
        self._owner_source = None
        self._location = None
        self._properties = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if catalog_name is not None:
            self.catalog_name = catalog_name
        if catalog_id is not None:
            self.catalog_id = catalog_id
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if description is not None:
            self.description = description
        if database_name is not None:
            self.database_name = database_name
        if database_id is not None:
            self.database_id = database_id
        if storage_type is not None:
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this UpdateDatasetResponse.

        catalog名称

        :return: The catalog_name of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this UpdateDatasetResponse.

        catalog名称

        :param catalog_name: The catalog_name of this UpdateDatasetResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this UpdateDatasetResponse.

        catalogID

        :return: The catalog_id of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this UpdateDatasetResponse.

        catalogID

        :param catalog_id: The catalog_id of this UpdateDatasetResponse.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this UpdateDatasetResponse.

        数据集名称

        :return: The dataset_name of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this UpdateDatasetResponse.

        数据集名称

        :param dataset_name: The dataset_name of this UpdateDatasetResponse.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this UpdateDatasetResponse.

        DatasetID

        :return: The dataset_id of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this UpdateDatasetResponse.

        DatasetID

        :param dataset_id: The dataset_id of this UpdateDatasetResponse.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def description(self):
        r"""Gets the description of this UpdateDatasetResponse.

        数据集的描述信息

        :return: The description of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateDatasetResponse.

        数据集的描述信息

        :param description: The description of this UpdateDatasetResponse.
        :type description: str
        """
        self._description = description

    @property
    def database_name(self):
        r"""Gets the database_name of this UpdateDatasetResponse.

        数据库名称。

        :return: The database_name of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this UpdateDatasetResponse.

        数据库名称。

        :param database_name: The database_name of this UpdateDatasetResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def database_id(self):
        r"""Gets the database_id of this UpdateDatasetResponse.

        数据库ID。

        :return: The database_id of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        r"""Sets the database_id of this UpdateDatasetResponse.

        数据库ID。

        :param database_id: The database_id of this UpdateDatasetResponse.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def storage_type(self):
        r"""Gets the storage_type of this UpdateDatasetResponse.

        数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储

        :return: The storage_type of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this UpdateDatasetResponse.

        数据集存储类型：EXTERNAL-外置存储,MANAGED-系统托管存储

        :param storage_type: The storage_type of this UpdateDatasetResponse.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def dataset_format(self):
        r"""Gets the dataset_format of this UpdateDatasetResponse.

        :return: The dataset_format of this UpdateDatasetResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        return self._dataset_format

    @dataset_format.setter
    def dataset_format(self, dataset_format):
        r"""Sets the dataset_format of this UpdateDatasetResponse.

        :param dataset_format: The dataset_format of this UpdateDatasetResponse.
        :type dataset_format: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        self._dataset_format = dataset_format

    @property
    def owner(self):
        r"""Gets the owner of this UpdateDatasetResponse.

        Dataset所有者

        :return: The owner of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this UpdateDatasetResponse.

        Dataset所有者

        :param owner: The owner of this UpdateDatasetResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this UpdateDatasetResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色。LakeFormation服务一期实例响应Body无该参数。

        :return: The owner_type of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this UpdateDatasetResponse.

        所有者类型,USER-用户,GROUP-组,ROLE-角色。LakeFormation服务一期实例响应Body无该参数。

        :param owner_type: The owner_type of this UpdateDatasetResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def owner_source(self):
        r"""Gets the owner_source of this UpdateDatasetResponse.

        所有者来源,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务一期实例响应Body无该参数。

        :return: The owner_source of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._owner_source

    @owner_source.setter
    def owner_source(self, owner_source):
        r"""Sets the owner_source of this UpdateDatasetResponse.

        所有者来源,IAM-云用户,SAML-联邦,LDAP-ld用户,LOCAL-本地用户,AGENTTENANT-委托,OTHER-其它。LakeFormation服务一期实例响应Body无该参数。

        :param owner_source: The owner_source of this UpdateDatasetResponse.
        :type owner_source: str
        """
        self._owner_source = owner_source

    @property
    def location(self):
        r"""Gets the location of this UpdateDatasetResponse.

        外置存储类型的元数据存储位置

        :return: The location of this UpdateDatasetResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this UpdateDatasetResponse.

        外置存储类型的元数据存储位置

        :param location: The location of this UpdateDatasetResponse.
        :type location: str
        """
        self._location = location

    @property
    def properties(self):
        r"""Gets the properties of this UpdateDatasetResponse.

        数据集其他属性

        :return: The properties of this UpdateDatasetResponse.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this UpdateDatasetResponse.

        数据集其他属性

        :param properties: The properties of this UpdateDatasetResponse.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateDatasetResponse.

        数据集创建时间

        :return: The create_time of this UpdateDatasetResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateDatasetResponse.

        数据集创建时间

        :param create_time: The create_time of this UpdateDatasetResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateDatasetResponse.

        数据集修改时间

        :return: The update_time of this UpdateDatasetResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateDatasetResponse.

        数据集修改时间

        :param update_time: The update_time of this UpdateDatasetResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("UpdateDatasetResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
