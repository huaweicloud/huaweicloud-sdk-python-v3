# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateXdmApplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name_cn': 'str',
        'app_name_en': 'str',
        'app_desc': 'str',
        'app_desc_en': 'str',
        'operate_type': 'str',
        'app_env': 'str',
        'database_type': 'str',
        'app_user_list': 'list[AppUserList]',
        'certified_data_source_name': 'str',
        'certified_data_source_number': 'str',
        'integration_mode': 'str',
        'metadata_synchronization': 'bool'
    }

    attribute_map = {
        'app_name_cn': 'app_name_cn',
        'app_name_en': 'app_name_en',
        'app_desc': 'app_desc',
        'app_desc_en': 'app_desc_en',
        'operate_type': 'operate_type',
        'app_env': 'app_env',
        'database_type': 'database_type',
        'app_user_list': 'app_user_list',
        'certified_data_source_name': 'certified_data_source_name',
        'certified_data_source_number': 'certified_data_source_number',
        'integration_mode': 'integration_mode',
        'metadata_synchronization': 'metadata_synchronization'
    }

    def __init__(self, app_name_cn=None, app_name_en=None, app_desc=None, app_desc_en=None, operate_type=None, app_env=None, database_type=None, app_user_list=None, certified_data_source_name=None, certified_data_source_number=None, integration_mode=None, metadata_synchronization=None):
        """CreateXdmApplicationRequestBody

        The model defined in huaweicloud sdk

        :param app_name_cn: 应用的中文名称。
        :type app_name_cn: str
        :param app_name_en: 应用的英文名称。
        :type app_name_en: str
        :param app_desc: 应用的中文描述。
        :type app_desc: str
        :param app_desc_en: 应用的英文描述。
        :type app_desc_en: str
        :param operate_type: 操作类型。
        :type operate_type: str
        :param app_env: 环境标识。 - dev：用于开发环境。 - sit：用于功能测试环境。 - uat：用于用户测试环境。 - train：用于培训环境。 - beta：用于灰度部署环境。 - production：用于生产环境。
        :type app_env: str
        :param database_type: 数据库类型，支持MySQL和PostgreSQL。
        :type database_type: str
        :param app_user_list: 应用责任人。
        :type app_user_list: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        :param certified_data_source_name: 认证数据源中文名称。
        :type certified_data_source_name: str
        :param certified_data_source_number: 认证数据源编码。
        :type certified_data_source_number: str
        :param integration_mode: 集成模式。 - API - SDK
        :type integration_mode: str
        :param metadata_synchronization: 元模型同步。
        :type metadata_synchronization: bool
        """
        
        

        self._app_name_cn = None
        self._app_name_en = None
        self._app_desc = None
        self._app_desc_en = None
        self._operate_type = None
        self._app_env = None
        self._database_type = None
        self._app_user_list = None
        self._certified_data_source_name = None
        self._certified_data_source_number = None
        self._integration_mode = None
        self._metadata_synchronization = None
        self.discriminator = None

        self.app_name_cn = app_name_cn
        self.app_name_en = app_name_en
        if app_desc is not None:
            self.app_desc = app_desc
        if app_desc_en is not None:
            self.app_desc_en = app_desc_en
        if operate_type is not None:
            self.operate_type = operate_type
        self.app_env = app_env
        self.database_type = database_type
        self.app_user_list = app_user_list
        if certified_data_source_name is not None:
            self.certified_data_source_name = certified_data_source_name
        if certified_data_source_number is not None:
            self.certified_data_source_number = certified_data_source_number
        self.integration_mode = integration_mode
        if metadata_synchronization is not None:
            self.metadata_synchronization = metadata_synchronization

    @property
    def app_name_cn(self):
        """Gets the app_name_cn of this CreateXdmApplicationRequestBody.

        应用的中文名称。

        :return: The app_name_cn of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._app_name_cn

    @app_name_cn.setter
    def app_name_cn(self, app_name_cn):
        """Sets the app_name_cn of this CreateXdmApplicationRequestBody.

        应用的中文名称。

        :param app_name_cn: The app_name_cn of this CreateXdmApplicationRequestBody.
        :type app_name_cn: str
        """
        self._app_name_cn = app_name_cn

    @property
    def app_name_en(self):
        """Gets the app_name_en of this CreateXdmApplicationRequestBody.

        应用的英文名称。

        :return: The app_name_en of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._app_name_en

    @app_name_en.setter
    def app_name_en(self, app_name_en):
        """Sets the app_name_en of this CreateXdmApplicationRequestBody.

        应用的英文名称。

        :param app_name_en: The app_name_en of this CreateXdmApplicationRequestBody.
        :type app_name_en: str
        """
        self._app_name_en = app_name_en

    @property
    def app_desc(self):
        """Gets the app_desc of this CreateXdmApplicationRequestBody.

        应用的中文描述。

        :return: The app_desc of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._app_desc

    @app_desc.setter
    def app_desc(self, app_desc):
        """Sets the app_desc of this CreateXdmApplicationRequestBody.

        应用的中文描述。

        :param app_desc: The app_desc of this CreateXdmApplicationRequestBody.
        :type app_desc: str
        """
        self._app_desc = app_desc

    @property
    def app_desc_en(self):
        """Gets the app_desc_en of this CreateXdmApplicationRequestBody.

        应用的英文描述。

        :return: The app_desc_en of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._app_desc_en

    @app_desc_en.setter
    def app_desc_en(self, app_desc_en):
        """Sets the app_desc_en of this CreateXdmApplicationRequestBody.

        应用的英文描述。

        :param app_desc_en: The app_desc_en of this CreateXdmApplicationRequestBody.
        :type app_desc_en: str
        """
        self._app_desc_en = app_desc_en

    @property
    def operate_type(self):
        """Gets the operate_type of this CreateXdmApplicationRequestBody.

        操作类型。

        :return: The operate_type of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this CreateXdmApplicationRequestBody.

        操作类型。

        :param operate_type: The operate_type of this CreateXdmApplicationRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def app_env(self):
        """Gets the app_env of this CreateXdmApplicationRequestBody.

        环境标识。 - dev：用于开发环境。 - sit：用于功能测试环境。 - uat：用于用户测试环境。 - train：用于培训环境。 - beta：用于灰度部署环境。 - production：用于生产环境。

        :return: The app_env of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._app_env

    @app_env.setter
    def app_env(self, app_env):
        """Sets the app_env of this CreateXdmApplicationRequestBody.

        环境标识。 - dev：用于开发环境。 - sit：用于功能测试环境。 - uat：用于用户测试环境。 - train：用于培训环境。 - beta：用于灰度部署环境。 - production：用于生产环境。

        :param app_env: The app_env of this CreateXdmApplicationRequestBody.
        :type app_env: str
        """
        self._app_env = app_env

    @property
    def database_type(self):
        """Gets the database_type of this CreateXdmApplicationRequestBody.

        数据库类型，支持MySQL和PostgreSQL。

        :return: The database_type of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """Sets the database_type of this CreateXdmApplicationRequestBody.

        数据库类型，支持MySQL和PostgreSQL。

        :param database_type: The database_type of this CreateXdmApplicationRequestBody.
        :type database_type: str
        """
        self._database_type = database_type

    @property
    def app_user_list(self):
        """Gets the app_user_list of this CreateXdmApplicationRequestBody.

        应用责任人。

        :return: The app_user_list of this CreateXdmApplicationRequestBody.
        :rtype: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        return self._app_user_list

    @app_user_list.setter
    def app_user_list(self, app_user_list):
        """Sets the app_user_list of this CreateXdmApplicationRequestBody.

        应用责任人。

        :param app_user_list: The app_user_list of this CreateXdmApplicationRequestBody.
        :type app_user_list: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        self._app_user_list = app_user_list

    @property
    def certified_data_source_name(self):
        """Gets the certified_data_source_name of this CreateXdmApplicationRequestBody.

        认证数据源中文名称。

        :return: The certified_data_source_name of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._certified_data_source_name

    @certified_data_source_name.setter
    def certified_data_source_name(self, certified_data_source_name):
        """Sets the certified_data_source_name of this CreateXdmApplicationRequestBody.

        认证数据源中文名称。

        :param certified_data_source_name: The certified_data_source_name of this CreateXdmApplicationRequestBody.
        :type certified_data_source_name: str
        """
        self._certified_data_source_name = certified_data_source_name

    @property
    def certified_data_source_number(self):
        """Gets the certified_data_source_number of this CreateXdmApplicationRequestBody.

        认证数据源编码。

        :return: The certified_data_source_number of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._certified_data_source_number

    @certified_data_source_number.setter
    def certified_data_source_number(self, certified_data_source_number):
        """Sets the certified_data_source_number of this CreateXdmApplicationRequestBody.

        认证数据源编码。

        :param certified_data_source_number: The certified_data_source_number of this CreateXdmApplicationRequestBody.
        :type certified_data_source_number: str
        """
        self._certified_data_source_number = certified_data_source_number

    @property
    def integration_mode(self):
        """Gets the integration_mode of this CreateXdmApplicationRequestBody.

        集成模式。 - API - SDK

        :return: The integration_mode of this CreateXdmApplicationRequestBody.
        :rtype: str
        """
        return self._integration_mode

    @integration_mode.setter
    def integration_mode(self, integration_mode):
        """Sets the integration_mode of this CreateXdmApplicationRequestBody.

        集成模式。 - API - SDK

        :param integration_mode: The integration_mode of this CreateXdmApplicationRequestBody.
        :type integration_mode: str
        """
        self._integration_mode = integration_mode

    @property
    def metadata_synchronization(self):
        """Gets the metadata_synchronization of this CreateXdmApplicationRequestBody.

        元模型同步。

        :return: The metadata_synchronization of this CreateXdmApplicationRequestBody.
        :rtype: bool
        """
        return self._metadata_synchronization

    @metadata_synchronization.setter
    def metadata_synchronization(self, metadata_synchronization):
        """Sets the metadata_synchronization of this CreateXdmApplicationRequestBody.

        元模型同步。

        :param metadata_synchronization: The metadata_synchronization of this CreateXdmApplicationRequestBody.
        :type metadata_synchronization: bool
        """
        self._metadata_synchronization = metadata_synchronization

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
        if not isinstance(other, CreateXdmApplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
