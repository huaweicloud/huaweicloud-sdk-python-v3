# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndPointResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'EndPointResponseAuthorization',
        'uuid': 'str',
        'url': 'str',
        'name': 'str',
        'project_uuid': 'str',
        'region_name': 'str',
        'data': 'object',
        'module_id': 'str',
        'created_by': 'EndPointResponseCreatedBy'
    }

    attribute_map = {
        'authorization': 'authorization',
        'uuid': 'uuid',
        'url': 'url',
        'name': 'name',
        'project_uuid': 'project_uuid',
        'region_name': 'region_name',
        'data': 'data',
        'module_id': 'module_id',
        'created_by': 'created_by'
    }

    def __init__(self, authorization=None, uuid=None, url=None, name=None, project_uuid=None, region_name=None, data=None, module_id=None, created_by=None):
        r"""EndPointResponse

        The model defined in huaweicloud sdk

        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseAuthorization`
        :param uuid: uuid
        :type uuid: str
        :param url: 访问地址
        :type url: str
        :param name: 名称
        :type name: str
        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param region_name: 区域名称
        :type region_name: str
        :param data: 数据
        :type data: object
        :param module_id: 模块id
        :type module_id: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseCreatedBy`
        """
        
        

        self._authorization = None
        self._uuid = None
        self._url = None
        self._name = None
        self._project_uuid = None
        self._region_name = None
        self._data = None
        self._module_id = None
        self._created_by = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if uuid is not None:
            self.uuid = uuid
        if url is not None:
            self.url = url
        if name is not None:
            self.name = name
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if region_name is not None:
            self.region_name = region_name
        if data is not None:
            self.data = data
        if module_id is not None:
            self.module_id = module_id
        if created_by is not None:
            self.created_by = created_by

    @property
    def authorization(self):
        r"""Gets the authorization of this EndPointResponse.

        :return: The authorization of this EndPointResponse.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseAuthorization`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this EndPointResponse.

        :param authorization: The authorization of this EndPointResponse.
        :type authorization: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseAuthorization`
        """
        self._authorization = authorization

    @property
    def uuid(self):
        r"""Gets the uuid of this EndPointResponse.

        uuid

        :return: The uuid of this EndPointResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this EndPointResponse.

        uuid

        :param uuid: The uuid of this EndPointResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def url(self):
        r"""Gets the url of this EndPointResponse.

        访问地址

        :return: The url of this EndPointResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this EndPointResponse.

        访问地址

        :param url: The url of this EndPointResponse.
        :type url: str
        """
        self._url = url

    @property
    def name(self):
        r"""Gets the name of this EndPointResponse.

        名称

        :return: The name of this EndPointResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EndPointResponse.

        名称

        :param name: The name of this EndPointResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this EndPointResponse.

        项目uuid

        :return: The project_uuid of this EndPointResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this EndPointResponse.

        项目uuid

        :param project_uuid: The project_uuid of this EndPointResponse.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def region_name(self):
        r"""Gets the region_name of this EndPointResponse.

        区域名称

        :return: The region_name of this EndPointResponse.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this EndPointResponse.

        区域名称

        :param region_name: The region_name of this EndPointResponse.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def data(self):
        r"""Gets the data of this EndPointResponse.

        数据

        :return: The data of this EndPointResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this EndPointResponse.

        数据

        :param data: The data of this EndPointResponse.
        :type data: object
        """
        self._data = data

    @property
    def module_id(self):
        r"""Gets the module_id of this EndPointResponse.

        模块id

        :return: The module_id of this EndPointResponse.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this EndPointResponse.

        模块id

        :param module_id: The module_id of this EndPointResponse.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def created_by(self):
        r"""Gets the created_by of this EndPointResponse.

        :return: The created_by of this EndPointResponse.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseCreatedBy`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this EndPointResponse.

        :param created_by: The created_by of this EndPointResponse.
        :type created_by: :class:`huaweicloudsdkcodeartsbuild.v3.EndPointResponseCreatedBy`
        """
        self._created_by = created_by

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
        if not isinstance(other, EndPointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
