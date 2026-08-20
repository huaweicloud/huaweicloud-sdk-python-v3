# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_by': 'EndpointCreatorInfo',
        'data': 'object',
        'module_id': 'str',
        'name': 'str',
        'project_uuid': 'str',
        'region_name': 'str',
        'url': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'created_by': 'created_by',
        'data': 'data',
        'module_id': 'module_id',
        'name': 'name',
        'project_uuid': 'project_uuid',
        'region_name': 'region_name',
        'url': 'url',
        'uuid': 'uuid'
    }

    def __init__(self, created_by=None, data=None, module_id=None, name=None, project_uuid=None, region_name=None, url=None, uuid=None):
        r"""Endpoint

        The model defined in huaweicloud sdk

        :param created_by: 
        :type created_by: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointCreatorInfo`
        :param data: 扩展点数据
        :type data: object
        :param module_id: 模块id
        :type module_id: str
        :param name: 模块名称（用于搜索）
        :type name: str
        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param region_name: 区域名
        :type region_name: str
        :param url: 链接地址
        :type url: str
        :param uuid: 扩展点id
        :type uuid: str
        """
        
        

        self._created_by = None
        self._data = None
        self._module_id = None
        self._name = None
        self._project_uuid = None
        self._region_name = None
        self._url = None
        self._uuid = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if data is not None:
            self.data = data
        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if region_name is not None:
            self.region_name = region_name
        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_by(self):
        r"""Gets the created_by of this Endpoint.

        :return: The created_by of this Endpoint.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointCreatorInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this Endpoint.

        :param created_by: The created_by of this Endpoint.
        :type created_by: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointCreatorInfo`
        """
        self._created_by = created_by

    @property
    def data(self):
        r"""Gets the data of this Endpoint.

        扩展点数据

        :return: The data of this Endpoint.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this Endpoint.

        扩展点数据

        :param data: The data of this Endpoint.
        :type data: object
        """
        self._data = data

    @property
    def module_id(self):
        r"""Gets the module_id of this Endpoint.

        模块id

        :return: The module_id of this Endpoint.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this Endpoint.

        模块id

        :param module_id: The module_id of this Endpoint.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        r"""Gets the name of this Endpoint.

        模块名称（用于搜索）

        :return: The name of this Endpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Endpoint.

        模块名称（用于搜索）

        :param name: The name of this Endpoint.
        :type name: str
        """
        self._name = name

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this Endpoint.

        项目uuid

        :return: The project_uuid of this Endpoint.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this Endpoint.

        项目uuid

        :param project_uuid: The project_uuid of this Endpoint.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def region_name(self):
        r"""Gets the region_name of this Endpoint.

        区域名

        :return: The region_name of this Endpoint.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this Endpoint.

        区域名

        :param region_name: The region_name of this Endpoint.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def url(self):
        r"""Gets the url of this Endpoint.

        链接地址

        :return: The url of this Endpoint.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Endpoint.

        链接地址

        :param url: The url of this Endpoint.
        :type url: str
        """
        self._url = url

    @property
    def uuid(self):
        r"""Gets the uuid of this Endpoint.

        扩展点id

        :return: The uuid of this Endpoint.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this Endpoint.

        扩展点id

        :param uuid: The uuid of this Endpoint.
        :type uuid: str
        """
        self._uuid = uuid

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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
