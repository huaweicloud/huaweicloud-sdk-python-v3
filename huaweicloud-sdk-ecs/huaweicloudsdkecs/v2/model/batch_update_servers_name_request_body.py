# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateServersNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'dry_run': 'bool',
        'servers': 'list[ServerId]'
    }

    attribute_map = {
        'name': 'name',
        'dry_run': 'dry_run',
        'servers': 'servers'
    }

    def __init__(self, name=None, dry_run=None, servers=None):
        """BatchUpdateServersNameRequestBody

        The model defined in huaweicloud sdk

        :param name: 弹性云服务器修改后的名称。  规则如下：  只能允许包含中文汉字、大小写字母、数字及 \&quot;-\&quot; 、 \&quot;_\&quot; 、\&quot;.\&quot; 等特殊字符，长度限制在64个字符以内。  批量修改弹性云服务器名称时，名不会自动按序增加数字尾缀。例如： 三个ECS的名称为test_0001，test_0002，test_0003，批量修改云服务器名称为develop，则修改后3个云服务器名称为develop，develop，develop。
        :type name: str
        :param dry_run: 是否只预检此次请求。  - true：发送检查请求，不会修改云服务器名称。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回正常响应信息。 - false：发送正常请求，通过检查后并且执行修改云服务器名称的请求。  默认值：false
        :type dry_run: bool
        :param servers: 待修改的弹性云服务器ID信息。
        :type servers: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        
        

        self._name = None
        self._dry_run = None
        self._servers = None
        self.discriminator = None

        self.name = name
        if dry_run is not None:
            self.dry_run = dry_run
        self.servers = servers

    @property
    def name(self):
        """Gets the name of this BatchUpdateServersNameRequestBody.

        弹性云服务器修改后的名称。  规则如下：  只能允许包含中文汉字、大小写字母、数字及 \"-\" 、 \"_\" 、\".\" 等特殊字符，长度限制在64个字符以内。  批量修改弹性云服务器名称时，名不会自动按序增加数字尾缀。例如： 三个ECS的名称为test_0001，test_0002，test_0003，批量修改云服务器名称为develop，则修改后3个云服务器名称为develop，develop，develop。

        :return: The name of this BatchUpdateServersNameRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchUpdateServersNameRequestBody.

        弹性云服务器修改后的名称。  规则如下：  只能允许包含中文汉字、大小写字母、数字及 \"-\" 、 \"_\" 、\".\" 等特殊字符，长度限制在64个字符以内。  批量修改弹性云服务器名称时，名不会自动按序增加数字尾缀。例如： 三个ECS的名称为test_0001，test_0002，test_0003，批量修改云服务器名称为develop，则修改后3个云服务器名称为develop，develop，develop。

        :param name: The name of this BatchUpdateServersNameRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchUpdateServersNameRequestBody.

        是否只预检此次请求。  - true：发送检查请求，不会修改云服务器名称。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回正常响应信息。 - false：发送正常请求，通过检查后并且执行修改云服务器名称的请求。  默认值：false

        :return: The dry_run of this BatchUpdateServersNameRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchUpdateServersNameRequestBody.

        是否只预检此次请求。  - true：发送检查请求，不会修改云服务器名称。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回正常响应信息。 - false：发送正常请求，通过检查后并且执行修改云服务器名称的请求。  默认值：false

        :param dry_run: The dry_run of this BatchUpdateServersNameRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def servers(self):
        """Gets the servers of this BatchUpdateServersNameRequestBody.

        待修改的弹性云服务器ID信息。

        :return: The servers of this BatchUpdateServersNameRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchUpdateServersNameRequestBody.

        待修改的弹性云服务器ID信息。

        :param servers: The servers of this BatchUpdateServersNameRequestBody.
        :type servers: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        self._servers = servers

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
        if not isinstance(other, BatchUpdateServersNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
