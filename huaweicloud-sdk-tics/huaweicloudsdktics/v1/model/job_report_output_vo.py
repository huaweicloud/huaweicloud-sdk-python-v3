# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobReportOutputVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ext': 'str',
        'result_storage_agent_name': 'str',
        'result_storage_domain_alias': 'str'
    }

    attribute_map = {
        'ext': 'ext',
        'result_storage_agent_name': 'result_storage_agent_name',
        'result_storage_domain_alias': 'result_storage_domain_alias'
    }

    def __init__(self, ext=None, result_storage_agent_name=None, result_storage_domain_alias=None):
        """JobReportOutputVo

        The model defined in huaweicloud sdk

        :param ext: 参数等额外信息
        :type ext: str
        :param result_storage_agent_name: 结果存储agent名称
        :type result_storage_agent_name: str
        :param result_storage_domain_alias: 结果存储方别名
        :type result_storage_domain_alias: str
        """
        
        

        self._ext = None
        self._result_storage_agent_name = None
        self._result_storage_domain_alias = None
        self.discriminator = None

        if ext is not None:
            self.ext = ext
        if result_storage_agent_name is not None:
            self.result_storage_agent_name = result_storage_agent_name
        if result_storage_domain_alias is not None:
            self.result_storage_domain_alias = result_storage_domain_alias

    @property
    def ext(self):
        """Gets the ext of this JobReportOutputVo.

        参数等额外信息

        :return: The ext of this JobReportOutputVo.
        :rtype: str
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this JobReportOutputVo.

        参数等额外信息

        :param ext: The ext of this JobReportOutputVo.
        :type ext: str
        """
        self._ext = ext

    @property
    def result_storage_agent_name(self):
        """Gets the result_storage_agent_name of this JobReportOutputVo.

        结果存储agent名称

        :return: The result_storage_agent_name of this JobReportOutputVo.
        :rtype: str
        """
        return self._result_storage_agent_name

    @result_storage_agent_name.setter
    def result_storage_agent_name(self, result_storage_agent_name):
        """Sets the result_storage_agent_name of this JobReportOutputVo.

        结果存储agent名称

        :param result_storage_agent_name: The result_storage_agent_name of this JobReportOutputVo.
        :type result_storage_agent_name: str
        """
        self._result_storage_agent_name = result_storage_agent_name

    @property
    def result_storage_domain_alias(self):
        """Gets the result_storage_domain_alias of this JobReportOutputVo.

        结果存储方别名

        :return: The result_storage_domain_alias of this JobReportOutputVo.
        :rtype: str
        """
        return self._result_storage_domain_alias

    @result_storage_domain_alias.setter
    def result_storage_domain_alias(self, result_storage_domain_alias):
        """Sets the result_storage_domain_alias of this JobReportOutputVo.

        结果存储方别名

        :param result_storage_domain_alias: The result_storage_domain_alias of this JobReportOutputVo.
        :type result_storage_domain_alias: str
        """
        self._result_storage_domain_alias = result_storage_domain_alias

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
        if not isinstance(other, JobReportOutputVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
