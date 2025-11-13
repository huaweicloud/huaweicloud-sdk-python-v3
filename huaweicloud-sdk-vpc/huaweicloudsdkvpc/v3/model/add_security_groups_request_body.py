# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSecurityGroupsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'InsertSecurityGroupOption',
        'dry_run': 'bool'
    }

    attribute_map = {
        'port': 'port',
        'dry_run': 'dry_run'
    }

    def __init__(self, port=None, dry_run=None):
        r"""AddSecurityGroupsRequestBody

        The model defined in huaweicloud sdk

        :param port: 
        :type port: :class:`huaweicloudsdkvpc.v3.InsertSecurityGroupOption`
        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会执行端口插入安全组。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接执行端口插入安全组。
        :type dry_run: bool
        """
        
        

        self._port = None
        self._dry_run = None
        self.discriminator = None

        self.port = port
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def port(self):
        r"""Gets the port of this AddSecurityGroupsRequestBody.

        :return: The port of this AddSecurityGroupsRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.InsertSecurityGroupOption`
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AddSecurityGroupsRequestBody.

        :param port: The port of this AddSecurityGroupsRequestBody.
        :type port: :class:`huaweicloudsdkvpc.v3.InsertSecurityGroupOption`
        """
        self._port = port

    @property
    def dry_run(self):
        r"""Gets the dry_run of this AddSecurityGroupsRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会执行端口插入安全组。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接执行端口插入安全组。

        :return: The dry_run of this AddSecurityGroupsRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this AddSecurityGroupsRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会执行端口插入安全组。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接执行端口插入安全组。

        :param dry_run: The dry_run of this AddSecurityGroupsRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, AddSecurityGroupsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
