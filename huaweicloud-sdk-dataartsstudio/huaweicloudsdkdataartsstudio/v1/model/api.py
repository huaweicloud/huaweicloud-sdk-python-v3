# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Api:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_id': 'str',
        'name': 'str',
        'description': 'str',
        'log_flag': 'bool',
        'api_type': 'str',
        'auth_type': 'str',
        'publish_type': 'str',
        'manager': 'str',
        'path': 'str',
        'protocol': 'str',
        'request_type': 'str',
        'tags': 'list[str]',
        'visibility': 'str',
        'request_paras': 'list[RequestPara]',
        'datasource_config': 'DatasourceConfig',
        'backend_config': 'BackendConfig'
    }

    attribute_map = {
        'catalog_id': 'catalog_id',
        'name': 'name',
        'description': 'description',
        'log_flag': 'log_flag',
        'api_type': 'api_type',
        'auth_type': 'auth_type',
        'publish_type': 'publish_type',
        'manager': 'manager',
        'path': 'path',
        'protocol': 'protocol',
        'request_type': 'request_type',
        'tags': 'tags',
        'visibility': 'visibility',
        'request_paras': 'request_paras',
        'datasource_config': 'datasource_config',
        'backend_config': 'backend_config'
    }

    def __init__(self, catalog_id=None, name=None, description=None, log_flag=None, api_type=None, auth_type=None, publish_type=None, manager=None, path=None, protocol=None, request_type=None, tags=None, visibility=None, request_paras=None, datasource_config=None, backend_config=None):
        """Api

        The model defined in huaweicloud sdk

        :param catalog_id: 目录ID
        :type catalog_id: str
        :param name: api 名称
        :type name: str
        :param description: api 描述
        :type description: str
        :param log_flag: 是否启用访问日志
        :type log_flag: bool
        :param api_type: Api类型
        :type api_type: str
        :param auth_type: 
        :type auth_type: str
        :param publish_type: 发布类型
        :type publish_type: str
        :param manager: api 审核人
        :type manager: str
        :param path: api路径
        :type path: str
        :param protocol: api 协议
        :type protocol: str
        :param request_type: 请求类型
        :type request_type: str
        :param tags: 标签
        :type tags: list[str]
        :param visibility: 可见性
        :type visibility: str
        :param request_paras: API请求参数列表
        :type request_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        :param datasource_config: 
        :type datasource_config: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        :param backend_config: 
        :type backend_config: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        
        

        self._catalog_id = None
        self._name = None
        self._description = None
        self._log_flag = None
        self._api_type = None
        self._auth_type = None
        self._publish_type = None
        self._manager = None
        self._path = None
        self._protocol = None
        self._request_type = None
        self._tags = None
        self._visibility = None
        self._request_paras = None
        self._datasource_config = None
        self._backend_config = None
        self.discriminator = None

        if catalog_id is not None:
            self.catalog_id = catalog_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if log_flag is not None:
            self.log_flag = log_flag
        if api_type is not None:
            self.api_type = api_type
        if auth_type is not None:
            self.auth_type = auth_type
        if publish_type is not None:
            self.publish_type = publish_type
        if manager is not None:
            self.manager = manager
        if path is not None:
            self.path = path
        if protocol is not None:
            self.protocol = protocol
        if request_type is not None:
            self.request_type = request_type
        if tags is not None:
            self.tags = tags
        if visibility is not None:
            self.visibility = visibility
        if request_paras is not None:
            self.request_paras = request_paras
        if datasource_config is not None:
            self.datasource_config = datasource_config
        if backend_config is not None:
            self.backend_config = backend_config

    @property
    def catalog_id(self):
        """Gets the catalog_id of this Api.

        目录ID

        :return: The catalog_id of this Api.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this Api.

        目录ID

        :param catalog_id: The catalog_id of this Api.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def name(self):
        """Gets the name of this Api.

        api 名称

        :return: The name of this Api.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Api.

        api 名称

        :param name: The name of this Api.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Api.

        api 描述

        :return: The description of this Api.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Api.

        api 描述

        :param description: The description of this Api.
        :type description: str
        """
        self._description = description

    @property
    def log_flag(self):
        """Gets the log_flag of this Api.

        是否启用访问日志

        :return: The log_flag of this Api.
        :rtype: bool
        """
        return self._log_flag

    @log_flag.setter
    def log_flag(self, log_flag):
        """Sets the log_flag of this Api.

        是否启用访问日志

        :param log_flag: The log_flag of this Api.
        :type log_flag: bool
        """
        self._log_flag = log_flag

    @property
    def api_type(self):
        """Gets the api_type of this Api.

        Api类型

        :return: The api_type of this Api.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this Api.

        Api类型

        :param api_type: The api_type of this Api.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def auth_type(self):
        """Gets the auth_type of this Api.

        :return: The auth_type of this Api.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this Api.

        :param auth_type: The auth_type of this Api.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def publish_type(self):
        """Gets the publish_type of this Api.

        发布类型

        :return: The publish_type of this Api.
        :rtype: str
        """
        return self._publish_type

    @publish_type.setter
    def publish_type(self, publish_type):
        """Sets the publish_type of this Api.

        发布类型

        :param publish_type: The publish_type of this Api.
        :type publish_type: str
        """
        self._publish_type = publish_type

    @property
    def manager(self):
        """Gets the manager of this Api.

        api 审核人

        :return: The manager of this Api.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this Api.

        api 审核人

        :param manager: The manager of this Api.
        :type manager: str
        """
        self._manager = manager

    @property
    def path(self):
        """Gets the path of this Api.

        api路径

        :return: The path of this Api.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Api.

        api路径

        :param path: The path of this Api.
        :type path: str
        """
        self._path = path

    @property
    def protocol(self):
        """Gets the protocol of this Api.

        api 协议

        :return: The protocol of this Api.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Api.

        api 协议

        :param protocol: The protocol of this Api.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def request_type(self):
        """Gets the request_type of this Api.

        请求类型

        :return: The request_type of this Api.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this Api.

        请求类型

        :param request_type: The request_type of this Api.
        :type request_type: str
        """
        self._request_type = request_type

    @property
    def tags(self):
        """Gets the tags of this Api.

        标签

        :return: The tags of this Api.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Api.

        标签

        :param tags: The tags of this Api.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def visibility(self):
        """Gets the visibility of this Api.

        可见性

        :return: The visibility of this Api.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Api.

        可见性

        :param visibility: The visibility of this Api.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def request_paras(self):
        """Gets the request_paras of this Api.

        API请求参数列表

        :return: The request_paras of this Api.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        """
        return self._request_paras

    @request_paras.setter
    def request_paras(self, request_paras):
        """Sets the request_paras of this Api.

        API请求参数列表

        :param request_paras: The request_paras of this Api.
        :type request_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        """
        self._request_paras = request_paras

    @property
    def datasource_config(self):
        """Gets the datasource_config of this Api.

        :return: The datasource_config of this Api.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        """
        return self._datasource_config

    @datasource_config.setter
    def datasource_config(self, datasource_config):
        """Sets the datasource_config of this Api.

        :param datasource_config: The datasource_config of this Api.
        :type datasource_config: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        """
        self._datasource_config = datasource_config

    @property
    def backend_config(self):
        """Gets the backend_config of this Api.

        :return: The backend_config of this Api.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        return self._backend_config

    @backend_config.setter
    def backend_config(self, backend_config):
        """Sets the backend_config of this Api.

        :param backend_config: The backend_config of this Api.
        :type backend_config: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        self._backend_config = backend_config

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
        if not isinstance(other, Api):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
