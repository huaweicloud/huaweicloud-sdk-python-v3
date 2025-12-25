# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModuleUpdateRequestPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'cloud_pack_version': 'str',
        'description': 'str',
        'module_json': 'str',
        'name': 'str',
        'update_time': 'str',
        'thumbnail': 'str',
        'module_type': 'str',
        'metric_ids': 'str',
        'data_query': 'str',
        'boa_version': 'str'
    }

    attribute_map = {
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'cloud_pack_version': 'cloud_pack_version',
        'description': 'description',
        'module_json': 'module_json',
        'name': 'name',
        'update_time': 'update_time',
        'thumbnail': 'thumbnail',
        'module_type': 'module_type',
        'metric_ids': 'metric_ids',
        'data_query': 'data_query',
        'boa_version': 'boa_version'
    }

    def __init__(self, cloud_pack_id=None, cloud_pack_name=None, cloud_pack_version=None, description=None, module_json=None, name=None, update_time=None, thumbnail=None, module_type=None, metric_ids=None, data_query=None, boa_version=None):
        r"""ModuleUpdateRequestPojo

        The model defined in huaweicloud sdk

        :param cloud_pack_id: 订阅包id
        :type cloud_pack_id: str
        :param cloud_pack_name: 订阅包名称
        :type cloud_pack_name: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param description: 描述
        :type description: str
        :param module_json: 布局模块相关信息
        :type module_json: str
        :param name: 名称
        :type name: str
        :param update_time: 更新时间
        :type update_time: str
        :param thumbnail: 模块缩略图
        :type thumbnail: str
        :param module_type: 模块类型,tab/section
        :type module_type: str
        :param metric_ids: section类模块关联的指标id
        :type metric_ids: str
        :param data_query: 数据查询方式
        :type data_query: str
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._cloud_pack_version = None
        self._description = None
        self._module_json = None
        self._name = None
        self._update_time = None
        self._thumbnail = None
        self._module_type = None
        self._metric_ids = None
        self._data_query = None
        self._boa_version = None
        self.discriminator = None

        if cloud_pack_id is not None:
            self.cloud_pack_id = cloud_pack_id
        if cloud_pack_name is not None:
            self.cloud_pack_name = cloud_pack_name
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if description is not None:
            self.description = description
        if module_json is not None:
            self.module_json = module_json
        self.name = name
        if update_time is not None:
            self.update_time = update_time
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if module_type is not None:
            self.module_type = module_type
        if metric_ids is not None:
            self.metric_ids = metric_ids
        if data_query is not None:
            self.data_query = data_query
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this ModuleUpdateRequestPojo.

        订阅包id

        :return: The cloud_pack_id of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this ModuleUpdateRequestPojo.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this ModuleUpdateRequestPojo.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this ModuleUpdateRequestPojo.

        订阅包名称

        :return: The cloud_pack_name of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this ModuleUpdateRequestPojo.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this ModuleUpdateRequestPojo.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this ModuleUpdateRequestPojo.

        订阅包版本

        :return: The cloud_pack_version of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this ModuleUpdateRequestPojo.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this ModuleUpdateRequestPojo.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def description(self):
        r"""Gets the description of this ModuleUpdateRequestPojo.

        描述

        :return: The description of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModuleUpdateRequestPojo.

        描述

        :param description: The description of this ModuleUpdateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def module_json(self):
        r"""Gets the module_json of this ModuleUpdateRequestPojo.

        布局模块相关信息

        :return: The module_json of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._module_json

    @module_json.setter
    def module_json(self, module_json):
        r"""Sets the module_json of this ModuleUpdateRequestPojo.

        布局模块相关信息

        :param module_json: The module_json of this ModuleUpdateRequestPojo.
        :type module_json: str
        """
        self._module_json = module_json

    @property
    def name(self):
        r"""Gets the name of this ModuleUpdateRequestPojo.

        名称

        :return: The name of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModuleUpdateRequestPojo.

        名称

        :param name: The name of this ModuleUpdateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def update_time(self):
        r"""Gets the update_time of this ModuleUpdateRequestPojo.

        更新时间

        :return: The update_time of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModuleUpdateRequestPojo.

        更新时间

        :param update_time: The update_time of this ModuleUpdateRequestPojo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this ModuleUpdateRequestPojo.

        模块缩略图

        :return: The thumbnail of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this ModuleUpdateRequestPojo.

        模块缩略图

        :param thumbnail: The thumbnail of this ModuleUpdateRequestPojo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def module_type(self):
        r"""Gets the module_type of this ModuleUpdateRequestPojo.

        模块类型,tab/section

        :return: The module_type of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this ModuleUpdateRequestPojo.

        模块类型,tab/section

        :param module_type: The module_type of this ModuleUpdateRequestPojo.
        :type module_type: str
        """
        self._module_type = module_type

    @property
    def metric_ids(self):
        r"""Gets the metric_ids of this ModuleUpdateRequestPojo.

        section类模块关联的指标id

        :return: The metric_ids of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._metric_ids

    @metric_ids.setter
    def metric_ids(self, metric_ids):
        r"""Sets the metric_ids of this ModuleUpdateRequestPojo.

        section类模块关联的指标id

        :param metric_ids: The metric_ids of this ModuleUpdateRequestPojo.
        :type metric_ids: str
        """
        self._metric_ids = metric_ids

    @property
    def data_query(self):
        r"""Gets the data_query of this ModuleUpdateRequestPojo.

        数据查询方式

        :return: The data_query of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._data_query

    @data_query.setter
    def data_query(self, data_query):
        r"""Sets the data_query of this ModuleUpdateRequestPojo.

        数据查询方式

        :param data_query: The data_query of this ModuleUpdateRequestPojo.
        :type data_query: str
        """
        self._data_query = data_query

    @property
    def boa_version(self):
        r"""Gets the boa_version of this ModuleUpdateRequestPojo.

        BOA底座版本

        :return: The boa_version of this ModuleUpdateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this ModuleUpdateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this ModuleUpdateRequestPojo.
        :type boa_version: str
        """
        self._boa_version = boa_version

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
        if not isinstance(other, ModuleUpdateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
