# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaySourceConfigResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'source_endpoint_type': 'str',
        'source_db_origin': 'str',
        'traffic_source': 'str',
        'support_traffic_types': 'list[str]',
        'support_os_types': 'list[str]',
        'support_mirror_database_types': 'list[str]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'source_endpoint_type': 'source_endpoint_type',
        'source_db_origin': 'source_db_origin',
        'traffic_source': 'traffic_source',
        'support_traffic_types': 'support_traffic_types',
        'support_os_types': 'support_os_types',
        'support_mirror_database_types': 'support_mirror_database_types'
    }

    def __init__(self, engine_type=None, source_endpoint_type=None, source_db_origin=None, traffic_source=None, support_traffic_types=None, support_os_types=None, support_mirror_database_types=None):
        r"""ReplaySourceConfigResp

        The model defined in huaweicloud sdk

        :param engine_type: 流量回放源数据库引擎类型
        :type engine_type: str
        :param source_endpoint_type: 流量回放源数据库类型
        :type source_endpoint_type: str
        :param source_db_origin: 流量回放源数据库来源
        :type source_db_origin: str
        :param traffic_source: 流量回放流量文件来源
        :type traffic_source: str
        :param support_traffic_types: 流量回放流量类型
        :type support_traffic_types: list[str]
        :param support_os_types: 流量回放agent支持的操作系统
        :type support_os_types: list[str]
        :param support_mirror_database_types: 流量回放引擎支持的镜像库
        :type support_mirror_database_types: list[str]
        """
        
        

        self._engine_type = None
        self._source_endpoint_type = None
        self._source_db_origin = None
        self._traffic_source = None
        self._support_traffic_types = None
        self._support_os_types = None
        self._support_mirror_database_types = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if source_endpoint_type is not None:
            self.source_endpoint_type = source_endpoint_type
        if source_db_origin is not None:
            self.source_db_origin = source_db_origin
        if traffic_source is not None:
            self.traffic_source = traffic_source
        if support_traffic_types is not None:
            self.support_traffic_types = support_traffic_types
        if support_os_types is not None:
            self.support_os_types = support_os_types
        if support_mirror_database_types is not None:
            self.support_mirror_database_types = support_mirror_database_types

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ReplaySourceConfigResp.

        流量回放源数据库引擎类型

        :return: The engine_type of this ReplaySourceConfigResp.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ReplaySourceConfigResp.

        流量回放源数据库引擎类型

        :param engine_type: The engine_type of this ReplaySourceConfigResp.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def source_endpoint_type(self):
        r"""Gets the source_endpoint_type of this ReplaySourceConfigResp.

        流量回放源数据库类型

        :return: The source_endpoint_type of this ReplaySourceConfigResp.
        :rtype: str
        """
        return self._source_endpoint_type

    @source_endpoint_type.setter
    def source_endpoint_type(self, source_endpoint_type):
        r"""Sets the source_endpoint_type of this ReplaySourceConfigResp.

        流量回放源数据库类型

        :param source_endpoint_type: The source_endpoint_type of this ReplaySourceConfigResp.
        :type source_endpoint_type: str
        """
        self._source_endpoint_type = source_endpoint_type

    @property
    def source_db_origin(self):
        r"""Gets the source_db_origin of this ReplaySourceConfigResp.

        流量回放源数据库来源

        :return: The source_db_origin of this ReplaySourceConfigResp.
        :rtype: str
        """
        return self._source_db_origin

    @source_db_origin.setter
    def source_db_origin(self, source_db_origin):
        r"""Sets the source_db_origin of this ReplaySourceConfigResp.

        流量回放源数据库来源

        :param source_db_origin: The source_db_origin of this ReplaySourceConfigResp.
        :type source_db_origin: str
        """
        self._source_db_origin = source_db_origin

    @property
    def traffic_source(self):
        r"""Gets the traffic_source of this ReplaySourceConfigResp.

        流量回放流量文件来源

        :return: The traffic_source of this ReplaySourceConfigResp.
        :rtype: str
        """
        return self._traffic_source

    @traffic_source.setter
    def traffic_source(self, traffic_source):
        r"""Sets the traffic_source of this ReplaySourceConfigResp.

        流量回放流量文件来源

        :param traffic_source: The traffic_source of this ReplaySourceConfigResp.
        :type traffic_source: str
        """
        self._traffic_source = traffic_source

    @property
    def support_traffic_types(self):
        r"""Gets the support_traffic_types of this ReplaySourceConfigResp.

        流量回放流量类型

        :return: The support_traffic_types of this ReplaySourceConfigResp.
        :rtype: list[str]
        """
        return self._support_traffic_types

    @support_traffic_types.setter
    def support_traffic_types(self, support_traffic_types):
        r"""Sets the support_traffic_types of this ReplaySourceConfigResp.

        流量回放流量类型

        :param support_traffic_types: The support_traffic_types of this ReplaySourceConfigResp.
        :type support_traffic_types: list[str]
        """
        self._support_traffic_types = support_traffic_types

    @property
    def support_os_types(self):
        r"""Gets the support_os_types of this ReplaySourceConfigResp.

        流量回放agent支持的操作系统

        :return: The support_os_types of this ReplaySourceConfigResp.
        :rtype: list[str]
        """
        return self._support_os_types

    @support_os_types.setter
    def support_os_types(self, support_os_types):
        r"""Sets the support_os_types of this ReplaySourceConfigResp.

        流量回放agent支持的操作系统

        :param support_os_types: The support_os_types of this ReplaySourceConfigResp.
        :type support_os_types: list[str]
        """
        self._support_os_types = support_os_types

    @property
    def support_mirror_database_types(self):
        r"""Gets the support_mirror_database_types of this ReplaySourceConfigResp.

        流量回放引擎支持的镜像库

        :return: The support_mirror_database_types of this ReplaySourceConfigResp.
        :rtype: list[str]
        """
        return self._support_mirror_database_types

    @support_mirror_database_types.setter
    def support_mirror_database_types(self, support_mirror_database_types):
        r"""Sets the support_mirror_database_types of this ReplaySourceConfigResp.

        流量回放引擎支持的镜像库

        :param support_mirror_database_types: The support_mirror_database_types of this ReplaySourceConfigResp.
        :type support_mirror_database_types: list[str]
        """
        self._support_mirror_database_types = support_mirror_database_types

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
        if not isinstance(other, ReplaySourceConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
