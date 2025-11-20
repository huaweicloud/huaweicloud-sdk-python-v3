# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageCheckRuleResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'check_name': 'str',
        'check_type': 'str',
        'standard': 'str',
        'check_type_desc': 'str',
        'check_rule_name': 'str',
        'check_rule_id': 'str',
        'scan_result': 'str',
        'latest_scan_time': 'int',
        'image_num': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'check_type_desc': 'check_type_desc',
        'check_rule_name': 'check_rule_name',
        'check_rule_id': 'check_rule_id',
        'scan_result': 'scan_result',
        'latest_scan_time': 'latest_scan_time',
        'image_num': 'image_num'
    }

    def __init__(self, severity=None, check_name=None, check_type=None, standard=None, check_type_desc=None, check_rule_name=None, check_rule_id=None, scan_result=None, latest_scan_time=None, image_num=None):
        r"""ImageCheckRuleResponseInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 风险等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 
        :type severity: str
        :param check_name: **参数解释**: 基线名称 **取值范围**: 字符长度0-256 
        :type check_name: str
        :param check_type: **参数解释**: 基线类型 **取值范围**: 字符长度0-256 
        :type check_type: str
        :param standard: **参数解释**: 标准类型 **取值范围**: - cn_standard：等保合规标准 - hw_standard：华为标准 - qt_standard：青腾标准
        :type standard: str
        :param check_type_desc: **参数解释**: 基线描述信息 **取值范围**: 字符长度0-65534 
        :type check_type_desc: str
        :param check_rule_name: **参数解释**: 检查项 **取值范围**: 字符长度0-2048 
        :type check_rule_name: str
        :param check_rule_id: **参数解释**: 检查项ID **取值范围**: 字符长度0-128 
        :type check_rule_id: str
        :param scan_result: **参数解释**: 检测结果 **取值范围**: - pass：通过 - failed：未通过
        :type scan_result: str
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位：毫秒（ms） **取值范围**: 大小0-9223372036854775807 
        :type latest_scan_time: int
        :param image_num: **参数解释**: 受影响的镜像的数量，进行了当前基线检测的镜像数量 **取值范围**: 大小0-2097152 
        :type image_num: int
        """
        
        

        self._severity = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._check_type_desc = None
        self._check_rule_name = None
        self._check_rule_id = None
        self._scan_result = None
        self._latest_scan_time = None
        self._image_num = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_name is not None:
            self.check_name = check_name
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if check_type_desc is not None:
            self.check_type_desc = check_type_desc
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if scan_result is not None:
            self.scan_result = scan_result
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if image_num is not None:
            self.image_num = image_num

    @property
    def severity(self):
        r"""Gets the severity of this ImageCheckRuleResponseInfo.

        **参数解释**： 风险等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :return: The severity of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ImageCheckRuleResponseInfo.

        **参数解释**： 风险等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :param severity: The severity of this ImageCheckRuleResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_name(self):
        r"""Gets the check_name of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线名称 **取值范围**: 字符长度0-256 

        :return: The check_name of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线名称 **取值范围**: 字符长度0-256 

        :param check_name: The check_name of this ImageCheckRuleResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        r"""Gets the check_type of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线类型 **取值范围**: 字符长度0-256 

        :return: The check_type of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线类型 **取值范围**: 字符长度0-256 

        :param check_type: The check_type of this ImageCheckRuleResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ImageCheckRuleResponseInfo.

        **参数解释**: 标准类型 **取值范围**: - cn_standard：等保合规标准 - hw_standard：华为标准 - qt_standard：青腾标准

        :return: The standard of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ImageCheckRuleResponseInfo.

        **参数解释**: 标准类型 **取值范围**: - cn_standard：等保合规标准 - hw_standard：华为标准 - qt_standard：青腾标准

        :param standard: The standard of this ImageCheckRuleResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_type_desc(self):
        r"""Gets the check_type_desc of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线描述信息 **取值范围**: 字符长度0-65534 

        :return: The check_type_desc of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        r"""Sets the check_type_desc of this ImageCheckRuleResponseInfo.

        **参数解释**: 基线描述信息 **取值范围**: 字符长度0-65534 

        :param check_type_desc: The check_type_desc of this ImageCheckRuleResponseInfo.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ImageCheckRuleResponseInfo.

        **参数解释**: 检查项 **取值范围**: 字符长度0-2048 

        :return: The check_rule_name of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ImageCheckRuleResponseInfo.

        **参数解释**: 检查项 **取值范围**: 字符长度0-2048 

        :param check_rule_name: The check_rule_name of this ImageCheckRuleResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ImageCheckRuleResponseInfo.

        **参数解释**: 检查项ID **取值范围**: 字符长度0-128 

        :return: The check_rule_id of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ImageCheckRuleResponseInfo.

        **参数解释**: 检查项ID **取值范围**: 字符长度0-128 

        :param check_rule_id: The check_rule_id of this ImageCheckRuleResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ImageCheckRuleResponseInfo.

        **参数解释**: 检测结果 **取值范围**: - pass：通过 - failed：未通过

        :return: The scan_result of this ImageCheckRuleResponseInfo.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ImageCheckRuleResponseInfo.

        **参数解释**: 检测结果 **取值范围**: - pass：通过 - failed：未通过

        :param scan_result: The scan_result of this ImageCheckRuleResponseInfo.
        :type scan_result: str
        """
        self._scan_result = scan_result

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageCheckRuleResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位：毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :return: The latest_scan_time of this ImageCheckRuleResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageCheckRuleResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位：毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this ImageCheckRuleResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def image_num(self):
        r"""Gets the image_num of this ImageCheckRuleResponseInfo.

        **参数解释**: 受影响的镜像的数量，进行了当前基线检测的镜像数量 **取值范围**: 大小0-2097152 

        :return: The image_num of this ImageCheckRuleResponseInfo.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ImageCheckRuleResponseInfo.

        **参数解释**: 受影响的镜像的数量，进行了当前基线检测的镜像数量 **取值范围**: 大小0-2097152 

        :param image_num: The image_num of this ImageCheckRuleResponseInfo.
        :type image_num: int
        """
        self._image_num = image_num

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
        if not isinstance(other, ImageCheckRuleResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
