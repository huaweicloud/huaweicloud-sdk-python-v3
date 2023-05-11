# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryApplicationBriefResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'last_published_version': 'str',
        'app_type': 'str',
        'function_type': 'str',
        'deploy_type': 'str',
        'protocol': 'str',
        'edge_app_name': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'last_published_version': 'last_published_version',
        'app_type': 'app_type',
        'function_type': 'function_type',
        'deploy_type': 'deploy_type',
        'protocol': 'protocol',
        'edge_app_name': 'edge_app_name'
    }

    def __init__(self, edge_app_id=None, description=None, create_time=None, update_time=None, last_published_version=None, app_type=None, function_type=None, deploy_type=None, protocol=None, edge_app_name=None):
        """QueryApplicationBriefResponseDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用id
        :type edge_app_id: str
        :param description: 应用描述
        :type description: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param last_published_version: 最新发布版本
        :type last_published_version: str
        :param app_type: 应用类型SYSTEM_REQUIRED|SYSTEM_OPTIONAL|USER
        :type app_type: str
        :param function_type: 应用类型DATA_PROCESSING|PROTOCOL_PARSING
        :type function_type: str
        :param deploy_type: 部署类型docker|process
        :type deploy_type: str
        :param protocol: 驱动协议类型OPCUA|Modbus-TCP
        :type protocol: str
        :param edge_app_name: 应用名称
        :type edge_app_name: str
        """
        
        

        self._edge_app_id = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._last_published_version = None
        self._app_type = None
        self._function_type = None
        self._deploy_type = None
        self._protocol = None
        self._edge_app_name = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if last_published_version is not None:
            self.last_published_version = last_published_version
        if app_type is not None:
            self.app_type = app_type
        if function_type is not None:
            self.function_type = function_type
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if protocol is not None:
            self.protocol = protocol
        if edge_app_name is not None:
            self.edge_app_name = edge_app_name

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this QueryApplicationBriefResponseDTO.

        应用id

        :return: The edge_app_id of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this QueryApplicationBriefResponseDTO.

        应用id

        :param edge_app_id: The edge_app_id of this QueryApplicationBriefResponseDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def description(self):
        """Gets the description of this QueryApplicationBriefResponseDTO.

        应用描述

        :return: The description of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryApplicationBriefResponseDTO.

        应用描述

        :param description: The description of this QueryApplicationBriefResponseDTO.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this QueryApplicationBriefResponseDTO.

        创建时间

        :return: The create_time of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryApplicationBriefResponseDTO.

        创建时间

        :param create_time: The create_time of this QueryApplicationBriefResponseDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryApplicationBriefResponseDTO.

        最后一次修改时间

        :return: The update_time of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryApplicationBriefResponseDTO.

        最后一次修改时间

        :param update_time: The update_time of this QueryApplicationBriefResponseDTO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def last_published_version(self):
        """Gets the last_published_version of this QueryApplicationBriefResponseDTO.

        最新发布版本

        :return: The last_published_version of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._last_published_version

    @last_published_version.setter
    def last_published_version(self, last_published_version):
        """Sets the last_published_version of this QueryApplicationBriefResponseDTO.

        最新发布版本

        :param last_published_version: The last_published_version of this QueryApplicationBriefResponseDTO.
        :type last_published_version: str
        """
        self._last_published_version = last_published_version

    @property
    def app_type(self):
        """Gets the app_type of this QueryApplicationBriefResponseDTO.

        应用类型SYSTEM_REQUIRED|SYSTEM_OPTIONAL|USER

        :return: The app_type of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this QueryApplicationBriefResponseDTO.

        应用类型SYSTEM_REQUIRED|SYSTEM_OPTIONAL|USER

        :param app_type: The app_type of this QueryApplicationBriefResponseDTO.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def function_type(self):
        """Gets the function_type of this QueryApplicationBriefResponseDTO.

        应用类型DATA_PROCESSING|PROTOCOL_PARSING

        :return: The function_type of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this QueryApplicationBriefResponseDTO.

        应用类型DATA_PROCESSING|PROTOCOL_PARSING

        :param function_type: The function_type of this QueryApplicationBriefResponseDTO.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def deploy_type(self):
        """Gets the deploy_type of this QueryApplicationBriefResponseDTO.

        部署类型docker|process

        :return: The deploy_type of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this QueryApplicationBriefResponseDTO.

        部署类型docker|process

        :param deploy_type: The deploy_type of this QueryApplicationBriefResponseDTO.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def protocol(self):
        """Gets the protocol of this QueryApplicationBriefResponseDTO.

        驱动协议类型OPCUA|Modbus-TCP

        :return: The protocol of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this QueryApplicationBriefResponseDTO.

        驱动协议类型OPCUA|Modbus-TCP

        :param protocol: The protocol of this QueryApplicationBriefResponseDTO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def edge_app_name(self):
        """Gets the edge_app_name of this QueryApplicationBriefResponseDTO.

        应用名称

        :return: The edge_app_name of this QueryApplicationBriefResponseDTO.
        :rtype: str
        """
        return self._edge_app_name

    @edge_app_name.setter
    def edge_app_name(self, edge_app_name):
        """Sets the edge_app_name of this QueryApplicationBriefResponseDTO.

        应用名称

        :param edge_app_name: The edge_app_name of this QueryApplicationBriefResponseDTO.
        :type edge_app_name: str
        """
        self._edge_app_name = edge_app_name

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
        if not isinstance(other, QueryApplicationBriefResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
