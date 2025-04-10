# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDcDsReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'object',
        'name': 'str',
        'quality_report': 'bool'
    }

    attribute_map = {
        'config': 'config',
        'name': 'name',
        'quality_report': 'quality_report'
    }

    def __init__(self, config=None, name=None, quality_report=None):
        r"""UpdateDcDsReqDTO

        The model defined in huaweicloud sdk

        :param config: 数据源的连接及采集信息
        :type config: object
        :param name: 采集数据源名称，允许中、数字、英文大小写、下划线、中划线
        :type name: str
        :param quality_report: 质量上报开关，不携带或值不为true，默认为false
        :type quality_report: bool
        """
        
        

        self._config = None
        self._name = None
        self._quality_report = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if name is not None:
            self.name = name
        if quality_report is not None:
            self.quality_report = quality_report

    @property
    def config(self):
        r"""Gets the config of this UpdateDcDsReqDTO.

        数据源的连接及采集信息

        :return: The config of this UpdateDcDsReqDTO.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this UpdateDcDsReqDTO.

        数据源的连接及采集信息

        :param config: The config of this UpdateDcDsReqDTO.
        :type config: object
        """
        self._config = config

    @property
    def name(self):
        r"""Gets the name of this UpdateDcDsReqDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :return: The name of this UpdateDcDsReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateDcDsReqDTO.

        采集数据源名称，允许中、数字、英文大小写、下划线、中划线

        :param name: The name of this UpdateDcDsReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def quality_report(self):
        r"""Gets the quality_report of this UpdateDcDsReqDTO.

        质量上报开关，不携带或值不为true，默认为false

        :return: The quality_report of this UpdateDcDsReqDTO.
        :rtype: bool
        """
        return self._quality_report

    @quality_report.setter
    def quality_report(self, quality_report):
        r"""Sets the quality_report of this UpdateDcDsReqDTO.

        质量上报开关，不携带或值不为true，默认为false

        :param quality_report: The quality_report of this UpdateDcDsReqDTO.
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
        if not isinstance(other, UpdateDcDsReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
