# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDcDsReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ds_id': 'str',
        'config': 'object',
        'name': 'str',
        'module_id': 'str',
        'tpl_id': 'str',
        'quality_report': 'bool'
    }

    attribute_map = {
        'ds_id': 'ds_id',
        'config': 'config',
        'name': 'name',
        'module_id': 'module_id',
        'tpl_id': 'tpl_id',
        'quality_report': 'quality_report'
    }

    def __init__(self, ds_id=None, config=None, name=None, module_id=None, tpl_id=None, quality_report=None):
        r"""CreateDcDsReqDTO

        The model defined in huaweicloud sdk

        :param ds_id: 采集数据源id，节点下唯一
        :type ds_id: str
        :param config: 数据源的连接及采集信息
        :type config: object
        :param name: 采集数据源名称，允许中、数字、英文大小写、下划线、中划线
        :type name: str
        :param module_id: 模块id
        :type module_id: str
        :param tpl_id: 模板id，节点下唯一
        :type tpl_id: str
        :param quality_report: 质量上报开关，不携带或值不为true，默认为false
        :type quality_report: bool
        """
        
        

        self._ds_id = None
        self._config = None
        self._name = None
        self._module_id = None
        self._tpl_id = None
        self._quality_report = None
        self.discriminator = None

        self.ds_id = ds_id
        self.config = config
        self.name = name
        self.module_id = module_id
        self.tpl_id = tpl_id
        if quality_report is not None:
            self.quality_report = quality_report

    @property
    def ds_id(self):
        r"""Gets the ds_id of this CreateDcDsReqDTO.

        采集数据源id，节点下唯一

        :return: The ds_id of this CreateDcDsReqDTO.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        r"""Sets the ds_id of this CreateDcDsReqDTO.

        采集数据源id，节点下唯一

        :param ds_id: The ds_id of this CreateDcDsReqDTO.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def config(self):
        r"""Gets the config of this CreateDcDsReqDTO.

        数据源的连接及采集信息

        :return: The config of this CreateDcDsReqDTO.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this CreateDcDsReqDTO.

        数据源的连接及采集信息

        :param config: The config of this CreateDcDsReqDTO.
        :type config: object
        """
        self._config = config

    @property
    def name(self):
        r"""Gets the name of this CreateDcDsReqDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :return: The name of this CreateDcDsReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDcDsReqDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :param name: The name of this CreateDcDsReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def module_id(self):
        r"""Gets the module_id of this CreateDcDsReqDTO.

        模块id

        :return: The module_id of this CreateDcDsReqDTO.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this CreateDcDsReqDTO.

        模块id

        :param module_id: The module_id of this CreateDcDsReqDTO.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this CreateDcDsReqDTO.

        模板id，节点下唯一

        :return: The tpl_id of this CreateDcDsReqDTO.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this CreateDcDsReqDTO.

        模板id，节点下唯一

        :param tpl_id: The tpl_id of this CreateDcDsReqDTO.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def quality_report(self):
        r"""Gets the quality_report of this CreateDcDsReqDTO.

        质量上报开关，不携带或值不为true，默认为false

        :return: The quality_report of this CreateDcDsReqDTO.
        :rtype: bool
        """
        return self._quality_report

    @quality_report.setter
    def quality_report(self, quality_report):
        r"""Sets the quality_report of this CreateDcDsReqDTO.

        质量上报开关，不携带或值不为true，默认为false

        :param quality_report: The quality_report of this CreateDcDsReqDTO.
        :type quality_report: bool
        """
        self._quality_report = quality_report

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
        if not isinstance(other, CreateDcDsReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
