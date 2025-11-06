# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, template_id=None, template_name=None, template_type=None):
        r"""StructConfig

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。
        :type log_group_id: str
        :param log_stream_id: 日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。
        :type log_stream_id: str
        :param template_id: 所用模板id。当使用系统模板时，当前属性可以为空
        :type template_id: str
        :param template_name: 所用模板名称，会对模板名称及id进行校验
        :type template_name: str
        :param template_type: 所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。
        :type template_type: str
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._template_id = None
        self._template_name = None
        self._template_type = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this StructConfig.

        日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The log_group_id of this StructConfig.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this StructConfig.

        日志组ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param log_group_id: The log_group_id of this StructConfig.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this StructConfig.

        日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The log_stream_id of this StructConfig.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this StructConfig.

        日志流ID，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param log_stream_id: The log_stream_id of this StructConfig.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def template_id(self):
        r"""Gets the template_id of this StructConfig.

        所用模板id。当使用系统模板时，当前属性可以为空

        :return: The template_id of this StructConfig.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this StructConfig.

        所用模板id。当使用系统模板时，当前属性可以为空

        :param template_id: The template_id of this StructConfig.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this StructConfig.

        所用模板名称，会对模板名称及id进行校验

        :return: The template_name of this StructConfig.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this StructConfig.

        所用模板名称，会对模板名称及id进行校验

        :param template_name: The template_name of this StructConfig.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this StructConfig.

        所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。

        :return: The template_type of this StructConfig.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this StructConfig.

        所用模板类型，分为built_in及custom两种类型，对应系统模板和自定义模板，系统模板分为CTS，VPC和ELB三种。

        :param template_type: The template_type of this StructConfig.
        :type template_type: str
        """
        self._template_type = template_type

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
        if not isinstance(other, StructConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
