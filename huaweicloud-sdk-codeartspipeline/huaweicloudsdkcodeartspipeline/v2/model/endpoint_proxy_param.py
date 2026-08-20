# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointProxyParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'EndpointAuthorizationBody',
        'data': 'object',
        'datasource_name': 'str',
        'endpoint_uuid': 'str',
        'module_id': 'str',
        'url': 'str',
        'is_inner': 'bool',
        'project_uuid': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'authorization': 'authorization',
        'data': 'data',
        'datasource_name': 'datasource_name',
        'endpoint_uuid': 'endpoint_uuid',
        'module_id': 'module_id',
        'url': 'url',
        'is_inner': 'is_inner',
        'project_uuid': 'project_uuid',
        'region_name': 'region_name'
    }

    def __init__(self, authorization=None, data=None, datasource_name=None, endpoint_uuid=None, module_id=None, url=None, is_inner=None, project_uuid=None, region_name=None):
        r"""EndpointProxyParam

        The model defined in huaweicloud sdk

        :param authorization: 
        :type authorization: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointAuthorizationBody`
        :param data: 
        :type data: object
        :param datasource_name: 数据源名称
        :type datasource_name: str
        :param endpoint_uuid: 接入点uuid
        :type endpoint_uuid: str
        :param module_id: 模块id
        :type module_id: str
        :param url: 
        :type url: str
        :param is_inner: 
        :type is_inner: bool
        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param region_name: 区域名
        :type region_name: str
        """
        
        

        self._authorization = None
        self._data = None
        self._datasource_name = None
        self._endpoint_uuid = None
        self._module_id = None
        self._url = None
        self._is_inner = None
        self._project_uuid = None
        self._region_name = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if data is not None:
            self.data = data
        if datasource_name is not None:
            self.datasource_name = datasource_name
        if endpoint_uuid is not None:
            self.endpoint_uuid = endpoint_uuid
        if module_id is not None:
            self.module_id = module_id
        if url is not None:
            self.url = url
        if is_inner is not None:
            self.is_inner = is_inner
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if region_name is not None:
            self.region_name = region_name

    @property
    def authorization(self):
        r"""Gets the authorization of this EndpointProxyParam.

        :return: The authorization of this EndpointProxyParam.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointAuthorizationBody`
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this EndpointProxyParam.

        :param authorization: The authorization of this EndpointProxyParam.
        :type authorization: :class:`huaweicloudsdkcodeartspipeline.v2.EndpointAuthorizationBody`
        """
        self._authorization = authorization

    @property
    def data(self):
        r"""Gets the data of this EndpointProxyParam.

        

        :return: The data of this EndpointProxyParam.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this EndpointProxyParam.

        

        :param data: The data of this EndpointProxyParam.
        :type data: object
        """
        self._data = data

    @property
    def datasource_name(self):
        r"""Gets the datasource_name of this EndpointProxyParam.

        数据源名称

        :return: The datasource_name of this EndpointProxyParam.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        r"""Sets the datasource_name of this EndpointProxyParam.

        数据源名称

        :param datasource_name: The datasource_name of this EndpointProxyParam.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def endpoint_uuid(self):
        r"""Gets the endpoint_uuid of this EndpointProxyParam.

        接入点uuid

        :return: The endpoint_uuid of this EndpointProxyParam.
        :rtype: str
        """
        return self._endpoint_uuid

    @endpoint_uuid.setter
    def endpoint_uuid(self, endpoint_uuid):
        r"""Sets the endpoint_uuid of this EndpointProxyParam.

        接入点uuid

        :param endpoint_uuid: The endpoint_uuid of this EndpointProxyParam.
        :type endpoint_uuid: str
        """
        self._endpoint_uuid = endpoint_uuid

    @property
    def module_id(self):
        r"""Gets the module_id of this EndpointProxyParam.

        模块id

        :return: The module_id of this EndpointProxyParam.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this EndpointProxyParam.

        模块id

        :param module_id: The module_id of this EndpointProxyParam.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def url(self):
        r"""Gets the url of this EndpointProxyParam.

        

        :return: The url of this EndpointProxyParam.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this EndpointProxyParam.

        

        :param url: The url of this EndpointProxyParam.
        :type url: str
        """
        self._url = url

    @property
    def is_inner(self):
        r"""Gets the is_inner of this EndpointProxyParam.

        

        :return: The is_inner of this EndpointProxyParam.
        :rtype: bool
        """
        return self._is_inner

    @is_inner.setter
    def is_inner(self, is_inner):
        r"""Sets the is_inner of this EndpointProxyParam.

        

        :param is_inner: The is_inner of this EndpointProxyParam.
        :type is_inner: bool
        """
        self._is_inner = is_inner

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this EndpointProxyParam.

        项目uuid

        :return: The project_uuid of this EndpointProxyParam.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this EndpointProxyParam.

        项目uuid

        :param project_uuid: The project_uuid of this EndpointProxyParam.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def region_name(self):
        r"""Gets the region_name of this EndpointProxyParam.

        区域名

        :return: The region_name of this EndpointProxyParam.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this EndpointProxyParam.

        区域名

        :param region_name: The region_name of this EndpointProxyParam.
        :type region_name: str
        """
        self._region_name = region_name

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
        if not isinstance(other, EndpointProxyParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
