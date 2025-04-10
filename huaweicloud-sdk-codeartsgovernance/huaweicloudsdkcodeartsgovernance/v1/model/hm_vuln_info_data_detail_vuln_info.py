# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HmVulnInfoDataDetailVulnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'problem_file_path': 'str',
        'identity_info': 'str',
        'risk_level': 'str',
        'app_name': 'str',
        'category_id': 'str',
        'type_cn': 'str',
        'type_en': 'str',
        'problem_cn': 'str',
        'problem_en': 'str',
        'solution_cn': 'str',
        'solution_en': 'str',
        'detection_scenario_cn': 'str',
        'detection_scenario_en': 'str',
        'wiki_url': 'str',
        'standard_info': 'str',
        'confirm_state': 'int',
        'confirm_result': 'int',
        'confirmer': 'str',
        'confirm_description': 'str',
        'confirm_time': 'date',
        'dts_id': 'str',
        'standard_no': 'str'
    }

    attribute_map = {
        'problem_file_path': 'problem_file_path',
        'identity_info': 'identity_info',
        'risk_level': 'risk_level',
        'app_name': 'app_name',
        'category_id': 'category_id',
        'type_cn': 'type_cn',
        'type_en': 'type_en',
        'problem_cn': 'problem_cn',
        'problem_en': 'problem_en',
        'solution_cn': 'solution_cn',
        'solution_en': 'solution_en',
        'detection_scenario_cn': 'detection_scenario_cn',
        'detection_scenario_en': 'detection_scenario_en',
        'wiki_url': 'wiki_url',
        'standard_info': 'standard_info',
        'confirm_state': 'confirm_state',
        'confirm_result': 'confirm_result',
        'confirmer': 'confirmer',
        'confirm_description': 'confirm_description',
        'confirm_time': 'confirm_time',
        'dts_id': 'dts_id',
        'standard_no': 'standard_no'
    }

    def __init__(self, problem_file_path=None, identity_info=None, risk_level=None, app_name=None, category_id=None, type_cn=None, type_en=None, problem_cn=None, problem_en=None, solution_cn=None, solution_en=None, detection_scenario_cn=None, detection_scenario_en=None, wiki_url=None, standard_info=None, confirm_state=None, confirm_result=None, confirmer=None, confirm_description=None, confirm_time=None, dts_id=None, standard_no=None):
        r"""HmVulnInfoDataDetailVulnInfo

        The model defined in huaweicloud sdk

        :param problem_file_path: 问题文件路径
        :type problem_file_path: str
        :param identity_info: 问题特征信息
        :type identity_info: str
        :param risk_level: 问题等级
        :type risk_level: str
        :param app_name: 应用名称
        :type app_name: str
        :param category_id: 问题项大类id
        :type category_id: str
        :param type_cn: 问题项大类中文名
        :type type_cn: str
        :param type_en: 问题项大类英文名
        :type type_en: str
        :param problem_cn: 问题描述中文
        :type problem_cn: str
        :param problem_en: 问题描述英文
        :type problem_en: str
        :param solution_cn: 解决办法中文
        :type solution_cn: str
        :param solution_en: 解决办法英文
        :type solution_en: str
        :param detection_scenario_cn: 问题详细描述中文
        :type detection_scenario_cn: str
        :param detection_scenario_en: 问题详细描述英文
        :type detection_scenario_en: str
        :param wiki_url: 问题wiki
        :type wiki_url: str
        :param standard_info: 问题来源规范
        :type standard_info: str
        :param confirm_state: 漏洞确认: 0 - 未确认 1 - 已确认
        :type confirm_state: int
        :param confirm_result: 漏洞确认结果: 0 - 未误报 1 - 误报
        :type confirm_result: int
        :param confirmer: 确认人
        :type confirmer: str
        :param confirm_description: 确认描述
        :type confirm_description: str
        :param confirm_time: 确认时间
        :type confirm_time: date
        :param dts_id: 问题单编号
        :type dts_id: str
        :param standard_no: 标准标号
        :type standard_no: str
        """
        
        

        self._problem_file_path = None
        self._identity_info = None
        self._risk_level = None
        self._app_name = None
        self._category_id = None
        self._type_cn = None
        self._type_en = None
        self._problem_cn = None
        self._problem_en = None
        self._solution_cn = None
        self._solution_en = None
        self._detection_scenario_cn = None
        self._detection_scenario_en = None
        self._wiki_url = None
        self._standard_info = None
        self._confirm_state = None
        self._confirm_result = None
        self._confirmer = None
        self._confirm_description = None
        self._confirm_time = None
        self._dts_id = None
        self._standard_no = None
        self.discriminator = None

        if problem_file_path is not None:
            self.problem_file_path = problem_file_path
        if identity_info is not None:
            self.identity_info = identity_info
        if risk_level is not None:
            self.risk_level = risk_level
        if app_name is not None:
            self.app_name = app_name
        if category_id is not None:
            self.category_id = category_id
        if type_cn is not None:
            self.type_cn = type_cn
        if type_en is not None:
            self.type_en = type_en
        if problem_cn is not None:
            self.problem_cn = problem_cn
        if problem_en is not None:
            self.problem_en = problem_en
        if solution_cn is not None:
            self.solution_cn = solution_cn
        if solution_en is not None:
            self.solution_en = solution_en
        if detection_scenario_cn is not None:
            self.detection_scenario_cn = detection_scenario_cn
        if detection_scenario_en is not None:
            self.detection_scenario_en = detection_scenario_en
        if wiki_url is not None:
            self.wiki_url = wiki_url
        if standard_info is not None:
            self.standard_info = standard_info
        if confirm_state is not None:
            self.confirm_state = confirm_state
        if confirm_result is not None:
            self.confirm_result = confirm_result
        if confirmer is not None:
            self.confirmer = confirmer
        if confirm_description is not None:
            self.confirm_description = confirm_description
        if confirm_time is not None:
            self.confirm_time = confirm_time
        if dts_id is not None:
            self.dts_id = dts_id
        if standard_no is not None:
            self.standard_no = standard_no

    @property
    def problem_file_path(self):
        r"""Gets the problem_file_path of this HmVulnInfoDataDetailVulnInfo.

        问题文件路径

        :return: The problem_file_path of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._problem_file_path

    @problem_file_path.setter
    def problem_file_path(self, problem_file_path):
        r"""Sets the problem_file_path of this HmVulnInfoDataDetailVulnInfo.

        问题文件路径

        :param problem_file_path: The problem_file_path of this HmVulnInfoDataDetailVulnInfo.
        :type problem_file_path: str
        """
        self._problem_file_path = problem_file_path

    @property
    def identity_info(self):
        r"""Gets the identity_info of this HmVulnInfoDataDetailVulnInfo.

        问题特征信息

        :return: The identity_info of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._identity_info

    @identity_info.setter
    def identity_info(self, identity_info):
        r"""Sets the identity_info of this HmVulnInfoDataDetailVulnInfo.

        问题特征信息

        :param identity_info: The identity_info of this HmVulnInfoDataDetailVulnInfo.
        :type identity_info: str
        """
        self._identity_info = identity_info

    @property
    def risk_level(self):
        r"""Gets the risk_level of this HmVulnInfoDataDetailVulnInfo.

        问题等级

        :return: The risk_level of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this HmVulnInfoDataDetailVulnInfo.

        问题等级

        :param risk_level: The risk_level of this HmVulnInfoDataDetailVulnInfo.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def app_name(self):
        r"""Gets the app_name of this HmVulnInfoDataDetailVulnInfo.

        应用名称

        :return: The app_name of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this HmVulnInfoDataDetailVulnInfo.

        应用名称

        :param app_name: The app_name of this HmVulnInfoDataDetailVulnInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def category_id(self):
        r"""Gets the category_id of this HmVulnInfoDataDetailVulnInfo.

        问题项大类id

        :return: The category_id of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this HmVulnInfoDataDetailVulnInfo.

        问题项大类id

        :param category_id: The category_id of this HmVulnInfoDataDetailVulnInfo.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def type_cn(self):
        r"""Gets the type_cn of this HmVulnInfoDataDetailVulnInfo.

        问题项大类中文名

        :return: The type_cn of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._type_cn

    @type_cn.setter
    def type_cn(self, type_cn):
        r"""Sets the type_cn of this HmVulnInfoDataDetailVulnInfo.

        问题项大类中文名

        :param type_cn: The type_cn of this HmVulnInfoDataDetailVulnInfo.
        :type type_cn: str
        """
        self._type_cn = type_cn

    @property
    def type_en(self):
        r"""Gets the type_en of this HmVulnInfoDataDetailVulnInfo.

        问题项大类英文名

        :return: The type_en of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._type_en

    @type_en.setter
    def type_en(self, type_en):
        r"""Sets the type_en of this HmVulnInfoDataDetailVulnInfo.

        问题项大类英文名

        :param type_en: The type_en of this HmVulnInfoDataDetailVulnInfo.
        :type type_en: str
        """
        self._type_en = type_en

    @property
    def problem_cn(self):
        r"""Gets the problem_cn of this HmVulnInfoDataDetailVulnInfo.

        问题描述中文

        :return: The problem_cn of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._problem_cn

    @problem_cn.setter
    def problem_cn(self, problem_cn):
        r"""Sets the problem_cn of this HmVulnInfoDataDetailVulnInfo.

        问题描述中文

        :param problem_cn: The problem_cn of this HmVulnInfoDataDetailVulnInfo.
        :type problem_cn: str
        """
        self._problem_cn = problem_cn

    @property
    def problem_en(self):
        r"""Gets the problem_en of this HmVulnInfoDataDetailVulnInfo.

        问题描述英文

        :return: The problem_en of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._problem_en

    @problem_en.setter
    def problem_en(self, problem_en):
        r"""Sets the problem_en of this HmVulnInfoDataDetailVulnInfo.

        问题描述英文

        :param problem_en: The problem_en of this HmVulnInfoDataDetailVulnInfo.
        :type problem_en: str
        """
        self._problem_en = problem_en

    @property
    def solution_cn(self):
        r"""Gets the solution_cn of this HmVulnInfoDataDetailVulnInfo.

        解决办法中文

        :return: The solution_cn of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._solution_cn

    @solution_cn.setter
    def solution_cn(self, solution_cn):
        r"""Sets the solution_cn of this HmVulnInfoDataDetailVulnInfo.

        解决办法中文

        :param solution_cn: The solution_cn of this HmVulnInfoDataDetailVulnInfo.
        :type solution_cn: str
        """
        self._solution_cn = solution_cn

    @property
    def solution_en(self):
        r"""Gets the solution_en of this HmVulnInfoDataDetailVulnInfo.

        解决办法英文

        :return: The solution_en of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._solution_en

    @solution_en.setter
    def solution_en(self, solution_en):
        r"""Sets the solution_en of this HmVulnInfoDataDetailVulnInfo.

        解决办法英文

        :param solution_en: The solution_en of this HmVulnInfoDataDetailVulnInfo.
        :type solution_en: str
        """
        self._solution_en = solution_en

    @property
    def detection_scenario_cn(self):
        r"""Gets the detection_scenario_cn of this HmVulnInfoDataDetailVulnInfo.

        问题详细描述中文

        :return: The detection_scenario_cn of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._detection_scenario_cn

    @detection_scenario_cn.setter
    def detection_scenario_cn(self, detection_scenario_cn):
        r"""Sets the detection_scenario_cn of this HmVulnInfoDataDetailVulnInfo.

        问题详细描述中文

        :param detection_scenario_cn: The detection_scenario_cn of this HmVulnInfoDataDetailVulnInfo.
        :type detection_scenario_cn: str
        """
        self._detection_scenario_cn = detection_scenario_cn

    @property
    def detection_scenario_en(self):
        r"""Gets the detection_scenario_en of this HmVulnInfoDataDetailVulnInfo.

        问题详细描述英文

        :return: The detection_scenario_en of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._detection_scenario_en

    @detection_scenario_en.setter
    def detection_scenario_en(self, detection_scenario_en):
        r"""Sets the detection_scenario_en of this HmVulnInfoDataDetailVulnInfo.

        问题详细描述英文

        :param detection_scenario_en: The detection_scenario_en of this HmVulnInfoDataDetailVulnInfo.
        :type detection_scenario_en: str
        """
        self._detection_scenario_en = detection_scenario_en

    @property
    def wiki_url(self):
        r"""Gets the wiki_url of this HmVulnInfoDataDetailVulnInfo.

        问题wiki

        :return: The wiki_url of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._wiki_url

    @wiki_url.setter
    def wiki_url(self, wiki_url):
        r"""Sets the wiki_url of this HmVulnInfoDataDetailVulnInfo.

        问题wiki

        :param wiki_url: The wiki_url of this HmVulnInfoDataDetailVulnInfo.
        :type wiki_url: str
        """
        self._wiki_url = wiki_url

    @property
    def standard_info(self):
        r"""Gets the standard_info of this HmVulnInfoDataDetailVulnInfo.

        问题来源规范

        :return: The standard_info of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._standard_info

    @standard_info.setter
    def standard_info(self, standard_info):
        r"""Sets the standard_info of this HmVulnInfoDataDetailVulnInfo.

        问题来源规范

        :param standard_info: The standard_info of this HmVulnInfoDataDetailVulnInfo.
        :type standard_info: str
        """
        self._standard_info = standard_info

    @property
    def confirm_state(self):
        r"""Gets the confirm_state of this HmVulnInfoDataDetailVulnInfo.

        漏洞确认: 0 - 未确认 1 - 已确认

        :return: The confirm_state of this HmVulnInfoDataDetailVulnInfo.
        :rtype: int
        """
        return self._confirm_state

    @confirm_state.setter
    def confirm_state(self, confirm_state):
        r"""Sets the confirm_state of this HmVulnInfoDataDetailVulnInfo.

        漏洞确认: 0 - 未确认 1 - 已确认

        :param confirm_state: The confirm_state of this HmVulnInfoDataDetailVulnInfo.
        :type confirm_state: int
        """
        self._confirm_state = confirm_state

    @property
    def confirm_result(self):
        r"""Gets the confirm_result of this HmVulnInfoDataDetailVulnInfo.

        漏洞确认结果: 0 - 未误报 1 - 误报

        :return: The confirm_result of this HmVulnInfoDataDetailVulnInfo.
        :rtype: int
        """
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, confirm_result):
        r"""Sets the confirm_result of this HmVulnInfoDataDetailVulnInfo.

        漏洞确认结果: 0 - 未误报 1 - 误报

        :param confirm_result: The confirm_result of this HmVulnInfoDataDetailVulnInfo.
        :type confirm_result: int
        """
        self._confirm_result = confirm_result

    @property
    def confirmer(self):
        r"""Gets the confirmer of this HmVulnInfoDataDetailVulnInfo.

        确认人

        :return: The confirmer of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._confirmer

    @confirmer.setter
    def confirmer(self, confirmer):
        r"""Sets the confirmer of this HmVulnInfoDataDetailVulnInfo.

        确认人

        :param confirmer: The confirmer of this HmVulnInfoDataDetailVulnInfo.
        :type confirmer: str
        """
        self._confirmer = confirmer

    @property
    def confirm_description(self):
        r"""Gets the confirm_description of this HmVulnInfoDataDetailVulnInfo.

        确认描述

        :return: The confirm_description of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._confirm_description

    @confirm_description.setter
    def confirm_description(self, confirm_description):
        r"""Sets the confirm_description of this HmVulnInfoDataDetailVulnInfo.

        确认描述

        :param confirm_description: The confirm_description of this HmVulnInfoDataDetailVulnInfo.
        :type confirm_description: str
        """
        self._confirm_description = confirm_description

    @property
    def confirm_time(self):
        r"""Gets the confirm_time of this HmVulnInfoDataDetailVulnInfo.

        确认时间

        :return: The confirm_time of this HmVulnInfoDataDetailVulnInfo.
        :rtype: date
        """
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, confirm_time):
        r"""Sets the confirm_time of this HmVulnInfoDataDetailVulnInfo.

        确认时间

        :param confirm_time: The confirm_time of this HmVulnInfoDataDetailVulnInfo.
        :type confirm_time: date
        """
        self._confirm_time = confirm_time

    @property
    def dts_id(self):
        r"""Gets the dts_id of this HmVulnInfoDataDetailVulnInfo.

        问题单编号

        :return: The dts_id of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._dts_id

    @dts_id.setter
    def dts_id(self, dts_id):
        r"""Sets the dts_id of this HmVulnInfoDataDetailVulnInfo.

        问题单编号

        :param dts_id: The dts_id of this HmVulnInfoDataDetailVulnInfo.
        :type dts_id: str
        """
        self._dts_id = dts_id

    @property
    def standard_no(self):
        r"""Gets the standard_no of this HmVulnInfoDataDetailVulnInfo.

        标准标号

        :return: The standard_no of this HmVulnInfoDataDetailVulnInfo.
        :rtype: str
        """
        return self._standard_no

    @standard_no.setter
    def standard_no(self, standard_no):
        r"""Sets the standard_no of this HmVulnInfoDataDetailVulnInfo.

        标准标号

        :param standard_no: The standard_no of this HmVulnInfoDataDetailVulnInfo.
        :type standard_no: str
        """
        self._standard_no = standard_no

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
        if not isinstance(other, HmVulnInfoDataDetailVulnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
