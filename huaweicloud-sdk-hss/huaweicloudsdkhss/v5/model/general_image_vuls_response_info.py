# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralImageVulsResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_name': 'str',
        'vul_id': 'str',
        'type': 'str',
        'image_type': 'str',
        'label_list': 'list[str]',
        'severity_level': 'str',
        'image_num': 'int',
        'cve_list': 'list[GeneralImageVulsResponseInfoCveList]',
        'max_cvss_score': 'float',
        'scan_time': 'int',
        'description': 'str',
        'url': 'str',
        'solution_detail': 'str',
        'cluster_num': 'int'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'type': 'type',
        'image_type': 'image_type',
        'label_list': 'label_list',
        'severity_level': 'severity_level',
        'image_num': 'image_num',
        'cve_list': 'cve_list',
        'max_cvss_score': 'max_cvss_score',
        'scan_time': 'scan_time',
        'description': 'description',
        'url': 'url',
        'solution_detail': 'solution_detail',
        'cluster_num': 'cluster_num'
    }

    def __init__(self, vul_name=None, vul_id=None, type=None, image_type=None, label_list=None, severity_level=None, image_num=None, cve_list=None, max_cvss_score=None, scan_time=None, description=None, url=None, solution_detail=None, cluster_num=None):
        r"""GeneralImageVulsResponseInfo

        The model defined in huaweicloud sdk

        :param vul_name: 漏洞名称
        :type vul_name: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞
        :type type: str
        :param image_type: 镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像
        :type image_type: str
        :param label_list: 漏洞标签列表
        :type label_list: list[str]
        :param severity_level: 漏洞的风险程度，取值如下：  -Critical : 严重  -High : 高危  -Medium : 中危  -Low : 低危
        :type severity_level: str
        :param image_num: 受影响镜像总数
        :type image_num: int
        :param cve_list: CVE列表
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.GeneralImageVulsResponseInfoCveList`]
        :param max_cvss_score: 镜像最大CVSS分值
        :type max_cvss_score: float
        :param scan_time: 最近扫描时间，时间单位：毫秒（ms）
        :type scan_time: int
        :param description: 漏洞描述
        :type description: str
        :param url: 漏洞修复参考链接
        :type url: str
        :param solution_detail: 修复建议
        :type solution_detail: str
        :param cluster_num: 受影响集群总数
        :type cluster_num: int
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._type = None
        self._image_type = None
        self._label_list = None
        self._severity_level = None
        self._image_num = None
        self._cve_list = None
        self._max_cvss_score = None
        self._scan_time = None
        self._description = None
        self._url = None
        self._solution_detail = None
        self._cluster_num = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if type is not None:
            self.type = type
        if image_type is not None:
            self.image_type = image_type
        if label_list is not None:
            self.label_list = label_list
        if severity_level is not None:
            self.severity_level = severity_level
        if image_num is not None:
            self.image_num = image_num
        if cve_list is not None:
            self.cve_list = cve_list
        if max_cvss_score is not None:
            self.max_cvss_score = max_cvss_score
        if scan_time is not None:
            self.scan_time = scan_time
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if solution_detail is not None:
            self.solution_detail = solution_detail
        if cluster_num is not None:
            self.cluster_num = cluster_num

    @property
    def vul_name(self):
        r"""Gets the vul_name of this GeneralImageVulsResponseInfo.

        漏洞名称

        :return: The vul_name of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this GeneralImageVulsResponseInfo.

        漏洞名称

        :param vul_name: The vul_name of this GeneralImageVulsResponseInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this GeneralImageVulsResponseInfo.

        漏洞ID

        :return: The vul_id of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this GeneralImageVulsResponseInfo.

        漏洞ID

        :param vul_id: The vul_id of this GeneralImageVulsResponseInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def type(self):
        r"""Gets the type of this GeneralImageVulsResponseInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :return: The type of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GeneralImageVulsResponseInfo.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :param type: The type of this GeneralImageVulsResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def image_type(self):
        r"""Gets the image_type of this GeneralImageVulsResponseInfo.

        镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像

        :return: The image_type of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this GeneralImageVulsResponseInfo.

        镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像

        :param image_type: The image_type of this GeneralImageVulsResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def label_list(self):
        r"""Gets the label_list of this GeneralImageVulsResponseInfo.

        漏洞标签列表

        :return: The label_list of this GeneralImageVulsResponseInfo.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this GeneralImageVulsResponseInfo.

        漏洞标签列表

        :param label_list: The label_list of this GeneralImageVulsResponseInfo.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def severity_level(self):
        r"""Gets the severity_level of this GeneralImageVulsResponseInfo.

        漏洞的风险程度，取值如下：  -Critical : 严重  -High : 高危  -Medium : 中危  -Low : 低危

        :return: The severity_level of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this GeneralImageVulsResponseInfo.

        漏洞的风险程度，取值如下：  -Critical : 严重  -High : 高危  -Medium : 中危  -Low : 低危

        :param severity_level: The severity_level of this GeneralImageVulsResponseInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def image_num(self):
        r"""Gets the image_num of this GeneralImageVulsResponseInfo.

        受影响镜像总数

        :return: The image_num of this GeneralImageVulsResponseInfo.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this GeneralImageVulsResponseInfo.

        受影响镜像总数

        :param image_num: The image_num of this GeneralImageVulsResponseInfo.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def cve_list(self):
        r"""Gets the cve_list of this GeneralImageVulsResponseInfo.

        CVE列表

        :return: The cve_list of this GeneralImageVulsResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.GeneralImageVulsResponseInfoCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this GeneralImageVulsResponseInfo.

        CVE列表

        :param cve_list: The cve_list of this GeneralImageVulsResponseInfo.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.GeneralImageVulsResponseInfoCveList`]
        """
        self._cve_list = cve_list

    @property
    def max_cvss_score(self):
        r"""Gets the max_cvss_score of this GeneralImageVulsResponseInfo.

        镜像最大CVSS分值

        :return: The max_cvss_score of this GeneralImageVulsResponseInfo.
        :rtype: float
        """
        return self._max_cvss_score

    @max_cvss_score.setter
    def max_cvss_score(self, max_cvss_score):
        r"""Sets the max_cvss_score of this GeneralImageVulsResponseInfo.

        镜像最大CVSS分值

        :param max_cvss_score: The max_cvss_score of this GeneralImageVulsResponseInfo.
        :type max_cvss_score: float
        """
        self._max_cvss_score = max_cvss_score

    @property
    def scan_time(self):
        r"""Gets the scan_time of this GeneralImageVulsResponseInfo.

        最近扫描时间，时间单位：毫秒（ms）

        :return: The scan_time of this GeneralImageVulsResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this GeneralImageVulsResponseInfo.

        最近扫描时间，时间单位：毫秒（ms）

        :param scan_time: The scan_time of this GeneralImageVulsResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def description(self):
        r"""Gets the description of this GeneralImageVulsResponseInfo.

        漏洞描述

        :return: The description of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GeneralImageVulsResponseInfo.

        漏洞描述

        :param description: The description of this GeneralImageVulsResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def url(self):
        r"""Gets the url of this GeneralImageVulsResponseInfo.

        漏洞修复参考链接

        :return: The url of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this GeneralImageVulsResponseInfo.

        漏洞修复参考链接

        :param url: The url of this GeneralImageVulsResponseInfo.
        :type url: str
        """
        self._url = url

    @property
    def solution_detail(self):
        r"""Gets the solution_detail of this GeneralImageVulsResponseInfo.

        修复建议

        :return: The solution_detail of this GeneralImageVulsResponseInfo.
        :rtype: str
        """
        return self._solution_detail

    @solution_detail.setter
    def solution_detail(self, solution_detail):
        r"""Sets the solution_detail of this GeneralImageVulsResponseInfo.

        修复建议

        :param solution_detail: The solution_detail of this GeneralImageVulsResponseInfo.
        :type solution_detail: str
        """
        self._solution_detail = solution_detail

    @property
    def cluster_num(self):
        r"""Gets the cluster_num of this GeneralImageVulsResponseInfo.

        受影响集群总数

        :return: The cluster_num of this GeneralImageVulsResponseInfo.
        :rtype: int
        """
        return self._cluster_num

    @cluster_num.setter
    def cluster_num(self, cluster_num):
        r"""Sets the cluster_num of this GeneralImageVulsResponseInfo.

        受影响集群总数

        :param cluster_num: The cluster_num of this GeneralImageVulsResponseInfo.
        :type cluster_num: int
        """
        self._cluster_num = cluster_num

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
        if not isinstance(other, GeneralImageVulsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
