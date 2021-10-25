# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppRulesSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_type': 'str',
        'attr_list': 'list[str]',
        'detect_log': 'str',
        'discovery_rule': 'list[DiscoveryRule]',
        'is_default_rule': 'str',
        'is_detect': 'str',
        'log_file_fix': 'list[str]',
        'log_path_rule': 'list[LogPathRule]',
        'name_rule': 'list[NameRule]',
        'priority': 'int'
    }

    attribute_map = {
        'app_type': 'appType',
        'attr_list': 'attrList',
        'detect_log': 'detectLog',
        'discovery_rule': 'discoveryRule',
        'is_default_rule': 'isDefaultRule',
        'is_detect': 'isDetect',
        'log_file_fix': 'logFileFix',
        'log_path_rule': 'logPathRule',
        'name_rule': 'nameRule',
        'priority': 'priority'
    }

    def __init__(self, app_type=None, attr_list=None, detect_log=None, discovery_rule=None, is_default_rule=None, is_detect=None, log_file_fix=None, log_path_rule=None, name_rule=None, priority=None):
        """AppRulesSpec - a model defined in huaweicloud sdk"""
        
        

        self._app_type = None
        self._attr_list = None
        self._detect_log = None
        self._discovery_rule = None
        self._is_default_rule = None
        self._is_detect = None
        self._log_file_fix = None
        self._log_path_rule = None
        self._name_rule = None
        self._priority = None
        self.discriminator = None

        self.app_type = app_type
        if attr_list is not None:
            self.attr_list = attr_list
        self.detect_log = detect_log
        self.discovery_rule = discovery_rule
        self.is_default_rule = is_default_rule
        self.is_detect = is_detect
        self.log_file_fix = log_file_fix
        if log_path_rule is not None:
            self.log_path_rule = log_path_rule
        self.name_rule = name_rule
        self.priority = priority

    @property
    def app_type(self):
        """Gets the app_type of this AppRulesSpec.

        服务类型,用于标记服务的分类,仅用于规则分类和界面展示。可以填写任意字段,如按技术栈分类可填写Java,Python。按作用分类可填写collector(采集),database(数据库)等。

        :return: The app_type of this AppRulesSpec.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppRulesSpec.

        服务类型,用于标记服务的分类,仅用于规则分类和界面展示。可以填写任意字段,如按技术栈分类可填写Java,Python。按作用分类可填写collector(采集),database(数据库)等。

        :param app_type: The app_type of this AppRulesSpec.
        :type: str
        """
        self._app_type = app_type

    @property
    def attr_list(self):
        """Gets the attr_list of this AppRulesSpec.

        cmdLine、env 属性列表(暂不使用,可不传)。

        :return: The attr_list of this AppRulesSpec.
        :rtype: list[str]
        """
        return self._attr_list

    @attr_list.setter
    def attr_list(self, attr_list):
        """Sets the attr_list of this AppRulesSpec.

        cmdLine、env 属性列表(暂不使用,可不传)。

        :param attr_list: The attr_list of this AppRulesSpec.
        :type: list[str]
        """
        self._attr_list = attr_list

    @property
    def detect_log(self):
        """Gets the detect_log of this AppRulesSpec.

        true、false 是否开启日志采集。

        :return: The detect_log of this AppRulesSpec.
        :rtype: str
        """
        return self._detect_log

    @detect_log.setter
    def detect_log(self, detect_log):
        """Sets the detect_log of this AppRulesSpec.

        true、false 是否开启日志采集。

        :param detect_log: The detect_log of this AppRulesSpec.
        :type: str
        """
        self._detect_log = detect_log

    @property
    def discovery_rule(self):
        """Gets the discovery_rule of this AppRulesSpec.

        checkType为cmdLine时checkMode填contain,checkContent格式为[“xxx”]表示进程命令行参数中需要包含xxx。checkType为env时checkMode填contain,checkContent格式为 [\"k1\",\"v1\"]表示进程环境变量中需要包含名为k1值为v1的环境变量。checkType为scope时checkMode填equals,checkContent格式为节点ID数组[\"hostId1”,”hostId2”],表示规则仅会在这些节点上生效(如果不指定节点范围,规则将下发到该项目所有的节点)。 规则发现部分,数组中有多个对象时表示需要同时满足所有条件的进程才会被匹配到。

        :return: The discovery_rule of this AppRulesSpec.
        :rtype: list[DiscoveryRule]
        """
        return self._discovery_rule

    @discovery_rule.setter
    def discovery_rule(self, discovery_rule):
        """Sets the discovery_rule of this AppRulesSpec.

        checkType为cmdLine时checkMode填contain,checkContent格式为[“xxx”]表示进程命令行参数中需要包含xxx。checkType为env时checkMode填contain,checkContent格式为 [\"k1\",\"v1\"]表示进程环境变量中需要包含名为k1值为v1的环境变量。checkType为scope时checkMode填equals,checkContent格式为节点ID数组[\"hostId1”,”hostId2”],表示规则仅会在这些节点上生效(如果不指定节点范围,规则将下发到该项目所有的节点)。 规则发现部分,数组中有多个对象时表示需要同时满足所有条件的进程才会被匹配到。

        :param discovery_rule: The discovery_rule of this AppRulesSpec.
        :type: list[DiscoveryRule]
        """
        self._discovery_rule = discovery_rule

    @property
    def is_default_rule(self):
        """Gets the is_default_rule of this AppRulesSpec.

        true、false 是否为默认规则。

        :return: The is_default_rule of this AppRulesSpec.
        :rtype: str
        """
        return self._is_default_rule

    @is_default_rule.setter
    def is_default_rule(self, is_default_rule):
        """Sets the is_default_rule of this AppRulesSpec.

        true、false 是否为默认规则。

        :param is_default_rule: The is_default_rule of this AppRulesSpec.
        :type: str
        """
        self._is_default_rule = is_default_rule

    @property
    def is_detect(self):
        """Gets the is_detect of this AppRulesSpec.

        true、false 是否为规则预探测场景(预探测场景不会保存规则,仅用于规则下发之前对规则正确性的检测)。

        :return: The is_detect of this AppRulesSpec.
        :rtype: str
        """
        return self._is_detect

    @is_detect.setter
    def is_detect(self, is_detect):
        """Sets the is_detect of this AppRulesSpec.

        true、false 是否为规则预探测场景(预探测场景不会保存规则,仅用于规则下发之前对规则正确性的检测)。

        :param is_detect: The is_detect of this AppRulesSpec.
        :type: str
        """
        self._is_detect = is_detect

    @property
    def log_file_fix(self):
        """Gets the log_file_fix of this AppRulesSpec.

        log、trace、out 日志文件的后缀。

        :return: The log_file_fix of this AppRulesSpec.
        :rtype: list[str]
        """
        return self._log_file_fix

    @log_file_fix.setter
    def log_file_fix(self, log_file_fix):
        """Sets the log_file_fix of this AppRulesSpec.

        log、trace、out 日志文件的后缀。

        :param log_file_fix: The log_file_fix of this AppRulesSpec.
        :type: list[str]
        """
        self._log_file_fix = log_file_fix

    @property
    def log_path_rule(self):
        """Gets the log_path_rule of this AppRulesSpec.

        当cmdLineHash为固定字符串时,指定日志路径或者日志文件。否则只采集进程当前打开的以.log和.trace结尾的文件。nameType取值cmdLineHash时,args格式为[\"00001\"],value格式为[\"/xxx/xx.log\"],表示当启动命令是00001时,日志路径为/xxx/xx.log。 日志路径配置规则。

        :return: The log_path_rule of this AppRulesSpec.
        :rtype: list[LogPathRule]
        """
        return self._log_path_rule

    @log_path_rule.setter
    def log_path_rule(self, log_path_rule):
        """Sets the log_path_rule of this AppRulesSpec.

        当cmdLineHash为固定字符串时,指定日志路径或者日志文件。否则只采集进程当前打开的以.log和.trace结尾的文件。nameType取值cmdLineHash时,args格式为[\"00001\"],value格式为[\"/xxx/xx.log\"],表示当启动命令是00001时,日志路径为/xxx/xx.log。 日志路径配置规则。

        :param log_path_rule: The log_path_rule of this AppRulesSpec.
        :type: list[LogPathRule]
        """
        self._log_path_rule = log_path_rule

    @property
    def name_rule(self):
        """Gets the name_rule of this AppRulesSpec.

        服务发现规则命名部分。

        :return: The name_rule of this AppRulesSpec.
        :rtype: list[NameRule]
        """
        return self._name_rule

    @name_rule.setter
    def name_rule(self, name_rule):
        """Sets the name_rule of this AppRulesSpec.

        服务发现规则命名部分。

        :param name_rule: The name_rule of this AppRulesSpec.
        :type: list[NameRule]
        """
        self._name_rule = name_rule

    @property
    def priority(self):
        """Gets the priority of this AppRulesSpec.

        1~9999的整数,默认取值为9999 规则优先级。

        :return: The priority of this AppRulesSpec.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AppRulesSpec.

        1~9999的整数,默认取值为9999 规则优先级。

        :param priority: The priority of this AppRulesSpec.
        :type: int
        """
        self._priority = priority

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
        if not isinstance(other, AppRulesSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
