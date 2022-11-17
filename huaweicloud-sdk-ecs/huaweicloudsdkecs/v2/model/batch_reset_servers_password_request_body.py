# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResetServersPasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'dry_run': 'bool',
        'servers': 'list[ServerId]'
    }

    attribute_map = {
        'new_password': 'new_password',
        'dry_run': 'dry_run',
        'servers': 'servers'
    }

    def __init__(self, new_password=None, dry_run=None, servers=None):
        """BatchResetServersPasswordRequestBody

        The model defined in huaweicloud sdk

        :param new_password: 新密码。  当dry_run字段为true时，该字段为非必填字段，否则为必填字段。  新密码的校验规则：  - 允许输入的字符包括：!@%-_&#x3D;+[]:./? - 禁止输入的字符包括：汉字及【】：；“”‘’、，。《》？￥…（）—— ·！~&#x60;#&amp;^,{}*();\&quot;&#39;&lt;&gt;|\\ $ - 复杂度上必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、以及允许的特殊字符中的3种以上搭配 - 不能包含用户名 \&quot;Administrator\&quot; 和“root”及逆序字符 - 不能包含用户名 \&quot;Administrator\&quot; 中连续3个字符
        :type new_password: str
        :param dry_run: 是否只预检此次请求。  - true：发送检查请求，不会重置密码。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应结果。 - false：发送正常请求，通过检查后并且进行重置密码请求。  默认值：false
        :type dry_run: bool
        :param servers: 待批量重置密码的弹性云服务器ID信息。
        :type servers: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        
        

        self._new_password = None
        self._dry_run = None
        self._servers = None
        self.discriminator = None

        self.new_password = new_password
        if dry_run is not None:
            self.dry_run = dry_run
        self.servers = servers

    @property
    def new_password(self):
        """Gets the new_password of this BatchResetServersPasswordRequestBody.

        新密码。  当dry_run字段为true时，该字段为非必填字段，否则为必填字段。  新密码的校验规则：  - 允许输入的字符包括：!@%-_=+[]:./? - 禁止输入的字符包括：汉字及【】：；“”‘’、，。《》？￥…（）—— ·！~`#&^,{}*();\"'<>|\\ $ - 复杂度上必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、以及允许的特殊字符中的3种以上搭配 - 不能包含用户名 \"Administrator\" 和“root”及逆序字符 - 不能包含用户名 \"Administrator\" 中连续3个字符

        :return: The new_password of this BatchResetServersPasswordRequestBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this BatchResetServersPasswordRequestBody.

        新密码。  当dry_run字段为true时，该字段为非必填字段，否则为必填字段。  新密码的校验规则：  - 允许输入的字符包括：!@%-_=+[]:./? - 禁止输入的字符包括：汉字及【】：；“”‘’、，。《》？￥…（）—— ·！~`#&^,{}*();\"'<>|\\ $ - 复杂度上必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、以及允许的特殊字符中的3种以上搭配 - 不能包含用户名 \"Administrator\" 和“root”及逆序字符 - 不能包含用户名 \"Administrator\" 中连续3个字符

        :param new_password: The new_password of this BatchResetServersPasswordRequestBody.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchResetServersPasswordRequestBody.

        是否只预检此次请求。  - true：发送检查请求，不会重置密码。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应结果。 - false：发送正常请求，通过检查后并且进行重置密码请求。  默认值：false

        :return: The dry_run of this BatchResetServersPasswordRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchResetServersPasswordRequestBody.

        是否只预检此次请求。  - true：发送检查请求，不会重置密码。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应结果。 - false：发送正常请求，通过检查后并且进行重置密码请求。  默认值：false

        :param dry_run: The dry_run of this BatchResetServersPasswordRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def servers(self):
        """Gets the servers of this BatchResetServersPasswordRequestBody.

        待批量重置密码的弹性云服务器ID信息。

        :return: The servers of this BatchResetServersPasswordRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchResetServersPasswordRequestBody.

        待批量重置密码的弹性云服务器ID信息。

        :param servers: The servers of this BatchResetServersPasswordRequestBody.
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
        if not isinstance(other, BatchResetServersPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
