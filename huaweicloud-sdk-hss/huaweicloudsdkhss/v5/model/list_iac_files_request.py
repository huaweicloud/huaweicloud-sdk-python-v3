# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIacFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'scan_type': 'str',
        'file_id': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'risky': 'bool',
        'cicd_id': 'str',
        'cicd_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'scan_type': 'scan_type',
        'file_id': 'file_id',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'risky': 'risky',
        'cicd_id': 'cicd_id',
        'cicd_name': 'cicd_name'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, scan_type=None, file_id=None, file_name=None, file_type=None, risky=None, cicd_id=None, cicd_name=None):
        r"""ListIacFilesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param scan_type: **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 
        :type scan_type: str
        :param file_id: **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 
        :type file_id: str
        :param file_name: **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512  **默认取值**: 不涉及 
        :type file_name: str
        :param file_type: **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 
        :type file_type: str
        :param risky: **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险  **默认取值**: 不涉及 
        :type risky: bool
        :param cicd_id: **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 
        :type cicd_id: str
        :param cicd_name: **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 
        :type cicd_name: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._scan_type = None
        self._file_id = None
        self._file_name = None
        self._file_type = None
        self._risky = None
        self._cicd_id = None
        self._cicd_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        self.scan_type = scan_type
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if risky is not None:
            self.risky = risky
        if cicd_id is not None:
            self.cicd_id = cicd_id
        if cicd_name is not None:
            self.cicd_name = cicd_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIacFilesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListIacFilesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIacFilesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListIacFilesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListIacFilesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListIacFilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIacFilesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListIacFilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListIacFilesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListIacFilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIacFilesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListIacFilesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ListIacFilesRequest.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 

        :return: The scan_type of this ListIacFilesRequest.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ListIacFilesRequest.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描 - cicd_scan：cicd扫描 **默认取值**: 不涉及 

        :param scan_type: The scan_type of this ListIacFilesRequest.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def file_id(self):
        r"""Gets the file_id of this ListIacFilesRequest.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 

        :return: The file_id of this ListIacFilesRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ListIacFilesRequest.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 

        :param file_id: The file_id of this ListIacFilesRequest.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ListIacFilesRequest.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512  **默认取值**: 不涉及 

        :return: The file_name of this ListIacFilesRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListIacFilesRequest.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512  **默认取值**: 不涉及 

        :param file_name: The file_name of this ListIacFilesRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this ListIacFilesRequest.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 

        :return: The file_type of this ListIacFilesRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ListIacFilesRequest.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件 - k8s_yaml：k8s yaml文件  **默认取值**: 不涉及 

        :param file_type: The file_type of this ListIacFilesRequest.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def risky(self):
        r"""Gets the risky of this ListIacFilesRequest.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险  **默认取值**: 不涉及 

        :return: The risky of this ListIacFilesRequest.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this ListIacFilesRequest.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险 - false：无风险  **默认取值**: 不涉及 

        :param risky: The risky of this ListIacFilesRequest.
        :type risky: bool
        """
        self._risky = risky

    @property
    def cicd_id(self):
        r"""Gets the cicd_id of this ListIacFilesRequest.

        **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :return: The cicd_id of this ListIacFilesRequest.
        :rtype: str
        """
        return self._cicd_id

    @cicd_id.setter
    def cicd_id(self, cicd_id):
        r"""Sets the cicd_id of this ListIacFilesRequest.

        **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :param cicd_id: The cicd_id of this ListIacFilesRequest.
        :type cicd_id: str
        """
        self._cicd_id = cicd_id

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this ListIacFilesRequest.

        **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :return: The cicd_name of this ListIacFilesRequest.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this ListIacFilesRequest.

        **参数解释**: CI/CD名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128 **默认取值**: 不涉及 

        :param cicd_name: The cicd_name of this ListIacFilesRequest.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

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
        if not isinstance(other, ListIacFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
