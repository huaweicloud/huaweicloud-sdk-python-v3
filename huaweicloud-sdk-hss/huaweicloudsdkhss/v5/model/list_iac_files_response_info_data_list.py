# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIacFilesResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'risky': 'bool',
        'risk_num': 'int',
        'first_scan_time': 'int',
        'last_scan_time': 'int',
        'upload_file_time': 'int',
        'cicd_id': 'str',
        'cicd_name': 'str',
        'scan_type': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'risky': 'risky',
        'risk_num': 'risk_num',
        'first_scan_time': 'first_scan_time',
        'last_scan_time': 'last_scan_time',
        'upload_file_time': 'upload_file_time',
        'cicd_id': 'cicd_id',
        'cicd_name': 'cicd_name',
        'scan_type': 'scan_type'
    }

    def __init__(self, file_id=None, file_name=None, file_type=None, risky=None, risk_num=None, first_scan_time=None, last_scan_time=None, upload_file_time=None, cicd_id=None, cicd_name=None, scan_type=None):
        r"""ListIacFilesResponseInfoDataList

        The model defined in huaweicloud sdk

        :param file_id: **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 
        :type file_id: str
        :param file_name: **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512 **默认取值**: 不涉及 
        :type file_name: str
        :param file_type: **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 
        :type file_type: str
        :param risky: **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险 **默认取值**: 不涉及 
        :type risky: bool
        :param risk_num: 风险项数量
        :type risk_num: int
        :param first_scan_time: 首次扫描时间
        :type first_scan_time: int
        :param last_scan_time: 最近扫描时间
        :type last_scan_time: int
        :param upload_file_time: 上传文件时间
        :type upload_file_time: int
        :param cicd_id: **参数解释**: cicd标识 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 
        :type cicd_id: str
        :param cicd_name: **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 
        :type cicd_name: str
        :param scan_type: **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 
        :type scan_type: str
        """
        
        

        self._file_id = None
        self._file_name = None
        self._file_type = None
        self._risky = None
        self._risk_num = None
        self._first_scan_time = None
        self._last_scan_time = None
        self._upload_file_time = None
        self._cicd_id = None
        self._cicd_name = None
        self._scan_type = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if risky is not None:
            self.risky = risky
        if risk_num is not None:
            self.risk_num = risk_num
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if last_scan_time is not None:
            self.last_scan_time = last_scan_time
        if upload_file_time is not None:
            self.upload_file_time = upload_file_time
        if cicd_id is not None:
            self.cicd_id = cicd_id
        if cicd_name is not None:
            self.cicd_name = cicd_name
        if scan_type is not None:
            self.scan_type = scan_type

    @property
    def file_id(self):
        r"""Gets the file_id of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :return: The file_id of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :param file_id: The file_id of this ListIacFilesResponseInfoDataList.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512 **默认取值**: 不涉及 

        :return: The file_name of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512 **默认取值**: 不涉及 

        :param file_name: The file_name of this ListIacFilesResponseInfoDataList.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 

        :return: The file_type of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ListIacFilesResponseInfoDataList.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 

        :param file_type: The file_type of this ListIacFilesResponseInfoDataList.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def risky(self):
        r"""Gets the risky of this ListIacFilesResponseInfoDataList.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险 **默认取值**: 不涉及 

        :return: The risky of this ListIacFilesResponseInfoDataList.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this ListIacFilesResponseInfoDataList.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险 **默认取值**: 不涉及 

        :param risky: The risky of this ListIacFilesResponseInfoDataList.
        :type risky: bool
        """
        self._risky = risky

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ListIacFilesResponseInfoDataList.

        风险项数量

        :return: The risk_num of this ListIacFilesResponseInfoDataList.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ListIacFilesResponseInfoDataList.

        风险项数量

        :param risk_num: The risk_num of this ListIacFilesResponseInfoDataList.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this ListIacFilesResponseInfoDataList.

        首次扫描时间

        :return: The first_scan_time of this ListIacFilesResponseInfoDataList.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this ListIacFilesResponseInfoDataList.

        首次扫描时间

        :param first_scan_time: The first_scan_time of this ListIacFilesResponseInfoDataList.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def last_scan_time(self):
        r"""Gets the last_scan_time of this ListIacFilesResponseInfoDataList.

        最近扫描时间

        :return: The last_scan_time of this ListIacFilesResponseInfoDataList.
        :rtype: int
        """
        return self._last_scan_time

    @last_scan_time.setter
    def last_scan_time(self, last_scan_time):
        r"""Sets the last_scan_time of this ListIacFilesResponseInfoDataList.

        最近扫描时间

        :param last_scan_time: The last_scan_time of this ListIacFilesResponseInfoDataList.
        :type last_scan_time: int
        """
        self._last_scan_time = last_scan_time

    @property
    def upload_file_time(self):
        r"""Gets the upload_file_time of this ListIacFilesResponseInfoDataList.

        上传文件时间

        :return: The upload_file_time of this ListIacFilesResponseInfoDataList.
        :rtype: int
        """
        return self._upload_file_time

    @upload_file_time.setter
    def upload_file_time(self, upload_file_time):
        r"""Sets the upload_file_time of this ListIacFilesResponseInfoDataList.

        上传文件时间

        :param upload_file_time: The upload_file_time of this ListIacFilesResponseInfoDataList.
        :type upload_file_time: int
        """
        self._upload_file_time = upload_file_time

    @property
    def cicd_id(self):
        r"""Gets the cicd_id of this ListIacFilesResponseInfoDataList.

        **参数解释**: cicd标识 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :return: The cicd_id of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._cicd_id

    @cicd_id.setter
    def cicd_id(self, cicd_id):
        r"""Sets the cicd_id of this ListIacFilesResponseInfoDataList.

        **参数解释**: cicd标识 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :param cicd_id: The cicd_id of this ListIacFilesResponseInfoDataList.
        :type cicd_id: str
        """
        self._cicd_id = cicd_id

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this ListIacFilesResponseInfoDataList.

        **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :return: The cicd_name of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this ListIacFilesResponseInfoDataList.

        **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :param cicd_name: The cicd_name of this ListIacFilesResponseInfoDataList.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ListIacFilesResponseInfoDataList.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 

        :return: The scan_type of this ListIacFilesResponseInfoDataList.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ListIacFilesResponseInfoDataList.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 

        :param scan_type: The scan_type of this ListIacFilesResponseInfoDataList.
        :type scan_type: str
        """
        self._scan_type = scan_type

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
        if not isinstance(other, ListIacFilesResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
