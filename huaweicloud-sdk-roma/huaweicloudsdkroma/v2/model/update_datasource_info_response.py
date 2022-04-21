# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatasourceInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datasource_id': 'str',
        'datasource_name': 'str',
        'datasource_type': 'str',
        'vpc_id': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'instance_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'custom_plugin_id': 'str',
        'content': 'Content',
        'description': 'str',
        'app_permission': 'list[str]'
    }

    attribute_map = {
        'datasource_id': 'datasource_id',
        'datasource_name': 'datasource_name',
        'datasource_type': 'datasource_type',
        'vpc_id': 'vpc_id',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'instance_id': 'instance_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'custom_plugin_id': 'custom_plugin_id',
        'content': 'content',
        'description': 'description',
        'app_permission': 'app_permission'
    }

    def __init__(self, datasource_id=None, datasource_name=None, datasource_type=None, vpc_id=None, app_id=None, app_name=None, instance_id=None, create_time=None, update_time=None, custom_plugin_id=None, content=None, description=None, app_permission=None):
        """UpdateDatasourceInfoResponse

        The model defined in huaweicloud sdk

        :param datasource_id: 数据源ID
        :type datasource_id: str
        :param datasource_name: 数据源名称
        :type datasource_name: str
        :param datasource_type: 数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS
        :type datasource_type: str
        :param vpc_id: 数据源所属虚拟私有云VpcId
        :type vpc_id: str
        :param app_id: 数据源所属应用ID
        :type app_id: str
        :param app_name: 数据源所属应用名称
        :type app_name: str
        :param instance_id: 数据源所属实例Id
        :type instance_id: str
        :param create_time: 数据源创建时间
        :type create_time: int
        :param update_time: 数据源修改时间
        :type update_time: int
        :param custom_plugin_id: 数据源所属连接器Id
        :type custom_plugin_id: str
        :param content: 
        :type content: :class:`huaweicloudsdkroma.v2.Content`
        :param description: 数据源描述
        :type description: str
        :param app_permission: 集成应用权限信息 - read (读权限) - access (调用权限) - delete (删除权限) - modify (修改权限)
        :type app_permission: list[str]
        """
        
        super(UpdateDatasourceInfoResponse, self).__init__()

        self._datasource_id = None
        self._datasource_name = None
        self._datasource_type = None
        self._vpc_id = None
        self._app_id = None
        self._app_name = None
        self._instance_id = None
        self._create_time = None
        self._update_time = None
        self._custom_plugin_id = None
        self._content = None
        self._description = None
        self._app_permission = None
        self.discriminator = None

        if datasource_id is not None:
            self.datasource_id = datasource_id
        if datasource_name is not None:
            self.datasource_name = datasource_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if instance_id is not None:
            self.instance_id = instance_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if custom_plugin_id is not None:
            self.custom_plugin_id = custom_plugin_id
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if app_permission is not None:
            self.app_permission = app_permission

    @property
    def datasource_id(self):
        """Gets the datasource_id of this UpdateDatasourceInfoResponse.

        数据源ID

        :return: The datasource_id of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """Sets the datasource_id of this UpdateDatasourceInfoResponse.

        数据源ID

        :param datasource_id: The datasource_id of this UpdateDatasourceInfoResponse.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def datasource_name(self):
        """Gets the datasource_name of this UpdateDatasourceInfoResponse.

        数据源名称

        :return: The datasource_name of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """Sets the datasource_name of this UpdateDatasourceInfoResponse.

        数据源名称

        :param datasource_name: The datasource_name of this UpdateDatasourceInfoResponse.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def datasource_type(self):
        """Gets the datasource_type of this UpdateDatasourceInfoResponse.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :return: The datasource_type of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this UpdateDatasourceInfoResponse.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :param datasource_type: The datasource_type of this UpdateDatasourceInfoResponse.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdateDatasourceInfoResponse.

        数据源所属虚拟私有云VpcId

        :return: The vpc_id of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdateDatasourceInfoResponse.

        数据源所属虚拟私有云VpcId

        :param vpc_id: The vpc_id of this UpdateDatasourceInfoResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def app_id(self):
        """Gets the app_id of this UpdateDatasourceInfoResponse.

        数据源所属应用ID

        :return: The app_id of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UpdateDatasourceInfoResponse.

        数据源所属应用ID

        :param app_id: The app_id of this UpdateDatasourceInfoResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this UpdateDatasourceInfoResponse.

        数据源所属应用名称

        :return: The app_name of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UpdateDatasourceInfoResponse.

        数据源所属应用名称

        :param app_name: The app_name of this UpdateDatasourceInfoResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDatasourceInfoResponse.

        数据源所属实例Id

        :return: The instance_id of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDatasourceInfoResponse.

        数据源所属实例Id

        :param instance_id: The instance_id of this UpdateDatasourceInfoResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def create_time(self):
        """Gets the create_time of this UpdateDatasourceInfoResponse.

        数据源创建时间

        :return: The create_time of this UpdateDatasourceInfoResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateDatasourceInfoResponse.

        数据源创建时间

        :param create_time: The create_time of this UpdateDatasourceInfoResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateDatasourceInfoResponse.

        数据源修改时间

        :return: The update_time of this UpdateDatasourceInfoResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateDatasourceInfoResponse.

        数据源修改时间

        :param update_time: The update_time of this UpdateDatasourceInfoResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def custom_plugin_id(self):
        """Gets the custom_plugin_id of this UpdateDatasourceInfoResponse.

        数据源所属连接器Id

        :return: The custom_plugin_id of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._custom_plugin_id

    @custom_plugin_id.setter
    def custom_plugin_id(self, custom_plugin_id):
        """Sets the custom_plugin_id of this UpdateDatasourceInfoResponse.

        数据源所属连接器Id

        :param custom_plugin_id: The custom_plugin_id of this UpdateDatasourceInfoResponse.
        :type custom_plugin_id: str
        """
        self._custom_plugin_id = custom_plugin_id

    @property
    def content(self):
        """Gets the content of this UpdateDatasourceInfoResponse.


        :return: The content of this UpdateDatasourceInfoResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.Content`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateDatasourceInfoResponse.


        :param content: The content of this UpdateDatasourceInfoResponse.
        :type content: :class:`huaweicloudsdkroma.v2.Content`
        """
        self._content = content

    @property
    def description(self):
        """Gets the description of this UpdateDatasourceInfoResponse.

        数据源描述

        :return: The description of this UpdateDatasourceInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDatasourceInfoResponse.

        数据源描述

        :param description: The description of this UpdateDatasourceInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def app_permission(self):
        """Gets the app_permission of this UpdateDatasourceInfoResponse.

        集成应用权限信息 - read (读权限) - access (调用权限) - delete (删除权限) - modify (修改权限)

        :return: The app_permission of this UpdateDatasourceInfoResponse.
        :rtype: list[str]
        """
        return self._app_permission

    @app_permission.setter
    def app_permission(self, app_permission):
        """Sets the app_permission of this UpdateDatasourceInfoResponse.

        集成应用权限信息 - read (读权限) - access (调用权限) - delete (删除权限) - modify (修改权限)

        :param app_permission: The app_permission of this UpdateDatasourceInfoResponse.
        :type app_permission: list[str]
        """
        self._app_permission = app_permission

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
        if not isinstance(other, UpdateDatasourceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
