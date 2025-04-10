# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_name': 'str',
        'datasource_type': 'str',
        'app_id': 'str',
        'content': 'Content',
        'description': 'str'
    }

    attribute_map = {
        'datasource_name': 'datasource_name',
        'datasource_type': 'datasource_type',
        'app_id': 'app_id',
        'content': 'content',
        'description': 'description'
    }

    def __init__(self, datasource_name=None, datasource_type=None, app_id=None, content=None, description=None):
        r"""DatasourceInfo

        The model defined in huaweicloud sdk

        :param datasource_name: 数据源名称，数据源名称不能包含&amp;、&lt;、&gt;、\&quot;、&#39;、(、) ，长度为1~255字符
        :type datasource_name: str
        :param datasource_type: 数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS
        :type datasource_type: str
        :param app_id: 数据源所属应用ID
        :type app_id: str
        :param content: 
        :type content: :class:`huaweicloudsdkroma.v2.Content`
        :param description: 数据源描述
        :type description: str
        """
        
        

        self._datasource_name = None
        self._datasource_type = None
        self._app_id = None
        self._content = None
        self._description = None
        self.discriminator = None

        self.datasource_name = datasource_name
        self.datasource_type = datasource_type
        self.app_id = app_id
        self.content = content
        if description is not None:
            self.description = description

    @property
    def datasource_name(self):
        r"""Gets the datasource_name of this DatasourceInfo.

        数据源名称，数据源名称不能包含&、<、>、\"、'、(、) ，长度为1~255字符

        :return: The datasource_name of this DatasourceInfo.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        r"""Sets the datasource_name of this DatasourceInfo.

        数据源名称，数据源名称不能包含&、<、>、\"、'、(、) ，长度为1~255字符

        :param datasource_name: The datasource_name of this DatasourceInfo.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this DatasourceInfo.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :return: The datasource_type of this DatasourceInfo.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this DatasourceInfo.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :param datasource_type: The datasource_type of this DatasourceInfo.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def app_id(self):
        r"""Gets the app_id of this DatasourceInfo.

        数据源所属应用ID

        :return: The app_id of this DatasourceInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DatasourceInfo.

        数据源所属应用ID

        :param app_id: The app_id of this DatasourceInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def content(self):
        r"""Gets the content of this DatasourceInfo.

        :return: The content of this DatasourceInfo.
        :rtype: :class:`huaweicloudsdkroma.v2.Content`
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this DatasourceInfo.

        :param content: The content of this DatasourceInfo.
        :type content: :class:`huaweicloudsdkroma.v2.Content`
        """
        self._content = content

    @property
    def description(self):
        r"""Gets the description of this DatasourceInfo.

        数据源描述

        :return: The description of this DatasourceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DatasourceInfo.

        数据源描述

        :param description: The description of this DatasourceInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, DatasourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
