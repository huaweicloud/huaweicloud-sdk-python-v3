# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NameRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_name_rule': 'list[AppNameRule]',
        'application_name_rule': 'list[ApplicationNameRule]'
    }

    attribute_map = {
        'app_name_rule': 'appNameRule',
        'application_name_rule': 'applicationNameRule'
    }

    def __init__(self, app_name_rule=None, application_name_rule=None):
        """NameRule

        The model defined in huaweicloud sdk

        :param app_name_rule: 服务命名部分,数组中有多个对象时表示将每个对象抽取到的字符串拼接作为服务的名称。 nameType取值cmdLine时args格式为[\&quot;start\&quot;,\&quot;end\&quot;],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为[\&quot;aa\&quot;],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\&quot;fix\&quot;],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\&quot;0001\&quot;],value格式为[\&quot;ser\&quot;],表示当启动命令是0001时,服务名称为ser。
        :type app_name_rule: list[:class:`huaweicloudsdkaom.v2.AppNameRule`]
        :param application_name_rule: 应用命名部分。 nameType取值cmdLine时args格式为[\&quot;start\&quot;,\&quot;end\&quot;],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为 [\&quot;aa\&quot;],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\&quot;fix\&quot;],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\&quot;0001\&quot;],value格式为[\&quot;ser\&quot;],表示当启动命令是0001时,应用名称为ser。
        :type application_name_rule: list[:class:`huaweicloudsdkaom.v2.ApplicationNameRule`]
        """
        
        

        self._app_name_rule = None
        self._application_name_rule = None
        self.discriminator = None

        self.app_name_rule = app_name_rule
        self.application_name_rule = application_name_rule

    @property
    def app_name_rule(self):
        """Gets the app_name_rule of this NameRule.

        服务命名部分,数组中有多个对象时表示将每个对象抽取到的字符串拼接作为服务的名称。 nameType取值cmdLine时args格式为[\"start\",\"end\"],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为[\"aa\"],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\"fix\"],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\"0001\"],value格式为[\"ser\"],表示当启动命令是0001时,服务名称为ser。

        :return: The app_name_rule of this NameRule.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AppNameRule`]
        """
        return self._app_name_rule

    @app_name_rule.setter
    def app_name_rule(self, app_name_rule):
        """Sets the app_name_rule of this NameRule.

        服务命名部分,数组中有多个对象时表示将每个对象抽取到的字符串拼接作为服务的名称。 nameType取值cmdLine时args格式为[\"start\",\"end\"],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为[\"aa\"],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\"fix\"],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\"0001\"],value格式为[\"ser\"],表示当启动命令是0001时,服务名称为ser。

        :param app_name_rule: The app_name_rule of this NameRule.
        :type app_name_rule: list[:class:`huaweicloudsdkaom.v2.AppNameRule`]
        """
        self._app_name_rule = app_name_rule

    @property
    def application_name_rule(self):
        """Gets the application_name_rule of this NameRule.

        应用命名部分。 nameType取值cmdLine时args格式为[\"start\",\"end\"],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为 [\"aa\"],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\"fix\"],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\"0001\"],value格式为[\"ser\"],表示当启动命令是0001时,应用名称为ser。

        :return: The application_name_rule of this NameRule.
        :rtype: list[:class:`huaweicloudsdkaom.v2.ApplicationNameRule`]
        """
        return self._application_name_rule

    @application_name_rule.setter
    def application_name_rule(self, application_name_rule):
        """Sets the application_name_rule of this NameRule.

        应用命名部分。 nameType取值cmdLine时args格式为[\"start\",\"end\"],表示抽取命令行中start、end之间的字符。 nameType取值cmdLine时args格式为 [\"aa\"],表示抽取环境变量名为aa对应的环境变量值。 nameType取值str时,args格式为[\"fix\"],表示服务名称最后拼接固定文字fix。 nameType取值cmdLineHash时,args格式为[\"0001\"],value格式为[\"ser\"],表示当启动命令是0001时,应用名称为ser。

        :param application_name_rule: The application_name_rule of this NameRule.
        :type application_name_rule: list[:class:`huaweicloudsdkaom.v2.ApplicationNameRule`]
        """
        self._application_name_rule = application_name_rule

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
        if not isinstance(other, NameRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
